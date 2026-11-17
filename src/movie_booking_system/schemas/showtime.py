from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, Field

from .audi import AudiRead
from .base import ORMModel
from .movie import MovieRead


class ShowtimeBase(BaseModel):
    starts_at: datetime
    price: Decimal = Field(gt=0, max_digits=8, decimal_places=2)  # base price


class ShowtimeCreate(ShowtimeBase):
    movie_id: int
    audi_id: int  # the cinema comes from the audi


class ShowtimeRead(ShowtimeBase, ORMModel):
    id: int
    movie: MovieRead
    audi: AudiRead  # audi.cinema is nested inside
