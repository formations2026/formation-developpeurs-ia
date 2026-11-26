# Aide-mémoire des deux jours

## Le prompt du développeur : C.R.O.F. + L
**C**ontexte (langage, fichiers) · **R**ôle · **O**bjectif testable · **F**ormat (diff, tests) · **L**imites (pas de dépendance, ne pas toucher à…)

## Douze réflexes
1. Le bon outil au bon niveau d'autonomie
2. Vos règles écrites dans `AGENTS.md`
3. Petites étapes, un commit par étape verte
4. Relire chaque ligne générée
5. Outils déterministes pour trouver, IA pour expliquer
6. Agents : branche dédiée, droits minimaux
7. Aucun secret ni donnée réelle dans un prompt
8. Toute dépendance proposée se vérifie
9. Cloud sous contrat ou local, selon les données
10. Une trace proportionnée à la criticité
11. Des tests divers contre les biais
12. Une charte vérifiable, automatisée

## Commandes utiles
```bash
make check                                   # qualité + sécurité + tests
git diff --staged | <assistant> "message de commit, dis le pourquoi"
pre-commit install                           # scan de secrets à chaque commit
docker run --rm --network none -v "$PWD":/app -w /app python:3.12-slim python script.py
docker history --no-trunc <image>            # un secret traîne-t-il dans une couche ?
```
