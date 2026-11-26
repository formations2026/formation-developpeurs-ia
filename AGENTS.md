# AGENTS.md — MeetRoom

> Ce fichier est lu par les assistants de code (Copilot, Claude Code, Junie, Cursor…).
> Il dit à l'IA ce qu'on dirait à un nouveau développeur le premier jour.
> Il est versionné et relu en pull request, comme le code.

## Projet
API de réservation de salles de réunion. Python 3.11+, FastAPI, SQLite (module `sqlite3`).
- `app/routers/` : routes HTTP, traduction des erreurs métier en codes HTTP
- `app/services/` : règles métier, sans dépendance au framework
- `app/repository.py` : seul endroit où l'on écrit du SQL
- `tests/` : pytest ; `tests/test_security.py` contient les tests d'attaque

## Commandes
- Installer : `pip install -r requirements-dev.txt`
- Lancer : `uvicorn app.main:app --reload`
- Tester : `pytest`
- Qualité : `ruff check .` puis `bandit -r app -ll`

## Règles de code
- Typage obligatoire ; fonctions de moins de 40 lignes
- Toute fonction publique a une docstring et au moins un test
- SQL : requêtes paramétrées uniquement (`:nom`), jamais de f-string ni de concaténation
- Les dates sont stockées et comparées en UTC (`app.schemas.to_utc`)
- Journalisation avec `logging`, identifiants techniques uniquement : jamais d'e-mail, de nom ni de titre de réunion
- Aucune nouvelle dépendance sans le demander explicitement

## Interdits
- Ne jamais lire, afficher ni modifier `.env` ou tout fichier de `secrets/`
- Ne jamais écrire de secret, de jeton ou de mot de passe dans le code, les tests ou la documentation
- Ne jamais modifier un test existant pour le faire passer : signaler le désaccord
- Ne jamais pousser sur `main` ni réécrire l'historique Git
- Ne pas modifier `ateliers/` (code volontairement imparfait, support d'exercices)

## Avant de rendre la main
1. `pytest` passe, `ruff check .` ne signale rien
2. Résumer les fichiers modifiés et les choix faits
3. Signaler ce qui n'a pas pu être vérifié
