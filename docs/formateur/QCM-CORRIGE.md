# QCM de validation — corrigé (20 questions)

Seuil de validation proposé : **14 bonnes réponses sur 20**. Réponse individuelle, puis correction collective.
Les questions 1 à 8 sont sur les diapositives « Quiz (1/5) » et « (2/5) », 9 à 20 sur les suivantes.

| N° | Question | Réponse | Pourquoi |
|---|---|---|---|
| 1 | Qu'est-ce qui distingue un agent d'un simple LLM ? | **B.** Il agit avec des outils dans une boucle | Observer, agir, vérifier, corriger : c'est la boucle d'agent (partie 1). |
| 2 | Où mettre les règles de codage lues par plusieurs assistants ? | **C.** Dans `AGENTS.md`, versionné | Écrit une fois, lu par les outils, relu en pull request. |
| 3 | Un LLM dit « ce code n'a pas de faille ». Vous… | **B.** Gardez SAST et revue humaine | Un LLM est confiant, pas fiable : les outils déterministes trouvent, l'humain décide. |
| 4 | L'IA propose `pip install booking-helper-pro`. Vous… | **C.** Vérifiez existence, âge, mainteneur | Paquet possiblement halluciné, donc cible de slopsquatting. |
| 5 | Pour optimiser une requête sur des données personnelles, on envoie… | **B.** Le schéma et des données synthétiques | L'IA n'a pas besoin des vraies lignes (atelier 4). |
| 6 | Une clé d'API a fuité dans une image Docker. Vous… | **D.** Révoquez la clé, puis reconstruisez | Supprimer la ligne ne suffit pas : la clé reste dans les couches et les copies. |
| 7 | Des données pseudonymisées sont… | **A.** Toujours des données personnelles | La ré-identification reste possible : le RGPD s'applique. |
| 8 | ISO/IEC 23894 porte sur… | **C.** La gestion des risques de l'IA | Adaptation de l'ISO 31000 aux risques propres à l'IA. |
| 9 | L'agent oublie une consigne donnée au début d'une longue session. Cause probable ? | **B.** La fenêtre de contexte est saturée | Fichiers lus et sorties de commandes remplissent le contexte : une tâche, une session. |
| 10 | À quoi sert le mode plan ? | **C.** À corriger avant que le code existe | Corriger sept lignes de plan coûte moins que trois cents lignes de diff. |
| 11 | L'agent modifie un test existant « pour qu'il passe ». Vous… | **A.** Refusez et cherchez pourquoi | Le test décrit le comportement attendu : le modifier masque le défaut. |
| 12 | Différence entre une consigne dans `AGENTS.md` et un hook ? | **D.** Le hook est du code : il s'applique toujours | La consigne peut être oubliée par le modèle ; le hook, non. |
| 13 | La meilleure tâche à confier à un agent est… | **B.** Répétitive, délimitée, vérifiable par les tests | Les tests permettent de juger le résultat sans tout relire. |
| 14 | Étude METR (2025) sur des développeurs expérimentés : | **C.** 19 % plus lents, en se croyant plus rapides | Le ressenti de productivité ne remplace pas la mesure. |
| 15 | Le slopsquatting consiste à… | **A.** Publier un paquet piégé sous un nom halluciné | L'attaquant exploite les noms que les modèles inventent souvent. |
| 16 | Une injection de prompt indirecte, c'est… | **B.** Des instructions cachées dans un contenu lu | Issue, README, page web, réponse MCP : tout contenu lu peut donner des ordres. |
| 17 | Un secret passé en `ARG` dans un Dockerfile… | **D.** Reste visible dans l'historique de l'image | `docker history` le révèle ; utiliser un secret de construction. |
| 18 | Avant d'envoyer une trace d'erreur à une IA, on… | **C.** Retire secrets et données personnelles | Type d'erreur, code minimal, comportement attendu : cela suffit. |
| 19 | Un code 100 % généré, au regard du droit d'auteur : | **A.** Protection incertaine | La protection suppose des choix créatifs humains ; la question n'est pas tranchée. |
| 20 | Quel engagement de charte est vérifiable ? | **B.** « Toute PR est approuvée par un humain » | Vérifiable dans l'historique, contrairement à « prudence » ou « vigilance ». |

## Lecture des résultats
- **Moins de 14** : revoir en priorité les questions manquées avec l'aide-mémoire (`docs/AIDE-MEMOIRE.md`).
- **Questions les plus souvent manquées** (à surveiller) : 7 (pseudonymisation), 12 (hook), 17 (`ARG` Docker).
