"""_summary_
"""
from rest_framework.exceptions import APIException


class BaseCustomException(APIException):
    """Base Cution Expection For APIs
    raise BaseCustomException(detail = detail, code = code)

    """

    detail = None
    status_code = None

    def __init__(self, *, detail, code):
        if isinstance(detail, dict):
            detail = {"detail": detail}

        super().__init__(detail, code)
        self.detail = detail
        self.status_code = code
