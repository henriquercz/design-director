#!/usr/bin/env bash
set -euo pipefail
AGENTS="codex,claude-code"
SCOPE="global"
TARGET=""
NO_EXTRAS=0
while [[ $# -gt 0 ]]; do
  case "$1" in
    --agents) AGENTS="${2:-}"; shift 2 ;;
    --project) SCOPE="project"; shift ;;
    --global) SCOPE="global"; shift ;;
    --target) TARGET="${2:-}"; shift 2 ;;
    --no-extras) NO_EXTRAS=1; shift ;;
    -h|--help) echo "Usage: update.sh [--agents codex,claude-code] [--global|--project] [--target PATH] [--no-extras]"; exit 0 ;;
    *) echo "Unknown option: $1" >&2; exit 2 ;;
  esac
done

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ARGS=(--agents "$AGENTS" --no-extras)
if [[ "$SCOPE" == "global" ]]; then ARGS+=(--global); else ARGS+=(--project); [[ -n "$TARGET" ]] && ARGS+=(--target "$TARGET"); fi
"$SCRIPT_DIR/install.sh" "${ARGS[@]}"

if [[ "$NO_EXTRAS" -eq 0 ]] && command -v npx >/dev/null 2>&1; then
  [[ "$SCOPE" == "project" ]] && cd "${TARGET:-$PWD}"
  IFS=',' read -r -a A <<< "$AGENTS"; FLAGS=(); for a in "${A[@]}"; do FLAGS+=( -a "$a" ); done
  SCOPE_FLAG=(); [[ "$SCOPE" == "global" ]] && SCOPE_FLAG+=( -g )
  npx -y skills update frontend-design ui-ux-pro-max web-design-guidelines popular-web-designs react-best-practices claude-design "${SCOPE_FLAG[@]}" -y "${FLAGS[@]}" || true
fi

echo "Design Director core refreshed from this package."
