#!/usr/bin/env bash
set -euo pipefail

SCOPE="global"
AGENTS="codex,claude-code"
TARGET=""
WITH_REACT=0
WITH_CLAUDE_DESIGN=0
WITH_REVENUE=0
NO_EXTRAS=0

usage() {
  cat <<'USAGE'
Usage: install.sh [options]

Options:
  --global                 Install globally (default)
  --project                Install into a project
  --target PATH            Project directory when using --project
  --agents LIST            Comma-separated: codex,claude-code (default both)
  --react                  Also install Vercel react-best-practices
  --with-claude-design     Also install Hermes claude-design (optional)
  --revenue                Also install heliocosta-dev/revenue-centric-design (separate source-available license)
  --no-extras              Install only design-director; Node/npx not required
  -h, --help               Show help
USAGE
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --global) SCOPE="global"; shift ;;
    --project) SCOPE="project"; shift ;;
    --target) TARGET="${2:-}"; shift 2 ;;
    --agents) AGENTS="${2:-}"; shift 2 ;;
    --react) WITH_REACT=1; shift ;;
    --with-claude-design) WITH_CLAUDE_DESIGN=1; shift ;;
    --revenue) WITH_REVENUE=1; shift ;;
    --no-extras) NO_EXTRAS=1; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown option: $1" >&2; usage; exit 2 ;;
  esac
done

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SOURCE_SKILL="$ROOT/skills/design-director"
[[ -f "$SOURCE_SKILL/SKILL.md" ]] || { echo "Missing bundled design-director skill." >&2; exit 1; }

if [[ "$SCOPE" == "project" ]]; then
  BASE="${TARGET:-$PWD}"
  mkdir -p "$BASE"
else
  BASE="${HOME:?HOME is required for global installation}"
fi

IFS=',' read -r -a AGENT_ARRAY <<< "$AGENTS"
selected() {
  local needle="$1"
  for a in "${AGENT_ARRAY[@]}"; do [[ "$a" == "$needle" ]] && return 0; done
  return 1
}

copy_core() {
  local dst="$1"
  mkdir -p "$(dirname "$dst")"
  rm -rf "$dst"
  cp -a "$SOURCE_SKILL" "$dst"
  echo "✓ design-director -> $dst"
}

# Install the bundled core directly. This avoids making local skill installation
# depend on a third-party CLI and follows the hosts' normal skill directories.
if selected "codex"; then
  if [[ "$SCOPE" == "global" ]]; then
    copy_core "$HOME/.agents/skills/design-director"
  else
    copy_core "$BASE/.agents/skills/design-director"
  fi
fi

if selected "claude-code"; then
  if [[ "$SCOPE" == "global" ]]; then
    copy_core "$HOME/.claude/skills/design-director"
  else
    copy_core "$BASE/.claude/skills/design-director"
  fi
fi

if [[ "$NO_EXTRAS" -eq 1 ]]; then
  echo
  echo "Core installed without companion skills."
  exit 0
fi

command -v node >/dev/null 2>&1 || { echo "Node.js is required only for companion skill installation. Core is already installed." >&2; exit 1; }
command -v npx >/dev/null 2>&1 || { echo "npx is required only for companion skill installation. Core is already installed." >&2; exit 1; }

AGENT_FLAGS=()
for a in "${AGENT_ARRAY[@]}"; do [[ -n "$a" ]] && AGENT_FLAGS+=( -a "$a" ); done
SCOPE_FLAGS=()
[[ "$SCOPE" == "global" ]] && SCOPE_FLAGS+=( -g )
[[ "$SCOPE" == "project" ]] && cd "$BASE"

install_companion() {
  local source="$1" skill="$2"
  echo "==> Installing companion $skill from $source"
  npx -y skills add "$source" --skill "$skill" "${AGENT_FLAGS[@]}" "${SCOPE_FLAGS[@]}" --copy -y
}

install_companion "anthropics/skills" "frontend-design"
install_companion "nextlevelbuilder/ui-ux-pro-max-skill" "ui-ux-pro-max"
install_companion "vercel-labs/agent-skills" "web-design-guidelines"
install_companion "NousResearch/hermes-agent" "popular-web-designs"

if [[ "$WITH_REACT" -eq 1 ]]; then
  install_companion "vercel-labs/agent-skills" "react-best-practices"
fi

if [[ "$WITH_REVENUE" -eq 1 ]]; then
  echo "==> Installing separately licensed revenue-centric-design companion"
  echo "    Note: attribution required; not for gambling/betting/casino use; see upstream LICENSE."
  install_companion "heliocosta-dev/revenue-centric-design" "revenue-centric-design"
fi

if [[ "$WITH_CLAUDE_DESIGN" -eq 1 ]]; then
  if ! install_companion "NousResearch/hermes-agent" "claude-design"; then
    echo "WARNING: optional claude-design failed; Design Director remains usable." >&2
  fi
fi

echo
echo "Installed. Run: $SCRIPT_DIR/doctor.sh"
echo "Codex:  \$design-director ..."
echo "Claude: /design-director ..."
