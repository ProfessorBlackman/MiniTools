import qrcode
from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile

from apps.rapidqr.models.qr_code_model import QRCode


class QRCodeService:
    qr_code = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    def __init__(self, data):
        self.data = data

    def generate_qrcode_with_image_at_the_center(self):
        pass
    def save_qrcode(self):
        qr_image = self.generate_qrcode()

        buffer = BytesIO()
        qr_image.save(buffer, format="PNG")
        qr_file = SimpleUploadedFile(f"qrcode_{self.data}.png", buffer.getvalue())

        qrcode_instance = QRCode.objects.create(qr_code=qr_file)
        return qrcode_instance

    def generate_qrcode(self):
        self.qr_code.add_data(self.data)
        self.qr_code.make(fit=True)

        qr_image = self.qr_code.make_image(fill_color="black", back_color="white")
        return qr_image
        pass
