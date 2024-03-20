from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controller.tag_creator_controller import TagCreatorController

class TagCreatorView:
    '''
      responsability fro interacting with HTTP
    '''

    def validate_and_create(self, http_request: HttpRequest):
        body = http_request.body
        product_code = body["product_code"]

        # logica de regra de negocio
        print(">>View Tag Creator")
        tag_creator_controller = TagCreatorController()
        formatted_response = tag_creator_controller.create(product_code)

        # retorno do HTTP
        return HttpResponse(status_code=200, body=formatted_response)
