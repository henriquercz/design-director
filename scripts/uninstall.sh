#!/usr/bin/env bash
set -euo pipefail
AGENTS="codex,claude-code"
SCOPE="global"
TARGET=""
WITH_EXTRAS=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --agents) AGENTS="${2:-}"; shift 2 ;;
    --project) SCOPE="project"; shift ;;
    --global) SCOPE="global"; shift ;;
    --target) TARGET="${2:-}"; shift 2 ;;
    --with-extras) WITH_EXTRAS=1; shift ;;
    -h|--help) echo "Usage: uninstall.sh [--agents codex,claude-code] [--global|--project] [--target PATH] [--with-extras]"; exit 0 ;;
    *) echo "Unknown option: $1" >&2; exit 2 ;;
  esac
done

BASE="${HOME:-}"
[[ "$SCOPE" == "project" ]] && BASE="${TARGET:-$PWD}"
IFS=',' read -r -a A <<< "$AGENTS"
selected(){ local n="$1"; for a in "${A[@]}"; do [[ "$a" == "$n" ]] && return 0; done; return 1; }

if selected codex; then
  p="$BASE/.agents/skills/design-director"; rm -rf "$p"; echo "removed $p"
fi
if selected claude-code; then
  p="$BASE/.claude/skills/design-director"; rm -rf "$p"; echo "removed $p"
fi

if [[ "$WITH_EXTRAS" -eq 1 ]] && command -v npx >/dev/null 2>&1; then
  FLAGS=(); for a in "${A[@]}"; do FLAGS+=( -a "$a" ); done
  SCOPE_FLAG=(); [[ "$SCOPE" == "global" ]] && SCOPE_FLAG+=( -g )
  npx -y skills remove frontend-design ui-ux-pro-max web-design-guidelines popular-web-designs react-best-practices claude-design "${FLAGS[@]}" "${SCOPE_FLAG[@]}" -y || true
fi
