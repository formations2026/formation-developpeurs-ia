# Instructions pour Claude Code

Les règles du projet sont dans AGENTS.md, partagé avec tous les assistants :

@AGENTS.md

## Spécifique à Claude Code
- Les permissions (allow / ask / deny) et le hook de garde sont dans `.claude/settings.json`.
- La commande `/tests-docs-commit <module>` enchaîne tests, docstrings et proposition de message de commit.
- Pour toute tâche de plus de deux fichiers : proposer un plan et attendre la validation.
