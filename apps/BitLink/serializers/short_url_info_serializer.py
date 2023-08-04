from rest_framework import serializers


#  serializer for ShortenUrlView
class ShortUrlInfoSerializer(serializers.Serializer):

    """
    Serializer for url shortening endpoint.
    """
    url = serializers.CharField(max_length=300, required=True)
