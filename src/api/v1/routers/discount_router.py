from typing import List
from fastapi import APIRouter, Depends
from src.dependencies.service_dependencies import get_discount_service
from src.schemes.discount_schemes import DiscountResponse, DiscountCreateRequest
from src.services.discount_service import DiscountService

router = APIRouter(
    prefix="/discount",
    tags=["discount"],
)


@router.post("/", response_model=DiscountResponse)
async def add_discount(
        discount_data: DiscountCreateRequest,
        discount_service: DiscountService = Depends(get_discount_service)
):
    return await discount_service.add_discount(discount_data.dict())


@router.get("/{discount_id}", response_model=DiscountResponse)
async def get_discount_by_id(
        discount_id: int,
        discount_service: DiscountService = Depends(get_discount_service)
):
    return await discount_service.get_discount_by_id(discount_id)


@router.get("/", response_model=List[DiscountResponse])
async def get_all_discounts(
        discount_service: DiscountService = Depends(get_discount_service)
):
    return await discount_service.get_all_discounts()


@router.delete("/{discount_id}", status_code=204)
async def delete_discount(
        discount_id: int,
        discount_service: DiscountService = Depends(get_discount_service)
):
    await discount_service.delete_discount(discount_id)
