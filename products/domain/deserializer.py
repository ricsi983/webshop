from products.domain.model import Product


class ProductDeserializer:
    def __init__(self, product):
        self.__product = product

    def deserialize(self):
        if type(self.__product) is list:
            deserialized_products = []
            for product in self.__product:
                deserialized_product = Product()
                deserialized_product.set_name(product["name"])
                deserialized_product.set_price(product["price"])
                deserialized_product.set_description(product["description"])
                deserialized_product.set_image(product["image"])
                deserialized_product.set_availability(product["available"])
                deserialized_products.append(deserialized_product)
            return deserialized_products
        else:
            deserialized_product = Product()
            deserialized_product.set_name(self.__product["name"])
            deserialized_product.set_price(self.__product["price"])
            deserialized_product.set_description(self.__product["description"])
            deserialized_product.set_image(self.__product["image"])
            deserialized_product.set_availability(self.__product["available"])
            return deserialized_product
