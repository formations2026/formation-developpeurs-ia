# Atelier 5 — Revoir une user story « IA » (40 min)

**Objectif :** repérer les risques d'une fonctionnalité à base d'IA et en proposer une version remédiée, qui garde sa valeur.

## La user story n° 42 — Assistant intelligent de réservation
> **En tant que** salarié, **je veux** qu'un assistant IA me propose automatiquement la meilleure salle, **afin de** gagner du temps.
>
> **Détails :** l'assistant lit les agendas de tous les participants et envoie les titres des réunions et la liste
> des participants à un LLM cloud. En cas de conflit, la priorité est donnée au participant de plus haut niveau hiérarchique.
> Une réservation est annulée automatiquement si aucun badge n'est détecté dans la salle dix minutes après le début.
> Les prompts et les réponses sont conservés deux ans pour améliorer le modèle.

## Étapes
1. Listez les risques et classez-les.

| Risque identifié | Catégorie (sécurité, RGPD, biais, éthique, coût) | Gravité (1-3) | Remédiation proposée |
|---|---|---|---|
| | | | |

2. Réécrivez la user story et ses critères d'acceptation.
3. Rédigez la note de décision à partir de `docs/adr/000-modele.md`.
4. **Exercice de code (biais).** Ouvrez [`validation_noms.py`](validation_noms.py) : la validation refuse de vrais noms.
   Écrivez les tests qui le montrent, puis corrigez… ou supprimez la règle.

## Si vous ne codez pas
Cet atelier ne demande pas de coder : vous menez l'analyse des risques et la réécriture de la user story. L'exercice de code (étape 4) est facultatif pour vous.

## Critères de réussite
- [ ] Au moins six risques, dont un de chaque catégorie
- [ ] La version remédiée reste utile à l'utilisateur
- [ ] La note de décision dit quelles données partent, et lesquelles ne partent jamais

## Le corrigé
Branche formateur : voir [`CORRIGE.md`](CORRIGE.md).
