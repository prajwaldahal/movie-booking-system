from pydantic import BaseModel, Field

from .base import ORMModel


class CinemaBase(BaseModel):
    name: str = Field(min_length=1, max_length=150)
    city: str
    address: str | None = None


class CinemaCreate(CinemaBase):
    pass


class CinemaRead(CinemaBase, ORMModel):
    id: int
