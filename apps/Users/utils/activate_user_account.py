from django.contrib.auth import get_user_model

from utils.logging.loggers import db_logger

User = get_user_model()


def activate_user_account(email):
    global user
    try:
        user = User.objects.get(email_address=email)
        user.verified = True
        user.save()
    except user.DoesNotExist as error:
        db_logger.error(f"[DatabaseError: account couldn't be verified] {error}")
