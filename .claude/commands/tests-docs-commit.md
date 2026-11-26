---
description: Tests, docstrings et message de commit pour un module
argument-hint: <chemin du module>
---

Pour le module `$ARGUMENTS` :

1. Lis le module et liste les cas limites de chaque fonction publique. N'écris rien encore.
2. Ajoute les tests pytest manquants dans `tests/`. N'invente aucune fixture : utilise celles de `tests/conftest.py`.
3. Lance `pytest`. Si un test échoue, cherche la cause : ne modifie jamais un test existant pour le faire passer.
4. Ajoute ou corrige les docstrings (ce que fait la fonction, paramètres, erreurs levées). Pas de paraphrase du code.
5. Lance `ruff check .`.
6. Propose un message de commit au format Conventional Commits qui dit le pourquoi. Ne commite pas.

Termine par : fichiers modifiés, tests ajoutés, ce que tu n'as pas pu vérifier.
