class Product:
    def __init__(self):
        self.__name = ""
        self.__price = 0
        self.__image = ""
        self.__description = ""
        self.__available = True

    def __eq__(self, other):
        return self.__name == other.get_name() and self.__price == other.get_price() and \
               self.__image == other.get_image() and self.__description == other.get_description() \
               and self.__available == other.get_availability()

    def set_name(self, name):
        self.__name = name

    def set_price(self, price):
        self.__price = price

    def set_image(self, image):
        self.__image = image

    def set_description(self, description):
        self.__description = description

    def set_availability(self, available):
        self.__available = available

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_image(self):
        return self.__image

    def get_description(self):
        return self.__description

    def get_availability(self):
        return self.__available
