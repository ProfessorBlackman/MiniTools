# from django.contrib.auth.models import AbstractBaseUser
# from django.core.validators import RegexValidator
# from django.db import models
#
# from .User import User
#
#
# class AdminUser(AbstractBaseUser):
#     email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#     email_validator = RegexValidator(
#         regex=email_regex,
#         message='Enter a valid email address.'
#     )
#
#     user_id = models.UUIDField(verbose_name="User ID", primary_key=True, unique=True)
#     emailAddress = models.EmailField(verbose_name="Email Address", max_length=200, unique=True,
#                                      validators=[email_validator])
#     firstName = models.CharField(verbose_name="First Name", max_length=100)
#     lastName = models.CharField(verbose_name="Last Name", max_length=100)
#     country = models.CharField(verbose_name="Country", max_length=100)
#     verified = models.BooleanField(default=False)
#     is_blocked = models.BooleanField(default=False)
#     date_registered = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.emailAddress
