from django.http import JsonResponse


def exceptionResponse(message, status):
        response = JsonResponse(data={'status':'error', 'error':message,  'status_code': status})
        response.status_code = status
        
        return response