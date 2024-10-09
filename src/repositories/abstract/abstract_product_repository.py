from abc import ABC, abstractmethod

from src.infrastructure.db.models.models import Product


class AbstractProductRepository(ABC):

    @abstractmethod
    async def get_all_products(self):
        pass

    @abstractmethod
    async def add_product(self, product):
        pass

    @abstractmethod
    async def get_product_by_id(self, product_id: int):
        pass

    @abstractmethod
    async def update_product(self, product_id: int, updated_data: dict):
        pass

    @abstractmethod
    async def update_price(self, product_id: int, new_price: float):
        pass

    @abstractmethod
    async def delete_product(self, product_id: int):
        pass

    @abstractmethod
    async def get_products_by_category(self, category_id: int):
        pass

    @abstractmethod
    async def add_discount_to_product(self, product_id: int, discount_id: int) -> Product:
        pass

    @abstractmethod
    async def remove_discount_from_product(self, product_id: int) -> Product:
        pass


