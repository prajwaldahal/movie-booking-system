from datetime import datetime

from pydantic import BaseModel, Field, field_validator

from config import settings

from .base import ORMModel
from .seat import SeatRead


class HoldCreate(BaseModel):
    showtime_id: int
    seat_ids: list[int] = Field(min_length=1)
    # no user_id (comes from auth) and no expires_at (server sets now + settings.hold_minutes)

    @field_validator("seat_ids")
    @classmethod
    def check_seat_ids(cls, v: list[int]) -> list[int]:
        if len(v) != len(set(v)):
            raise ValueError("seat_ids must not contain duplicates")
        if len(v) > settings.max_seats_per_hold:
            raise ValueError(f"at most {settings.max_seats_per_hold} seats per hold")
        return v


class HoldRead(ORMModel):
    id: int
    expires_at: datetime  # frontend counts down to this, not to its own clock + 5 min
    seat: SeatRead
