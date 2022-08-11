from products.domain.repo import IProductRepository
from products.domain.model import Product


class SimpleProductRepository(IProductRepository):
    products = []

    def __init__(self):
        pass

    def add_product(self, product):
        SimpleProductRepository.products.append(product)

    def remove_product_by_name(self, name):
        for product in SimpleProductRepository.products:
            if product.get_name() == name:
                SimpleProductRepository.products.remove(product)

    def get_all_products(self):
        return SimpleProductRepository.products

    def get_product_by_name(self, name):
        for product in SimpleProductRepository.products:
            if product.get_name() == name:
                return product

    def get_available_products(self):
        available_products = []
        for product in SimpleProductRepository.products:
            if product.get_availability() is True:
                available_products.append(product)
        return available_products
