from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.db.database import get_db
from src.repositories.implementation.category_repository import CategoryRepository
from src.repositories.implementation.discount_repository import DiscountRepository
from src.repositories.implementation.product_repository import ProductRepository
from src.repositories.implementation.reservation_repository import ReservationRepository


def get_product_repository(db: AsyncSession = Depends(get_db)) -> ProductRepository:
    return ProductRepository(db)


def get_category_repository(db: AsyncSession = Depends(get_db)) -> CategoryRepository:
    return CategoryRepository(db)


def get_discount_repository(db: AsyncSession = Depends(get_db)) -> DiscountRepository:
    return DiscountRepository(db)


def get_reservation_repository(db: AsyncSession = Depends(get_db)) -> ReservationRepository:
    return ReservationRepository(db)

