"""Configuration lue depuis l'environnement. Aucun secret n'est écrit dans le code."""
from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    """Paramètres de l'application."""

    db_path: str
    max_booking_hours: int


def get_settings() -> Settings:
    """Construit la configuration à partir des variables d'environnement."""
    return Settings(
        db_path=os.environ.get("MEETROOM_DB", "meetroom.db"),
        max_booking_hours=int(os.environ.get("MEETROOM_MAX_HOURS", "8")),
    )
