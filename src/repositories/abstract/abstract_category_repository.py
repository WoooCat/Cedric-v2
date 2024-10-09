from abc import ABC, abstractmethod
from typing import Optional

from src.infrastructure.db.models.models import Category


class AbstractCategoryRepository(ABC):

    @abstractmethod
    async def get_all_categories(self):
        pass

    @abstractmethod
    async def add_category(self, category: Category) -> Category:
        pass

    @abstractmethod
    async def get_category_by_id(self, category_id: int) -> Category:
        pass

    @abstractmethod
    async def get_category_by_name(self, name: str) -> Optional[Category]:
        pass

    @abstractmethod
    async def update_category_by_id(self, category_id: int, updated_data) -> Category:
        pass

    @abstractmethod
    async def delete_category_by_id(self, category_id: int) -> Category:
        pass
