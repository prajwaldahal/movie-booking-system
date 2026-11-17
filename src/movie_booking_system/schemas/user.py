from datetime import datetime

from pydantic import BaseModel, EmailStr, Field

from .base import ORMModel


class UserBase(BaseModel):
    email: EmailStr  # pip install "pydantic[email]"
    name: str = Field(min_length=1, max_length=100)


class UserCreate(UserBase):
    password: str = Field(min_length=8)


class UserRead(UserBase, ORMModel):
    id: int
    created_at: datetime
    # no password / hashed_password here, ever
