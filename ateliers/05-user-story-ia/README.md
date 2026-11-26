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

## Critères de réussite
- [ ] Au moins six risques, dont un de chaque catégorie
- [ ] La version remédiée reste utile à l'utilisateur
- [ ] La note de décision dit quelles données partent, et lesquelles ne partent jamais

<details><summary>Corrigé indicatif</summary>

**Risques :** titres de réunion et participants envoyés à un tiers (données personnelles, parfois très sensibles) ·
priorité hiérarchique (discrimination indirecte) · annulation automatique sans recours (décision automatisée) ·
détection par badge (surveillance des salariés) · conservation deux ans pour une autre finalité ·
injection de prompt par les titres de réunion · coût non borné.

**Remédiations :** n'envoyer que créneau, effectif, équipements · priorité selon le besoin, pas le grade ·
notification et confirmation avant toute annulation · pas de badge · conservation courte ·
information des salariés, avis du DPO. Voir `docs/adr/012-suggestion-salle.md`.

**Code :** souvent, « non vide et de longueur raisonnable » suffit ; le biais vient d'une règle inutile.
</details>
