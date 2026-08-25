# Design Director

> A portable design director for AI coding agents and web LLMs: diagnose first, route automatically, learn the real design system from evidence, reuse real component APIs, implement complete interaction contracts, and verify the rendered result.

**Design Director v4** combines frontend/UI craft, product design, anti-AI-slop judgment, accessibility, responsive behavior, brand/product registers, outcome-aware product design, evidence-aware design-system inference, component contracts, micro-craft, and purpose/frequency-aware motion.

The user experience stays intentionally simple: **describe what you want changed; Design Director decides how to get there.** You do not need to memorize modes, component rules, or specialist names.

```text
$design-director
I don't like this section. Redesign it so it feels more professional, intentional and specific to our product. Preserve the working behavior.
```

That is enough. Internally, v4 can inspect evidence, classify the surface/register, diagnose root causes, route to relayout/redesign/deslop/voice/etc., validate real component APIs, apply the relevant component contracts and craft, then verify the result.

## What's new in v4

- **Design evidence:** distinguishes Normative / Observed / Inferred / Unknown instead of inventing design-system truth from screenshots.
- **Component contracts:** dialogs, tooltips, tabs, toasts, forms, loading states, tables/collections, drag interactions, and media are evaluated beyond their resting appearance.
- **Micro-craft:** optical alignment, nested radii, relationship spacing, media geometry/crops, stacking/clipping, explicit transitions, and state geometry.
- **Better motion judgment:** purpose × frequency × input × spatial change × cost; high-frequency actions stay fast, overlays preserve origin/causality, reversible motion is interruptible.
- **Reuse/API-first implementation:** current project primitives, types, registries, MCPs, and examples beat model memory. Do not invent props or hand-roll complex behavior without checking what already exists.
- **Responsive interaction adaptation:** the same task can legitimately use a different primitive on another constraint (for example Dialog → Drawer) while preserving data/state/semantics.
- **Stronger verification:** keyboard-only walk, semantic/accessibility pass, component-contract pass, real API checks, craft checks, and slow-motion inspection when useful.
- **Bounded specialist routing:** 0–1 companion is normal, 2 only for independent gaps, 3 only for broad work, never more than 3.
- **46 behavioral eval cases** covering v1–v4 routing and regression expectations.

See [`V4-RESEARCH-AUDIT.md`](V4-RESEARCH-AUDIT.md) for the source-by-source merge rationale.

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
I don't like this dashboard section. Redesign it to feel more professional and easier to operate. Keep the current flows working and choose the right design treatments yourself.
```

Freeform requests are routed automatically. Explicit modes are optional and useful only when you want to constrain scope:

```text
$design-director review this dashboard. Do not edit files.
$design-director relayout this hero. Preserve color and typography.
$design-director responsive fix tablet and mobile only.
$design-director surface harden this production dashboard with real states and edge data.
```

## How v4 thinks

```text
abstract user goal
   ↓
prompt invariants + product truth
   ↓
existing design evidence
Normative / Observed / Inferred / Unknown
   ↓
work surface
Monitor / Operate / Compare / Configure / Learn / Decide / Explore
   ↓
register
Brand / Product
   ↓
optional outcome
Acquire / Activate / Retain / Expand / Monetize / Differentiate
   ↓
root-cause diagnosis
   ↓
smallest treatment chain
   ↓
real project primitive/API lookup
   ↓
component contracts + implementation
   ↓
micro-craft + purposeful motion
   ↓
rendered behavior verification
   ↓
review /100 → bounded repair → finish
```

The internal sophistication is deliberately hidden from the user. **v4 does not require more commands than v3.**

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

Design Director ships a web-friendly packaging workflow.

### Claude on the web — native Skill

```bash
python scripts/build-web-bundles.py --claude
```

Creates:

```text
dist/claude/design-director-claude-web.zip
```

Then in Claude:

1. Enable **Code execution** if disabled.
2. Open **Customize → Skills**.
3. Click **+ → Create skill → Upload a skill**.
4. Upload the ZIP.
5. Enable **Design Director**.
6. Describe your design task normally.

The builder derives the web package from the canonical `SKILL.md` + all current references, so v4's new evidence/contracts/craft knowledge is included automatically.

Official Claude documentation: [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude) and [Create custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills).

### ChatGPT on the web — Custom GPT or Project

```bash
python scripts/build-web-bundles.py --chatgpt
```

Creates:

```text
dist/chatgpt/INSTRUCTIONS.md
dist/chatgpt/design-director-knowledge.md
```

**Custom GPT:**
1. Open **GPTs → Create**.
2. Paste `INSTRUCTIONS.md` into **Instructions**.
3. Upload `design-director-knowledge.md` as **Knowledge**.
4. Enable the tools you want it to use.
5. Test in Preview and save.

**Project:**
1. Create a ChatGPT **Project**.
2. Paste `INSTRUCTIONS.md` into **Project instructions**.
3. Add `design-director-knowledge.md` to project files/sources.
4. Start design chats inside that Project.

OpenAI docs: [Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt) and [Creating and editing GPTs](https://help.openai.com/en/articles/8554397-creating-and-editing-gpts).

More detail: [`web/README.md`](web/README.md).

## Core modes

You normally do not need to name these. They exist for scope control and internal routing.

| Group | Modes |
|---|---|
| Diagnose | `checkup`, `smell`, `review`, `audit` |
| Create / transform | `direction`, `create`, `build`, `redesign`, `deslop`, `relayout` |
| Systems | `typeset`, `recolor`, `interaction`, `motion`, `responsive`, `a11y`, `tokenize` |
| Character / production | `refine`, `voice`, `surface`, `writing`, `finish` |
| Product outcome | `outcome` plus conversion, activation, retention, monetization, experimentation, and feature-discipline references |

Explicit `checkup`, `smell`, and `review` are report-only unless you separately request treatment. Freeform improvement requests may diagnose and fix in the same pass.

## What makes it different

- **Abstract-input friendly:** "I don't like this section; make it professional" is a valid request.
- **Surface-first composition:** no default centered hero/card-grid/pill reflex.
- **Prompt invariants:** preserve the real name, category, user pressure, domain artifact, evidence, constraints, and forbidden drift.
- **Evidence-aware design-system learning:** screenshots are not treated as hidden token/API truth.
- **Brand vs Product registers:** marketing spectacle does not leak into operational UI by accident.
- **Anti-slop diagnosis:** detects predictable AI-generated reflexes without banning legitimate patterns.
- **Real component contracts:** states, focus, keyboard, geometry, collision, loading, recovery, responsive adaptation.
- **Real API reuse:** current component source/types/registry outrank model memory.
- **Motion restraint:** frequency-sensitive, origin-aware, interruptible, reduced-motion safe.
- **Responsive recomposition:** the interaction primitive itself may adapt when constraints demand it.
- **Micro-craft:** optical polish is explicit without turning craft into numeric dogma.
- **Outcome-aware design:** qualified conversion, activation/TTV, retention, pricing, experimentation, feature adoption.
- **Ethical persuasion:** rejects fake scarcity, hidden costs, cancellation obstruction, fabricated proof, artificial lock-in.
- **Truthful completion:** no visual claims without real implementation/verification evidence.
- **Bounded iteration:** one broad repair, one targeted repair, then stop/expose tradeoffs.

## Companion skills

The bundled installer can add specialists while keeping Design Director as the orchestrator:

- `frontend-design` — Anthropic art direction/frontend implementation
- `ui-ux-pro-max` — large UI/UX reference library
- `web-design-guidelines` — final interface/a11y review
- `popular-web-designs` — real product visual references
- `react-best-practices` — optional React/Next.js performance guidance
- `revenue-centric-design` — optional, separately licensed outcome/CRO specialist
- `claude-design` — optional experimental second opinion

v4 adds a context budget: **0–1 companion normally, 2 for independent gaps, 3 only for broad work, never more than 3.** Companions advise; Design Director remains responsible for final direction, scope, implementation, and verification.

COSS, ReUI, or other component registries are not mandatory dependencies. If the current project uses one, Design Director can treat its live/current API as implementation truth.

## Repository map

```text
skills/design-director/
├── SKILL.md
├── references/
│   ├── design-evidence.md       # v4
│   ├── component-contracts.md   # v4
│   ├── micro-craft.md           # v4
│   └── ...
├── templates/
├── evals/
└── agents/

scripts/
├── install.sh
├── update.sh
├── uninstall.sh
├── doctor.sh
├── validate.py
├── catalog.py
└── build-web-bundles.py

web/
├── README.md
├── chatgpt/
│   └── INSTRUCTIONS.md
└── claude/
    └── README.md
```

## Validation and maintenance

```bash
python scripts/test_validate_v4.py
python scripts/validate.py
python scripts/catalog.py > CATALOG.json
python scripts/build-web-bundles.py
```

Knowledge additions follow a source → assess/license → distill → calibrate → human review → merge/supersede process rather than simply accumulating rules. See [`MAINTAINING.md`](MAINTAINING.md).

## Research / merge notes

- [`MERGE-ANALYSIS.md`](MERGE-ANALYSIS.md) — Command Code design-skill analysis and v2 merge rationale.
- [`RCD-REPOSITORY-AUDIT.md`](RCD-REPOSITORY-AUDIT.md) — Revenue-Centric Design repository audit and v3 merge rationale.
- [`V4-RESEARCH-AUDIT.md`](V4-RESEARCH-AUDIT.md) — UI Skills, COSS, Design System Checklist, Emil Kowalski UI motion, and ReUI → v4 rationale.
- [`SOURCE-STRUCTURE-INDEX.md`](SOURCE-STRUCTURE-INDEX.md) — source structure/index used during the Command Code analysis.
- [`THIRD_PARTY.md`](THIRD_PARTY.md) — companion licenses and boundaries.

## License

The Design Director core is released under the [`MIT License`](LICENSE).

Third-party companion skills are not bundled into the MIT core unless their licenses allow it. Research-derived v4 guidance is independently distilled rather than copied from third-party skill/component text or code.
