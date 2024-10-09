from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

from src.infrastructure.db.context_managers import transaction_context
from src.infrastructure.db.models.models import Product, Category
from src.repositories.abstract.abstract_product_repository import AbstractProductRepository
from typing import List, Optional


class ProductRepository(AbstractProductRepository):
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all_products(self) -> List[Product]:
        query = (
            select(Product)
                .options(
                selectinload(Product.discount),
                selectinload(Product.reservations)
            )
        )
        result = await self.db.execute(query)
        products = result.scalars().all()
        return products

    async def add_product(self, product: Product) -> Product:
        async with transaction_context(self.db):
            self.db.add(product)
            await self.db.commit()
            await self.db.refresh(product)
        return product

    async def get_product_by_id(self, product_id: int) -> Optional[Product]:
        query = select(Product).options(
            selectinload(Product.reservations),
            selectinload(Product.discount)).filter(Product.id == product_id)
        result = await self.db.execute(query)
        return result.scalar_one_or_none()

    async def update_product(self, product_id: int, updated_data: dict) -> Product:
        async with transaction_context(self.db):
            product = await self.get_product_by_id(product_id)
            if product:
                self._update_product_fields(product, updated_data)
                await self.db.commit()
                await self.db.refresh(product)
        return product

    async def update_price(self, product_id: int, new_price: float) -> Product:
        async with transaction_context(self.db):
            product = await self.get_product_by_id(product_id)
            if product:
                product.price = new_price
                await self.db.commit()
                await self.db.refresh(product)
            return product

    async def delete_product(self, product_id: int) -> bool:
        async with transaction_context(self.db):
            product = await self.get_product_by_id(product_id)
            if not product:
                return False
            await self.db.delete(product)
            await self.db.commit()
            return True

    async def get_products_by_category(self, category_id: int) -> List[Product]:
        query = (
            select(Product)
            .options(selectinload(Product.reservations))
            .filter(
                (Product.category_id == category_id) |
                (Product.category.has(Category.parent_id == category_id)),
                Product.stock > 0
            )
        )
        result = await self.db.execute(query)
        products = result.scalars().all()
        return products

    async def add_discount_to_product(self, product_id: int, discount_id: int) -> Product:
        async with transaction_context(self.db):
            product = await self.get_product_by_id(product_id)
            product.discount_id = discount_id
            await self.db.commit()
            await self.db.refresh(product)
        return product

    async def remove_discount_from_product(self, product_id: int) -> Product:
        async with transaction_context(self.db):
            product = await self.get_product_by_id(product_id)
            product.discount_id = None
            await self.db.commit()
            await self.db.refresh(product)
        return product

    @staticmethod
    def _update_product_fields(product: Product, updated_data: dict) -> None:
        for key, value in updated_data.items():
            setattr(product, key, value)
