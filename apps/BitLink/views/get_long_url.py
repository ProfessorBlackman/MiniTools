from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..models.urlmodel import UrlData
from ..serializers.short_url_info_serializer import ShortUrlInfoSerializer
from ..utils.generate_url import urlgen


class GetLongUrlView(generics.GenericAPIView):
    serializer_class = ShortUrlInfoSerializer

    @swagger_auto_schema(operation_summary='Get a shortened url\'s details')
    def get(self, request):
        data = request.data
        url = data.get('url')

        serializer = self.serializer_class(data=data)
        if not serializer.is_valid():
            response = {
                'status': 'error',
                'errors': "invalid url"
            }
            return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
        try:
            url_details = UrlData.objects.get(short_url=url)
        except UrlData.DoesNotExist:
            response = {
                'status': 'error',
                'errors': "url does not exist"
            }
            return Response(data=response, status=status.HTTP_400_BAD_REQUEST)

        response = {
            'status': 'success',
            'data': url_details.long_url
        }
        return Response(data=response, status=status.HTTP_201_CREATED)
