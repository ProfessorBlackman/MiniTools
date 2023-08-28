from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.BitLink.serializers.url_details_serializer import UrlDetailsSerializer
from apps.BitLink.services.url_service import UrlService


class UrlDetailsView(APIView):

    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary='Get a shortened url\'s details')
    def get(self, request):
        url_service = UrlService(UrlDetailsSerializer)
        return Response(data=url_service.read_all(request), status=status.HTTP_201_CREATED)
