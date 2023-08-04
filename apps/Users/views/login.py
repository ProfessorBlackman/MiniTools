from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, generics
from rest_framework.response import Response

from ..serializers.login import LoginSerializer
from ..services.user_service import UserService


class LoginUser(generics.GenericAPIView):
    """_summary_"""

    serializer_class = LoginSerializer

    @swagger_auto_schema(operation_summary="Login User")
    def post(self, request, *args, **kwargs):

        user_service = UserService(serializer=self.serializer_class)

        return Response(data=user_service.login(request), status=status.HTTP_200_OK)
