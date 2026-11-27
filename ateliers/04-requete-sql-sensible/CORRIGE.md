# Corrigé — Atelier 4 : Sécuriser une requête SQL sensible (50 min)

> Branche formateur. Requête corrigée et testée : [`requete_securisee.py`](requete_securisee.py),
> tests : [`test_corrige_atelier4.py`](test_corrige_atelier4.py) (`python -m pytest ateliers`).

## Étape 1 — Les risques (au moins cinq attendus, sept au total)
| N° | Risque | Où | Catégorie |
|---|---|---|---|
| 1 | **Mot de passe de production** collé dans un chat public | La demande | Secret |
| 2 | **Données personnelles nominatives** (noms, e-mails, service) envoyées à un tiers | La demande | RGPD |
| 3 | **Outil sans contrat** (chat public) : conservation et réutilisation inconnues | Le choix d'outil | RGPD, confidentialité |
| 4 | **Injection SQL** par concaténation de `debut` et `service` | Le code | Sécurité |
| 5 | **Exécution directe en production**, sans test ni plan d'exécution | La demande | Sécurité, disponibilité |
| 6 | **Classement nominatif des salariés** : finalité non justifiée, surveillance possible | Le besoin | RGPD, éthique |
| 7 | **Compte administrateur** utilisé pour une simple lecture | La chaîne de connexion | Moindre privilège |

**Si le message a déjà été envoyé :** le mot de passe est compromis. Les cinq gestes, dans l'ordre :
révoquer, remplacer, chercher l'usage, nettoyer, signaler (voir `SECURITY.md`).

## Étape 2 — Le workflow rempli
| Étape | Ce que nous faisons | Validé par |
|---|---|---|
| 1. Données | On retire noms, e-mails et identifiants ; on remplace par des données synthétiques (`Emp A`, `DEPT_1`). On se demande si le nominatif est utile : **non**, un agrégat par service répond au besoin. | DPO |
| 2. Contexte envoyé à l'IA | Le **schéma** des deux tables, le volume approximatif, la requête actuelle, le temps mesuré. Aucun secret, aucune donnée réelle. | RSSI |
| 3. Outil | Cloud **sous contrat d'entreprise** : sans donnée réelle, le risque est faible et la qualité meilleure. Local si la politique l'impose. | RSSI |
| 4. Requête obtenue | Paramétrée, agrégée, index proposés, plan d'exécution lu. | Développeur |
| 5. Avant exécution | Sur une **copie anonymisée**, avec un compte en **lecture seule**, test d'attaque passé. | Développeur + RSSI |
| 6. Trace | Mention dans le commit, note dans la pull request ; aucune donnée dans les journaux. | Tous |

## Étape 3 — Le prompt envoyé (exemple)
```text
PostgreSQL 16. Schéma :
  employees(id, name, email, dept)          ~ 2 000 lignes
  bookings(id, employee_id, start_at)       ~ 400 000 lignes
Requête actuelle (40 s) : [la requête, sans valeurs réelles]
Besoin : nombre de réservations d'un service depuis une date. Pas de données nominatives en sortie.
Donne une requête paramétrée, les index utiles et le plan d'exécution attendu.
Ne propose aucune exécution : je teste d'abord sur une copie.
```

## Étape 3 — La requête corrigée
```sql
SELECT e.dept, COUNT(*) AS nb
FROM bookings b
JOIN employees e ON e.id = b.employee_id
WHERE b.start_at >= :debut AND e.dept = :service
GROUP BY e.dept;

CREATE INDEX idx_bookings_start    ON bookings(start_at);
CREATE INDEX idx_bookings_employee ON bookings(employee_id);
CREATE INDEX idx_employees_dept    ON employees(dept);
```
Pourquoi c'était lent : aucune colonne filtrée n'était indexée, d'où un parcours complet de `bookings`.
Le plan d'exécution (`EXPLAIN` / `EXPLAIN ANALYZE` sur la copie) doit montrer l'usage des index.

## Étape 4 — Le test d'attaque
```python
def test_injection_sans_effet(conn):
    assert reservations_par_service(conn, "2000-01-01", "x' OR '1'='1") == []
    reservations_par_service(conn, "2000-01-01", "x'; DROP TABLE employees; --")
    assert conn.execute("SELECT COUNT(*) FROM employees").fetchone()[0] == 2
```

## Débrief (10 min)
- **« Le classement nominatif était-il nécessaire ? »** → Non : la question métier portait sur l'occupation par service. Minimiser, c'est d'abord **reformuler le besoin**.
- **« Cloud ou local ? »** → Les deux se défendent ; ce qui compte, c'est qu'**aucune donnée réelle** ne parte et que l'outil soit **sous contrat**.
- **« Qui a pensé au compte administrateur ? »** → Rarement relevé : le moindre privilège vaut aussi pour les requêtes.

## Grille d'évaluation
| Critère | Acquis | En cours |
|---|---|---|
| Au moins cinq risques identifiés, dont le secret | | |
| Aucune donnée réelle ni secret envoyé à l'IA | | |
| Requête paramétrée, plan d'exécution lu | | |
| Test d'attaque écrit | | |
| Chaque rôle a validé sa ligne | | |
