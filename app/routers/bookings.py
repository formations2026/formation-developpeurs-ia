"""Routes des réservations. La couche API traduit les erreurs métier en codes HTTP."""
from __future__ import annotations

import sqlite3
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from app.config import get_settings
from app.db import get_db
from app.deps import current_user_id
from app.schemas import Booking, BookingIn
from app.services import booking as service

router = APIRouter(prefix="/bookings", tags=["réservations"])
Db = Annotated[sqlite3.Connection, Depends(get_db)]
User = Annotated[int, Depends(current_user_id)]


@router.post("", response_model=Booking, status_code=status.HTTP_201_CREATED)
def create(data: BookingIn, db: Db, user_id: User) -> Booking:
    """Crée une réservation pour l'utilisateur courant."""
    try:
        return service.create_booking(db, user_id, data, get_settings().max_booking_hours)
    except service.RoomNotFound as exc:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Salle inconnue") from exc
    except service.TooLong as exc:
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_ENTITY, "Réservation trop longue") from exc
    except service.RoomNotFree as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, "Salle déjà réservée sur ce créneau") from exc


@router.get("/{ref}", response_model=Booking)
def read(ref: str, db: Db, user_id: User) -> Booking:
    """Lit une réservation. Celle d'un autre utilisateur est introuvable (404)."""
    try:
        return service.get_booking_for(db, ref, user_id)
    except service.BookingNotFound as exc:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Réservation introuvable") from exc


@router.delete("/{ref}", status_code=status.HTTP_204_NO_CONTENT)
def cancel(ref: str, db: Db, user_id: User) -> None:
    """Annule une réservation : 404 inconnue, 403 autre utilisateur, 409 déjà commencée."""
    try:
        service.cancel_booking(db, ref, user_id)
    except service.BookingNotFound as exc:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Réservation introuvable") from exc
    except service.NotOwner as exc:
        raise HTTPException(status.HTTP_403_FORBIDDEN, "Réservation d'un autre utilisateur") from exc
    except service.AlreadyStarted as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, "Réservation déjà commencée") from exc
