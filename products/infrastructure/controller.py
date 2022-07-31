from rest_framework.views import APIView
from products.infrastructure.simplerepo import SimpleProductRepository
from products.application.service import ProductService
from products.application.exceptions import *
from rest_framework.response import Response
from rest_framework import status


def map_exception(e):
    if type(e) is InvalidProductRequestException:
        return status.HTTP_400_BAD_REQUEST
    elif type(e) is ProductNotFoundException:
        return status.HTTP_404_NOT_FOUND
    else:
        return status.HTTP_500_INTERNAL_SERVER_ERROR


class ProductController(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__service = ProductService(SimpleProductRepository())

    def get(self, request):
        response = {
            "status": status.HTTP_200_OK,
            "data": ""
        }
        try:
            response["data"] = self.__service.handle_request(request)
        except Exception as e:
            response["status"] = map_exception(e)
        return Response(response["data"], response["status"])
