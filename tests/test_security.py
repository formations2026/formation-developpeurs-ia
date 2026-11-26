"""Tests d'attaque : ils restent dans la suite pour empêcher toute régression (partie 4)."""
from __future__ import annotations

import logging
from datetime import timedelta

from app import repository
from tests.conftest import ALICE, BOB


def _payload(start, title="Point d'équipe"):
    return {"room_id": 1, "title": title, "start_at": start.isoformat(),
            "end_at": (start + timedelta(hours=1)).isoformat()}


def test_lecture_de_la_reservation_d_un_autre_refusee(client, tomorrow):
    """Contrôle du propriétaire : Bob ne lit pas la réservation d'Alice (et ne sait pas qu'elle existe)."""
    ref = client.post("/bookings", json=_payload(tomorrow), headers=ALICE).json()["ref"]
    assert client.get(f"/bookings/{ref}", headers=ALICE).status_code == 200
    assert client.get(f"/bookings/{ref}", headers=BOB).status_code == 404


def test_injection_sql_dans_la_reference(client, db, tomorrow):
    """Une référence piégée ne renvoie rien et ne détruit rien."""
    client.post("/bookings", json=_payload(tomorrow), headers=ALICE)
    assert repository.get_booking(db, "x' OR '1'='1") is None
    assert client.get("/bookings/x' OR '1'='1", headers=BOB).status_code == 404
    assert db.execute("SELECT COUNT(*) FROM bookings").fetchone()[0] == 1


def test_injection_sql_dans_le_titre(client, db, tomorrow):
    """Le titre est stocké comme une donnée, jamais interprété comme du SQL."""
    piege = "x'); DROP TABLE bookings; --"
    r = client.post("/bookings", json=_payload(tomorrow, title=piege), headers=ALICE)
    assert r.status_code == 201 and r.json()["title"] == piege
    assert db.execute("SELECT COUNT(*) FROM bookings").fetchone()[0] == 1


def test_les_journaux_ne_contiennent_ni_titre_ni_identite(client, tomorrow, caplog):
    """RGPD : le journal porte des identifiants techniques, pas le contenu de la réunion."""
    with caplog.at_level(logging.INFO, logger="meetroom.booking"):
        client.post("/bookings", json=_payload(tomorrow, title="Entretien confidentiel"), headers=ALICE)
    assert caplog.records, "la création doit être journalisée"
    assert "Entretien confidentiel" not in caplog.text
    assert "@" not in caplog.text
