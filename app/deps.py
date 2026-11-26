"""Dépendances communes de l'API."""
from __future__ import annotations

from typing import Annotated

from fastapi import Header, HTTPException, status


def current_user_id(x_user_id: Annotated[int | None, Header()] = None) -> int:
    """Identifie l'appelant par l'en-tête X-User-Id.

    SIMPLIFICATION PÉDAGOGIQUE : dans un vrai projet, l'identité vient d'un jeton
    vérifié (OIDC, session), jamais d'un en-tête que le client choisit librement.
    Voir docs/SECURITE.md.
    """
    if x_user_id is None or x_user_id <= 0:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "En-tête X-User-Id requis")
    return x_user_id
