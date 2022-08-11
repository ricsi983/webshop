from rest_framework import status

from products.application.requests import *
from products.domain.serializer import ProductSerializer
from products.domain.deserializer import ProductDeserializer
from products.domain.deserializer import ProductDeserializer
from products.application.methods import HttpMethods
from products.application.exceptions import *
from products.application.handlers import *
from products.application.responses import *


class ProductService:
    def __init__(self, repository):
        self.__repository = repository

    def __post_product(self, request):
        request_handler = RequestHandlerFactory.create_request_handler(request, self.__repository)
        try:
            response = request_handler.handle_request(request)
        except Exception as e:
            response = ErrorResponse(e)
        return response

    def __get_product(self, request):
        if type(request) is GetProductByNameRequest:
            product = self.__repository.get_product_by_name(request.name)
            if product is None:
                raise ProductNotFoundException()
            serializer = ProductSerializer(product)
            return serializer.serialize()
        elif type(request) is GetProductsRequest:
            serializer = ProductSerializer(self.__repository.get_all_products())
            return serializer.serialize()
        else:
            raise ProductRequestHandlerNotFoundException()

    def handle_request(self, method, request):
        product_request = ProductRequestFactory.create_product_request(method, request)
        request_handler = RequestHandlerFactory.create_request_handler(product_request, self.__repository)
        try:
            response = request_handler.handle_request()
        except Exception as e:
            response = ErrorResponse(e)
        return response

