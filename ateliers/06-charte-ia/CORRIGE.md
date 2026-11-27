# Corrigé — Atelier 6 : La charte IA de l'équipe (40 min)

> Branche formateur. Exemple complet de charte : `docs/CHARTE-IA.md`.

## Engagements : de la version vague à la version vérifiable
| Rubrique | Vague (à refuser) | Vérifiable (à viser) | Vérifié par |
|---|---|---|---|
| Outils | « Nous utilisons des outils sûrs. » | « Nous utilisons uniquement les assistants listés en annexe, avec nos comptes d'entreprise. » | Console d'administration |
| Données | « Nous protégeons les données. » | « Nous n'envoyons aucune donnée personnelle réelle à un outil d'IA ; nous utilisons `scripts/fake_data.py`. » | Revue, sensibilisation |
| Secrets | « Attention aux secrets. » | « Aucun secret dans le code, les prompts ou les images ; un hook bloque le commit sinon. » | Hook gitleaks + CI |
| Relecture | « Nous relisons le code. » | « Toute pull request est approuvée par un humain avant fusion. » | Protection de branche |
| Sécurité | « Le code est sécurisé. » | « La CI bloque sur faille, secret ou dépendance vulnérable. » | `.github/workflows/garde-fous.yml` |
| Licences et trace | « Nous respectons les licences. » | « Mention `Assisted-by:` dans les commits de production assistés par l'IA ; scan des licences en CI. » | Modèle de PR, CI |
| Agents | « Les agents sont encadrés. » | « Nos agents travaillent sur une branche dédiée, sans accès à la production. » | `.claude/settings.json`, protection de branche |
| Vie de la charte | « La charte évoluera. » | « Référent : le tech lead. Révision le premier lundi de chaque trimestre. » | Invitation datée |

## Le test des quatre questions, appliqué
« Nous utilisons l'IA de manière responsable. »
- Vérifiable ? **Non.** Précis ? **Non.** Tenable ? Oui. Utile contre un vrai risque ? **Non.** → À réécrire.

« Toute pull request est approuvée par un humain avant fusion. »
- Vérifiable ? **Oui** (historique GitHub). Précis ? **Oui.** Tenable ? **Oui.** Utile ? **Oui** (code non relu). → À garder.

## Bonus — Trois engagements automatisés
| Engagement | Contrôle automatique | Fichier du dépôt |
|---|---|---|
| Aucun secret | Hook pre-commit + scan en CI | `.pre-commit-config.yaml`, `garde-fous.yml` |
| La CI bloque sur faille | `bandit`, `pip-audit` | `.github/workflows/garde-fous.yml` |
| Usage de l'IA déclaré et relu | Cases à cocher dans la pull request | `.github/pull_request_template.md` |

## Les erreurs fréquentes
- **Trop d'engagements** : au-delà de dix, personne ne les retient. Six à huit suffisent.
- **Des interdits sans alternative** : « pas d'IA sur les données personnelles » sans dire quoi faire à la place (données synthétiques).
- **Aucun responsable ni date de révision** : la charte meurt en trois mois.

## Restitution (15 min) — grille
| Critère | Acquis | En cours |
|---|---|---|
| Six engagements au moins, tous vérifiables | | |
| Chaque engagement a sa vérification | | |
| Trois engagements automatisés | | |
| Un référent et une date de révision | | |

Noter au tableau les engagements présents dans **toutes** les chartes : ils forment le socle d'une charte d'entreprise.
