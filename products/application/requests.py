from products.application.exceptions import *
from products.application.methods import HttpMethods


class ProductRequestFactory:
    @staticmethod
    def create_product_request(method, request):
        if method is HttpMethods.POST:
            return AddProductRequest(request)
        elif method is HttpMethods.GET:
            if len(request.query_params) != 0:
                return GetProductByNameRequest(request)
            elif len(request.query_params) == 0:
                return GetProductsRequest()
            else:
                raise InvalidProductRequestException()
        elif method is HttpMethods.DELETE:
            return RemoveProductByName(request)


class GetProductsRequest:
    def __init__(self):
        pass


class GetProductByNameRequest:
    def __init__(self, request):
        self.name = request.query_params["name"]


class AddProductRequest:
    def __init__(self, request):
        self.product = request.data


class RemoveProductByName:
    def __init__(self, request):
        self.name = request.query_params["name"]
