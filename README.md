# Design Director

> A portable design director for AI coding agents and web LLMs: diagnose first, route automatically, design from the user's real job, implement real states, and verify the rendered result.

**Design Director v3** combines frontend/UI craft, product design, anti-AI-slop judgment, accessibility, responsive behavior, brand/product registers, and an outcome-aware layer for conversion, activation, retention, monetization, experimentation, and ethical persuasion.

It is designed around one idea: **you describe the goal; the skill decides the smallest effective design workflow.** You do not need to memorize mode names.

## Install in 30 seconds

### Codex + Claude Code with `npx skills`

Global installation:

```bash
npx skills add henriquercz/design-director \
  --skill design-director \
  -g \
  -a codex \
  -a claude-code \
  -y
```

Project-only installation:

```bash
npx skills add henriquercz/design-director \
  --skill design-director \
  -a codex \
  -a claude-code \
  -y
```

Install for only one agent:

```bash
# Codex
npx skills add henriquercz/design-director --skill design-director -g -a codex -y

# Claude Code
npx skills add henriquercz/design-director --skill design-director -g -a claude-code -y
```

The repository follows the open Agent Skills layout (`skills/design-director/SKILL.md`), so the same source can be installed by compatible hosts.

## Use without memorizing modes

Codex:

```text
$design-director
This landing page feels generic and weak. Diagnose the real problems, preserve the working product behavior, choose the right treatments yourself, implement them, and verify desktop and mobile.
```

Claude Code:

```text
/design-director
Improve this SaaS onboarding. Find the real activation friction, fix the highest-impact design problems, preserve functionality, and verify the result.
```

Freeform requests are routed automatically. Explicit modes are optional and useful only when you want to constrain scope:

```text
$design-director review this dashboard. Do not edit files.
$design-director relayout this hero. Preserve color and typography.
$design-director responsive fix tablet and mobile only.
$design-director surface harden this production dashboard with real states and edge data.
```

## Full skillset installer

`npx skills` installs the **Design Director core**. If you also want the recommended companion skills, clone/download the repository and run the bundled installer:

```bash
git clone https://github.com/henriquercz/design-director.git
cd design-director
chmod +x scripts/*.sh

./scripts/install.sh --global --agents codex,claude-code --react
./scripts/doctor.sh
python scripts/validate.py
```

Optional Revenue-Centric Design specialist (separately licensed upstream):

```bash
./scripts/install.sh --global --agents codex,claude-code --react --revenue
```

See [`THIRD_PARTY.md`](THIRD_PARTY.md) before enabling separately licensed companions.

## No install: run it from a prompt

For a one-off session, open [`PROMPT-INSTALL.md`](PROMPT-INSTALL.md), copy the bootstrap prompt, paste it into your agent/LLM, then send your design task.

If you use the Skills CLI, you can also start a supported coding agent with the skill resolved temporarily:

```bash
npx skills use henriquercz/design-director@design-director --agent codex
npx skills use henriquercz/design-director@design-director --agent claude-code
```

## Web LLM installation

Design Director also ships a web-friendly packaging workflow.

### Claude on the web — native Skill

Claude supports custom Skills uploaded as ZIP files. Build the upload package:

```bash
python scripts/build-web-bundles.py --claude
```

This creates:

```text
dist/claude/design-director-claude-web.zip
```

Then in Claude:

1. Enable **Code execution** if it is disabled.
2. Open **Customize → Skills**.
3. Click **+ → Create skill → Upload a skill**.
4. Upload `dist/claude/design-director-claude-web.zip`.
5. Enable **Design Director**.
6. Describe your design task normally; Claude can invoke the skill automatically when relevant.

The builder converts the canonical `SKILL.md` into the `skill.md` package shape expected by Claude without maintaining a second source of truth.

Official Claude documentation: [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude) and [Create custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills).

### ChatGPT on the web — Custom GPT or Project

ChatGPT's persistent configuration model is different from Agent Skills. This repo provides a web bundle for the two supported persistent patterns: **Custom GPT** and **Project**.

Build the ChatGPT bundle:

```bash
python scripts/build-web-bundles.py --chatgpt
```

This creates:

```text
dist/chatgpt/INSTRUCTIONS.md
dist/chatgpt/design-director-knowledge.md
```

**Custom GPT (recommended if you can create GPTs):**

1. Open **GPTs → Create** in ChatGPT on the web.
2. Paste `dist/chatgpt/INSTRUCTIONS.md` into the GPT **Instructions** field.
3. Upload `dist/chatgpt/design-director-knowledge.md` as **Knowledge**.
4. Enable the tools you want it to use (for example web search or data/code tools where available).
5. Test in Preview, then save the GPT.

**Project (works as a project-scoped Design Director):**

1. Create a new ChatGPT **Project**.
2. Open **Project settings** and paste `dist/chatgpt/INSTRUCTIONS.md` into **Project instructions**.
3. Add `dist/chatgpt/design-director-knowledge.md` to the project files/sources.
4. Start design chats inside that Project.

OpenAI's documentation describes Projects as persistent workspaces with uploaded reference files and project instructions, and Custom GPTs as configurations with Instructions + Knowledge. See [Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt) and [Creating and editing GPTs](https://help.openai.com/en/articles/8554397-creating-and-editing-gpts).

More detail: [`web/README.md`](web/README.md).

## Build all web bundles

```bash
python scripts/build-web-bundles.py
```

The generated `dist/` directory is intentionally derived from the canonical skill. Do not hand-maintain generated copies.

## How Design Director thinks

```text
user goal
   ↓
prompt invariants + existing product truth
   ↓
work surface: Monitor / Operate / Compare / Configure / Learn / Decide / Explore
   ↓
register: Brand / Product
   ↓
optional outcome: Acquire / Activate / Retain / Expand / Monetize / Differentiate
   ↓
diagnosis
   ↓
smallest effective treatment chain
   ↓
implementation with real states
   ↓
rendered verification
   ↓
review /100 → bounded repair → finish
```

The core deliberately separates **design quality** from **product outcome** while allowing both to inform the final decision when business performance is relevant.

## Core modes

You normally do not need to name these. They exist for scope control and internal routing.

| Group | Modes |
|---|---|
| Diagnose | `checkup`, `smell`, `review` |
| Create / transform | `create`, `build`, `redesign`, `deslop`, `relayout` |
| Systems | `typeset`, `recolor`, `interaction`, `motion`, `responsive`, `a11y`, `tokenize` |
| Character / production | `refine`, `voice`, `surface`, `writing`, `finish` |
| Product outcome | `outcome` plus conversion, activation, retention, monetization, experimentation, and feature-discipline references |

Explicit `checkup`, `smell`, and `review` are report-only unless you separately request treatment. Freeform improvement requests may diagnose and fix in the same pass.

## What makes it different

- **Surface-first composition** instead of defaulting to centered heroes, cards, pills, and generic SaaS patterns.
- **Prompt invariants** preserve the real name, category, user pressure, domain artifact, evidence, constraints, and forbidden drift.
- **Brand vs Product registers** prevent marketing-page spectacle from leaking into operational product UI.
- **Anti-slop diagnosis** detects predictable AI-generated design reflexes without banning legitimate patterns.
- **Real-state coverage** includes loading, empty, error, success, disabled, selected, focus, overflow, and edge data where applicable.
- **Calibration** distinguishes standards, ergonomic targets, heuristics, project tokens, and subjective rules of thumb.
- **Outcome-aware design** can reason about qualified conversion, activation/TTV, retention, pricing, experimentation, and feature adoption.
- **Ethical persuasion** rejects fake scarcity, hidden costs, cancellation obstruction, fabricated proof, and artificial lock-in.
- **Truthful completion** forbids claiming a visual improvement that was not implemented and, when possible, actually observed.
- **Bounded iteration** avoids endless redesign loops: one broad repair pass, one targeted repair pass, then stop and expose tradeoffs.

## Companion skills

The bundled installer can add specialists while keeping Design Director as the orchestrator:

- `frontend-design` — Anthropic art direction/frontend implementation
- `ui-ux-pro-max` — large UI/UX reference library
- `web-design-guidelines` — final interface/a11y review
- `popular-web-designs` — real product visual references
- `react-best-practices` — optional React/Next.js performance guidance
- `revenue-centric-design` — optional, separately licensed outcome/CRO specialist
- `claude-design` — optional experimental second opinion

Companions advise; **Design Director remains responsible for the final direction, routing, implementation scope, and verification**.

## Repository map

```text
skills/design-director/
├── SKILL.md                 # portable Agent Skill entrypoint
├── references/              # progressively disclosed design knowledge
├── templates/               # brief/report/decision templates
├── evals/                   # behavioral evaluation cases
└── agents/                  # host-specific optional metadata

scripts/
├── install.sh
├── update.sh
├── uninstall.sh
├── doctor.sh
├── validate.py
├── catalog.py
└── build-web-bundles.py     # Claude Web + ChatGPT packaging

web/
├── README.md
├── chatgpt/
│   └── INSTRUCTIONS.md
└── claude/
    └── README.md
```

## Validation and maintenance

```bash
python scripts/validate.py
python scripts/catalog.py
python scripts/build-web-bundles.py
```

Knowledge additions follow a source → distill → review → merge/supersede process rather than simply accumulating more rules. See [`MAINTAINING.md`](MAINTAINING.md).

## Research / merge notes

- [`MERGE-ANALYSIS.md`](MERGE-ANALYSIS.md) — Command Code design-skill analysis and v2 merge rationale.
- [`RCD-REPOSITORY-AUDIT.md`](RCD-REPOSITORY-AUDIT.md) — Revenue-Centric Design repository audit and v3 merge rationale.
- [`SOURCE-STRUCTURE-INDEX.md`](SOURCE-STRUCTURE-INDEX.md) — source structure/index used during the Command Code analysis.
- [`THIRD_PARTY.md`](THIRD_PARTY.md) — companion licenses and boundaries.

## License

The Design Director core is released under the [`MIT License`](LICENSE).

Third-party companion skills are **not bundled into the MIT core** unless their licenses allow it. Their upstream terms continue to apply when installed separately.
