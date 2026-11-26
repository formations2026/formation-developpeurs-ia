"""Règles métier des réservations. Aucune dépendance au framework web : tout est testable."""
from __future__ import annotations

import logging
import secrets
import sqlite3
from datetime import UTC, datetime, timedelta

from app import repository
from app.schemas import Booking, BookingIn, SlotIn, WaitlistEntry

logger = logging.getLogger("meetroom.booking")


class BookingError(Exception):
    """Erreur métier, traduite en code HTTP par la couche API."""


class RoomNotFound(BookingError):
    pass


class RoomNotFree(BookingError):
    pass


class BookingNotFound(BookingError):
    pass


class NotOwner(BookingError):
    pass


class AlreadyStarted(BookingError):
    pass


class TooLong(BookingError):
    pass


class RoomIsFree(BookingError):
    """La salle est libre : il suffit de la réserver."""


class AlreadyWaiting(BookingError):
    pass


def new_ref() -> str:
    """Référence non devinable (pas un compteur séquentiel)."""
    return secrets.token_hex(6)


def is_room_free(
    db: sqlite3.Connection, room_id: int, start: datetime, end: datetime
) -> bool:
    """Vrai si aucune réservation de la salle ne chevauche le créneau."""
    return not repository.overlapping(db, room_id, start, end)


def create_booking(
    db: sqlite3.Connection, owner_id: int, data: BookingIn, max_hours: int = 8
) -> Booking:
    """Crée une réservation après contrôle de la salle, de la durée et du créneau."""
    if repository.get_room(db, data.room_id) is None:
        raise RoomNotFound(data.room_id)
    if data.end_at - data.start_at > timedelta(hours=max_hours):
        raise TooLong(max_hours)
    if not is_room_free(db, data.room_id, data.start_at, data.end_at):
        raise RoomNotFree(data.room_id)
    booking = repository.insert_booking(db, new_ref(), owner_id, data)
    # Journalisation : identifiants techniques uniquement, jamais le titre ni une identité.
    logger.info("réservation créée", extra={"booking_ref": booking.ref, "owner_id": owner_id})
    return booking


def get_booking_for(db: sqlite3.Connection, ref: str, user_id: int) -> Booking:
    """Renvoie la réservation si elle appartient à l'utilisateur.

    Une réservation d'un autre utilisateur est signalée comme introuvable,
    pour ne pas révéler qu'elle existe.
    """
    booking = repository.get_booking(db, ref)
    if booking is None or booking.owner_id != user_id:
        raise BookingNotFound(ref)
    return booking


def cancel_booking(
    db: sqlite3.Connection, ref: str, user_id: int, now: datetime | None = None
) -> None:
    """Annule une réservation : propriétaire uniquement, et pas après son début."""
    booking = repository.get_booking(db, ref)
    if booking is None:
        raise BookingNotFound(ref)
    if booking.owner_id != user_id:
        raise NotOwner(ref)
    if booking.start_at <= (now or datetime.now(UTC)):
        raise AlreadyStarted(ref)
    repository.delete_booking(db, ref)
    logger.info("réservation annulée", extra={"booking_ref": ref, "owner_id": user_id})


def join_waitlist(db: sqlite3.Connection, room_id: int, user_id: int, slot: SlotIn) -> None:
    """Inscrit l'utilisateur en liste d'attente d'une salle occupée sur le créneau.

    Le piège de la user story : si la salle est libre, l'inscription n'a pas de sens.
    """
    if repository.get_room(db, room_id) is None:
        raise RoomNotFound(room_id)
    if is_room_free(db, room_id, slot.start_at, slot.end_at):
        raise RoomIsFree(room_id)
    if not repository.add_waitlist(db, room_id, user_id, slot.start_at, slot.end_at):
        raise AlreadyWaiting(room_id)
    logger.info("inscription en liste d'attente", extra={"room_id": room_id, "user_id": user_id})


def waitlist_of(db: sqlite3.Connection, room_id: int) -> list[WaitlistEntry]:
    """Liste d'attente d'une salle, dans l'ordre d'arrivée."""
    if repository.get_room(db, room_id) is None:
        raise RoomNotFound(room_id)
    return repository.list_waitlist(db, room_id)
