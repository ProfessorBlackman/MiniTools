from django.db import models


class UrlData(models.Model):
    name = models.CharField(max_length=300, blank=False, null=False, unique=True)
    long_url = models.CharField(max_length=300, blank=False, null=False, unique=True)
    short_url = models.CharField(max_length=20, blank=False, null=False, unique=True)
    slug = models.CharField(max_length=8, unique=True)
    no_of_uses = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    date_created = models.DateTimeField(auto_now_add=True, blank=False, editable=False)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
