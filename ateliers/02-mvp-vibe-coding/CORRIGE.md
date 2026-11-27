# Corrigé — Atelier 2 : La liste d'attente, en vibe coding encadré (60 min)

> Branche formateur. Le code complet est déjà dans cette branche : `git log --oneline main..formateur`.

## Partie 1 — Échauffement : les huit défauts de `code_a_corriger.py`
Version corrigée et testée : [`code_corrige.py`](code_corrige.py), tests : [`test_corrige_atelier2.py`](test_corrige_atelier2.py).

| N° | Ligne fautive | Défaut | Gravité | Correction |
|---|---|---|---|---|
| 1 | `f"SELECT * FROM bookings WHERE owner_email = '{email}'"` | **Injection SQL** | Critique | Requête paramétrée (`:owner_id`) |
| 2 | `DB_PASSWORD = "N0valine2026"` | **Secret dans le code** (partira dans Git) | Critique | Variable d'environnement ou coffre ; révoquer s'il a été poussé |
| 3 | `requests.post(..., verify=False)` | **TLS désactivé** : interception possible | Élevée | Laisser la vérification active (comportement par défaut) |
| 4 | `except: pass` | Erreurs **avalées** : panne silencieuse | Élevée | Laisser remonter, ou journaliser puis relever |
| 5 | `print(f"Réservation de {email} : {r[3]}")` | **Données personnelles dans le journal** (e-mail, titre) | Élevée | Identifiant technique uniquement, via `logging` |
| 6 | `eval(filtre)` | **Exécution de code arbitraire** | Critique | Paramètre typé (`since: datetime`) |
| 7 | `from fastapi_booking_utils import format_slot` | **Paquet inventé** : risque de slopsquatting | Élevée | Ne pas l'installer ; utiliser une bibliothèque réelle |
| 8 | Aucun typage, aucun test, dates en texte | Dette, bugs de fuseau horaire | Moyenne | Types, tests, dates ISO 8601 en UTC |

**Défauts trouvables sans savoir coder** (pour les copilotes) : le mot de passe (2), l'e-mail dans le journal (5), le paquet inconnu (7).
**Défauts que l'IA trouve presque toujours** : 1, 2, 3, 6. **Ceux qu'elle oublie souvent** : 5 (données personnelles) et 7 (paquet inventé),
précisément parce qu'elle a elle-même tendance à les produire.

## Partie 2 — La liste d'attente

### Le plan attendu (à obtenir avant tout code)
1. Table `waitlist` (salle, utilisateur, créneau) avec **unicité** (salle, utilisateur, créneau) dans la base.
2. Accès aux données dans `app/repository.py` : ajout et liste **dans l'ordre d'arrivée**.
3. Règles métier dans `app/services/booking.py` : salle inconnue, **salle libre**, déjà inscrit.
4. Routes `POST` et `GET /rooms/{id}/waitlist` dans `app/routers/rooms.py`.
5. Tests : un par critère d'acceptation.

**Corrections de plan typiques à faire faire :**
| Plan de l'IA | Correction humaine |
|---|---|
| « Installer Celery pour les notifications » | Hors périmètre, et aucune nouvelle dépendance |
| Oublie le cas « salle libre » | C'est le critère US2 : 409 si la salle est libre |
| Vérifie le doublon seulement dans le code Python | Contrainte `UNIQUE` en base : sinon, deux requêtes simultanées passent |
| `GET` renvoie `user_id` de chaque inscrit | Fuite de données : position et créneau uniquement |
| Tests à la fin | Tests écrits avec chaque étape |

### Le corrigé, commit par commit
| Commit | Contenu | Fichiers |
|---|---|---|
| `feat(waitlist): table et accès aux données` | Table avec `UNIQUE`, `add_waitlist` (renvoie `False` si doublon), `list_waitlist` | `app/db.py`, `app/repository.py`, `app/schemas.py` |
| `feat(waitlist): règles d'inscription et tests` | `join_waitlist` (404, salle libre, doublon), `waitlist_of`, 5 tests | `app/services/booking.py`, `tests/test_waitlist_service.py` |
| `feat(waitlist): routes POST et GET` | Routes, codes HTTP, 6 tests dont 401 et « sans donnée personnelle » | `app/routers/rooms.py`, `tests/test_waitlist_api.py` |

Montrer au débrief :
```bash
git log --oneline main..formateur
git show <commit>                 # un commit à la fois
git diff main formateur -- app/   # tout le code ajouté
```

### Les quatre pièges, et comment les reconnaître
1. **US2, la salle libre** : l'agent inscrit en attente sur une salle libre. Le test `test_salle_libre_409` le révèle.
2. **La fuite de données** : `GET /rooms/{id}/waitlist` renvoie `user_id`. Le test `test_liste_sans_donnee_personnelle` vérifie les clés exactes.
3. **Le doublon concurrent** : vérifier en Python puis insérer laisse passer deux requêtes simultanées. La contrainte `UNIQUE` règle le problème.
4. **Le test modifié** : l'agent modifie un test existant pour qu'il passe. Refuser, toujours.

### Exemple de journal de bord rempli
| Étape | Prompt utilisé | Accepté tel quel ? | Ce que j'ai corrigé |
|---|---|---|---|
| Plan | `prompts/10-planifier.md` + les trois user stories | Non | Retiré Celery, ajouté le cas « salle libre » |
| Données | « Applique l'étape 1 et 2 du plan, avec tests » | Oui, après relecture | — |
| Règles | « Étape 3. Un test par règle. » | Non | Doublon vérifié en base, pas en Python |
| Routes | « Étape 4. Un test par code de retour. » | Non | `user_id` retiré de la réponse |

## Débrief (10 min)
- **« Qui est tombé dans le piège de la salle libre ? »** → Souvent la moitié du groupe. Leçon : les critères d'acceptation se testent, ils ne se relisent pas seulement.
- **« Combien de prompts pour finir ? »** → 4 à 8 avec un plan, 10 à 20 sans. Le plan fait gagner du temps.
- **« Qu'avez-vous refusé ? »** → Faire citer au moins une proposition refusée par binôme.

## Grille d'évaluation
| Critère | Acquis | En cours |
|---|---|---|
| Six défauts au moins trouvés à l'échauffement | | |
| Le plan a été corrigé avant le code | | |
| Un test par critère d'acceptation | | |
| Aucun test existant modifié, `make check` vert | | |
| Au moins trois commits lisibles | | |
| Le participant explique chaque ligne de son diff | | |
