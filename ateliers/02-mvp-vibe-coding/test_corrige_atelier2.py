"""Tests du corrigé de l'échauffement (lancer : python -m pytest ateliers)."""
from __future__ import annotations

import logging
import sqlite3
from datetime import UTC, datetime

import httpx
import pytest

from code_corrige import get_bookings, notify_owner


@pytest.fixture
def db() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE bookings (ref TEXT, owner_id INTEGER, title TEXT, start_at TEXT, end_at TEXT)")
    rows = [("a1", 1, "Point", "2030-01-10T09:00:00+00:00", "2030-01-10T10:00:00+00:00"),
            ("a2", 1, "Revue", "2030-02-10T09:00:00+00:00", "2030-02-10T10:00:00+00:00"),
            ("b1", 2, "Démo", "2030-01-10T09:00:00+00:00", "2030-01-10T10:00:00+00:00")]
    conn.executemany("INSERT INTO bookings VALUES (?, ?, ?, ?, ?)", rows)
    return conn


def test_seulement_les_reservations_du_proprietaire(db):
    assert [r.ref for r in get_bookings(db, 1)] == ["a1", "a2"]


def test_filtre_par_date(db):
    assert [r.ref for r in get_bookings(db, 1, since=datetime(2030, 2, 1, tzinfo=UTC))] == ["a2"]


def test_pas_de_filtre_executable(db):
    """Plus d'eval : une chaîne piégée ne peut plus être passée comme filtre."""
    with pytest.raises(TypeError):
        get_bookings(db, 1, filtre="__import__('os').system('id')")  # type: ignore[call-arg]


def test_notification_sans_donnee_personnelle(caplog):
    sent = {}

    def handler(request: httpx.Request) -> httpx.Response:
        sent["body"] = request.content
        return httpx.Response(204)

    with caplog.at_level(logging.INFO, logger="meetroom.notify"):
        notify_owner(httpx.Client(transport=httpx.MockTransport(handler)), "https://messagerie.example/notify", "a1")
    assert b"@" not in sent["body"] and "@" not in caplog.text


def test_erreur_remontee_et_non_avalee():
    client = httpx.Client(transport=httpx.MockTransport(lambda r: httpx.Response(500)))
    with pytest.raises(httpx.HTTPStatusError):
        notify_owner(client, "https://messagerie.example/notify", "a1")
