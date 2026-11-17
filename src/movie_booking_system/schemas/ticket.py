from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel

from .base import ORMModel
from .seat import SeatRead
from .showtime import ShowtimeRead


class TicketCreate(BaseModel):
    showtime_id: int
    seat_id: int
    # no user_id (comes from auth) and no price (server works it out)


class TicketRead(ORMModel):
    id: int
    price: Decimal  # what was actually paid
    booked_at: datetime
    seat: SeatRead
    showtime: ShowtimeRead
