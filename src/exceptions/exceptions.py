class BaseAppException(Exception):
    """Base exception for all custom exceptions in the application."""
    def __init__(self, message: str, status_code: int = 400, **kwargs):
        formatted_message = message.format(**kwargs)
        super().__init__(formatted_message)
        self.message = formatted_message
        self.status_code = status_code


class CategoryNotFoundError(BaseAppException):
    """Exception raised when a requested category is not found."""
    def __init__(self, category_id: int = None, name: str = None):
        if category_id is not None:
            message = f"Category with ID {category_id} not found."
        elif name is not None:
            message = f"Category with name '{name}' not found."
        else:
            message = "Category not found."
        super().__init__(message, status_code=404)
        # super().__init__(f"Category with ID {category_id} not found.", status_code=404)


class ProductNotFoundError(BaseAppException):
    """Exception raised when a requested category is not found."""
    def __init__(self, product_id: int = None, product_name: str = None):
        if product_id is not None:
            message = f"Product with ID {product_id} not found."
        elif product_name is not None:
            message = f"Product with name '{product_name}' not found."
        else:
            message = "Product not found."
        super().__init__(message, status_code=404)


class DiscountNotFoundError(BaseAppException):
    """Exception raised when a requested discount is not found."""
    def __init__(self, discount_id: int = None, discount_name: str = None):
        if discount_id is not None:
            message = f"Discount with ID {discount_id} not found."
        elif discount_name is not None:
            message = f"Discount with name '{discount_name}' not found."
        else:
            message = "Discount not found."
        super().__init__(message, status_code=404)


class NotEnoughStockError(BaseAppException):
    """Exception raised when there is not enough stock to fulfill the reservation."""
    def __init__(self, product_id: int, available_quantity: int = None, requested_quantity: int = None):
        if available_quantity is not None and requested_quantity is not None:
            message = f"Not enough stock for Product ID {product_id}. Available: {available_quantity}, Requested: {requested_quantity}."
        else:
            message = f"Not enough stock for Product ID {product_id}."
        super().__init__(message, status_code=400)


class ReservationNotFoundError(BaseAppException):
    """Exception raised when a requested reservation is not found."""
    def __init__(self, reservation_id: int):
        message = f"Reservation with ID {reservation_id} not found."
        super().__init__(message, status_code=404)
