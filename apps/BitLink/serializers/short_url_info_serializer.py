from rest_framework import serializers


#  serializer for ShortenUrlView
class ShortUrlInfoSerializer(serializers.Serializer):

    """
    Serializer for url shortening endpoint.
    """
    url = serializers.URLField(max_length=300, required=True)
