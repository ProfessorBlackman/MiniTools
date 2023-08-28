from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..serializers.shorten_serializer import ShortenUrlSerializer
from ..serializers.update_serializer import UpdateSerializer
from ..serializers.url_details_serializer import UrlDetailsSerializer
from ..services.url_service import UrlService


class Url(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ShortenUrlSerializer
        elif self.request.method == 'PUT':
            return UpdateSerializer
        if self.request.method == 'GET':
            return UrlDetailsSerializer
        else:
            return super().get_serializer_class()

    @swagger_auto_schema(operation_summary='Shortening a url')
    def post(self, request):
        url_service = UrlService(self.get_serializer_class())
        return Response(data=url_service.shorten_url(request), status=status.HTTP_200_OK)

    def put(self, request):
        url_service = UrlService(self.get_serializer_class())
        return Response(data=url_service.update_url_data(request), status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary='Get a shortened url\'s details')
    def get(self, request, url_id=None):
        url_service = UrlService(self.get_serializer_class())
        if url_id is not None:
            return Response(data=url_service.read_one(request, url_id), status=status.HTTP_200_OK)
        return Response(data=url_service.read_all(request), status=status.HTTP_201_CREATED)

    # def get_queryset(self, request):

    @swagger_auto_schema(operation_summary='delete a url')
    def delete(self, url_id):
        url_service = UrlService()
        return Response(data=url_service.delete_url(url_id), status=status.HTTP_200_OK)
