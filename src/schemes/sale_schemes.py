from pydantic import BaseModel
from datetime import datetime


class SaleBase(BaseModel):
    product_id: int
    quantity: int
    discount: float
    sold_at: datetime = datetime.utcnow()

    class Config:
        from_attributes = True


class SaleCreateRequest(SaleBase):
    pass


class SaleResponse(SaleBase):
    id: int
