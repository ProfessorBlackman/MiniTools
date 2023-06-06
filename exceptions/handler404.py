from exceptions.utils.exceptionResponse import exceptionResponse

def error_404(request, exception):
    
    return exceptionResponse('Sorry page not found', 404)
