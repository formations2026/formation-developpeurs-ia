"""Routes des salles."""
from __future__ import annotations

import sqlite3
from datetime import datetime
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, status

from app import repository
from app.db import get_db
from app.deps import current_user_id
from app.schemas import Room, RoomPage, SlotIn, WaitlistEntry, to_utc
from app.services import booking as service

router = APIRouter(prefix="/rooms", tags=["salles"])
Db = Annotated[sqlite3.Connection, Depends(get_db)]
User = Annotated[int, Depends(current_user_id)]


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


@router.post("/{room_id}/waitlist", status_code=status.HTTP_201_CREATED)
def join_waitlist(room_id: int, slot: SlotIn, db: Db, user_id: User) -> dict[str, str]:
    """Inscription en liste d'attente : 404 salle inconnue, 409 salle libre ou déjà inscrit."""
    try:
        service.join_waitlist(db, room_id, user_id, slot)
    except service.RoomNotFound as exc:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Salle inconnue") from exc
    except service.RoomIsFree as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, "Salle libre : réservez-la") from exc
    except service.AlreadyWaiting as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, "Déjà inscrit pour ce créneau") from exc
    return {"status": "inscrit"}


@router.get("/{room_id}/waitlist", response_model=list[WaitlistEntry])
def read_waitlist(room_id: int, db: Db) -> list[WaitlistEntry]:
    """Liste d'attente dans l'ordre d'arrivée, sans donnée personnelle."""
    try:
        return service.waitlist_of(db, room_id)
    except service.RoomNotFound as exc:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Salle inconnue") from exc
