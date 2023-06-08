from django.contrib.auth import authenticate
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, generics
from rest_framework.response import Response

from exceptions.base_custom_exception import BaseCustomException
from ..serializers.login import LoginSerializer
from ..tokens.tokenSerializers.myTokenObtainPairSerializer import MyTokenObtainPairSerializer


class LoginUser(generics.GenericAPIView):
    """_summary_"""

    serializer_class = LoginSerializer

    @swagger_auto_schema(operation_summary="Login User")
    def post(self, request, *args, **kwargs):
        email_address = request.data.get("email_address")
        password = request.data.get("password")
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
                    response = {
                        "status": "success",
                        "data": tokens,
                    }
                    return Response(data=response, status=status.HTTP_200_OK)
                else:
                    raise BaseCustomException(
                        detail="You are not verified \n Please verify your account", code=status.HTTP_401_UNAUTHORIZED
                    )

        raise BaseCustomException(
            detail="Invalid Email or Password", code=status.HTTP_400_BAD_REQUEST
        )
