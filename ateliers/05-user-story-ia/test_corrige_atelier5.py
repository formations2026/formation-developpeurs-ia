"""Tests du corrigé de l'atelier 5 : le test qui révèle le biais, puis la correction."""
from __future__ import annotations

import pytest

from validation_noms import valider_nom as valider_nom_initiale
from validation_noms_corrigee import valider_nom, valider_nom_minimal

VRAIS_NOMS = ["Martin", "Zoé N'Diaye-Lefèvre", "O'Brien", "Nguyễn Thị Minh Khai", "李小龍",
              "Jean-Baptiste de La Tour", "Ødegård", "Mª José", "J. R. R. Tolkien", "José"]


@pytest.mark.parametrize("nom", VRAIS_NOMS[1:5])
def test_la_version_initiale_refuse_de_vrais_noms(nom):
    """Le test qui prouve le biais : il passe parce que la version initiale échoue."""
    assert valider_nom_initiale(nom) is False


@pytest.mark.parametrize("nom", [n for n in VRAIS_NOMS if n != "Mª José"])
def test_la_version_corrigee_accepte_les_vrais_noms(nom):
    assert valider_nom(nom) is True


def test_accents_decomposes_acceptes():
    assert valider_nom("José") is True  # « José » saisi avec un accent combinant


@pytest.mark.parametrize("valeur", ["", "   ", "1234", "<script>", "x" * 101, "-Martin"])
def test_valeurs_invalides_refusees(valeur):
    assert valider_nom(valeur) is False


def test_validation_minimale():
    assert valider_nom_minimal("李") and not valider_nom_minimal("  ")
