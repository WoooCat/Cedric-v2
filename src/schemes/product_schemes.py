from pydantic import BaseModel
from typing import Optional


class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    stock: Optional[int] = None

    class Config:
        from_attributes = True


class ProductCreateRequest(ProductBase):
    category_id: int


class ProductPriceUpdateRequest(BaseModel):
    price: float

    class Config:
        from_attributes = True


class ProductUpdateRequest(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    category_id: Optional[int] = None
    stock: Optional[int] = None

    class Config:
        from_attributes = True


class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float
    final_price: float
    category_id: int
    discount_id: Optional[int] = None
    stock: Optional[int] = None
    reserved_quantity: Optional[int] = None

    class Config:
        from_attributes = True
