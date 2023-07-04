from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..models.urlmodel import UrlData
from ..serializers.shorten_serializer import ShortenUrlSerializer
from ..utils.generate_url import urlgen


class ShortenUrl(generics.GenericAPIView):
    serializer_class = ShortenUrlSerializer

    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary='Shortening a url')
    def post(self, request):
        data = request.data
        long = data.get('long_url')
        name = data.get('name')
        print(long)
        print(name)
        self.serializer_class(data=data)
        if UrlData.objects.filter(long_url=long).exists():  # see if any object with long as long_url exists
            response = {
                'status': 'error',
                'errors': 'url already exists',
            }
            return Response(data=response, status=status.HTTP_406_NOT_ACCEPTABLE)
        result_url, slug = urlgen(long)
        try:
            new = UrlData(name=name, long_url=long, short_url=result_url, slug=slug)  # storing info in database
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
        return Response(data=response, status=status.HTTP_201_CREATED)
