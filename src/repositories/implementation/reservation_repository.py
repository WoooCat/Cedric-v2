from typing import List, Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.infrastructure.db.models.models import Reservation
from src.repositories.abstract.abstract_reservation_repository import AbstractReservationRepository


class ReservationRepository(AbstractReservationRepository):
    def __init__(self, db: AsyncSession):
        self.db = db

    async def reserve_product(self, reservation: Reservation) -> Reservation:
        self.db.add(reservation)
        await self.db.commit()
        await self.db.refresh(reservation)
        return reservation

    async def cancel_reservation(self, reservation_id: int) -> bool:
        reservation = await self.get_reservation_by_id(reservation_id)
        if reservation:
            reservation.active = False
            await self.db.commit()
            return True
        return False

    async def get_reservation_by_id(self, reservation_id: int) -> Optional[Reservation]:
        query = select(Reservation).filter(Reservation.id == reservation_id)
        result = await self.db.execute(query)
        return result.scalar_one_or_none()

    async def get_reservations_by_product_id(self, product_id: int) -> List[Reservation]:
        query = select(Reservation).filter(Reservation.product_id == product_id)
        result = await self.db.execute(query)
        return result.scalars().all()

    async def get_all_reservations(self) -> List[Reservation]:
        query = select(Reservation)
        result = await self.db.execute(query)
        return result.scalars().all()
