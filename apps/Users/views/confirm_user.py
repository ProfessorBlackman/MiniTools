from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, generics
from rest_framework.response import Response

from ..serializers.confirm_user import ConfirmUserSerializer
from ..services.user_service import UserService


class ConfirmUser(generics.GenericAPIView):
    serializer_class = ConfirmUserSerializer

    # This function verifies the OTP
    @swagger_auto_schema(operation_summary="Confirming A User")
    def post(self, request, *args, **kwargs):
        user_service = UserService(serializer=self.serializer_class)
        return Response(data=user_service.confirm_user(request), status=status.HTTP_201_CREATED)
