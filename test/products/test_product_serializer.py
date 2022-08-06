from products.domain.serializer import *
from products.domain.model import *
import unittest


class TestProductSerializer(unittest.TestCase):

    def test_single_product(self):
        test_product = Product()
        test_product.set_name("test_product")
        test_product.set_price(1)
        test_product.set_image("test_image")
        test_product.set_description("test_description")
        test_product.set_availability(False)

        test_serializer = ProductSerializer(test_product)
        expected_result = {
            "name": "test_product",
            "price": 1,
            "image": "test_image",
            "description": "test_description",
            "available": False
        }
        assert test_serializer.serialize() == expected_result

    def test_multiple_products(self):
        test_product_list = []
        test_product_1 = Product()
        test_product_1.set_name("test_product_1")
        test_product_1.set_price(1)
        test_product_1.set_image("test_image_1")
        test_product_1.set_description("test_description_1")
        test_product_1.set_availability(False)
        test_product_list.append(test_product_1)

        test_product_2 = Product()
        test_product_2.set_name("test_product_2")
        test_product_2.set_price(2)
        test_product_2.set_image("test_image_2")
        test_product_2.set_description("test_description_2")
        test_product_2.set_availability(True)
        test_product_list.append(test_product_2)

        test_serializer = ProductSerializer(test_product_list)
        expected_result = [
            {
                "name": "test_product_1",
                "price": 1,
                "image": "test_image_1",
                "description": "test_description_1",
                "available": False
            },
            {
                "name": "test_product_2",
                "price": 2,
                "image": "test_image_2",
                "description": "test_description_2",
                "available": False
            }
        ]
        assert test_serializer.serialize() == expected_result
