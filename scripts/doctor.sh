#!/usr/bin/env bash
set -u
pass=0; warn=0; fail=0
ok(){ printf '✓ %s\n' "$1"; pass=$((pass+1)); }
warning(){ printf '! %s\n' "$1"; warn=$((warn+1)); }
bad(){ printf '✗ %s\n' "$1"; fail=$((fail+1)); }

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
[[ -f "$ROOT/skills/design-director/SKILL.md" ]] && ok "Bundled design-director present" || bad "Bundled design-director missing"
PYTHON_BIN="$(command -v python3 || command -v python || true)"
[[ -n "$PYTHON_BIN" ]] && "$PYTHON_BIN" "$SCRIPT_DIR/validate.py" >/dev/null 2>&1 && ok "Bundled package validates" || bad "Bundled package validation failed"
command -v node >/dev/null 2>&1 && ok "Node.js found: $(node --version)" || warning "Node.js not found (needed only for companion installer)"
command -v npx >/dev/null 2>&1 && ok "npx found" || warning "npx not found (needed only for companion installer)"

check_skill(){
  local label="$1"; shift; local found=0
  for p in "$@"; do
    if [[ -f "$p/SKILL.md" ]]; then ok "$label: $p"; found=1; break; fi
  done
  [[ $found -eq 1 ]] || warning "$label not installed in common paths"
}

HOME_DIR="${HOME:-}"; CWD="$(pwd)"
check_skill "Claude design-director" "$CWD/.claude/skills/design-director" "$HOME_DIR/.claude/skills/design-director"
check_skill "Codex design-director" "$CWD/.agents/skills/design-director" "$HOME_DIR/.agents/skills/design-director"
for s in frontend-design ui-ux-pro-max web-design-guidelines popular-web-designs revenue-centric-design; do
  check_skill "$s" "$CWD/.claude/skills/$s" "$CWD/.agents/skills/$s" "$HOME_DIR/.claude/skills/$s" "$HOME_DIR/.agents/skills/$s" "$HOME_DIR/.codex/skills/$s"
done

echo
echo "Doctor summary: $pass passed, $warn warnings, $fail failures"
[[ $fail -eq 0 ]]
