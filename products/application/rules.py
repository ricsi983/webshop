'''from cryptos.application.exceptions import *


class GetCryptoByNameOrSymbolRequestRule:
    def __init__(self, request):
        self.__request = request

    def check(self):
        if "symbol" or "name" not in self.__request.query_params:
            raise InvalidCryptoRequestException()


class AddCryptoRule:
    def __init__(self, request):
        self.__request = request

    def check(self):
        pass'''
