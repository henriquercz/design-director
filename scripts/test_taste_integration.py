#!/usr/bin/env python3
from pathlib import Path
import re
import sys

root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]

def read(rel):
    return (root / rel).read_text(encoding="utf-8")

skill_md = read("skills/design-director/SKILL.md")
registers = read("skills/design-director/references/registers.md")
evidence = read("skills/design-director/references/design-evidence.md")
redesign = read("skills/design-director/references/creation-redesign.md")
slop = read("skills/design-director/references/anti-slop.md")
writing = read("skills/design-director/references/writing.md")
implementation = read("skills/design-director/references/implementation.md")
responsive = read("skills/design-director/references/responsive.md")
calibration = read("skills/design-director/references/calibration.md")
verification = read("skills/design-director/references/verification.md")
evals = read("skills/design-director/evals/EVALS.md")

checks = {
    "version 4.1.0": 'version: "4.1.0"' in skill_md,
    "posture axes": all(x in registers.lower() for x in ("visual variance", "motion intensity", "information density")),
    "system-vs-aesthetic honesty": "aesthetic" in evidence.lower() and "official" in evidence.lower() and "system" in evidence.lower(),
    "redesign preservation envelope": all(x in redesign.lower() for x in ("seo", "structured data", "analytics", "legal", "route")),
    "marketing anti-slop additions": all(x in slop.lower() for x in ("eyebrow", "section numbering", "fake product", "status dot")),
    "copy self-audit": all(x in writing.lower() for x in ("self-audit", "cta intent", "precision")),
    "dependency + high-frequency implementation safety": all(x in implementation.lower() for x in ("dependency", "high-frequency", "re-render")),
    "dynamic viewport guidance": "dvh" in responsive.lower(),
    "calibration rejects taste dogma": all(x in calibration.lower() for x in ("inter", "em dash", "dark mode", "one accent")),
    "redesign preservation verified": "seo" in verification.lower() and "analytics" in verification.lower(),
    "56 evals": len(re.findall(r"^##\s+\d+\.", evals, flags=re.M)) >= 56,
}

failed = [name for name, ok in checks.items() if not ok]
if failed:
    print("Taste integration regression FAILED")
    for name in failed:
        print(" -", name)
    raise SystemExit(1)

print("Taste integration regression OK")
for name in checks:
    print(" -", name)
