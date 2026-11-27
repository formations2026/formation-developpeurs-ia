# Exercices éclair — corrigés

## Jour 1 — Réécrire son dernier prompt avec C.R.O.F. + L (2 min)
Prompt de départ typique : « Corrige le bug de réservation. »

Version attendue :
> **Contexte :** API FastAPI MeetRoom, `app/services/booking.py`, le test `test_creneaux_contigus_acceptes` échoue.
> **Rôle :** développeur backend attentif aux dates et fuseaux horaires.
> **Objectif :** une réservation 11 h-12 h doit être acceptée après une réservation 10 h-11 h.
> **Format :** la cause en trois lignes, puis le diff minimal.
> **Limites :** ne modifie aucun test ; aucune nouvelle dépendance.

Brique la plus souvent manquante : **l'objectif vérifiable**, puis **les limites**.

## Jour 1 — Six prompts à ne plus écrire
Réponse attendue au vote « lequel avez-vous écrit cette semaine ? » : presque toujours « Corrige ce bug » ou
« Écris les tests ». Point commun de toutes les versions utiles : **un critère de réussite vérifiable**.

## Jour 2 — Trouvez les cinq fuites (3 min)
| N° | Fuite | Nature | Action |
|---|---|---|---|
| 1 | `user=claire.morel@novaline.fr ip=10.4.12.87` | Donnée personnelle et plan du réseau interne | Retirer |
| 2 | `postgres://meetroom:N0valine2026@db-prod…` | **Secret** de production | Retirer ; **révoquer** s'il est parti |
| 3 | `Authorization: Bearer eyJ…` | Jeton d'accès | Retirer ; révoquer s'il est parti |
| 4 | `'title': 'Entretien préalable - K. Benali'` | Donnée personnelle **très sensible** | Retirer |
| 5 | `/srv/meetroom/app/pricing/algo_tarif_v3.py` | Secret d'affaires (algorithme interne) | Remplacer par un nom neutre |

Question bonus — ce qui suffit à l'IA : le type d'erreur, l'extrait de code minimal avec des noms neutres,
le comportement attendu.

## Jour 2 — Le feu tricolore : classez les huit situations (5 min)
Classement indicatif, à adapter à la politique de l'entreprise. Les désaccords sont l'intérêt de l'exercice.

| N° | Situation | Couleur | Pourquoi |
|---|---|---|---|
| 1 | Faire expliquer une expression régulière | **Vert** | Aucun risque, outil autorisé |
| 2 | Coller un export de la table des salariés | **Rouge** | Données personnelles réelles |
| 3 | Agent qui modifie douze fichiers du service | **Orange** | Code de production : branche, PR, revue |
| 4 | Compte personnel gratuit « juste pour ce bug » | **Rouge** | Outil sans contrat, code d'entreprise |
| 5 | Générer les docstrings d'un module utilitaire | **Vert** | Faible risque, relecture rapide |
| 6 | Accepter une bibliothèque proposée par l'IA | **Orange** | Vérifier existence, âge, mainteneur, licence |
| 7 | Identifiants de production donnés à l'agent | **Rouge** | Secret et accès à la production |
| 8 | Réécrire le module d'authentification | **Orange à rouge** | Code de sécurité : accord du RSSI |

## Jour 2 — Quatre situations, cloud ou local
Réponses détaillées sur la diapositive « Exemple : quatre situations, quatre décisions ». Point clé :
avec des données synthétiques, le cloud sous contrat redevient souvent possible.
