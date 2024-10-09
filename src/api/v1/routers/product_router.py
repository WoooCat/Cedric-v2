from typing import List

from fastapi import APIRouter, Depends, status
from src.dependencies.service_dependencies import get_product_service
from src.schemes.product_schemes import ProductCreateRequest, ProductResponse, ProductUpdateRequest, \
    ProductPriceUpdateRequest
from src.services.product_service import ProductService

router = APIRouter(
    prefix="/products",
    tags=["products"],
)


@router.get("/", response_model=List[ProductResponse])
async def get_all_products(product_service: ProductService = Depends(get_product_service)):
    return await product_service.get_all_products()


@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def add_product(product_data: ProductCreateRequest, product_service: ProductService = Depends(get_product_service)):
    product = await product_service.add_product(product_data.dict())
    return product


@router.get("/{product_id}", response_model=ProductResponse)
async def get_product_by_id(product_id: int, product_service: ProductService = Depends(get_product_service)):
    return await product_service.get_product_by_id(product_id)


@router.put("/{product_id}", response_model=ProductResponse)
async def update_product(
    product_id: int,
    product_data: ProductUpdateRequest,
    product_service: ProductService = Depends(get_product_service)
):
    updated_product = await product_service.update_product(product_id, product_data.dict())
    return updated_product


@router.patch("/{product_id}/price", response_model=ProductResponse)
async def update_price(
    product_id: int,
    price_data: ProductPriceUpdateRequest,
    product_service: ProductService = Depends(get_product_service)
):
    updated_product = await product_service.update_price(product_id, price_data.price)
    return updated_product


@router.delete("/{product_id}")
async def delete_product(product_id: int, product_service: ProductService = Depends(get_product_service)):
    await product_service.delete_product(product_id)
    return {"detail": f"Product with ID '{product_id}' has been successfully deleted."}


@router.get("/category/{category_id}", response_model=List[ProductResponse])
async def get_products_by_category(
    category_id: int,
    product_service: ProductService = Depends(get_product_service)
):
    return await product_service.get_products_by_category(category_id)


@router.post("/products/{product_id}/discount", response_model=ProductResponse)
async def add_discount_to_product(
    product_id: int,
    discount_id: int,
    product_service: ProductService = Depends(get_product_service)
):
    return await product_service.add_discount_to_product(product_id, discount_id)


@router.delete("/products/{product_id}/discount", response_model=ProductResponse)
async def remove_discount_from_product(
    product_id: int,
    product_service: ProductService = Depends(get_product_service)
):
    return await product_service.remove_discount_from_product(product_id)
