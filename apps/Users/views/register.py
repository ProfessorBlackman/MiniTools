"""_summary_
"""
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, generics
from rest_framework.response import Response

from apps.Users.serializers.signup import SignUpSerializer
from exceptions.base_custom_exception import BaseCustomException


class CreateUser(generics.GenericAPIView):
    """_summary_"""

    serializer_class = SignUpSerializer

    @swagger_auto_schema(operation_summary="Registering A User")
    def post(self, request):
        """
        view for registering a user
        """
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()

            response = {"status": "success", "data": serializer.data}
            return Response(data=response, status=status.HTTP_201_CREATED)

        raise BaseCustomException(
            detail=serializer.errors, code=status.HTTP_400_BAD_REQUEST
        )