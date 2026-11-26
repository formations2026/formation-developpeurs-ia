# Contribuer à MeetRoom

1. **Une branche par tâche** : `git switch -c feat/pagination`. Jamais de commit direct sur `main`.
2. **De petites étapes** : un commit par étape verte (`pytest` passe).
3. **Des messages qui disent le pourquoi** (Conventional Commits) :

   ```
   fix(bookings): accepte les réservations contiguës

   Une salle libérée à 11 h était refusée pour 11 h-12 h (comparaison inclusive).
   Ajout du test de contiguïté. Refs #131

   Assisted-by: assistant de code (outil autorisé)
   ```
4. **Avant la pull request** : `make check`, puis relire son propre diff (`git diff main`).
5. **La pull request** remplit le modèle (`.github/pull_request_template.md`) et attend une approbation humaine.

## Travailler avec un assistant de code
- Lire `AGENTS.md` : c'est aussi ce que lit l'assistant.
- Plus de deux fichiers à modifier : demander un plan d'abord.
- Ne jamais accepter qu'un test existant soit modifié « pour passer ».
- Toute nouvelle dépendance est une décision : existence, âge, mainteneur, licence.
- Un incident (fuite, mauvaise commande, hallucination coûteuse) se signale sans blâme : voir `SECURITY.md`.
