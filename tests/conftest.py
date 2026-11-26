"""Fixtures communes : une base SQLite temporaire par test, données 100 % synthétiques."""
from __future__ import annotations

import sqlite3
from collections.abc import Iterator
from datetime import UTC, datetime, timedelta

import pytest
from fastapi.testclient import TestClient

from app import repository
from app.db import connect, get_db
from app.main import app


@pytest.fixture
def db(tmp_path) -> Iterator[sqlite3.Connection]:
    conn = connect(str(tmp_path / "test.db"))
    repository.add_room(conn, "Atlas", 8)
    repository.add_room(conn, "Boréal", 4)
    repository.add_room(conn, "Cassiopée", 12)
    yield conn
    conn.close()


@pytest.fixture
def client(db: sqlite3.Connection) -> Iterator[TestClient]:
    app.dependency_overrides[get_db] = lambda: db
    yield TestClient(app)
    app.dependency_overrides.clear()


@pytest.fixture
def tomorrow() -> datetime:
    """Demain à 10 h UTC : un créneau toujours dans le futur."""
    base = datetime.now(UTC) + timedelta(days=1)
    return base.replace(hour=10, minute=0, second=0, microsecond=0)


ALICE = {"X-User-Id": "1"}
BOB = {"X-User-Id": "2"}
