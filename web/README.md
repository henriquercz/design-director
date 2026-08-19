# Design Director on web LLMs

The canonical source remains `skills/design-director/`. Web packages are generated from that source so the repository does not maintain divergent copies of the design knowledge.

## Generate packages

```bash
python scripts/build-web-bundles.py
```

Or one platform only:

```bash
python scripts/build-web-bundles.py --claude
python scripts/build-web-bundles.py --chatgpt
```

## Claude web

Claude supports native custom Skill ZIP upload.

Generated artifact:

```text
dist/claude/design-director-claude-web.zip
```

Install:

1. Enable Code execution.
2. Customize → Skills.
3. + → Create skill → Upload a skill.
4. Upload the generated ZIP.
5. Enable the skill.

The generated archive contains `design-director/skill.md` plus the canonical references/templates needed by the skill.

See [`claude/README.md`](claude/README.md).

## ChatGPT web

Generated artifacts:

```text
dist/chatgpt/INSTRUCTIONS.md
dist/chatgpt/design-director-knowledge.md
```

Use them in either:

- a Custom GPT: instructions + Knowledge;
- a Project: Project instructions + uploaded project source.

See [`chatgpt/README.md`](chatgpt/README.md).

## Prompt-only

If persistent configuration is unavailable, use the root [`PROMPT-INSTALL.md`](../PROMPT-INSTALL.md).
