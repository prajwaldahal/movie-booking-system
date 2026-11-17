from pydantic import BaseModel, Field, model_validator

from config import settings

from .base import ORMModel
from .cinema import CinemaRead
from .seat import SeatSection


MAX_ROWS = 26 * 27 


class AudiBase(BaseModel):
    name: str = Field(min_length=3, max_length=20)
    screen_width: float | None = Field(default=None, gt=0)  # metres
    screen_height: float | None = Field(default=None, gt=0)

    @model_validator(mode="after")
    def screen_both_or_neither(self):
        if (self.screen_width is None) != (self.screen_height is None):
            raise ValueError("screen_width and screen_height must be given together")
        return self


class AudiCreate(AudiBase):
    cinema_id: int
    # optional: leave columns and sections out to use the default layout
    columns: int | None = Field(default=None, gt=0)  # seats per row, numbered 1..columns
    aisle_after: list[int] = Field(default_factory=list)  # a passage after these seat numbers
    sections: list[SeatSection] | None = Field(default=None, min_length=1)  # front to back

    @model_validator(mode="after")
    def check_layout(self):
        # columns and sections only make sense as a pair
        if (self.columns is None) != (self.sections is None):
            raise ValueError("columns and sections must be given together")

        if self.columns is None:
            if self.aisle_after:
                raise ValueError("aisle_after needs columns and sections")
            return self  # default layout will be used

        if len(self.aisle_after) != len(set(self.aisle_after)):
            raise ValueError("aisle_after must not contain duplicates")
        for n in self.aisle_after:
            if not 1 <= n < self.columns:
                raise ValueError(f"aisle_after {n} must be between 1 and {self.columns - 1}")

        names = [section.name for section in self.sections]
        if len(names) != len(set(names)):
            raise ValueError("section names must be unique")

        rows = sum(section.rows for section in self.sections)
        if rows > MAX_ROWS:
            raise ValueError(f"at most {MAX_ROWS} rows, got {rows}")

        total = rows * self.columns
        if total > settings.max_seats_per_audi:
            raise ValueError(
                f"layout has {total} seats, the maximum is {settings.max_seats_per_audi}"
            )
        return self


class AudiRead(AudiBase, ORMModel):
    id: int
    cinema: CinemaRead  # needs joinedload(Audi.cinema)
