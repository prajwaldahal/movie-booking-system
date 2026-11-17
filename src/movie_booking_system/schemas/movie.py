from pydantic import BaseModel, Field

from .base import ORMModel


class MovieBase(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: str | None = None
    duration_minutes: int = Field(gt=0)
    rating: str | None = None


class MovieCreate(MovieBase):
    pass


class MovieRead(MovieBase, ORMModel):
    id: int
