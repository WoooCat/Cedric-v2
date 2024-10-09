from abc import ABC, abstractmethod
from src.infrastructure.db.models.models import Discount
from typing import Optional, List


class AbstractDiscountRepository(ABC):
    @abstractmethod
    async def add_discount(self, discount: Discount) -> Discount:
        pass

    @abstractmethod
    async def get_discount_by_id(self, discount_id: int) -> Optional[Discount]:
        pass

    @abstractmethod
    async def get_all_discounts(self) -> List[Discount]:
        pass

    @abstractmethod
    async def delete_discount(self, discount_id: int) -> bool:
        pass
