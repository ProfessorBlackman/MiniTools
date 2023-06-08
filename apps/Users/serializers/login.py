from rest_framework import serializers
from rest_framework.validators import ValidationError
from apps.Users.models.User import User


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email_address', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return None

    def update(self, instance, validated_data):
        return None
