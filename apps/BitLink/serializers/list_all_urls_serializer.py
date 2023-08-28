from rest_framework import serializers

from apps.BitLink.models.urlmodel import UrlData


class ListAllUrlsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlData
        exclude = ("is_deleted", "related_user")
