from rest_framework import serializers

from apps.BitLink.models.urlmodel import UrlData


class UrlDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlData
        fields = '__all__'
