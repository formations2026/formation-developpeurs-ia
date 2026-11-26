"""Accès à la base SQLite. Toutes les requêtes du projet sont paramétrées."""
from __future__ import annotations

import sqlite3
from collections.abc import Iterator

from app.config import get_settings

SCHEMA = """
CREATE TABLE IF NOT EXISTS rooms (
    id       INTEGER PRIMARY KEY,
    name     TEXT    NOT NULL UNIQUE,
    capacity INTEGER NOT NULL CHECK (capacity > 0)
);
CREATE TABLE IF NOT EXISTS bookings (
    ref      TEXT    PRIMARY KEY,
    room_id  INTEGER NOT NULL REFERENCES rooms(id),
    owner_id INTEGER NOT NULL,
    title    TEXT    NOT NULL,
    start_at TEXT    NOT NULL,
    end_at   TEXT    NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_bookings_room_start ON bookings(room_id, start_at);
CREATE TABLE IF NOT EXISTS waitlist (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    room_id  INTEGER NOT NULL REFERENCES rooms(id),
    user_id  INTEGER NOT NULL,
    start_at TEXT    NOT NULL,
    end_at   TEXT    NOT NULL,
    UNIQUE (room_id, user_id, start_at, end_at)
);
"""


def connect(path: str) -> sqlite3.Connection:
    """Ouvre une connexion et crée le schéma s'il n'existe pas."""
    conn = sqlite3.connect(path, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    conn.executescript(SCHEMA)
    return conn


def get_db() -> Iterator[sqlite3.Connection]:
    """Dépendance FastAPI : une connexion par requête, fermée à la fin."""
    conn = connect(get_settings().db_path)
    try:
        yield conn
    finally:
        conn.close()
