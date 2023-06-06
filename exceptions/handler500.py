from exceptions.utils.exceptionResponse import exceptionResponse


def error_500(request):
    
    return exceptionResponse('Server Error', 500)
