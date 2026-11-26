# Instructions pour GitHub Copilot

Les règles complètes du projet sont dans `AGENTS.md` à la racine. Résumé :

- Python 3.11+, FastAPI, SQLite. SQL paramétré uniquement, écrit dans `app/repository.py`.
- Typage, docstrings, un test par fonction publique. Dates en UTC.
- Aucune nouvelle dépendance sans le demander. Aucun secret dans le code.
- Journaux : identifiants techniques uniquement, aucune donnée personnelle.
- Ne jamais modifier un test existant pour le faire passer.
