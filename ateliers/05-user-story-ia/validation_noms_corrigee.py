"""CORRIGÉ — atelier 5 : une validation de nom qui n'exclut personne.

Première question à poser : faut-il valider un nom ? Souvent, « non vide et de longueur
raisonnable » suffit (valider_nom_minimal). Si une validation est exigée, elle accepte
les lettres de toutes les écritures, les accents (y compris décomposés), les apostrophes,
les traits d'union et les espaces (valider_nom). Sans dépendance externe.
"""
from __future__ import annotations

import unicodedata

SEPARATEURS = set(" '’-.")


def valider_nom_minimal(nom: str) -> bool:
    """Non vide une fois les espaces retirés, et 100 caractères au plus."""
    return 0 < len(nom.strip()) <= 100


def valider_nom(nom: str) -> bool:
    """Lettres de toute écriture, marques diacritiques, apostrophes, traits d'union, espaces, points."""
    nom = unicodedata.normalize("NFC", nom.strip())
    if not valider_nom_minimal(nom) or not nom[0].isalpha():
        return False
    return all(c.isalpha() or unicodedata.category(c).startswith("M") or c in SEPARATEURS for c in nom)
