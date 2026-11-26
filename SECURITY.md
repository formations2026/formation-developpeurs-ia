# Sécurité

## Signaler un problème
Ouvrir un ticket privé auprès du référent sécurité de l'équipe (ne pas décrire une faille dans une issue publique).
Les incidents liés à l'IA (secret collé dans un prompt, commande dangereuse exécutée par un agent,
paquet suspect installé) se signalent **sans blâme** : l'objectif est d'ajouter le contrôle qui manquait.

## Si un secret a fuité : cinq gestes, dans l'ordre
1. **Révoquer** la clé chez le fournisseur, tout de suite.
2. **Remplacer** : nouvelle clé, placée dans le coffre ou la variable d'environnement.
3. **Chercher l'usage** : la clé a-t-elle servi depuis la fuite ?
4. **Nettoyer** : code, historique Git, image, conversation.
5. **Signaler et apprendre** : prévenir le référent, ajouter le contrôle manquant.

Supprimer la ligne et pousser un nouveau commit ne suffit jamais : le secret est à considérer comme public.
