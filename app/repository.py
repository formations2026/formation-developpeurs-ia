"""Accès aux données. Règle du projet : SQL paramétré uniquement, jamais de f-string."""
from __future__ import annotations

import sqlite3
from datetime import datetime

from app.schemas import Booking, BookingIn, Room


def _iso(value: datetime) -> str:
    return value.isoformat()


def _to_booking(row: sqlite3.Row) -> Booking:
    return Booking(
        ref=row["ref"],
        room_id=row["room_id"],
        owner_id=row["owner_id"],
        title=row["title"],
        start_at=datetime.fromisoformat(row["start_at"]),
        end_at=datetime.fromisoformat(row["end_at"]),
    )


def count_rooms(db: sqlite3.Connection) -> int:
    return int(db.execute("SELECT COUNT(*) FROM rooms").fetchone()[0])


def list_rooms(db: sqlite3.Connection, limit: int, offset: int) -> list[Room]:
    rows = db.execute(
        "SELECT id, name, capacity FROM rooms ORDER BY name LIMIT :limit OFFSET :offset",
        {"limit": limit, "offset": offset},
    ).fetchall()
    return [Room(**dict(r)) for r in rows]


def get_room(db: sqlite3.Connection, room_id: int) -> Room | None:
    row = db.execute(
        "SELECT id, name, capacity FROM rooms WHERE id = :id", {"id": room_id}
    ).fetchone()
    return Room(**dict(row)) if row else None


def add_room(db: sqlite3.Connection, name: str, capacity: int) -> Room:
    cur = db.execute(
        "INSERT INTO rooms (name, capacity) VALUES (:name, :capacity)",
        {"name": name, "capacity": capacity},
    )
    db.commit()
    return Room(id=int(cur.lastrowid or 0), name=name, capacity=capacity)


def overlapping(
    db: sqlite3.Connection, room_id: int, start: datetime, end: datetime
) -> list[Booking]:
    """Réservations de la salle qui chevauchent [start, end[.

    Deux créneaux contigus (10 h-11 h puis 11 h-12 h) ne se chevauchent pas.
    """
    rows = db.execute(
        "SELECT * FROM bookings "
        "WHERE room_id = :room_id AND start_at < :end AND :start < end_at",
        {"room_id": room_id, "start": _iso(start), "end": _iso(end)},
    ).fetchall()
    return [_to_booking(r) for r in rows]


def free_rooms(db: sqlite3.Connection, start: datetime, end: datetime) -> list[Room]:
    rows = db.execute(
        "SELECT id, name, capacity FROM rooms r WHERE NOT EXISTS ("
        "  SELECT 1 FROM bookings b"
        "  WHERE b.room_id = r.id AND b.start_at < :end AND :start < b.end_at"
        ") ORDER BY name",
        {"start": _iso(start), "end": _iso(end)},
    ).fetchall()
    return [Room(**dict(r)) for r in rows]


def insert_booking(
    db: sqlite3.Connection, ref: str, owner_id: int, data: BookingIn
) -> Booking:
    db.execute(
        "INSERT INTO bookings (ref, room_id, owner_id, title, start_at, end_at) "
        "VALUES (:ref, :room_id, :owner_id, :title, :start_at, :end_at)",
        {
            "ref": ref,
            "room_id": data.room_id,
            "owner_id": owner_id,
            "title": data.title,
            "start_at": _iso(data.start_at),
            "end_at": _iso(data.end_at),
        },
    )
    db.commit()
    return Booking(ref=ref, owner_id=owner_id, **data.model_dump())


def get_booking(db: sqlite3.Connection, ref: str) -> Booking | None:
    row = db.execute("SELECT * FROM bookings WHERE ref = :ref", {"ref": ref}).fetchone()
    return _to_booking(row) if row else None


def delete_booking(db: sqlite3.Connection, ref: str) -> None:
    db.execute("DELETE FROM bookings WHERE ref = :ref", {"ref": ref})
    db.commit()
