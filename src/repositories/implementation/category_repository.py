from typing import List, Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from src.infrastructure.db.models.models import Category
from src.repositories.abstract.abstract_category_repository import AbstractCategoryRepository


class CategoryRepository(AbstractCategoryRepository):
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all_categories(self) -> List[Category]:
        query = select(Category).options(selectinload(Category.subcategories))
        result = await self.db.execute(query)
        categories = result.scalars().all()
        parent_categories = [category for category in categories if category.parent_id is None]
        return parent_categories

    async def add_category(self, category: Category) -> Category:
        self.db.add(category)
        await self.db.commit()
        await self.db.refresh(category)
        return category

    async def get_category_by_id(self, category_id: int) -> Optional[Category]:
        query = select(Category).options(selectinload(Category.subcategories)).filter(Category.id == category_id)
        result = await self.db.execute(query)
        category = result.scalar_one_or_none()
        if category:
            await self._load_all_subcategories(category)
        return category

    async def get_category_by_name(self, name: str) -> Optional[Category]:
        query = select(Category).options(selectinload(Category.subcategories)).where(Category.name == name)
        result = await self.db.execute(query)
        category = result.scalar_one_or_none()
        if category:
            await self._load_all_subcategories(category)
        return category

    async def update_category_by_id(self, category_id: int, updated_data: dict) -> Optional[Category]:
        category = await self.get_category_by_id(category_id)
        if not category:
            return None

        for key, value in updated_data.items():
            setattr(category, key, value)

        self.db.add(category)
        await self.db.commit()
        await self.db.refresh(category)
        await self._load_all_subcategories(category)
        return category

    async def delete_category_by_id(self, category_id: int) -> bool:
        category = await self.get_category_by_id(category_id)
        if not category:
            return False
        await self.db.delete(category)
        await self.db.commit()
        return True

    async def _load_all_subcategories(self, category: Category):
        queue = [category]
        while queue:
            current_category = queue.pop(0)
            await self.db.refresh(current_category, attribute_names=["subcategories"])
            queue.extend(current_category.subcategories)
