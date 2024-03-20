from src.views.http_types.http_response import HttpResponse
from .error_types.http_unprocessable_entity import HttpUnprocessableEntiryError

def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, HttpUnprocessableEntiryError):
        # poder ser usado para envio de log 
        # poder ser usado para enviar email de notificação de log
        return HttpResponse(
             status_code=error.status_code,
          body={
            "errors": [{
              "title": error.name,
              "detail": error.message
            }]
          }
        )

    return HttpResponse(
        status_code=500,
        body={
          "errors": [{
            "title": "Server Error",
            "detail": str(error)
          }]
        }
    )