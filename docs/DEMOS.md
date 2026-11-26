# Scénarios des démonstrations (formateur)

Règles communes : jouer chaque démonstration une fois avant la formation ; toujours sur une branche
(`git switch -c demo-N`) ; `make check` vert montré à l'écran avant de commencer ; faire des captures
d'écran de votre répétition, à coller dans les diapositives « LIVE DÉMO » comme plan B.

## Démo 1 — Une même tâche, trois outils (10 min)
Demande, identique dans les trois outils :
> Ajoute à MeetRoom `GET /rooms/{id}/bookings?date=YYYY-MM-DD` : les réservations d'une salle pour une journée,
> sans le titre ni le propriétaire, avec un test.

Cette route n'existe pas dans le dépôt.
1. Chat web : coller la demande seule. Faire relever les noms inventés.
2. Assistant d'IDE en mode agent, `app/routers/rooms.py` ouvert.
3. Agent en ligne de commande : le laisser lancer `pytest` et corriger.
4. `git diff` sur chaque essai ; remplir la grille d'observation. Entre deux essais : `git restore . && git clean -fd`.

À faire remarquer : qui a lu le projet, qui a écrit un test, qui l'a lancé, qui expose le titre.

## Démo 2 — Vibe coding encadré (10 min)
1. « Propose un plan pour `GET /rooms/{id}` (détail d'une salle). N'écris pas de code. » Corriger le plan à voix haute.
2. « Applique le plan. Un test pour 200, un pour 404. »
3. `make check`, puis appel dans `/docs`.
4. **Bug provoqué** par une demande vague : « Ajoute aussi les réservations de la salle. » → le titre des réunions fuit.
5. « Sans titre ni propriétaire. Ajoute le test qui le prouve. »
6. Faire rédiger le message de commit (le pourquoi).

Plan B : `git log --oneline main..solution/atelier-2` puis `git show` commit par commit.

## Démo 3 — Automatiser (8 min)
1. Ouvrir `.claude/commands/tests-docs-commit.md`.
2. Montrer le garde-fou : `echo '{"tool_input":{"command":"rm -rf /tmp/x"}}' | scripts/garde.sh ; echo $?` → `2`.
3. `/tests-docs-commit app/repository.py` (autre outil : `prompts/02-tester.md`).
4. Relire le diff : les tests ajoutés testent-ils vraiment quelque chose ?
5. Relancer sur `app/services/booking.py`.

Plan B : `git diff main solution/atelier-3`.
