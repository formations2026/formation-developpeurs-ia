"""CORRIGÉ — atelier 2, échauffement : la version relue de code_a_corriger.py.

Chaque correction porte le numéro du défaut dans CORRIGE.md.
"""
from __future__ import annotations

import logging
import sqlite3
from dataclasses import dataclass
from datetime import datetime

import httpx  # (7) bibliothèque réelle, déjà dans requirements-dev.txt — plus de paquet inventé

logger = logging.getLogger("meetroom.notify")

# (2) Aucun mot de passe dans le code : la connexion est fournie par l'appelant,
#     configurée à partir de variables d'environnement (voir app/config.py).


@dataclass(frozen=True)
class Reservation:
    """Une réservation, sans donnée personnelle (8 : typage explicite)."""

    ref: str
    title: str
    start_at: datetime
    end_at: datetime


def get_bookings(
    db: sqlite3.Connection, owner_id: int, since: datetime | None = None
) -> list[Reservation]:
    """Réservations d'un propriétaire, éventuellement à partir d'une date.

    (1) Requête paramétrée : la valeur voyage à côté du SQL, jamais dedans.
    (6) Le filtre libre évalué avec eval() est remplacé par un paramètre typé.
    (8) Les dates sont comparées en ISO 8601 UTC, pas sous forme de texte local.
    """
    query = "SELECT ref, title, start_at, end_at FROM bookings WHERE owner_id = :owner_id"
    params: dict[str, object] = {"owner_id": owner_id}
    if since is not None:
        query += " AND start_at >= :since"
        params["since"] = since.isoformat()
    rows = db.execute(query + " ORDER BY start_at", params).fetchall()
    return [
        Reservation(r[0], r[1], datetime.fromisoformat(r[2]), datetime.fromisoformat(r[3]))
        for r in rows
    ]


def notify_owner(client: httpx.Client, url: str, booking_ref: str) -> None:
    """Prévient la messagerie qu'une réservation a été créée.

    (3) Vérification TLS conservée (comportement par défaut d'httpx).
    (4) Les erreurs ne sont plus avalées : raise_for_status() les remonte.
    (5) Le journal ne contient qu'un identifiant technique : ni e-mail, ni titre.
    """
    response = client.post(url, json={"ref": booking_ref}, timeout=5)
    response.raise_for_status()
    logger.info("notification envoyée", extra={"booking_ref": booking_ref})
