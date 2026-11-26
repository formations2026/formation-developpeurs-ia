# Sécurité avec l'IA : les checklists

## Avant d'envoyer quelque chose à un outil d'IA
- [ ] L'outil est autorisé et utilisé avec le compte d'entreprise
- [ ] Aucun secret : clé, jeton, mot de passe, chaîne de connexion
- [ ] Aucune donnée personnelle réelle : schéma + données synthétiques (`scripts/fake_data.py`)
- [ ] Trace d'erreur nettoyée : e-mails, adresses IP, chemins internes, titres
- [ ] Je n'envoie que le nécessaire : type d'erreur, code minimal, comportement attendu

## Avant d'exécuter ce que l'IA propose
- [ ] J'ai lu le diff ou la commande en entier
- [ ] Les dépendances ajoutées existent, sont connues et maintenues
- [ ] Les tests passent, avant et après, sur une branche
- [ ] Exécution dans un bac à sable si le script est inconnu (`make sandbox`)
- [ ] Jamais sur la production ; droits minimaux ; mode simulation si possible

## Les garde-fous d'un agent, du plus faible au plus fort
| Couche | Fichier | Limite |
|---|---|---|
| Consigne | `AGENTS.md` | Le modèle peut l'oublier |
| Permissions | `.claude/settings.json` (`allow` / `ask` / `deny`) | Dépend de l'outil |
| Hook | `scripts/garde.sh` | Une liste de motifs se contourne |
| Bac à sable | conteneur sans réseau | Protège la machine, pas le dépôt |
| Revue humaine | protection de branche | Le dernier rempart, non délégable |

Aucune couche ne suffit seule. Les secrets ne sont dans aucune : ils sont **hors du poste**.

## Vérifier un paquet proposé par l'IA
1. Existe-t-il sur le registre officiel ? S'il n'existe pas : hallucination, ne pas le créer.
2. Depuis quand ? Créé il y a quelques jours : possible slopsquatting, ne pas installer.
3. Qui le maintient, où est le dépôt source, qui l'utilise ?
4. Quelle licence ?
5. Version et empreinte fixées, ajout relu en pull request.

## Simplification pédagogique : l'en-tête `X-User-Id`
MeetRoom identifie l'appelant par un en-tête que le client choisit. C'est une faille volontaire,
laissée pour garder le code court. Exercice : demandez à votre assistant de la trouver
(« relis `app/deps.py` comme un attaquant »), puis de proposer un plan de correction avec un jeton vérifié.
