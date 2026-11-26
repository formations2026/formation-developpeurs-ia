# ADR 012 — Suggestion de salle par un LLM

Statut : accepté (exemple pédagogique)

## Contexte
Les salariés perdent du temps à choisir une salle adaptée.

## Décision
Un LLM sous contrat propose trois salles. Le salarié choisit. Rien n'est réservé automatiquement.

## Données envoyées au modèle
Créneau, nombre de participants, équipements demandés.
**Jamais** : noms, titres de réunion, agendas, niveau hiérarchique.

## Risques et parades
| Risque | Parade | Vérification |
|---|---|---|
| Biais de priorité | Aucun critère hiérarchique dans la demande | Test contrefactuel |
| Injection de prompt | Aucun texte libre transmis au modèle | Revue + test |
| Fuite de données | Minimisation ci-dessus, fournisseur sous contrat (art. 28 RGPD) | Registre des traitements |
| Coût | Plafond mensuel et cache | Tableau de bord |

## Contrôle humain
Aucune réservation ni annulation automatique. Les salariés sont informés qu'une IA propose.

## Conséquences
Fonctionnalité classée « transparence » au sens du règlement européen sur l'IA (à confirmer par le juridique).
