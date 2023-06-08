from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

from apps.Users.models import User


def create_jwt_token_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'access': str(refresh.access_token),
        'refresh': str(refresh)
    }
