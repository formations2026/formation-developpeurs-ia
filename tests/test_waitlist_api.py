"""Liste d'attente : un test par critère d'acceptation (atelier 2)."""
from __future__ import annotations

from datetime import timedelta

from tests.conftest import ALICE, BOB


def _slot(start):
    return {"start_at": start.isoformat(), "end_at": (start + timedelta(hours=1)).isoformat()}


def _occupy(client, start):
    client.post("/bookings", json={"room_id": 1, "title": "Occupée", **_slot(start)}, headers=ALICE)


def test_inscription_201(client, tomorrow):
    _occupy(client, tomorrow)
    assert client.post("/rooms/1/waitlist", json=_slot(tomorrow), headers=BOB).status_code == 201


def test_salle_inconnue_404(client, tomorrow):
    assert client.post("/rooms/99/waitlist", json=_slot(tomorrow), headers=BOB).status_code == 404
    assert client.get("/rooms/99/waitlist").status_code == 404


def test_salle_libre_409(client, tomorrow):
    assert client.post("/rooms/1/waitlist", json=_slot(tomorrow), headers=BOB).status_code == 409


def test_deja_inscrit_409(client, tomorrow):
    _occupy(client, tomorrow)
    client.post("/rooms/1/waitlist", json=_slot(tomorrow), headers=BOB)
    assert client.post("/rooms/1/waitlist", json=_slot(tomorrow), headers=BOB).status_code == 409


def test_liste_sans_donnee_personnelle(client, tomorrow):
    _occupy(client, tomorrow)
    client.post("/rooms/1/waitlist", json=_slot(tomorrow), headers=BOB)
    body = client.get("/rooms/1/waitlist").json()
    assert [e["position"] for e in body] == [1]
    assert set(body[0]) == {"position", "start_at", "end_at"}


def test_sans_identite_401(client, tomorrow):
    assert client.post("/rooms/1/waitlist", json=_slot(tomorrow)).status_code == 401
