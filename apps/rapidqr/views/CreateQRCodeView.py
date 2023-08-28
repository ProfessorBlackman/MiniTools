"""_summary_
"""
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, generics
from rest_framework.response import Response
from silk.profiling.profiler import silk_profile

from apps.Users.services.user_service import UserService
from apps.rapidqr.serializers.QRCodeSerializer import QRCodeSerializer


class CreateQRCodeView(generics.GenericAPIView):
    """_summary_"""

    serializer_class = QRCodeSerializer

    @swagger_auto_schema(operation_summary="Generating a QR Code")
    @silk_profile(name="Generating a QR Code")
    def post(self, request):
        """
        view for Generating a QR Code
        """
        user_service = UserService(serializer=self.serializer_class)
        return Response(data=user_service.register(request), status=status.HTTP_201_CREATED)
