
class ProductSerializer:
    def __init__(self, product):
        self.__product = product

    def serialize(self):
        if type(self.__product) is list:
            serialized_products = []
            for product in self.__product:
                serialized_product = {
                    "name": product.get_name(),
                    "price": product.get_price(),
                    "image": product.get_image(),
                    "description": product.get_description(),
                    "available": product.get_availability()
                }
                serialized_products.append(serialized_product)
            return serialized_products
        else:
            serialized_product = {
                "name": self.__product.get_name(),
                "price": self.__product.get_price(),
                "image": self.__product.get_image(),
                "description": self.__product.get_description(),
                "available": self.__product.get_availability()
            }
            return serialized_product
