from products.application.exceptions import *


class ProductRequestFactory:
    @staticmethod
    def create_product_request(request):
        if len(request.query_params) != 0:
            return GetProductByNameRequest(request)
        elif len(request.query_params) == 0:
            return GetProductsRequest()
        else:
            raise InvalidProductRequestException()


class GetProductsRequest:
    def __init__(self):
        pass


class GetProductByNameRequest:
    def __init__(self, request):
        self.name = request.query_params["name"]
