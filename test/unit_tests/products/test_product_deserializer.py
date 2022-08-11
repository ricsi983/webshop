from products.domain.deserializer import *
from products.domain.model import *
import unittest


class TestProductDeserializer(unittest.TestCase):

    def test_single_product(self):
        test_serialized_product = {
            "name": "test_product",
            "price": 1,
            "image": "test_image",
            "description": "test_description",
            "available": "False"
        }
        expected_product = Product()
        expected_product.set_name("test_product")
        expected_product.set_price(1)
        expected_product.set_image("test_image")
        expected_product.set_description("test_description")
        expected_product.set_availability(False)
        test_deserializer = ProductDeserializer(test_serialized_product)
        deserialized_test_product = test_deserializer.deserialize()
        assert deserialized_test_product == expected_product

    def test_multiple_products(self):
        test_serialized_products = \
            [
                {
                    "name": "test_product_1",
                    "price": 1,
                    "image": "test_image_1",
                    "description": "test_description_1",
                    "available": "False"
                },
                {
                    "name": "test_product_2",
                    "price": 2,
                    "image": "test_image_2",
                    "description": "test_description_2",
                    "available": "True"
                }
            ]

        test_expected_list = []
        test_expected_product_1 = Product()
        test_expected_product_1.set_name("test_product_1")
        test_expected_product_1.set_price(1)
        test_expected_product_1.set_image("test_image_1")
        test_expected_product_1.set_description("test_description_1")
        test_expected_product_1.set_availability(False)
        test_expected_list.append(test_expected_product_1)

        test_expected_product_2 = Product()
        test_expected_product_2.set_name("test_product_2")
        test_expected_product_2.set_price(2)
        test_expected_product_2.set_image("test_image_2")
        test_expected_product_2.set_description("test_description_2")
        test_expected_product_2.set_availability(True)
        test_expected_list.append(test_expected_product_2)

        test_deserializer = ProductDeserializer(test_serialized_products)

        assert test_deserializer.deserialize() == test_expected_list
