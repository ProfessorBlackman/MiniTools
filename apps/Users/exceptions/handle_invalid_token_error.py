from accounts.exceptions.utils.exceptionResponse import exceptionResponse

def handle_invalid_token_error(exc, context, response):
    
    return exceptionResponse("Token is invalid or expired or blacklisted",  response)
