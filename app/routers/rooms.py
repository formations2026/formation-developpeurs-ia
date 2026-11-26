"""Routes des salles."""
from __future__ import annotations

import sqlite3
from datetime import datetime
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, status

from app import repository
from app.db import get_db
from app.schemas import Room, RoomPage, to_utc

router = APIRouter(prefix="/rooms", tags=["salles"])
Db = Annotated[sqlite3.Connection, Depends(get_db)]


@router.get("", response_model=RoomPage)
def list_rooms(
    db: Db,
    page: Annotated[int, Query(ge=1)] = 1,
    size: Annotated[int, Query(ge=1, le=100)] = 20,
) -> RoomPage:
    """Liste paginée des salles."""
    items = repository.list_rooms(db, limit=size, offset=(page - 1) * size)
    return RoomPage(items=items, total=repository.count_rooms(db), page=page, size=size)


@router.get("/available", response_model=list[Room])
def available_rooms(db: Db, start: datetime, end: datetime) -> list[Room]:
    """Salles libres sur le créneau [start, end[."""
    start_utc, end_utc = to_utc(start), to_utc(end)
    if end_utc <= start_utc:
        raise HTTPException(
            status.HTTP_422_UNPROCESSABLE_ENTITY, "end doit être postérieur à start"
        )
    return repository.free_rooms(db, start_utc, end_utc)
