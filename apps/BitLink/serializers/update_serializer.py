from rest_framework import serializers

from apps.BitLink.models.urlmodel import UrlData


class UpdateSerializer(serializers.ModelSerializer):
    generate_new_slug = serializers.BooleanField(default=False)

    class Meta:
        model = UrlData
        fields = ('id', 'long_url', 'name', 'expires_at', 'generate_new_slug')
