import qrcode

from apps.rapidqr.serializers.QRCodeSerializer import QRCodeSerializer
from utils.services.Service import Service


class YourService(Service):
    serializer_class = QRCodeSerializer
    request = None

    def process(self, *args):
        self.request = args[0]
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(self.request)

    def post_process(self):
        pass
