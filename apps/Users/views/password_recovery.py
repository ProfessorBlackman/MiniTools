from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from exceptions.base_custom_exception import BaseCustomException
from ..serializers.password_recovery import PasswordRecoverySerializer, CheckEmailSerializer
from ..services.user_service import UserService
from ..tasks.send_emails_task import send_email_task
from ..utils.generate_reset_token import generate_password_reset_token

User = get_user_model()


class PasswordRecoveryView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CheckEmailSerializer
        elif self.request.method == 'PUT':
            return PasswordRecoverySerializer
        else:
            return super().get_serializer_class()

    # This function verifies the OTP
    @swagger_auto_schema(operation_summary="Checking if email exists")
    def post(self, request, *args, **kwargs):

        user_service = UserService(serializer=self.get_serializer_class())

        return Response(data=user_service.confirm_email_to_reset_password(request), status=status.HTTP_201_CREATED)

    @swagger_auto_schema(operation_summary="Recovering user password")
    def put(self, request, *args, **kwargs):

        user_service = UserService(serializer=self.get_serializer_class())

        return Response(data=user_service.recover_password(request), status=status.HTTP_400_BAD_REQUEST)
