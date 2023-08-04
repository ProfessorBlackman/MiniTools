from django.http import HttpResponseRedirect
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models.urlmodel import UrlData


#  view for redirecting to long_url in browser
class RedirectUrl(APIView):

    @swagger_auto_schema(operation_summary='redirecting to long url')
    def get(self, request, slug):
        global url_data

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
        response = {
            'status': 'error',
            'errors': 'url not recognized'
        }
        return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
