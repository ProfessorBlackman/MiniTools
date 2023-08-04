from django.db import models

from apps.Users.models import User


class UrlData(models.Model):
    name = models.CharField(max_length=300, blank=False, null=False, unique=True)
    long_url = models.CharField(blank=False, null=False, unique=True)
    short_url = models.CharField(blank=False, null=False, unique=True)
    slug = models.CharField(max_length=8, unique=True)
    no_of_uses = models.IntegerField(default=0)
    related_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='urls')
    expires_at = models.DateTimeField( blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=False, editable=False)
    date_modified = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
