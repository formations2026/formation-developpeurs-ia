# Atelier 3 — Automatiser une tâche avec un agent (45 min)

**Objectif :** transformer une tâche répétitive en commande réutilisable, exécutée par un agent sous garde-fous.

## Étapes
1. **Choisissez une tâche** répétitive, délimitée et vérifiable (les cinq de la diapositive, plus une) :

   | N° | Tâche | Niveau |
   |---|---|---|
   | 1 | Tests manquants d'un module (`app/repository.py`) | Facile |
   | 2 | Docstrings des fonctions publiques | Facile |
   | 3 | Message de commit en français, format conventionnel | Facile |
   | 4 | Corriger toutes les alertes du linter sans changer le comportement | Moyen |
   | 5 | Journal des modifications à partir des commits | Moyen |
   | 6 | Paginer `GET /rooms/available` comme `GET /rooms` | Moyen |
2. **Écrivez le ticket** comme pour un collègue : périmètre, critères d'acceptation, interdits.
3. **Vérifiez les garde-fous** avant de lancer l'agent :
   - lisez `.claude/settings.json` (ou l'équivalent de votre outil) : que peut-il faire sans demander ?
   - testez le hook : `echo '{"tool_input":{"command":"rm -rf /tmp/x"}}' | scripts/garde.sh ; echo $?` → `2`
4. **Lancez l'agent sur une branche.** Exemple avec la commande fournie : `/tests-docs-commit app/repository.py`
5. **Relisez le diff** et remplissez le tableau.
6. **Rendez la commande réutilisable** : améliorez `.claude/commands/tests-docs-commit.md` ou ajoutez un prompt dans `prompts/`.

| Question | Réponse |
|---|---|
| Combien d'étapes l'agent a-t-il enchaînées seul ? | |
| Qu'a-t-il fait quand un test a échoué ? | |
| Qu'ai-je dû corriger moi-même ? | |
| A-t-il tenté quelque chose d'interdit ? | |
| Temps gagné ou perdu (estimation honnête) | |

## Si vous ne codez pas
Vous écrivez **le ticket** confié à l'agent (périmètre, critères d'acceptation, interdits) et vous réglez les garde-fous avec votre binôme : relisez les listes `allow`, `ask`, `deny` et proposez une règle à ajouter. Un bon ticket est ce qui fait réussir un agent.

## Critères de réussite
- [ ] La tâche est faite, `make check` est vert
- [ ] La commande est relançable sur un autre module
- [ ] Vous savez dire ce que l'agent ne peut pas faire, et grâce à quel fichier

## Le corrigé
Il est présenté par le formateur au débrief, après l'atelier. Comparer **votre** travail au corrigé est l'exercice le plus formateur : essayez d'abord.
