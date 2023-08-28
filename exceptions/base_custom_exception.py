"""_summary_
"""
from rest_framework.exceptions import APIException


class BaseCustomException(APIException):
    """Base Cution Expection For APIs
    raise BaseCustomException(detail = detail, code = code)

    """

    message = None
    status_code = None

    def __init__(self, *, message, status):
        if isinstance(message, dict):
            message = {"detail": message}

        super().__init__(message, status)
        self.message = message
        self.status_code = status
