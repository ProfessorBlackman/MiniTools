from rest_framework import serializers


class ConfirmUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()
