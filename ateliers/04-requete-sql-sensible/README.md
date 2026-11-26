# Atelier 4 — Sécuriser une requête SQL sensible (50 min)

**Objectif :** transformer un usage dangereux de l'IA en workflow sécurisé. En trinômes : développeur, RSSI, DPO.

## La situation
Un développeur pressé s'apprête à coller ceci dans un chat public (tout est **fictif**) :

> « Optimise cette requête, elle met 40 s en prod. Je l'exécuterai directement ensuite.
> Connexion : postgres://admin:N0valine2026@db-prod.novaline.local/meetroom.
> Voici quelques lignes pour que tu comprennes : Claire Morel, claire.morel@novaline.fr, RH, 14 réservations ;
> Karim Benali, k.benali@novaline.fr, DSI, 11 réservations… »

La requête est dans [`requete_a_securiser.py`](requete_a_securiser.py).

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

## Critères de réussite
- [ ] Aucune donnée réelle ni secret n'a été envoyé
- [ ] La requête est paramétrée et son plan d'exécution a été lu
- [ ] Un test d'attaque existe
- [ ] Chaque rôle a validé sa ligne

<details><summary>Corrigé indicatif</summary>

**Risques :** mot de passe de production dans le prompt (à révoquer) · données personnelles nominatives ·
chat public sans contrat · injection SQL par concaténation · exécution directe en production sans test ·
classement nominatif des salariés (finalité à justifier : un agrégat par service suffit sans doute).

**Requête :**
```sql
SELECT e.dept, COUNT(*) AS nb
FROM bookings b JOIN employees e ON e.id = b.employee_id
WHERE b.start_at >= :debut AND e.dept = :service
GROUP BY e.dept ORDER BY nb DESC;
```
Index utile : `bookings(start_at)` et `bookings(employee_id)`. Exécution : d'abord sur une copie anonymisée,
avec un compte en lecture seule.
</details>
