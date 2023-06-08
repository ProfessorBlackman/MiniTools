from rest_framework import serializers
from rest_framework.validators import ValidationError

from apps.Users.models.User import User


class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=300, min_length=8, write_only=True)

    class Meta:
        model = User
        exclude = ("id", "verified", "is_blocked", "date_registered", "last_login")

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        user = None
        try:
            password = validated_data.pop("password")
            user = User.objects.filter(email=validated_data.get("email")).update() #type: ignore
            user.set_password(password)
            user.save()
        except Exception as error:
            raise ValidationError("User does not exits")

        return user

    def validate(self, attrs):
        email_exits = User.objects.filter(email_address=attrs["email_address"]).exists() #type: ignore
        if email_exits:
            raise ValidationError("Email already exits")

        return super().validate(attrs)