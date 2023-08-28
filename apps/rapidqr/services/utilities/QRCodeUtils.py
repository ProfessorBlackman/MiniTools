import qrcode
from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile

from apps.rapidqr.models.qr_code_model import QRCode


class QRCodeService:
    def __init__(self, data):
        self.data = data

    def generate_qrcode(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self.data)
        qr.make(fit=True)

        qr_image = qr.make_image(fill_color="black", back_color="white")
        return qr_image

    def save_qrcode(self):
        qr_image = self.generate_qrcode()

        buffer = BytesIO()
        qr_image.save(buffer, format="PNG")
        qr_file = SimpleUploadedFile(f"qrcode_{self.data}.png", buffer.getvalue())

        qrcode_instance = QRCode.objects.create(qr_code=qr_file)
        return qrcode_instance
