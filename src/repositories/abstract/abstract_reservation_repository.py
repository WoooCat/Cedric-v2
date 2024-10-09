from abc import ABC, abstractmethod
from src.infrastructure.db.models.models import Reservation
from typing import Optional, List


class AbstractReservationRepository(ABC):
    @abstractmethod
    async def get_all_reservations(self) -> List[Reservation]:
        pass

    @abstractmethod
    async def reserve_product(self, reservation: Reservation) -> Reservation:
        pass

    @abstractmethod
    async def get_reservation_by_id(self, reservation_id: int) -> Optional[Reservation]:
        pass

    @abstractmethod
    async def get_reservations_by_product_id(self, product_id: int) -> List[Reservation]:
        pass

    @abstractmethod
    async def cancel_reservation(self, reservation_id: int) -> bool:
        pass
