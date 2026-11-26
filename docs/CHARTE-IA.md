# Charte IA de l'équipe MeetRoom

Une page, huit engagements, chacun avec sa vérification. Révisée chaque trimestre.

| Rubrique | Notre engagement | Vérifié par |
|---|---|---|
| Outils | Nous utilisons uniquement les assistants listés en annexe, avec nos comptes d'entreprise. | Console d'administration |
| Données | Nous n'envoyons aucune donnée personnelle réelle à un outil d'IA ; nous utilisons des données synthétiques (`scripts/fake_data.py`). | Revue, sensibilisation |
| Secrets | Aucun secret dans le code, les prompts ou les images. | Hook gitleaks + scan en CI |
| Relecture | Toute pull request est relue et approuvée par un humain qui comprend chaque ligne. | Protection de branche |
| Sécurité | La CI bloque la fusion sur faille détectée, secret détecté ou dépendance vulnérable. | `.github/workflows/garde-fous.yml` |
| Trace | Nous ajoutons `Assisted-by:` dans les commits de production assistés par l'IA. | Modèle de pull request |
| Agents | Nos agents travaillent sur une branche dédiée, sans accès à la production ; les commandes sensibles sont validées. | `.claude/settings.json`, `scripts/garde.sh` |
| Vie de la charte | Référent : tech lead. Les incidents se signalent sans blâme. Révision chaque trimestre. | Point d'équipe daté |

## Le feu tricolore
- **Vert — j'y vais** : expliquer du code, tests, docstrings, refactoring couvert par des tests, prototype sur données synthétiques.
- **Orange — avec précaution** : code de production, agent multi-fichiers, nouvelle dépendance → branche, pull request, revue humaine.
- **Rouge — pas sans accord** : secrets, données personnelles réelles, code de sécurité ou de paiement, compte personnel → accord du RSSI ou du DPO.

En cas de doute, c'est orange, et l'on demande avant.

## Annexe : outils autorisés
| Outil | Usage | Compte |
|---|---|---|
| _à compléter_ | | entreprise |

_Dernière révision : à dater · Prochaine révision : à dater_
