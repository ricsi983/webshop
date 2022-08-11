# from cryptos.domain.model import Crypto
from rest_framework import status
from products.application.exceptions import *


def map_exception(exception):
    if type(exception) is InvalidProductRequestException:
        return status.HTTP_400_BAD_REQUEST
    elif type(exception) is ProductNotFoundException:
        return status.HTTP_404_NOT_FOUND
    elif type(exception) is ProductAlreadyAddedException:
        return status.HTTP_409_CONFLICT
    else:
        return status.HTTP_500_INTERNAL_SERVER_ERROR


class ErrorResponse:
    def __init__(self, exception):
        self.status = map_exception(exception)
        self.description = exception.args[0]


class CreatedResponse:
    def __init__(self):
        self.status = status.HTTP_201_CREATED
        self.description = "Product successfully added."


class GetProductsResponse:
    def __init__(self, products):
        self.status = status.HTTP_200_OK
        self.description = products


class RemoveProductResponse:
    def __init__(self):
        self.status = status.HTTP_204_NO_CONTENT
        self.description = "Product successfully removed"
