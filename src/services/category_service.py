from src.exceptions.exceptions import CategoryNotFoundError
from src.infrastructure.db.models.models import Category
from src.repositories.abstract.abstract_category_repository import AbstractCategoryRepository


class CategoryService:
    def __init__(self, category_repo: AbstractCategoryRepository):
        self.category_repo = category_repo

    async def get_all_categories(self):
        return await self.category_repo.get_all_categories()

    async def add_category(self, category_data: dict) -> Category:
        parent_id = category_data.get("parent_id")
        if parent_id is not None:
            await self.get_category_by_id(parent_id)

        new_category = Category(**category_data)
        return await self.category_repo.add_category(new_category)

    async def get_category_by_id(self, category_id: int) -> Category:
        category = await self.category_repo.get_category_by_id(category_id)
        if not category:
            raise CategoryNotFoundError(category_id=category_id)
        return category

    async def get_category_by_name(self, name: str) -> Category:
        category = await self.category_repo.get_category_by_name(name)
        if not category:
            raise CategoryNotFoundError(name=name)
        return category

    async def update_category_by_id(self, category_id: int, updated_data: dict) -> Category:
        category = await self.category_repo.update_category_by_id(category_id, updated_data)
        if not category:
            raise CategoryNotFoundError(category_id=category_id)
        return category

    async def delete_category(self, category_id: int) -> None:
        success = await self.category_repo.delete_category_by_id(category_id)
        if not success:
            raise CategoryNotFoundError(category_id=category_id)

