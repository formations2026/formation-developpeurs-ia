# Branche formateur

Cette branche contient **tout `main`**, plus les réponses. **Ne la montrez aux participants qu'au débrief.**

> Si le dépôt est public, cette branche l'est aussi. Pour la garder confidentielle,
> passez le dépôt en privé et invitez les participants le jour J, ou copiez cette branche
> dans un dépôt privé séparé.

## Ce qu'elle ajoute
| Contenu | Où |
|---|---|
| Corrigé détaillé de chaque atelier (réponses, pièges, débrief, grille d'évaluation) | `ateliers/0X-…/CORRIGE.md` |
| Atelier 2 : la liste d'attente codée, en trois commits | `app/`, `tests/test_waitlist_*.py` |
| Atelier 2 : l'échauffement corrigé et testé | `ateliers/02-…/code_corrige.py` |
| Atelier 3 : la pagination faite par un agent, et son prompt | `app/routers/rooms.py`, `prompts/11-paginer.md` |
| Atelier 4 : la requête sécurisée et son test d'attaque | `ateliers/04-…/requete_securisee.py` |
| Atelier 5 : la validation de noms sans biais | `ateliers/05-…/validation_noms_corrigee.py` |
| QCM corrigé (20 questions, avec explications) | `docs/formateur/QCM-CORRIGE.md` |
| Exercices éclair corrigés | `docs/formateur/EXERCICES-ECLAIR-CORRIGES.md` |
| Déroulé minuté des deux jours | `docs/formateur/DEROULE.md` |
| Scénarios des trois démonstrations, avec plan B | `docs/formateur/DEMOS.md` |

## Pendant la formation
```bash
git switch formateur
make check                         # l'application corrigée : 40 tests
make corriges                      # le code corrigé des ateliers : 30 tests
git log --oneline main..formateur  # les étapes de la solution, une par commit
git diff main formateur -- app/    # tout le code ajouté pour les ateliers 2 et 3
```

Au débrief de l'atelier 2, montrez les commits **un par un** (`git show <commit>`) : c'est le rythme
« une étape verte, un commit » que les participants doivent retenir.
