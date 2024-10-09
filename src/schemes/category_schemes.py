from typing import List, Optional

from pydantic import BaseModel

"""CATEGORY SCHEMES"""


class CategoryBase(BaseModel):
    name: str

    class Config:
        from_attributes = True


class CategoryCreateRequest(CategoryBase):
    parent_id: Optional[int] = None


class CategoryUpdateRequest(CategoryBase):
    name: Optional[str] = None


class CategoryResponse(CategoryBase):
    id: int
    parent_id: Optional[int] = None
    subcategories: Optional[List['CategoryResponse']] = []
