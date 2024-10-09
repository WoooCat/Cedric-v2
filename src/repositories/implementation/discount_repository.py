from typing import Optional, List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.infrastructure.db.models.models import Discount
from src.repositories.abstract.abstract_discount_repository import AbstractDiscountRepository


class DiscountRepository(AbstractDiscountRepository):
    def __init__(self, db: AsyncSession):
        self.db = db

    async def add_discount(self, discount: Discount) -> Discount:
        self.db.add(discount)
        await self.db.commit()
        await self.db.refresh(discount)
        return discount

    async def get_discount_by_id(self, discount_id: int) -> Optional[Discount]:
        query = select(Discount).filter(Discount.id == discount_id)
        result = await self.db.execute(query)
        return result.scalar_one_or_none()

    async def get_all_discounts(self) -> List[Discount]:
        query = select(Discount)
        result = await self.db.execute(query)
        return result.scalars().all()

    async def delete_discount(self, discount_id: int) -> bool:
        discount = await self.get_discount_by_id(discount_id)
        if discount:
            await self.db.delete(discount)
            await self.db.commit()
            return True
        return False
