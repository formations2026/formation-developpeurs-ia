# Atelier 2 — La liste d'attente, en vibe coding encadré (60 min)

**Objectif :** livrer une fonctionnalité complète avec un assistant, en gardant le contrôle : plan, petites étapes, relecture, commits.

## Échauffement (10 min) : relire du code généré
Ouvrez [`code_a_corriger.py`](code_a_corriger.py). Ce code « fonctionne ». Trouvez au moins **six défauts**
avec la checklist de relecture, d'abord seul, puis en demandant à l'assistant :
« Relis ce fichier comme un attaquant puis comme un mainteneur. Classe par gravité. Ne corrige pas. »

## La fonctionnalité : la liste d'attente
> **En tant que** salarié, **je veux** m'inscrire sur la liste d'attente d'une salle pour un créneau occupé,
> **afin d'**être prévenu si elle se libère.

Trois user stories, de difficulté croissante (les mêmes que sur la diapositive) :

| | User story | Critères d'acceptation |
|---|---|---|
| US1 | S'inscrire en liste d'attente | `POST /rooms/{id}/waitlist` avec `start_at` et `end_at` → 201 ; salle inconnue → 404 |
| US2 | Refuser les inscriptions inutiles | 409 si la salle est **libre** sur le créneau (il suffit de réserver) ; 409 si déjà inscrit |
| US3 | Consulter la liste | `GET /rooms/{id}/waitlist` : inscrits dans l'ordre d'arrivée, **sans donnée personnelle** |

Un test par critère.

Définition de « terminé » : `make check` vert · aucun test existant modifié · aucune nouvelle dépendance · diff relu ligne à ligne.

## Étapes
1. `git switch -c atelier-2-prenom`
2. Demandez un **plan** (prompt `prompts/10-planifier.md`). Corrigez-le avant tout code.
3. Avancez par étapes : schéma → service → route → tests. **Un commit par étape verte.**
4. Relisez le diff final : `git diff main`.
5. Faites rédiger le message du dernier commit (le pourquoi, pas le comment).

## Journal de bord
| Étape | Prompt utilisé | Accepté tel quel ? | Ce que j'ai corrigé |
|---|---|---|---|
| Plan | | | |
| Service | | | |
| Route | | | |
| Tests | | | |

## Si vous ne codez pas
Vous êtes **copilote**. Vous ne tapez pas de code : vous tenez le journal de bord, vous vérifiez chaque critère d'acceptation dans `/docs` (l'interface de test de l'API), et vous faites l'échauffement en langage courant : « qu'est-ce qui vous inquiéterait dans ce fichier ? ». Les défauts 2, 5 et 7 se trouvent sans savoir programmer.

## Critères de réussite
- [ ] Les critères d'acceptation ont chacun leur test
- [ ] Au moins trois commits, messages lisibles
- [ ] Vous pouvez expliquer chaque ligne du diff

## Bloqué ?
Le corrigé complet est sur la branche `solution/atelier-2`, en trois commits (données, règles, routes) :
`git log --oneline main..solution/atelier-2` puis `git show <commit>`. Regardez un commit à la fois, pas tout le diff.

<details><summary>Corrigé indicatif de l'échauffement</summary>

1. Injection SQL (f-string) · 2. mot de passe en dur · 3. `verify=False` (TLS désactivé) · 4. `except: pass` qui avale les erreurs ·
5. e-mail et titre écrits dans le journal · 6. `eval` sur une entrée utilisateur · 7. paquet `fastapi-booking-utils` qui n'existe pas ·
8. aucun typage, aucun test, comparaison de dates sous forme de chaînes locales.
</details>
