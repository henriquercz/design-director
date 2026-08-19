#!/usr/bin/env python3
"""Build derived Design Director packages for Claude web and ChatGPT web.

Canonical source: skills/design-director/
Generated output: dist/ (ignored/replaceable build artifact)
"""

from __future__ import annotations

import argparse
import shutil
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "design-director"
DIST = ROOT / "dist"
WEB = ROOT / "web"


def reset_dir(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def build_claude() -> Path:
    source = SKILL
    skill_file = source / "SKILL.md"
    if not skill_file.exists():
        raise SystemExit(f"Missing canonical skill: {skill_file}")

    out_dir = DIST / "claude"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_zip = out_dir / "design-director-claude-web.zip"

    with tempfile.TemporaryDirectory() as tmp:
        pkg = Path(tmp) / "design-director"
        pkg.mkdir(parents=True)

        # Claude web's custom Skill docs use lowercase skill.md.
        shutil.copy2(skill_file, pkg / "skill.md")

        for dirname in ("references", "templates"):
            src = source / dirname
            if src.exists():
                shutil.copytree(src, pkg / dirname)

        license_file = ROOT / "LICENSE"
        if license_file.exists():
            shutil.copy2(license_file, pkg / "LICENSE")

        with zipfile.ZipFile(out_zip, "w", compression=zipfile.ZIP_DEFLATED) as zf:
            for path in sorted(pkg.rglob("*")):
                if path.is_file():
                    zf.write(path, path.relative_to(pkg.parent))

    print(f"Claude web bundle: {out_zip}")
    return out_zip


def append_markdown(out, path: Path, title: str) -> None:
    text = path.read_text(encoding="utf-8")
    out.write(f"\n\n---\n\n# SOURCE: {title}\n\n")
    out.write(text.rstrip())
    out.write("\n")


def build_chatgpt() -> tuple[Path, Path]:
    skill_file = SKILL / "SKILL.md"
    instructions = WEB / "chatgpt" / "INSTRUCTIONS.md"
    if not skill_file.exists() or not instructions.exists():
        raise SystemExit("Missing canonical skill or ChatGPT instructions")

    out_dir = DIST / "chatgpt"
    reset_dir(out_dir)

    instructions_out = out_dir / "INSTRUCTIONS.md"
    shutil.copy2(instructions, instructions_out)

    knowledge = out_dir / "design-director-knowledge.md"
    with knowledge.open("w", encoding="utf-8") as out:
        out.write(
            "# Design Director knowledge pack\n\n"
            "Generated from the canonical repository skill. Use the source sections "
            "progressively: load/apply only what the current task needs.\n"
        )
        append_markdown(out, skill_file, "skills/design-director/SKILL.md")

        refs = SKILL / "references"
        for path in sorted(refs.glob("*.md")):
            append_markdown(out, path, f"references/{path.name}")

        templates = SKILL / "templates"
        if templates.exists():
            for path in sorted(templates.glob("*.md")):
                append_markdown(out, path, f"templates/{path.name}")

    print(f"ChatGPT instructions: {instructions_out}")
    print(f"ChatGPT knowledge:    {knowledge}")
    return instructions_out, knowledge


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--claude", action="store_true", help="Build Claude web Skill ZIP only")
    parser.add_argument("--chatgpt", action="store_true", help="Build ChatGPT web bundle only")
    args = parser.parse_args()

    if not args.claude and not args.chatgpt:
        args.claude = args.chatgpt = True

    DIST.mkdir(parents=True, exist_ok=True)
    if args.claude:
        build_claude()
    if args.chatgpt:
        build_chatgpt()


if __name__ == "__main__":
    main()
