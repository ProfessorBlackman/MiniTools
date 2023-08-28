from rest_framework import serializers

from apps.rapidqr.models.qr_code_model import QRCode


class QRCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QRCode
        fields = '__all__'
        exclude = ("date_created", "date_modified", "is_deleted", "related_user", "qr_code_location")
