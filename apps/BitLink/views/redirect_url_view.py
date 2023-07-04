from django.http import HttpResponseRedirect
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models.urlmodel import UrlData
from ..serializers.redirect_serializer import RedirectUrlSerializer


#  view for redirecting to long_url in browser
class RedirectUrl(APIView):
    serializer_class = RedirectUrlSerializer

    @swagger_auto_schema(operation_summary='redirecting to long url')
    def get(self, request, slug):
        data = request.data
        self.serializer_class(data=data)

        if UrlData.objects.filter(slug=slug).exists():  # checking if object with slug exists in database
            try:
                url_data = UrlData.objects.get(slug=slug)
                long = url_data.long_url
                url_data.no_of_uses += 1
                url_data.save()

            except (TypeError, ValueError, OverflowError, url_data.DoesNotExist):
                response = {
                    'status': 'error',
                    'errors': 'object not in database'
                }
                return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
            return HttpResponseRedirect(long)
