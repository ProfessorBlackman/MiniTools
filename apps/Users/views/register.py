"""_summary_
"""
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, generics
from rest_framework.response import Response
from silk.profiling.profiler import silk_profile

from apps.Users.serializers.signup import SignUpSerializer
from apps.Users.services.user_service import UserService
from apps.Users.tasks.send_emails_task import send_email_task
from apps.Users.utils.create_otp import create_otp
from exceptions.base_custom_exception import BaseCustomException
from utils.logging.loggers import database_logger


class CreateUser(generics.GenericAPIView):
    """_summary_"""

    serializer_class = SignUpSerializer

    @swagger_auto_schema(operation_summary="Registering A User")
    @silk_profile(name=" Registering A User")
    def post(self, request):
        """
        view for registering a user
        """
        user_service = UserService(serializer=self.serializer_class)
        return Response(data=user_service.register(request), status=status.HTTP_201_CREATED)
