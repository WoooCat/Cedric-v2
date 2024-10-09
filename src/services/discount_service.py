from src.exceptions.exceptions import DiscountNotFoundError
from src.repositories.abstract.abstract_discount_repository import AbstractDiscountRepository
from src.infrastructure.db.models.models import Discount
from typing import List


class DiscountService:
    def __init__(self, discount_repo: AbstractDiscountRepository):
        self.discount_repo = discount_repo

    async def add_discount(self, discount_data: dict) -> Discount:
        new_discount = Discount(**discount_data)
        return await self.discount_repo.add_discount(new_discount)

    async def get_discount_by_id(self, discount_id: int) -> Discount:
        discount = await self.discount_repo.get_discount_by_id(discount_id)
        if not discount:
            raise DiscountNotFoundError(discount_id=discount_id)
        return discount

    async def get_all_discounts(self) -> List[Discount]:
        return await self.discount_repo.get_all_discounts()

    async def delete_discount(self, discount_id: int) -> None:
        success = await self.discount_repo.delete_discount(discount_id)
        if not success:
            raise DiscountNotFoundError(discount_id=discount_id)
