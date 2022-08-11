import unittest
from unittest.mock import *
from rest_framework import status
from products.infrastructure.simplerepo import *
from products.application.handlers import *


class TestRequest:
    def __init__(self):
        self.data = {}
        self.name = ""


class TestProductHandlers(unittest.TestCase):

    def test_add_product_request_handler_product_already_added(self):
        already_added_exception_occurred = False
        SimpleProductRepository.get_product_by_name = Mock(return_value=1)
        test_repository = SimpleProductRepository()
        test_add_request = AddProductRequest(TestRequest())
        test_add_request.product = {
            "name": "test_name",
            "price": 100,
            "image": "test_image",
            "description": "test_description",
            "available": False
        }
        try:
            test_handler = AddProductRequestHandler(test_add_request, test_repository)
            test_handler.handle_request()
        except Exception as e:
            if type(e) is ProductAlreadyAddedException:
                already_added_exception_occurred = True
        assert already_added_exception_occurred is True

    def test_post_request_product_added_successfully(self):
        exception_occurred = False
        SimpleProductRepository.get_product_by_name = Mock(return_value=None)
        SimpleProductRepository.add_product = Mock()
        test_repository = SimpleProductRepository()
        test_add_request = AddProductRequest(TestRequest())
        test_add_request.product = {
            "name": "test_name",
            "price": 100,
            "image": "test_image",
            "description": "test_description",
            "available": False
        }
        response = None
        try:
            test_handler = AddProductRequestHandler(test_add_request, test_repository)
            response = test_handler.handle_request()
        except Exception as e:
            exception_occurred = True
        SimpleProductRepository.add_product.assert_called_once()
        assert exception_occurred is False
        assert response.status is status.HTTP_201_CREATED
        assert response.description == "Product successfully added."

    def test_get_request_get_products(self):
        test_product_1 = Product()
        test_product_1.set_name("test_product_1")
        test_product_1.set_price(1)
        test_product_1.set_image("test_image_1")
        test_product_1.set_description("test_description_1")
        test_product_1.set_availability(True)
        test_product_2 = Product()
        test_product_2.set_name("test_product_2")
        test_product_2.set_price(2)
        test_product_2.set_image("test_image_2")
        test_product_2.set_description("test_description_2")
        test_product_2.set_availability(False)
        SimpleProductRepository.get_all_products = Mock(return_value=[test_product_1, test_product_2])
        test_handler = GetProductsRequestHandler(TestRequest(), SimpleProductRepository())
        response = test_handler.handle_request()
        assert response.status == status.HTTP_200_OK
        assert response.description == ProductSerializer([test_product_1, test_product_2]).serialize()

    def test_get_request_get_product_by_name_product_exists(self):
        test_product = Product()
        test_product.set_name("test_product")
        test_product.set_price(1)
        test_product.set_image("test_image")
        test_product.set_description("test_description")
        test_product.set_availability(True)
        SimpleProductRepository.get_product_by_name = Mock(return_value=test_product)
        exception_occurred = False
        response = None
        try:
            test_handler = GetProductByNameRequestHandler(TestRequest(), SimpleProductRepository())
            response = test_handler.handle_request()
        except Exception as e:
            exception_occurred = True
        assert response.status == status.HTTP_200_OK
        assert response.description == ProductSerializer(test_product).serialize()
        assert exception_occurred is False

    def test_get_request_get_product_by_name_product_not_exists(self):
        SimpleProductRepository.get_product_by_name = Mock(return_value=None)
        exception_occurred = False
        response = None
        try:
            test_handler = GetProductByNameRequestHandler(TestRequest(), SimpleProductRepository())
            response = test_handler.handle_request()
        except Exception as e:
            if type(e) is ProductNotFoundException:
                exception_occurred = True
        assert exception_occurred is True

    def test_delete_remove_product_by_name_product_exists(self):
        test_product = Product()
        test_product.set_name("test_product")
        test_product.set_price(1)
        test_product.set_image("test_image")
        test_product.set_description("test_description")
        test_product.set_availability(True)
        SimpleProductRepository.get_product_by_name = Mock(return_value=test_product)
        SimpleProductRepository.remove_product_by_name = Mock(return_value=None)
        exception_occurred = False
        response = None
        try:
            test_handler = RemoveProductByNameRequestHandler(TestRequest(), SimpleProductRepository())
            response = test_handler.handle_request()
        except Exception as e:
            exception_occurred = True
        assert response.status == status.HTTP_204_NO_CONTENT
        assert  response.description == "Product successfully removed"
        assert  exception_occurred is False

    def test_delete_remove_product_by_name_product_not_exists(self):
        SimpleProductRepository.get_product_by_name = Mock(return_value=None)
        SimpleProductRepository.remove_product_by_name = Mock(return_value=None)
        exception_occurred = False
        response = None
        try:
            test_handler = RemoveProductByNameRequestHandler(TestRequest(), SimpleProductRepository())
            response = test_handler.handle_request()
        except Exception as e:
            if type(e) is ProductNotFoundException:
                exception_occurred = True
        assert  exception_occurred is True