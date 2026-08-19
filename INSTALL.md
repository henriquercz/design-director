# Installation Guide

Design Director has four installation paths. Pick the one that matches where you work.

## 1. Codex / Claude Code via `npx skills`

### Global

```bash
npx skills add henriquercz/design-director --skill design-director -g -a codex -a claude-code -y
```

### Project-scoped

Run from the project root:

```bash
npx skills add henriquercz/design-director --skill design-director -a codex -a claude-code -y
```

### One agent only

```bash
npx skills add henriquercz/design-director --skill design-director -g -a codex -y
npx skills add henriquercz/design-director --skill design-director -g -a claude-code -y
```

### Temporary / no persistent install

```bash
npx skills use henriquercz/design-director@design-director --agent codex
npx skills use henriquercz/design-director@design-director --agent claude-code
```

## 2. Full local skillset

Use this when you want the companion skills too.

```bash
git clone https://github.com/henriquercz/design-director.git
cd design-director
chmod +x scripts/*.sh
./scripts/install.sh --global --agents codex,claude-code --react
./scripts/doctor.sh
python scripts/validate.py
```

Useful flags:

```text
--global              user-wide install
--project             project-only install
--target PATH         target repo for project install
--agents LIST         codex,claude-code
--react               add react-best-practices
--revenue             add separately licensed revenue-centric-design
--with-claude-design  add optional Hermes claude-design
--no-extras           install Design Director core only
```

## 3. Claude web native Skill

Claude supports uploaded custom Skills. Build the upload ZIP:

```bash
python scripts/build-web-bundles.py --claude
```

Upload:

```text
dist/claude/design-director-claude-web.zip
```

In Claude:

1. Enable Code execution.
2. Customize → Skills.
3. + → Create skill → Upload a skill.
4. Upload the ZIP.
5. Enable Design Director.

The generated ZIP contains:

```text
design-director/
├── skill.md
├── references/
└── templates/
```

The build script derives it from the canonical Agent Skill and intentionally renames `SKILL.md` to lowercase `skill.md` for Claude web packaging.

Official docs:
- https://support.claude.com/en/articles/12512180-use-skills-in-claude
- https://support.claude.com/en/articles/12512198-how-to-create-custom-skills

## 4. ChatGPT web

ChatGPT uses persistent Project/GPT configuration rather than the Agent Skill ZIP package.

Build the bundle:

```bash
python scripts/build-web-bundles.py --chatgpt
```

### Custom GPT

Use:

```text
dist/chatgpt/INSTRUCTIONS.md
dist/chatgpt/design-director-knowledge.md
```

1. GPTs → Create.
2. Paste `INSTRUCTIONS.md` into Instructions.
3. Upload `design-director-knowledge.md` as Knowledge.
4. Enable the tools you want available.
5. Test in Preview and save.

### ChatGPT Project

1. Create a Project.
2. Paste `INSTRUCTIONS.md` into Project settings → Project instructions.
3. Upload `design-director-knowledge.md` to the Project.
4. Keep Design Director work inside that Project.

Projects are available broadly across ChatGPT plans; creating/editing custom GPTs requires an eligible paid plan.

Official docs:
- https://help.openai.com/en/articles/10169521-projects-in-chatgpt
- https://help.openai.com/en/articles/8554397-creating-and-editing-gpts

## 5. Prompt-only bootstrap

For any LLM or agent that can read web URLs, use [`PROMPT-INSTALL.md`](PROMPT-INSTALL.md). This is session-scoped; it does not install persistent files.
