# Corrigé — Atelier 1 : Équiper son IDE (45 min)

> Branche formateur. À présenter au débrief, pas avant.

## Minutage conseillé
| Temps | Étape |
|---|---|
| 0 – 5 min | `make check` vert sur tous les postes (sinon : binôme immédiat) |
| 5 – 15 min | Assistants installés et connectés |
| 15 – 25 min | Lecture d'`AGENTS.md`, une règle ajoutée |
| 25 – 35 min | Explication de l'architecture, test des règles |
| 35 – 45 min | Tableau rempli, débrief |

## Étape 1 — Résultat attendu
`make check` (ou `pytest`) affiche **27 passed**. Les pannes fréquentes et leurs solutions sont dans `docs/INSTALLATION.md`.
Règle à faire respecter : **aucun usage de l'IA tant que le projet n'est pas vert**. Sinon, impossible de savoir si une
erreur vient de l'IA ou de l'installation.

## Étape 3 — Une bonne règle à ajouter dans `AGENTS.md`
Une bonne règle est **précise et vérifiable** dans le code ou dans la CI.

| Bonne règle (vérifiable) | Mauvaise règle (vague) |
|---|---|
| « Toute nouvelle route a un test par code de retour HTTP. » | « Écris du code de qualité. » |
| « Les réponses de l'API n'exposent jamais `owner_id` d'un autre utilisateur. » | « Fais attention à la sécurité. » |
| « Messages de commit au format Conventional Commits, en français. » | « Sois clair. » |
| « Une fonction de plus de 40 lignes est découpée avant la pull request. » | « Garde le code simple. » |

## Étape 4 — L'explication attendue de l'architecture
Un bon assistant doit produire à peu près ceci, **avec des fichiers à l'appui** :

1. API FastAPI, point d'entrée `app/main.py`, documentation sur `/docs`.
2. Deux routeurs : `app/routers/rooms.py` (salles) et `app/routers/bookings.py` (réservations).
3. Les routes traduisent les erreurs métier en codes HTTP (404, 403, 409, 422).
4. Les règles métier sont dans `app/services/booking.py`, sans dépendance au framework.
5. Tout le SQL est dans `app/repository.py`, en requêtes paramétrées.
6. Les schémas Pydantic (`app/schemas.py`) valident les entrées et normalisent les dates en UTC.
7. La base est SQLite, créée par `app/db.py`.
8. L'identité de l'appelant vient de l'en-tête `X-User-Id` (`app/deps.py`) : simplification volontaire.
9. Les tests sont dans `tests/`, dont les tests d'attaque dans `tests/test_security.py`.
10. La configuration vient de l'environnement (`app/config.py`), aucun secret dans le code.

**Deux affirmations à faire vérifier** dans le code : « tout le SQL est dans `repository.py` » (rechercher `execute(`)
et « les dates sont en UTC » (lire `to_utc` dans `app/schemas.py`).

## Étape 5 — Le test des règles
Demande : « Écris une fonction qui cherche les réservations d'un propriétaire. »

**Résultat attendu** (assistant qui a lu `AGENTS.md`) :

```python
# app/repository.py
def list_by_owner(db: sqlite3.Connection, owner_id: int) -> list[Booking]:
    """Réservations d'un propriétaire, de la plus proche à la plus lointaine."""
    rows = db.execute(
        "SELECT * FROM bookings WHERE owner_id = :owner_id ORDER BY start_at",
        {"owner_id": owner_id},
    ).fetchall()
    return [_to_booking(r) for r in rows]
```

```python
# tests/test_repository.py
def test_list_by_owner(db, tomorrow):
    ...  # deux réservations pour 1, une pour 2 → list_by_owner(db, 1) en renvoie deux
```

**Signaux d'échec à faire relever :**
| Ce que l'assistant produit | Ce que cela révèle |
|---|---|
| `f"... WHERE owner_email = '{email}'"` | Injection SQL **et** champ inventé : `owner_email` n'existe pas |
| Import de SQLAlchemy ou d'un ORM | Hallucination : le projet utilise `sqlite3` |
| Nouveau fichier `database.py` | N'a pas lu l'architecture |
| Pas de test | N'a pas lu `AGENTS.md` (ou l'outil ne le prend pas en charge) |

## Étape 6 — Exemple de tableau rempli
| | Chat web | Assistant d'IDE en mode agent |
|---|---|---|
| Connaît les fichiers du projet ? | Non, sauf copier-coller | Oui |
| Respecte « SQL paramétré » ? | Souvent oui, mais sur un schéma inventé | Oui, dans `repository.py` |
| Propose un test ? | Rarement sans le demander | Oui |
| Ce pour quoi je l'utiliserai | Questions générales, apprendre un concept | Coder dans le projet |

## Débrief (10 min) — questions et réponses attendues
- **« Lequel a le mieux respecté les règles ? »** → Celui qui avait accès au projet. Le critère n° 1 est le contexte, pas le modèle.
- **« Qu'avez-vous dû corriger ? »** → Noms inventés, tests absents, dépendances ajoutées sans prévenir.
- **« Quelle règle avez-vous ajoutée ? »** → Faire lire deux ou trois règles à voix haute et tester : est-elle vérifiable ?

## Grille d'évaluation
| Critère | Acquis | En cours |
|---|---|---|
| Deux assistants fonctionnent sur le projet | | |
| La règle ajoutée est vérifiable | | |
| Deux affirmations de l'IA ont été vérifiées dans le code | | |
| Le participant sait quel outil utiliser pour quoi | | |
