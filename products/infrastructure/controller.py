from rest_framework.views import APIView
from products.infrastructure.simplerepo import SimpleProductRepository
from products.application.service import ProductService
from rest_framework.response import Response
from products.application.methods import HttpMethods


class ProductController(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__service = ProductService(SimpleProductRepository())

    def get(self, request):
        response = self.__service.handle_request(HttpMethods.GET, request)
        return Response(response.description, response.status)

    def post(self, request):
        response = self.__service.handle_request(HttpMethods.POST, request)
        return Response(response.description, response.status)

    def delete(self, request):
        response = self.__service.handle_request(HttpMethods.DELETE, request)
        return Response(response.description, response.status)
