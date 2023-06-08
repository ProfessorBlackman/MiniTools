from rest_framework import serializers

from django.contrib.auth import get_user_model

User = get_user_model()


class CheckEmailSerializer(serializers.Serializer):
    email_address = serializers.EmailField()


class PasswordRecoverySerializer(serializers.Serializer):
    """
        Serializer for password change endpoint.
        """
    password = serializers.CharField(required=True, write_only=True)
    uid = serializers.CharField(required=True, write_only=True)
    token = serializers.CharField(required=True, write_only=True)