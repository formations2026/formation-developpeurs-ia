# Atelier 3 — Automatiser une tâche avec un agent (45 min)

**Objectif :** transformer une tâche répétitive en commande réutilisable, exécutée par un agent sous garde-fous.

## Étapes
1. **Choisissez une tâche** répétitive, délimitée et vérifiable. Suggestions sur MeetRoom :
   - ajouter la pagination à `GET /rooms/available` ;
   - compléter les docstrings et les tests de `app/repository.py` ;
   - ajouter un test d'attaque par route.
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

## Critères de réussite
- [ ] La tâche est faite, `make check` est vert
- [ ] La commande est relançable sur un autre module
- [ ] Vous savez dire ce que l'agent ne peut pas faire, et grâce à quel fichier

<details><summary>Corrigé indicatif</summary>

Une bonne tâche pour un agent est répétitive, délimitée et vérifiable par les tests. Si l'agent modifie un test existant
pour le faire passer, refusez et regardez pourquoi : c'est le signal d'alerte le plus important de l'atelier.
</details>
