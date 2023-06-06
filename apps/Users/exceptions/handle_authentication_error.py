from accounts.exceptions.utils.exceptionResponse import exceptionResponse
def handle_authentication_error(exc, context, response):

    return exceptionResponse("Please Login To Proceed", response)
