#from cryptos.domain.repo import ICryptoRepository
#from cryptos.domain.model import Crypto
import requests
import json

coingecko_api = "https://api.coingecko.com/api/v3/"


'''class ExternalCryptoRepository(ICryptoRepository):
    def add_crypto(self, crypto):
        pass

    def remove_crypto_by_symbol(self, symbol):
        pass

    def remove_crypto_by_name(self, name):
        pass

    def get_cryptos(self):
        crypto_list = []
        available_cryptos = requests.get(coingecko_api + "/coins/list").json()
        for available_crypto in available_cryptos:
            crypto = Crypto()
            crypto.set_name(available_crypto["name"])
            crypto.set_symbol(available_crypto["id"])
            crypto.set_currency("USD")
            crypto_list.append(crypto)
        return crypto_list

    def get_crypto_by_name(self, name):
        pass

    def get_crypto_by_symbol(self, symbol):
        crypto = Crypto()
        requested_crypto = requests.get(coingecko_api + "")'''

