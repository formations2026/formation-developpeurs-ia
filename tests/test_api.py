"""Contrat HTTP : un test par code de retour."""
from __future__ import annotations

from datetime import timedelta

from tests.conftest import ALICE, BOB


def _payload(start, hours=1, room_id=1):
    return {"room_id": room_id, "title": "Point d'équipe",
            "start_at": start.isoformat(), "end_at": (start + timedelta(hours=hours)).isoformat()}


def test_health(client):
    assert client.get("/health").json() == {"status": "ok"}


def test_liste_paginee(client):
    body = client.get("/rooms", params={"page": 1, "size": 2}).json()
    assert body["total"] == 3 and len(body["items"]) == 2 and body["page"] == 1


def test_pagination_invalide_422(client):
    assert client.get("/rooms", params={"size": 0}).status_code == 422
    assert client.get("/rooms", params={"size": 101}).status_code == 422


def test_creation_201(client, tomorrow):
    r = client.post("/bookings", json=_payload(tomorrow), headers=ALICE)
    assert r.status_code == 201 and r.json()["owner_id"] == 1


def test_creation_sans_identite_401(client, tomorrow):
    assert client.post("/bookings", json=_payload(tomorrow)).status_code == 401


def test_creation_conflit_409(client, tomorrow):
    client.post("/bookings", json=_payload(tomorrow), headers=ALICE)
    assert client.post("/bookings", json=_payload(tomorrow), headers=BOB).status_code == 409


def test_creation_salle_inconnue_404(client, tomorrow):
    assert client.post("/bookings", json=_payload(tomorrow, room_id=99), headers=ALICE).status_code == 404


def test_creation_dates_inversees_422(client, tomorrow):
    assert client.post("/bookings", json=_payload(tomorrow, hours=-1), headers=ALICE).status_code == 422


def test_salles_libres(client, tomorrow):
    client.post("/bookings", json=_payload(tomorrow), headers=ALICE)
    params = {"start": tomorrow.isoformat(), "end": (tomorrow + timedelta(hours=1)).isoformat()}
    body = client.get("/rooms/available", params=params).json()
    assert [r["name"] for r in body["items"]] == ["Boréal", "Cassiopée"] and body["total"] == 2


def test_salles_libres_paginees(client, tomorrow):
    params = {"start": tomorrow.isoformat(), "end": (tomorrow + timedelta(hours=1)).isoformat()}
    body = client.get("/rooms/available", params={**params, "page": 2, "size": 2}).json()
    assert [r["name"] for r in body["items"]] == ["Cassiopée"] and body["total"] == 3


def test_salles_libres_pagination_invalide_422(client, tomorrow):
    params = {"start": tomorrow.isoformat(), "end": (tomorrow + timedelta(hours=1)).isoformat()}
    assert client.get("/rooms/available", params={**params, "size": 0}).status_code == 422


def test_salles_libres_date_invalide_422(client):
    assert client.get("/rooms/available", params={"start": "demain", "end": "plus tard"}).status_code == 422


def test_annulation_204_puis_404(client, tomorrow):
    ref = client.post("/bookings", json=_payload(tomorrow), headers=ALICE).json()["ref"]
    assert client.delete(f"/bookings/{ref}", headers=ALICE).status_code == 204
    assert client.delete(f"/bookings/{ref}", headers=ALICE).status_code == 404


def test_annulation_autre_utilisateur_403(client, tomorrow):
    ref = client.post("/bookings", json=_payload(tomorrow), headers=ALICE).json()["ref"]
    assert client.delete(f"/bookings/{ref}", headers=BOB).status_code == 403
