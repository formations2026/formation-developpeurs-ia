# MeetRoom — dépôt de la formation « Développeurs : boostez vos performances grâce à l'IA »

MeetRoom est une petite API de réservation de salles de réunion (Python, FastAPI, SQLite).
C'est l'application **fil rouge** de la formation : on y pratique le développement assisté par IA,
puis on la sécurise et on l'encadre.

Ce dépôt a deux rôles :

1. **Un terrain d'exercice** : les six ateliers de la formation se font ici (`ateliers/`).
2. **Un modèle à copier** : tous les fichiers de bonnes pratiques vus en cours sont présents, fonctionnels et commentés.

> Toutes les données sont **fictives**. L'entreprise « Novaline », les noms et les identifiants
> qui apparaissent dans les ateliers sont inventés.

## Démarrer en cinq minutes

```bash
python -m venv .venv && source .venv/bin/activate      # Windows : .venv\Scripts\activate
pip install -r requirements-dev.txt
make check           # ruff + bandit + pytest, comme la CI : doit être vert avant de toucher à l'IA
make seed            # données synthétiques
make run             # http://127.0.0.1:8000/docs
```

Sans `make` (Windows, par exemple), les mêmes commandes :

| `make` | Commande directe |
|---|---|
| `make check` | `ruff check .` puis `bandit -q -r app -ll` puis `pytest` |
| `make seed` | `python -m scripts.fake_data` |
| `make run` | `uvicorn app.main:app --reload` |

Installation détaillée des outils et pannes fréquentes : [`docs/INSTALLATION.md`](docs/INSTALLATION.md).

Essayer l'API :

```bash
curl "http://127.0.0.1:8000/rooms?page=1&size=5"
curl -X POST http://127.0.0.1:8000/bookings -H "X-User-Id: 1" -H "Content-Type: application/json" \
  -d '{"room_id": 1, "title": "Point équipe", "start_at": "2030-01-15T10:00:00Z", "end_at": "2030-01-15T11:00:00Z"}'
```

## La carte du dépôt

| Chemin | Ce que c'est | Vu en |
|---|---|---|
| `AGENTS.md` | Les règles du projet, lues par les assistants de code | Partie 1 |
| `CLAUDE.md`, `.github/copilot-instructions.md` | Fichiers propres aux outils ; ils renvoient à `AGENTS.md` | Partie 1 |
| `app/` | L'application : routes, règles métier, accès aux données | Partie 2 |
| `tests/` | 27 tests, dont les **tests d'attaque** (`test_security.py`) | Parties 2 et 4 |
| `prompts/` | Bibliothèque de dix prompts réutilisables, versionnée | Partie 3 |
| `.claude/settings.json` | Permissions `allow` / `ask` / `deny` et hook de garde | Partie 3 |
| `.claude/commands/` | Commande réutilisable « tests + docstrings + commit » | Partie 3 |
| `scripts/garde.sh` | Hook qui bloque les commandes dangereuses d'un agent | Partie 3 |
| `.mcp.json.example` | Déclaration d'un serveur MCP en lecture seule | Partie 3 |
| `scripts/fake_data.py` | Données synthétiques multilingues | Parties 4 et 5 |
| `.pre-commit-config.yaml`, `.gitleaks.toml` | Scan de secrets avant chaque commit | Partie 4 |
| `Dockerfile`, `.dockerignore` | Image sans secret, utilisateur sans privilèges | Partie 4 |
| `docs/SECURITE.md` | Checklists : avant d'envoyer, avant d'exécuter, si un secret fuit | Partie 4 |
| `docs/adr/` | Notes de décision, dont une fonctionnalité à base d'IA | Partie 5 |
| `docs/CHARTE-IA.md` | La charte IA de l'équipe, une page, vérifiable | Partie 6 |
| `.github/pull_request_template.md` | Cases « usage de l'IA » et « relu et testé » | Partie 6 |
| `.github/workflows/garde-fous.yml` | La charte traduite en contrôles automatiques | Partie 6 |
| `ateliers/` | Les six ateliers : consignes, supports, critères de réussite | Jours 1 et 2 |
| `docs/INSTALLATION.md` | Installation pas à pas et pannes fréquentes | Avant le jour 1 |
| `docs/AUTRES-LANGAGES.md` | Équivalents Java, JavaScript, C# | Tout au long |
| `docs/DEROULE.md`, `docs/DEMOS.md` | Pour le formateur : déroulé minuté et scénarios des démonstrations | — |

## Les six ateliers

| N° | Atelier | Durée | Dossier |
|---|---|---|---|
| 1 | Équiper son IDE | 45 min | [`ateliers/01-equiper-son-ide`](ateliers/01-equiper-son-ide/README.md) |
| 2 | Le MVP de MeetRoom en vibe coding | 60 min | [`ateliers/02-mvp-vibe-coding`](ateliers/02-mvp-vibe-coding/README.md) |
| 3 | Automatiser une tâche avec un agent | 45 min | [`ateliers/03-automatiser-une-tache`](ateliers/03-automatiser-une-tache/README.md) |
| 4 | Sécuriser une requête SQL sensible | 50 min | [`ateliers/04-requete-sql-sensible`](ateliers/04-requete-sql-sensible/README.md) |
| 5 | Revoir une user story « IA » | 40 min | [`ateliers/05-user-story-ia`](ateliers/05-user-story-ia/README.md) |
| 6 | La charte IA de l'équipe | 40 min | [`ateliers/06-charte-ia`](ateliers/06-charte-ia/README.md) |

Travaillez sur une branche par atelier : `git switch -c atelier-2-prenom`.

### Bloqué ? Les corrigés
Deux branches contiennent un corrigé complet, commit par commit :

```bash
git log --oneline main..solution/atelier-2     # les étapes, une par commit
git diff main solution/atelier-2               # tout le corrigé de la liste d'attente
git diff main solution/atelier-3               # une tâche déléguée à un agent : la pagination
```

Les ateliers 1, 4, 5 et 6 ont leur corrigé indicatif replié en bas de leur page.
N'ouvrez un corrigé qu'après avoir essayé : comparer **votre** diff au corrigé est l'exercice le plus formateur.

### Vous ne codez pas, ou pas en Python ?
- Chaque atelier a une section « Si vous ne codez pas » : relire, juger, décider sont les compétences visées.
- Les équivalents Java, JavaScript et C# de chaque pratique sont dans [`docs/AUTRES-LANGAGES.md`](docs/AUTRES-LANGAGES.md).

## Les bonnes pratiques illustrées dans le code

- **SQL paramétré uniquement**, écrit dans un seul fichier (`app/repository.py`). Preuve : `tests/test_security.py`.
- **Contrôle du propriétaire** : on ne lit ni n'annule la réservation d'un autre (403 / 404).
- **Références non devinables** (`secrets.token_hex`), pas de compteur séquentiel.
- **Dates en UTC**, avec un test de régression sur le mélange « avec / sans fuseau ».
- **Journaux sans donnée personnelle** : identifiants techniques seulement, vérifié par un test.
- **Aucun secret dans le code** : configuration par variables d'environnement, `.env` ignoré, scan gitleaks.
- **Règles métier sans framework** (`app/services/`) : faciles à tester, faciles à relire.
- **Défense en couches pour les agents** : consigne (`AGENTS.md`) → permissions → hook → bac à sable → revue humaine.

## Une simplification à connaître

L'identité de l'appelant vient de l'en-tête `X-User-Id`. C'est **volontairement simpliste** pour garder
l'application lisible en formation : en production, l'identité vient d'un jeton vérifié. Voir `docs/SECURITE.md`.

## Règles d'usage de l'IA sur ce dépôt

Elles sont dans [`docs/CHARTE-IA.md`](docs/CHARTE-IA.md). En trois lignes :
on utilise des outils autorisés, on n'envoie ni secret ni donnée réelle, et un humain relit et signe chaque ligne.

## Publier ce dépôt (formateur)

```bash
git remote add origin https://github.com/formations2026/formation-developpeurs-ia.git
git push -u origin --all        # main et les deux branches de corrigé
```

Activez ensuite la protection de la branche `main` : pipeline « garde-fous » obligatoire et une approbation.
