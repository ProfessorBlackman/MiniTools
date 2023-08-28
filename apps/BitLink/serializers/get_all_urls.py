from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_list_or_404

from apps.BitLink.models.urlmodel import UrlData
from apps.BitLink.serializers.list_all_urls_serializer import ListAllUrlsSerializer


class ListAllUrlsView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ListAllUrlsSerializer

    def get_queryset(self):
        return get_list_or_404(UrlData, related_user=self.request.user)
