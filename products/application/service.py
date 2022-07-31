from products.application.requests import *
from products.domain.serializer import ProductSerializer
from products.application.methods import HttpMethods
from products.application.exceptions import *


class ProductService:
    def __init__(self, repository):
        self.__repository = repository

    def __add_product(self, request):
        pass

    def __get_product(self, request):
        serializer = None
        if type(request) is GetProductByNameRequest:
            product = self.__repository.get_product_by_name(request.name)
            if product is None:
                raise ProductNotFoundException()
            serializer = ProductSerializer(product)
        elif type(request) is GetProductsRequest:
            serializer = ProductSerializer(self.__repository.get_all_products())

        return serializer.serialize()

    def handle_request(self, method, request):
        product_request = ProductRequestFactory.create_product_request(request)
        if method == HttpMethods.GET:
            return self.__get_product(product_request)
        elif method == HttpMethods.POST:
            return self.__add_product(product_request)
