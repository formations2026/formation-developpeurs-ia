# Atelier 1 — Équiper son IDE (45 min)

**Objectif :** disposer de deux assistants fonctionnels et vérifier qu'ils respectent les règles du projet.

## Étapes
1. Ouvrez MeetRoom dans votre IDE. Lancez `make check` : tout doit être vert **avant** de toucher à l'IA.
2. Vérifiez que l'assistant de l'IDE répond dans le chat.
3. Lisez `AGENTS.md`. Ajoutez-y une règle qui vous semble manquer (une seule).
4. Demandez à chaque assistant : « Explique l'architecture de MeetRoom en dix lignes, avec les fichiers à l'appui. »
   Vérifiez deux affirmations dans le code.
5. **Test des règles.** Demandez : « Écris une fonction qui cherche les réservations d'un propriétaire. »
   Le SQL est-il paramétré ? Est-il écrit dans `app/repository.py` ? Y a-t-il un test ?
6. Remplissez le tableau.

| | Assistant 1 : ______ | Assistant 2 : ______ |
|---|---|---|
| Connaît les fichiers du projet ? | | |
| Respecte « SQL paramétré » ? | | |
| Propose un test ? | | |
| Ce pour quoi je l'utiliserai | | |

## Critères de réussite
- [ ] Deux assistants répondent sur le projet
- [ ] Le test des règles est passé pour au moins un des deux
- [ ] Vous savez quel assistant utiliser pour quoi

## Pour aller plus loin
Faites tourner un modèle local (Ollama + une extension d'IDE) et refaites l'étape 5. Que perdez-vous, que gagnez-vous ?

<details><summary>Corrigé indicatif</summary>

Un assistant qui lit `AGENTS.md` écrit la requête dans `app/repository.py`, avec un paramètre nommé (`:owner_id`),
et propose un test. Un chat web sans accès au projet invente souvent un ORM ou une table qui n'existent pas :
ce n'est pas un défaut du modèle, c'est une absence de contexte.
</details>
