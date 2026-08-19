# Claude web native Skill setup

Claude supports uploaded custom Skills.

## Build the ZIP

From the repository root:

```bash
python scripts/build-web-bundles.py --claude
```

Output:

```text
dist/claude/design-director-claude-web.zip
```

The builder creates the package shape expected by Claude:

```text
design-director/
├── skill.md
├── references/
└── templates/
```

It derives the package from `skills/design-director/`, renaming the canonical `SKILL.md` to `skill.md` inside the generated ZIP.

## Upload

1. Ensure Code execution is enabled.
2. Open Claude → Customize → Skills.
3. Click + → Create skill → Upload a skill.
4. Upload `design-director-claude-web.zip`.
5. Enable Design Director.
6. Describe your design task naturally; Claude can choose the skill automatically based on its description.

Official docs:
- https://support.claude.com/en/articles/12512180-use-skills-in-claude
- https://support.claude.com/en/articles/12512198-how-to-create-custom-skills
