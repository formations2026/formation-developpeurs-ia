# Atelier 4 — Sécuriser une requête SQL sensible (50 min)

**Objectif :** transformer un usage dangereux de l'IA en workflow sécurisé. En trinômes : développeur, RSSI, DPO.

## La situation
Un développeur pressé s'apprête à coller ceci dans un chat public (tout est **fictif**) :

> « Optimise cette requête, elle met 40 s en prod. Je l'exécuterai directement ensuite.
> Connexion : postgres://admin:N0valine2026@db-prod.novaline.local/meetroom.
> Voici quelques lignes pour que tu comprennes : Claire Morel, claire.morel@novaline.fr, RH, 14 réservations ;
> Karim Benali, k.benali@novaline.fr, DSI, 11 réservations… »

La requête est dans [`requete_a_securiser.py`](requete_a_securiser.py). Elle interroge une **autre base** (fictive) de Novaline,
qui contient une table `employees` : ce n'est pas le schéma de MeetRoom, et c'est voulu — MeetRoom ne stocke aucune identité.

## Étapes
1. Listez **au moins cinq risques** dans la demande et dans le code.
2. Complétez le workflow :

| Étape | Ce que nous faisons | Validé par |
|---|---|---|
| 1. Données : que retire-t-on, que remplace-t-on ? | | DPO |
| 2. Contexte envoyé à l'IA | | RSSI |
| 3. Outil : cloud sous contrat ou local ? Pourquoi ? | | RSSI |
| 4. Requête obtenue : paramétrée, optimisée | | Développeur |
| 5. Avant exécution : où, avec quels droits, quel test ? | | Développeur + RSSI |
| 6. Trace : que garde-t-on ? | | Tous |

3. Obtenez la requête finale avec l'outil choisi, en n'envoyant que **le schéma et des données synthétiques**.
4. Écrivez le test qui prouve que la requête résiste à une injection.

## Si vous ne codez pas
Cet atelier est fait pour vous : tenez le rôle **RSSI** ou **DPO**. Vous validez votre ligne du workflow et vous refusez tant que la réponse n'est pas précise.

## Critères de réussite
- [ ] Aucune donnée réelle ni secret n'a été envoyé
- [ ] La requête est paramétrée et son plan d'exécution a été lu
- [ ] Un test d'attaque existe
- [ ] Chaque rôle a validé sa ligne

## Le corrigé
Il est présenté par le formateur au débrief, après l'atelier. Comparer **votre** travail au corrigé est l'exercice le plus formateur : essayez d'abord.
