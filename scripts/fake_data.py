"""Remplit la base locale avec des données 100 % synthétiques.

Pourquoi : on n'envoie jamais de données réelles à un outil d'IA, et on ne teste jamais
avec une copie de la production. Plusieurs langues sont utilisées exprès : des données de
test uniformes cachent les biais (noms accentués, composés, alphabets non latins).

Usage : PYTHONPATH=. python scripts/fake_data.py [chemin_de_la_base]
"""
from __future__ import annotations

import random
import sys
from datetime import UTC, datetime, timedelta

from faker import Faker

from app import repository
from app.db import connect
from app.schemas import BookingIn
from app.services import booking as service

LOCALES = ["fr_FR", "en_GB", "vi_VN", "ar_SA", "zh_CN", "de_DE", "es_ES"]
ROOMS = [("Atlas", 8), ("Boréal", 4), ("Cassiopée", 12), ("Dune", 6), ("Équinoxe", 20)]
SUJETS = ["Point d'équipe", "Revue de sprint", "Atelier conception", "Démo client", "Rétrospective"]


def main(path: str = "meetroom.db") -> None:
    Faker.seed(42)
    random.seed(42)  # noqa: S311 - données de démonstration, pas de cryptographie
    fake = Faker(LOCALES)
    db = connect(path)
    if repository.count_rooms(db) == 0:
        for name, capacity in ROOMS:
            repository.add_room(db, name, capacity)
    base = (datetime.now(UTC) + timedelta(days=1)).replace(hour=8, minute=0, second=0, microsecond=0)
    created = 0
    for _ in range(40):
        start = base + timedelta(days=random.randint(0, 9), hours=random.randint(0, 9))  # noqa: S311
        data = BookingIn(
            room_id=random.randint(1, len(ROOMS)),  # noqa: S311
            title=f"{random.choice(SUJETS)} — {fake.last_name()}",  # noqa: S311
            start_at=start,
            end_at=start + timedelta(hours=1),
        )
        try:
            service.create_booking(db, owner_id=random.randint(1, 15), data=data)  # noqa: S311
            created += 1
        except service.RoomNotFree:
            continue
    print(f"{len(ROOMS)} salles, {created} réservations synthétiques dans {path}")


if __name__ == "__main__":
    main(*sys.argv[1:2])
