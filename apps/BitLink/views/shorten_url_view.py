from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from utils.logging.loggers import database_logger
from ..models.urlmodel import UrlData
from ..serializers.update_serializer import UpdateSerializer
from ..serializers.shorten_serializer import ShortenUrlSerializer
from ..utils.generate_url import urlgen
from ..utils.update_url import update_url
from ...Users.models import User


class ShortenUrl(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ShortenUrlSerializer
        elif self.request.method == 'PUT':
            return UpdateSerializer
        else:
            return super().get_serializer_class()

    @swagger_auto_schema(operation_summary='Shortening a url')
    def post(self, request):
        data = request.data
        long = data.get('long_url')
        name = data.get('name')
        user_email = request.user
        print(f"this is data: {data}")
        print(f"this is user: {user_email}")

        serializer_class = self.get_serializer_class()

        serializer = serializer_class(data=data)
        if not serializer.is_valid():
            response = {
                'status': 'error',
                'errors': 'Invalid name or url',
            }
            return Response(data=response, status=status.HTTP_406_NOT_ACCEPTABLE)
        if UrlData.objects.filter(long_url=long).exists():  # see if any object with long as long_url exists
            response = {
                'status': 'error',
                'errors': 'url already exists',
            }
            return Response(data=response, status=status.HTTP_406_NOT_ACCEPTABLE)
        result_url, slug = urlgen()
        try:
            user = User.objects.get(email_address=user_email)
        except Exception as e:
            print(f"this is error: {e}")
            response = {
                'status': 'error',
                'errors': e
            }
            return Response(data=response, status=status.HTTP_406_NOT_ACCEPTABLE)
        print(f"this is user: {user.email_address}")
        try:
            new = UrlData(name=name, long_url=long, short_url=result_url, slug=slug, related_user=user)
            print(f"new url: {new.short_url}")
            new.full_clean()
            new.save()
        except Exception as e:
            response = {
                'status': 'error',
                'errors': e
            }
            return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
        response = {
            'status': 'success',
            'data': result_url
        }
        database_logger.info("shortened url data successfully")
        return Response(data=response, status=status.HTTP_201_CREATED)

    def put(self, request):
        print(f"this is request: {request}")
        data = request.data
        print(f"this is data: {data}")
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=data)
        if not serializer.is_valid():
            response = {
                'status': 'error',
                'errors': 'Invalid argument',
            }
            return Response(data=response, status=status.HTTP_406_NOT_ACCEPTABLE)
        is_saved_to_db = update_url(data=data)
        if not is_saved_to_db:
            response = {
                'status': 'error',
                'error': 'Invalid id'
            }
            return Response(data=response, status=status)

        response = {
            'status': 'error',
            'errors': 'Invalid argument',
        }
        return Response(data=response, status=status.HTTP_200_OK)
