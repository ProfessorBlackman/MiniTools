"""_summary_
"""
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, generics
from rest_framework.response import Response
from silk.profiling.profiler import silk_profile

from apps.Users.serializers.signup import SignUpSerializer
from apps.Users.tasks.send_emails_task import send_email_task
from apps.Users.utils.create_otp import create_otp
from exceptions.base_custom_exception import BaseCustomException


class CreateUser(generics.GenericAPIView):
    """_summary_"""

    serializer_class = SignUpSerializer

    @swagger_auto_schema(operation_summary="Registering A User")
    @silk_profile(name=" Registering A User")
    def post(self, request):
        """
        view for registering a user
        """
        data = request.data
        serializer = self.serializer_class(data=data)
        email_address = data.get("email_address")
        extra = {'content': create_otp(email_address),
                 'domain': f'{settings.FRONTEND_DOMAIN}/confirm?email={email_address}'}
        if serializer.is_valid():
            serializer.save()
            send_email_task(email_address, 'account-confirmation.html',
                            'MiniTools Account Confirmation',
                            extra
                            )
            print("saved successfully")

            response = {"status": "success", "data": serializer.data}
            return Response(data=response, status=status.HTTP_201_CREATED)

        raise BaseCustomException(
            detail=serializer.errors, code=status.HTTP_400_BAD_REQUEST
        )
