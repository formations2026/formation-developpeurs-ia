"""Schémas d'entrée et de sortie de l'API (Pydantic)."""
from __future__ import annotations

from datetime import UTC, datetime

from pydantic import BaseModel, Field, field_validator, model_validator


def to_utc(value: datetime) -> datetime:
    """Normalise une date en UTC. Une date sans fuseau est considérée comme UTC."""
    if value.tzinfo is None:
        return value.replace(tzinfo=UTC)
    return value.astimezone(UTC)


class Room(BaseModel):
    id: int
    name: str
    capacity: int


class RoomPage(BaseModel):
    items: list[Room]
    total: int
    page: int
    size: int


class BookingIn(BaseModel):
    room_id: int = Field(gt=0)
    title: str = Field(min_length=1, max_length=120)
    start_at: datetime
    end_at: datetime

    @field_validator("start_at", "end_at")
    @classmethod
    def _normalise(cls, value: datetime) -> datetime:
        return to_utc(value)

    @model_validator(mode="after")
    def _check_order(self) -> BookingIn:
        if self.end_at <= self.start_at:
            raise ValueError("end_at doit être postérieur à start_at")
        return self


class Booking(BaseModel):
    ref: str
    room_id: int
    owner_id: int
    title: str
    start_at: datetime
    end_at: datetime
