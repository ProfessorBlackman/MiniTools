from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, generics
from rest_framework.response import Response

from exceptions.base_custom_exception import BaseCustomException
from ..serializers.password_recovery import PasswordRecoverySerializer, CheckEmailSerializer
from ..tasks.send_emails_task import send_email_task

User = get_user_model()


class PasswordRecoveryView(generics.GenericAPIView):

    # This function verifies the OTP
    @swagger_auto_schema(operation_summary="Checking if email exists")
    def post(self, request, *args, **kwargs):
        data = request.data
        email = data.get("email_address")
        serializer = CheckEmailSerializer(data=data)
        if serializer.is_valid():
            try:
                profile = User.objects.get(email_address=email)
            except:
                response = {"status": "error", "error": "Invalid Email"}
                return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
            if profile.email_address == email:
                uid, token = User.generate_password_reset_token()
                domain = settings.FRONTEND_DOMAIN
                send_email_task.delay((email,
                                       'forgot_password.html',
                                       'MiniTools Account Password Recovery',
                                       {'link': f"{domain}/reset/{uid}/{token}"}))

            else:
                response = {"status": "error", "error": "Email doesn't exist"}
                return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
        else:
            raise BaseCustomException(
                detail="Invalid Email", code=status.HTTP_400_BAD_REQUEST
            )

        response = {"status": "success", "data": f"The email: {email} exists"}
        return Response(data=response, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        data = request.data
        uid = data.get("uid")
        key = data.get("token")
        password = data.get("password")
        serializer = PasswordRecoverySerializer(data=data)
        if serializer.is_valid():
            uidb = force_str(urlsafe_base64_decode(uid))
            try:
                user = User.objects.get(pk=uidb)
            except (TypeError, ValueError, OverflowError, User.DoesNotExist):
                user = None  # TODO: log errors

            if user is not None and default_token_generator.check_token(key):
                user.set_password(password)
                user.save()
                send_email_task.delay(user.email_address, 'password-changed.html',
                                      'MiniTools Account Password Reset Successfully',
                                      )
                raise BaseCustomException(
                    detail="Password Reset Successfully", code=status.HTTP_400_BAD_REQUEST
                )
            else:
                raise BaseCustomException(
                    detail="Invalid Email or Password", code=status.HTTP_400_BAD_REQUEST
                )
        response = {
            "status": "error",
            "error": serializer.errors,
        }
        return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
