from abc import ABC, abstractmethod


class IProductRepository(ABC):

    @abstractmethod
    def add_product(self, crypto):
        pass

    @abstractmethod
    def remove_product_by_name(self, symbol):
        pass

    @abstractmethod
    def get_all_products(self):
        pass

    @abstractmethod
    def get_product_by_name(self, name):
        pass

    @abstractmethod
    def get_available_products(self):
        pass
