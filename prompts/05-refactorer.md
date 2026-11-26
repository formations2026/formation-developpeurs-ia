# Refactorer sans rien casser

**Quand l'utiliser :** quand une fonction fait trop de choses

```text
Découpe en fonctions de moins de 30 lignes. Le comportement ne change pas. Les tests existants doivent passer sans être modifiés.
```

**À vérifier après :** relire le résultat, lancer `pytest`, et noter ici ce qui a dû être corrigé pour améliorer le prompt.
