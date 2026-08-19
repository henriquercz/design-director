# ChatGPT web setup

ChatGPT does not use the same Agent Skill ZIP packaging as Codex/Claude Code. This directory provides the persistent web equivalent.

## Build

From the repository root:

```bash
python scripts/build-web-bundles.py --chatgpt
```

Outputs:

```text
dist/chatgpt/INSTRUCTIONS.md
dist/chatgpt/design-director-knowledge.md
```

## Option A — Custom GPT

1. Open ChatGPT on the web → GPTs → Create.
2. Paste `INSTRUCTIONS.md` into the GPT Instructions field.
3. Upload `design-director-knowledge.md` as Knowledge.
4. Enable desired capabilities/tools.
5. Test in Preview.
6. Save the GPT.

Custom GPT creation/editing requires an eligible paid ChatGPT plan.

## Option B — ChatGPT Project

1. Create a Project.
2. Project settings → Project instructions → paste `INSTRUCTIONS.md`.
3. Add `design-director-knowledge.md` as a project file/source.
4. Start all Design Director chats inside that Project.

Projects provide project-scoped instructions and reference files.

Official docs:
- https://help.openai.com/en/articles/10169521-projects-in-chatgpt
- https://help.openai.com/en/articles/8554397-creating-and-editing-gpts
