from fastapi import Depends
from src.dependencies.repository_dependencies import get_category_repository, get_product_repository, \
    get_discount_repository, get_reservation_repository
from src.repositories.implementation.category_repository import CategoryRepository
from src.repositories.implementation.discount_repository import DiscountRepository
from src.repositories.implementation.product_repository import ProductRepository
from src.repositories.implementation.reservation_repository import ReservationRepository

from src.services.category_service import CategoryService
from src.services.discount_service import DiscountService
from src.services.product_service import ProductService
from src.services.reservation_service import ReservationService


def get_category_service(category_repo: CategoryRepository = Depends(get_category_repository)) -> CategoryService:
    return CategoryService(category_repo)


def get_product_service(
    product_repo: ProductRepository = Depends(get_product_repository),
    category_repo: CategoryRepository = Depends(get_category_repository),
    discount_repo: DiscountRepository = Depends(get_discount_repository),
) -> ProductService:
    return ProductService(product_repo, category_repo, discount_repo)


def get_discount_service(discount_repo: DiscountRepository = Depends(get_discount_repository)) -> DiscountService:
    return DiscountService(discount_repo)


def get_reservation_service(
        reservation_repo: ReservationRepository = Depends(get_reservation_repository),
        product_repo: ProductRepository = Depends(get_product_repository),
) -> ReservationService:
    return ReservationService(reservation_repo, product_repo)