from typing import List, Optional

from src.exceptions.exceptions import NotEnoughStockError, ReservationNotFoundError, ProductNotFoundError
from src.repositories.abstract.abstract_reservation_repository import AbstractReservationRepository
from src.repositories.abstract.abstract_product_repository import AbstractProductRepository
from src.infrastructure.db.models.models import Reservation


class ReservationService:
    def __init__(self, reservation_repo: AbstractReservationRepository, product_repo: AbstractProductRepository):
        self.reservation_repo = reservation_repo
        self.product_repo = product_repo

    async def reserve_product(self, product_id: int, quantity: int) -> Reservation:
        product = await self.product_repo.get_product_by_id(product_id)
        if not product:
            raise ProductNotFoundError(product_id=product_id)
        if product.stock < quantity:
            raise NotEnoughStockError(product_id=product_id)

        reservation = Reservation(product_id=product_id, quantity=quantity)
        product.stock -= quantity
        await self.product_repo.update_product(product_id, {"stock": product.stock})
        return await self.reservation_repo.reserve_product(reservation)

    async def cancel_reservation(self, reservation_id: int) -> None:
        reservation = await self.reservation_repo.get_reservation_by_id(reservation_id)
        if not reservation or not reservation.active:
            raise ReservationNotFoundError(reservation_id=reservation_id)

        product = await self.product_repo.get_product_by_id(reservation.product_id)
        product.stock += reservation.quantity

        await self.product_repo.update_product(product.id, {"stock": product.stock})
        await self.reservation_repo.cancel_reservation(reservation_id)

    async def get_all_reservations(self) -> List[Reservation]:
        return await self.reservation_repo.get_all_reservations()

    async def get_reservation_by_id(self, reservation_id: int) -> Optional[Reservation]:
        reservation = await self.reservation_repo.get_reservation_by_id(reservation_id)
        if not reservation:
            raise ReservationNotFoundError(reservation_id=reservation_id)
        return reservation

    async def get_reservations_by_product_id(self, product_id: int) -> List[Reservation]:
        reservations = await self.reservation_repo.get_reservations_by_product_id(product_id)
        product = await self.product_repo.get_product_by_id(product_id)
        if not product:
            raise ProductNotFoundError(product_id=product_id)
        if not reservations:
            raise ProductNotFoundError()
        return reservations
