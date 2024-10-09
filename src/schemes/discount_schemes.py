from pydantic import BaseModel


class DiscountCreateRequest(BaseModel):
    name: str
    percentage: float
    description: str = None


class DiscountResponse(BaseModel):
    id: int
    name: str
    percentage: float
    description: str = None

    class Config:
        from_attributes = True
