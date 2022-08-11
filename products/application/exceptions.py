class ProductNotFoundException(Exception):
    def __init__(self, message="Requested product not found"):
        super().__init__(message)


class InvalidProductRequestException(Exception):
    def __init__(self, message="Invalid request to product API"):
        super().__init__(message)


class ProductAlreadyAddedException(Exception):
    def __init__(self, message="Product already added to database"):
        super().__init__(message)


class ProductRequestHandlerNotFoundException(Exception):
    def __init__(self, message="Request handler not found"):
        super().__init__(message)
