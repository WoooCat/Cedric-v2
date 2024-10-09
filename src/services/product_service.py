from src.exceptions.exceptions import ProductNotFoundError, CategoryNotFoundError, DiscountNotFoundError
from src.infrastructure.db.models.models import Product
from src.repositories.abstract.abstract_category_repository import AbstractCategoryRepository
from src.repositories.abstract.abstract_discount_repository import AbstractDiscountRepository
from src.repositories.abstract.abstract_product_repository import AbstractProductRepository
from typing import List


class ProductService:
    def __init__(
            self,
            product_repo: AbstractProductRepository,
            category_repo: AbstractCategoryRepository,
            discount_repo: AbstractDiscountRepository,
    ):
        self.product_repo = product_repo
        self.category_repo = category_repo
        self.discount_repo = discount_repo

    async def get_all_products(self) -> List[Product]:
        return await self.product_repo.get_all_products()

    async def add_product(self, product_data: dict) -> Product:
        category_id = product_data.get('category_id')
        category = await self.category_repo.get_category_by_id(category_id)
        if not category:
            raise CategoryNotFoundError(category_id=category_id)

        new_product = Product(**product_data)
        return await self.product_repo.add_product(new_product)

    async def get_product_by_id(self, product_id: int) -> Product:
        product = await self.product_repo.get_product_by_id(product_id)
        if not product:
            raise ProductNotFoundError(product_id=product_id)
        return product

    async def update_product(self, product_id: int, updated_data: dict) -> Product:
        product = await self.product_repo.update_product(product_id, updated_data)
        if not product:
            raise ProductNotFoundError(product_id=product_id)
        return product

    async def update_price(self, product_id: int, new_price: float) -> Product:
        product = await self.product_repo.update_price(product_id, new_price)
        if not product:
            raise ProductNotFoundError(product_id=product_id)
        return product

    async def delete_product(self, product_id: int) -> None:
        success = await self.product_repo.delete_product(product_id)
        if not success:
            raise ProductNotFoundError(product_id=product_id)

    async def get_products_by_category(self, category_id: int) -> List[Product]:
        category = await self.category_repo.get_category_by_id(category_id)
        if not category:
            raise CategoryNotFoundError(category_id=category_id)
        return await self.product_repo.get_products_by_category(category_id)

    async def add_discount_to_product(self, product_id: int, discount_id: int) -> Product:
        product = await self.product_repo.get_product_by_id(product_id)
        if not product:
            raise ProductNotFoundError(product_id=product_id)

        discount = await self.discount_repo.get_discount_by_id(discount_id)
        if not discount:
            raise DiscountNotFoundError(discount_id=discount_id)

        return await self.product_repo.add_discount_to_product(product_id, discount_id)

    async def remove_discount_from_product(self, product_id: int) -> Product:
        return await self.product_repo.remove_discount_from_product(product_id)

