"""Règles métier : chevauchement, contiguïté, durée, fuseaux horaires."""
from __future__ import annotations

from datetime import UTC, datetime, timedelta

import pytest

from app.schemas import BookingIn
from app.services import booking as service


def _data(start: datetime, hours: float = 1, room_id: int = 1) -> BookingIn:
    return BookingIn(room_id=room_id, title="Point d'équipe", start_at=start,
                     end_at=start + timedelta(hours=hours))


def test_salle_libre_quand_aucune_reservation(db, tomorrow):
    assert service.is_room_free(db, 1, tomorrow, tomorrow + timedelta(hours=1))


def test_chevauchement_refuse(db, tomorrow):
    service.create_booking(db, 1, _data(tomorrow))
    with pytest.raises(service.RoomNotFree):
        service.create_booking(db, 2, _data(tomorrow + timedelta(minutes=30)))


def test_creneaux_contigus_acceptes(db, tomorrow):
    """10 h-11 h puis 11 h-12 h : la salle libérée à 11 h est réservable à 11 h."""
    service.create_booking(db, 1, _data(tomorrow))
    booking = service.create_booking(db, 2, _data(tomorrow + timedelta(hours=1)))
    assert booking.ref


def test_autre_salle_acceptee(db, tomorrow):
    service.create_booking(db, 1, _data(tomorrow, room_id=1))
    assert service.create_booking(db, 2, _data(tomorrow, room_id=2)).room_id == 2


def test_salle_inconnue(db, tomorrow):
    with pytest.raises(service.RoomNotFound):
        service.create_booking(db, 1, _data(tomorrow, room_id=999))


def test_duree_maximale(db, tomorrow):
    with pytest.raises(service.TooLong):
        service.create_booking(db, 1, _data(tomorrow, hours=9), max_hours=8)


def test_dates_inversees_refusees(tomorrow):
    with pytest.raises(ValueError):
        BookingIn(room_id=1, title="x", start_at=tomorrow, end_at=tomorrow - timedelta(hours=1))


def test_dates_avec_et_sans_fuseau_comparables(db, tomorrow):
    """Régression : « can't compare offset-naive and offset-aware datetimes »."""
    service.create_booking(db, 1, _data(tomorrow))
    naive = tomorrow.replace(tzinfo=None)
    assert not service.is_room_free(db, 1, naive.replace(tzinfo=UTC),
                                    naive.replace(tzinfo=UTC) + timedelta(hours=1))
    with pytest.raises(service.RoomNotFree):
        service.create_booking(db, 2, _data(naive))


def test_annulation_par_le_proprietaire(db, tomorrow):
    booking = service.create_booking(db, 1, _data(tomorrow))
    service.cancel_booking(db, booking.ref, 1)
    assert service.is_room_free(db, 1, tomorrow, tomorrow + timedelta(hours=1))


def test_annulation_refusee_apres_le_debut(db, tomorrow):
    booking = service.create_booking(db, 1, _data(tomorrow))
    with pytest.raises(service.AlreadyStarted):
        service.cancel_booking(db, booking.ref, 1, now=tomorrow + timedelta(minutes=5))


def test_reference_non_sequentielle():
    refs = {service.new_ref() for _ in range(50)}
    assert len(refs) == 50 and all(len(r) == 12 for r in refs)
