class ProductNotFoundException(Exception):
    def __init__(self, message="Requested product not found"):
        super().__init__(message)


class InvalidProductRequestException(Exception):
    def __init__(self, message="Invalid request to product API"):
        super().__init__(message)
