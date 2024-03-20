from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntiryError
from cerberus import Validator

'''
  {
    "product_code": "123"
  }
'''


def tag_creator_validator(request: any) -> None:
    body_validator = Validator({
      "product_code": {"type": "string", "required": True, "empty": False}
    })

    response = body_validator.validate(request.json)
    if response is False:
        #raise Exception(body_validator.errors)
        raise HttpUnprocessableEntiryError(body_validator.errors)