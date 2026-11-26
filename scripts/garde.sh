#!/usr/bin/env bash
# Garde-fou : bloque les commandes shell dangereuses avant leur exécution par l'agent.
# Branché comme hook PreToolUse dans .claude/settings.json.
# Entrée : la description de l'appel d'outil en JSON sur l'entrée standard.
# Sortie : code 0 = autorisé ; code 2 = bloqué (le message d'erreur est renvoyé à l'agent).
#
# Une liste de motifs ne remplace ni les permissions, ni le bac à sable : c'est une couche de plus.
set -euo pipefail

cmd=$(python3 -c 'import json,sys; print(json.load(sys.stdin).get("tool_input", {}).get("command", ""))')

interdits='rm -rf|git push .*--force|git push .*-f( |$)|git reset --hard|DROP TABLE|DROP DATABASE|chmod -R 777|\.env'

if printf '%s' "$cmd" | grep -Eiq "$interdits"; then
  echo "Commande bloquée par scripts/garde.sh : motif interdit. Demander à un humain." >&2
  exit 2
fi
exit 0
