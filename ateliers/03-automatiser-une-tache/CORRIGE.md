# Corrigé — Atelier 3 : Automatiser une tâche avec un agent (45 min)

> Branche formateur. La tâche 6 réalisée est le commit `feat(rooms)!: pagine GET /rooms/available` de cette branche.

## Étape 2 — Un ticket bien écrit (tâche 6)
```text
Ticket — Paginer GET /rooms/available comme GET /rooms

Périmètre : app/routers/rooms.py (route available_rooms) et tests/test_api.py.
Critères d'acceptation :
- paramètres page (>= 1, défaut 1) et size (1 à 100, défaut 20)
- réponse RoomPage : items, total, page, size — comme GET /rooms
- 422 si page ou size invalide
- un test de deuxième page, un test de paramètre invalide
Interdits :
- aucune nouvelle dépendance
- ne modifier aucune autre route
- signaler explicitement le changement de contrat (une liste devient un objet)
```
Ce qui fait un bon ticket : **un périmètre de fichiers**, des **critères vérifiables par des tests**, des **interdits**,
et la demande de **signaler** ce qui casse la compatibilité.

## Étape 3 — Les garde-fous : réponses attendues
**Que peut faire l'agent sans demander ?** (`allow` dans `.claude/settings.json`)
`pytest`, `ruff check`, `git status`, `git diff`, `git log`. Uniquement de la lecture et des vérifications.

**Que doit-il demander ?** (`ask`) `git commit`, `git push`, `pip install`.

**Qu'est-ce qui est interdit ?** (`deny`) lire `.env` et `secrets/`, lancer `curl` ou `wget`.

**Le hook :**
```bash
$ echo '{"tool_input":{"command":"rm -rf /tmp/x"}}' | scripts/garde.sh ; echo $?
Commande bloquée par scripts/garde.sh : motif interdit. Demander à un humain.
2
$ echo '{"tool_input":{"command":"pytest -q"}}' | scripts/garde.sh ; echo $?
0
```
Règle à proposer en plus : `deny` sur `Bash(git push --force:*)`, ou `ask` sur `Edit(./tests/**)` pour être prévenu
quand l'agent touche aux tests.

## Étape 4 — Le résultat attendu de la tâche 6
- `app/routers/rooms.py` : `available_rooms` accepte `page` et `size`, renvoie un `RoomPage`.
- `tests/test_api.py` : le test existant est **mis à jour** (le contrat change), deux tests ajoutés.
- `prompts/11-paginer.md` : le prompt réutilisable.
- Message de commit avec `!` : `feat(rooms)!: …`, qui signale un **changement cassant**.

**Point de débat** : ici, modifier un test existant est légitime, parce que le contrat de l'API change volontairement.
La différence avec « modifier un test pour qu'il passe » : le changement est **demandé, annoncé et expliqué**.

## Étape 5 — Réponses typiques du tableau
| Question | Réponse typique |
|---|---|
| Étapes enchaînées seul | 6 à 12 : lecture, édition, `pytest`, correction, `ruff`, résumé |
| Après un échec de test | Il lit l'erreur, corrige le code, relance. S'il touche au test : alerte |
| Ce que j'ai dû corriger | Le test existant oublié, ou une docstring imprécise |
| Tentative interdite ? | Parfois `pip install` (demandé), rarement autre chose |
| Temps gagné | Réel sur les tâches répétitives ; nul ou négatif sur les tâches floues |

## Les autres tâches : résultat attendu
| N° | Tâche | Résultat attendu | Piège |
|---|---|---|---|
| 1 | Tests de `app/repository.py` | 6 à 10 tests sur une base temporaire | Des tests qui n'assertent rien |
| 2 | Docstrings | Une par fonction publique, avec les erreurs levées | La paraphrase du code |
| 3 | Message de commit | Conventional Commits, le pourquoi | « fix stuff » |
| 4 | Alertes du linter | `ruff check .` vide, tests verts | Désactiver la règle au lieu de corriger |
| 5 | Journal des modifications | Regroupé par type (ajouts, corrections) | Inventer des changements absents des commits |

## Étape 6 — La commande réutilisable, améliorée
Ajouts typiques à `.claude/commands/tests-docs-commit.md` : « Ne modifie aucun fichier hors du module et de son test »,
« Ne touche pas à `ateliers/` », « Si un test existant doit changer, arrête-toi et explique pourquoi ».

## Débrief (10 min)
- **« Qu'est-ce qui rend une automatisation acceptable ? »** → Les garde-fous testés avant, et la relecture du diff après.
- **« Quelle tâche ne confieriez-vous pas à un agent ? »** → Floue, architecturale, ou sans test pour juger.

## Grille d'évaluation
| Critère | Acquis | En cours |
|---|---|---|
| Ticket avec périmètre, critères et interdits | | |
| Garde-fous lus et hook testé avant de lancer l'agent | | |
| Diff relu ; aucun test modifié sans raison annoncée | | |
| Commande ou prompt réutilisable versionné | | |
