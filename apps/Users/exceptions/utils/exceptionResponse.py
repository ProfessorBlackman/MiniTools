def exceptionResponse(message, response):
        response.data ={
        "status":"error",
        "error": message,
        "status_code": response.status_code
        }        
        return response