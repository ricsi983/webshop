from products.domain.deserializer import ProductDeserializer
from products.domain.serializer import ProductSerializer
from products.application.requests import *
from abc import ABC, abstractmethod
from products.application.responses import *


class RequestHandlerFactory:
    @staticmethod
    def create_request_handler(request, repository):
        if type(request) is AddProductRequest:
            return AddProductRequestHandler(request, repository)
        elif type(request) is GetProductsRequest:
            return GetProductsRequestHandler(request, repository)
        elif type(request) is GetProductByNameRequest:
            return GetProductByNameRequestHandler(request, repository)
        elif type(request) is RemoveProductByName:
            return RemoveProductByNameRequestHandler(request, repository)


class RequestHandler(ABC):
    def __init__(self, request, repository):
        self._request = request
        self._repository = repository

    @abstractmethod
    def handle_request(self):
        pass


class AddProductRequestHandler(RequestHandler):

    def handle_request(self):
        deserializer = ProductDeserializer(self._request.product)
        product = deserializer.deserialize()
        if self._repository.get_product_by_name(product.get_name()) is not None:
            raise ProductAlreadyAddedException()
        self._repository.add_product(product)
        return CreatedResponse()


class GetProductsRequestHandler(RequestHandler):
    def handle_request(self):
        products = self._repository.get_all_products()
        serializer = ProductSerializer(products)
        return GetProductsResponse(serializer.serialize())


class GetProductByNameRequestHandler(RequestHandler):
    def handle_request(self):
        product = self._repository.get_product_by_name(self._request.name)
        if product is None:
            raise ProductNotFoundException()
        serializer = ProductSerializer(product)
        return GetProductsResponse(serializer.serialize())


class RemoveProductByNameRequestHandler(RequestHandler):
    def handle_request(self):
        product = self._repository.get_product_by_name(self._request.name)
        if product is None:
            raise ProductNotFoundException()
        self._repository.remove_product_by_name(self._request.name)
        return RemoveProductResponse()
