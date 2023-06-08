from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, generics
from rest_framework.response import Response

from exceptions.base_custom_exception import BaseCustomException
from ..serializers.confirm_user import ConfirmUserSerializer
from ..utils.activate_user_account import activate_user_account
from ..utils.get_otp import get_otp


class ConfirmUser(generics.GenericAPIView):

    serializer_class = ConfirmUserSerializer

    # This function verifies the OTP
    @swagger_auto_schema(operation_summary="Confirming A User")
    def post(self, request, *args, **kwargs):
        data = request.data
        user_otp = data.get("otp")
        email = data.get("email")
        try:
            otp = get_otp(email=email)
        except:
            response = {"status": "error", "error": "Invalid Email"}
            return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
        if otp is None:
            raise BaseCustomException(
                detail="Your Otp has expired, Login to generate a new one", code=status.HTTP_400_BAD_REQUEST
            )
        elif otp != user_otp:
            response = {"status": "error", "data": "invalid otp"}
            return Response(data=response, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            activate_user_account(email=email)
            response = {
                "status": "success",
                "data": f"The email: {email} has been confirmed",
            }
            raise BaseCustomException(
                detail=response, code=status.HTTP_201_CREATED
            )