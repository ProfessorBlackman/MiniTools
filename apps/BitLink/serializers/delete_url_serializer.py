from rest_framework import serializers


#  serializer for RedirectUrlView.py
class DeleteUrlSerializer(serializers.Serializer):
    url_id = serializers.IntegerField()
