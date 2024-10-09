from typing import List

from fastapi import APIRouter, Depends
from src.dependencies.service_dependencies import get_reservation_service
from src.schemes.reservation_schemes import ReservationResponse, ReservationRequest

from src.services.reservation_service import ReservationService

router = APIRouter(
    prefix="/reservation",
    tags=["reservation"],
)


@router.post("/", response_model=ReservationResponse, status_code=201)
async def reserve_product(
    reservation_data: ReservationRequest,
    reservation_service: ReservationService = Depends(get_reservation_service)
):
    reservation = await reservation_service.reserve_product(
        product_id=reservation_data.product_id,
        quantity=reservation_data.quantity,
    )
    return reservation


@router.get("/", response_model=List[ReservationResponse])
async def get_all_reservations(
    reservation_service: ReservationService = Depends(get_reservation_service)
):
    return await reservation_service.get_all_reservations()


@router.get("/{reservation_id}", response_model=ReservationResponse)
async def get_reservation_by_id(
    reservation_id: int,
    reservation_service: ReservationService = Depends(get_reservation_service)
):
    reservation = await reservation_service.get_reservation_by_id(reservation_id)
    return reservation


@router.get("/product/{product_id}", response_model=List[ReservationResponse])
async def get_reservations_by_product_id(
    product_id: int,
    reservation_service: ReservationService = Depends(get_reservation_service)
):
    reservations = await reservation_service.get_reservations_by_product_id(product_id)
    return reservations


@router.patch("/{reservation_id}/cancel", status_code=204)
async def cancel_reservation(
    reservation_id: int,
    reservation_service: ReservationService = Depends(get_reservation_service)
):
    await reservation_service.cancel_reservation(reservation_id)
    return {"detail": f"Reservation {reservation_id} has been canceled."}
