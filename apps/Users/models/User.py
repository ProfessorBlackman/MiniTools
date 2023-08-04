import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models

from apps.Users.Managers.custom_user_manager import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):

    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    email_validator = RegexValidator(
        regex=email_regex,
        message='Enter a valid email address.'
    )

    id = models.UUIDField(verbose_name="User ID", primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    email_address = models.EmailField(verbose_name="Email Address", max_length=200, unique=True, validators=[email_validator])
    first_name = models.CharField(verbose_name="First Name", max_length=100)
    last_name = models.CharField(verbose_name="Last Name", max_length=100)
    country = models.CharField(verbose_name="Country", max_length=100)
    verified = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_registered = models.DateTimeField(verbose_name="Date registered", auto_now_add=True, blank=False, null=False)
    is_deleted = models.BooleanField(default=False)

    USERNAME_FIELD = 'email_address'
    objects = CustomUserManager()

    def __str__(self):
        return self.email_address

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return self.first_name
