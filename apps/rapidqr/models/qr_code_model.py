from django.db import models

from apps.Users.models import User


class CodeType(models.TextChoices):
    IMAGE_QR = "QR code with image", "QR code with image"
    TEXT_QR = "QR code with text", "QR code with text",
    DYNAMIC_QR = "Dynamic QR code", "Dynamic QR code"


class QRCode(models.Model):
    name = models.CharField(max_length=300, blank=False, null=False, unique=True)
    qr_code_location = models.URLField(blank=False, null=False, unique=True)
    original_data = models.TextField(blank=False, null=False)
    related_user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='qr_code')
    code_type = models.CharField(max_length=15, choices=CodeType.choices, default=CodeType.TEXT_QR)
    date_created = models.DateTimeField(auto_now_add=True, blank=False, editable=False)
    date_modified = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
