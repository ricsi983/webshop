from products.domain.model import Product
from products.application.exceptions import *


class ProductDeserializer:
    def __init__(self, product):
        self.__product = product

    def deserialize(self):
        try:
            if type(self.__product) is list:
                deserialized_products = []
                for product in self.__product:
                    deserialized_product = Product()
                    deserialized_product.set_name(product["name"])
                    deserialized_product.set_price(product["price"])
                    deserialized_product.set_description(product["description"])
                    deserialized_product.set_image(product["image"])
                    if product["available"] == "True":
                        deserialized_product.set_availability(True)
                    else:
                        deserialized_product.set_availability(False)
                    deserialized_products.append(deserialized_product)
                return deserialized_products
            else:
                deserialized_product = Product()
                deserialized_product.set_name(self.__product["name"])
                deserialized_product.set_price(self.__product["price"])
                deserialized_product.set_description(self.__product["description"])
                deserialized_product.set_image(self.__product["image"])
                if self.__product["available"] == "True":
                    deserialized_product.set_availability(True)
                else:
                    deserialized_product.set_availability(False)
                return deserialized_product
        except KeyError:
            raise InvalidProductRequestException()
