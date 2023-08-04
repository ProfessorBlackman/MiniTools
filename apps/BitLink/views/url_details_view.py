from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models.urlmodel import UrlData
from ..serializers.url_details_serializer import UrlDetailsSerializer
from ...Users.models import User


class UrlDetailsView(APIView):

    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary='Get a shortened url\'s details')
    def get(self, request):
        global user
        user_email = request.user
        try:
            user = User.objects.get(email_address=user_email)
        except user.DoesNotExist:
            response = {
                'status': 'error',
                'errors': "User does not exist"
            }
            return Response(data=response, status=status.HTTP_400_BAD_REQUEST)

        try:
            urls = UrlData.objects.filter(related_user=user)
        except Exception as e:
            response = {
                'status': 'error',
                'errors': e
            }
            return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
        serializer = UrlDetailsSerializer(urls, many=True)

        response = {
            'status': 'success',
            'data': serializer.data
        }
        return Response(data=response, status=status.HTTP_201_CREATED)
