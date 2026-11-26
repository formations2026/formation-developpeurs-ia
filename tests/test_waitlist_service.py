"""Liste d'attente : règles métier (atelier 2)."""
from __future__ import annotations

from datetime import timedelta

import pytest

from app.schemas import BookingIn, SlotIn
from app.services import booking as service


def _occupy(db, start):
    data = BookingIn(room_id=1, title="Occupée", start_at=start, end_at=start + timedelta(hours=1))
    service.create_booking(db, 1, data)
    return SlotIn(start_at=start, end_at=start + timedelta(hours=1))


def test_inscription_sur_salle_occupee(db, tomorrow):
    slot = _occupy(db, tomorrow)
    service.join_waitlist(db, 1, 2, slot)
    assert [e.position for e in service.waitlist_of(db, 1)] == [1]


def test_salle_libre_refusee(db, tomorrow):
    """Le piège : une salle libre se réserve, on ne s'y inscrit pas en attente."""
    slot = SlotIn(start_at=tomorrow, end_at=tomorrow + timedelta(hours=1))
    with pytest.raises(service.RoomIsFree):
        service.join_waitlist(db, 1, 2, slot)


def test_double_inscription_refusee(db, tomorrow):
    slot = _occupy(db, tomorrow)
    service.join_waitlist(db, 1, 2, slot)
    with pytest.raises(service.AlreadyWaiting):
        service.join_waitlist(db, 1, 2, slot)


def test_ordre_d_arrivee(db, tomorrow):
    slot = _occupy(db, tomorrow)
    for user in (5, 3, 9):
        service.join_waitlist(db, 1, user, slot)
    assert [e.position for e in service.waitlist_of(db, 1)] == [1, 2, 3]


def test_salle_inconnue(db, tomorrow):
    with pytest.raises(service.RoomNotFound):
        service.waitlist_of(db, 999)
