from decimal import Decimal
from typing import Literal

from pydantic import BaseModel, Field

from .base import ORMModel


class SeatBlock(BaseModel):
    gap_before: int = Field(default=0, ge=0, le=20)
    count: int = Field(gt=0, le=40)


class SeatRowLayout(BaseModel):
    label: str = Field(pattern=r"^[A-Z]{1,2}$")  
    category: str = Field(min_length=1, max_length=30)
    blocks: list[SeatBlock] = Field(min_length=1)


class SeatCategoryBase(BaseModel):
    name: str = Field(min_length=1, max_length=30)
    price_multiplier: Decimal = Field(default=Decimal("1.00"), gt=0, max_digits=4, decimal_places=2)


class CategoryPricing(SeatCategoryBase):
    pass


class SeatCategoryRead(SeatCategoryBase, ORMModel):
    id: int


class SeatRead(ORMModel):
    id: int
    label: str  
    row_label: str
    seat_number: int
    grid_row: int
    grid_col: int
    category: SeatCategoryRead


class SeatMapItem(BaseModel):
    id: int
    label: str
    category: str
    grid_row: int
    grid_col: int
    status: Literal["available", "booked"]