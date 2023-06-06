from datetime import datetime
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    """_summary_"""
    response = exception_handler(exc, context)

    if response:
        response.data["status"] = "error"  # type: ignore
        response.data["status_code"] = response.status_code  # type: ignore
        response.data["time"] = datetime.now()  # type: ignore
        response.data["errors"] = response.data["detail"]  # type: ignore
        del response.data["detail"]  # type: ignore
    return response
