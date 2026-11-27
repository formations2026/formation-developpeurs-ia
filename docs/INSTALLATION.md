# Installation pas à pas

À faire **avant** la formation. Comptez vingt à trente minutes. Si votre poste ne vous permet pas d'installer
un outil, ce n'est pas bloquant : vous travaillerez en binôme.

## 1. Les prérequis
| Outil | Vérification | Attendu |
|---|---|---|
| Git | `git --version` | une version s'affiche |
| Python | `python --version` (ou `python3`) | 3.11 ou plus |
| Un IDE | VS Code, ou un IDE JetBrains | il s'ouvre |
| Docker (optionnel) | `docker --version` | pour le bac à sable de la partie 4 |

## 2. Le dépôt
```bash
git clone https://github.com/formations2026/formation-developpeurs-ia.git meetroom
cd meetroom
python -m venv .venv
source .venv/bin/activate          # Windows PowerShell : .venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt
pytest                             # attendu : 27 passed
```

## 3. Les assistants
Utilisez **uniquement** les outils et comptes autorisés par votre entreprise. Les procédures d'installation
changent : suivez la documentation officielle.

| Assistant | Où | Vérification |
|---|---|---|
| GitHub Copilot | Extension « GitHub Copilot » de votre IDE — https://docs.github.com/copilot | le chat répond à « bonjour » |
| Claude Code | https://docs.claude.com/en/docs/claude-code/overview | `claude --version`, puis `claude` dans le dossier du projet |
| JetBrains AI Assistant, Junie | Extensions de l'IDE JetBrains — https://www.jetbrains.com/help/junie/ | le panneau s'ouvre |
| Ollama (optionnel, LLM local) | https://ollama.com | `ollama run <un modèle de code>` répond |

Deux assistants suffisent : un dans l'IDE, un agent en ligne de commande (ou un modèle local).

## 4. Le scan de secrets
```bash
pre-commit install
pre-commit run --all-files         # attendu : tout passe
```

## 5. La vérification finale
```bash
make check        # sans make : ruff check . && bandit -q -r app -ll && pytest
make seed         # sans make : python -m scripts.fake_data
make run          # sans make : uvicorn app.main:app --reload
```
Ouvrez http://127.0.0.1:8000/docs : vous devez voir les routes et pouvoir appeler `GET /rooms`.

## Pannes fréquentes
| Symptôme | Cause probable | Solution |
|---|---|---|
| `python` introuvable | Python installé sous le nom `python3` | utilisez `python3`, ou cochez « Add to PATH » à l'installation (Windows) |
| `Activate.ps1 cannot be loaded` | Politique d'exécution PowerShell | `Set-ExecutionPolicy -Scope Process RemoteSigned`, puis réessayez |
| `make` introuvable | Windows sans make | utilisez les commandes directes ci-dessus |
| `pip install` échoue derrière un proxy | Proxy d'entreprise | demandez la configuration du proxy ou du registre interne à votre équipe |
| `ModuleNotFoundError: app` | Commande lancée hors du dossier du projet | `cd meetroom`, environnement virtuel activé |
| L'assistant ne voit pas le projet | IDE ouvert sur un fichier, pas sur le dossier | ouvrez le **dossier** `meetroom` |
| L'assistant ne suit pas `AGENTS.md` | Fichier non pris en charge par cette version | voir `.github/copilot-instructions.md` ou `CLAUDE.md`, propres à l'outil |
| `scripts/garde.sh` : permission refusée | Bit d'exécution perdu (Windows, zip) | `chmod +x scripts/garde.sh` ; sous Windows, le hook demande Git Bash ou WSL |
