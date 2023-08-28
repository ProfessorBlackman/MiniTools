from django.conf import settings
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode

from apps.Users.models import User
from apps.Users.tasks.send_emails_task import send_email_task
from apps.Users.tokens.tokenSerializers.myTokenObtainPairSerializer import MyTokenObtainPairSerializer
from apps.Users.utils.activate_user_account import activate_user_account
from apps.Users.utils.create_otp import create_otp
from apps.Users.utils.generate_reset_token import generate_password_reset_token
from apps.Users.utils.get_otp import get_otp
from exceptions.base_custom_exception import BaseCustomException
from utils.logging.loggers import database_logger


class UserService:

    def __init__(self, serializer):
        self.serializer_class = serializer

    def register(self, request) -> dict:
        data = request.data
        serializer = self.serializer_class(data=data)
        email_address = data.get("email_address")
        extra = {'content': create_otp(email_address),
                 'domain': f'{settings.FRONTEND_DOMAIN}/confirm?email={email_address}'}
        if serializer.is_valid():
            try:
                serializer.save()
            except Exception as e:
                database_logger.error(e)
                raise BaseCustomException(
                    message=e, status=status.HTTP_400_BAD_REQUEST
                )
            try:
                send_email_task(email_address, 'account-confirmation.html',
                                'MiniTools Account Confirmation',
                                extra
                                )
            except Exception as e:
                database_logger.error(e)
            database_logger.info("saved successfully")
            print("saved successfully")
            return {"status": "success", "data": serializer.data}
        raise BaseCustomException(
            message=serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def login(self, request) -> dict:
        data = request.data
        email_address = data.get("email_address")
        password = data.get("password")
        print(f"this is credentials: {email_address}, {password}")

        authenticated_user = authenticate(request, email_address=email_address, password=password, )

        print(f"this is user: {authenticated_user}")

        if authenticated_user is not None and not authenticated_user.is_blocked:
            if authenticated_user.check_password(password):
                refresh_tokens = MyTokenObtainPairSerializer.get_token(authenticated_user)

                tokens = {
                    "access": str(refresh_tokens.access_token),
                    "refresh": str(refresh_tokens),
                }
                if authenticated_user.verified:  # type:ignore
                    return {
                        "status": "success",
                        "data": tokens,
                    }
                else:
                    raise BaseCustomException(
                        message="You are not verified \n Please verify your account", status=status.HTTP_401_UNAUTHORIZED
                    )

        raise BaseCustomException(
            message="Invalid Email or Password", status=status.HTTP_400_BAD_REQUEST
        )

    def confirm_email_to_reset_password(self, request) -> dict:
        data = request.data
        email = data.get("email_address")
        if self.serializer_class(data=request.data).is_valid():
            try:
                profile = User.objects.get(email_address=email)
                user_id = profile.id
            except User.DoesNotExist:
                raise BaseCustomException(
                    message="Invalid Email", status=status.HTTP_400_BAD_REQUEST
                )
            if profile.email_address == email:
                uid, token = generate_password_reset_token(profile, user_id)
                domain = settings.FRONTEND_DOMAIN
                send_email_task(email,
                                'forgot_password.html',
                                'MiniTools Account Password Recovery',
                                {'link': f"{domain}/reset/{uid}/{token}"})

            else:
                raise BaseCustomException(
                    message="Email doesn't exist", status=status.HTTP_400_BAD_REQUEST
                )
        else:
            raise BaseCustomException(
                message="Not an email", status=status.HTTP_400_BAD_REQUEST
            )
        return {"status": "success", "data": f"The email: {email} exists"}

    def recover_password(self, request) -> dict:
        data = request.data
        uid = data.get("uid")
        key = data.get("token")
        password = data.get("password")
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            uidb = force_str(urlsafe_base64_decode(uid))
            try:
                user = User.objects.get(pk=uidb)
                print(f"This is user: {user}")
            except User.DoesNotExist:
                raise BaseCustomException(
                    message="User does not exist", status=status.HTTP_400_BAD_REQUEST
                )
            except (TypeError, ValueError, OverflowError):
                user = None  # TODO: log errors

            if user is not None and default_token_generator.check_token(user, key):
                print("We have gotten here")
                user.set_password(password)
                user.save()
                send_email_task(user.email_address, 'password-changed.html',
                                'MiniTools Account Password Reset Successfully',
                                )
                return {"status": "success", "data": "Password Reset Successfully"}
            else:
                raise BaseCustomException(
                    message="Invalid Token", status=status.HTTP_400_BAD_REQUEST
                )
        raise BaseCustomException(
            message=serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def confirm_user(self, request) -> dict:
        data = request.data
        user_otp = data.get("otp")
        print(f"This is user {user_otp}")
        print(f"This is user {type(user_otp)}")
        email = data.get("email")
        try:
            otp = get_otp(email=email)
            print(f"This is otp: {otp}")
        except Exception as e:
            raise BaseCustomException(
                message=f"Invalid Email, error: {e}", status=status.HTTP_400_BAD_REQUEST
            )
        if otp is None:
            raise BaseCustomException(
                message="Your Otp has expired, Login to generate a new one", status=status.HTTP_400_BAD_REQUEST
            )
        if otp != int(user_otp):
            raise BaseCustomException(
                message="Invalid otp", status=status.HTTP_400_BAD_REQUEST
            )
        else:
            activate_user_account(email=email)
            send_email_task.delay(email, 'welcome.html',
                                  'Your Account Has Been Confirmed'
                                  )
            return {
                "status": "success",
                "data": f"The email: {email} has been confirmed",
            }
