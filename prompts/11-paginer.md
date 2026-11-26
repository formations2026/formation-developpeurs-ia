# Paginer une route de liste

**Quand l'utiliser :** pour aligner une route de liste sur le modèle de `GET /rooms`.

```text
Ajoute la pagination à la route indiquée, sur le modèle exact de GET /rooms (app/routers/rooms.py) :
paramètres page (>= 1) et size (1 à 100), réponse RoomPage (items, total, page, size), 422 si invalide.
Mets à jour les tests existants de cette route en expliquant chaque changement de contrat,
ajoute un test de deuxième page et un test de paramètre invalide.
Aucune nouvelle dépendance. Ne touche à aucune autre route. Lance make check et résume.
```

**À vérifier après :** le changement de contrat (une liste devient un objet paginé) est un changement cassant :
il doit être dit dans le message de commit et dans la pull request.
