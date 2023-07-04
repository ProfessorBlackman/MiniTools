from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from apps.Users.models import User


def generate_password_reset_token(user: User, user_id: str):
    """
    Generates a password reset token

    encodes the user's id in base64 and then uses default_token_generator
    to generate a token from the given user object

    Parameters:
    ----------
    user : User object
        A user instance
    user_id: str
        The user id.

    Returns:
    -------
    tuple
        returns a tuple of (uid, token).
    """
    uid = urlsafe_base64_encode(force_bytes(user_id))
    token = default_token_generator.make_token(user)

    return uid, token
