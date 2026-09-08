# Design Director

> A portable design director for AI coding agents and web LLMs. Describe what you want changed; Design Director diagnoses the real problem, chooses the smallest effective design workflow, uses the project's real system, and verifies the result.

**Design Director v4.1** combines frontend/UI craft, product design, anti-AI-slop judgment, accessibility, responsive behavior, brand/product registers, outcome-aware product design, evidence-aware design-system inference, component contracts, micro-craft, purpose/frequency-aware motion, production-redesign safety, and calibrated taste.

The UX stays intentionally simple:

```text
$design-director
I don't like this section. Redesign it so it feels more professional, intentional, and specific to our product. Preserve what already works.
```

That is enough. You do **not** need to choose `relayout`, `deslop`, `motion`, typography rules, component contracts, or specialist skills yourself.

## What's new in v4.1

v4.1 incorporates selected, calibrated lessons from the MIT-licensed [Taste Skill](https://github.com/Leonxlnx/taste-skill) without importing its rigid universal style bans.

- **Qualitative design posture:** Design Director can internally infer visual variance, motion intensity, and information density from the brief, audience, risk, register, and existing system. No numeric sliders are required from the user.
- **Production-redesign preservation:** substantial redesigns now explicitly protect applicable routes/anchors, SEO/structured data/OG, analytics/experiment hooks, form contracts, legal/consent mechanics, brand assets, public data semantics, and existing accessibility wins.
- **Official system vs aesthetic honesty:** the agent verifies current platform/package evidence before claiming something is an official design system; aesthetic recreations are labeled as inspiration/approximation rather than invented vendor packages.
- **Marketing anti-slop:** stronger detection of repeated eyebrows, decorative numbering/status dots, fake operational chrome, fake product previews, fabricated precision, repeated section-layout loops, and performative micro-copy.
- **Product-proof integrity:** generated/editorial imagery can be great art direction, but must not masquerade as a real screenshot, metric, customer, status, or specification.
- **Copy self-audit:** changed visible copy is re-read for grammar, unclear referents, hallucinated claims, CTA-intent drift, terminology drift, and fake precision.
- **Implementation safeguards:** dependency verification, coherent component-system boundaries, high-frequency interaction state discipline, and listener/effect cleanup are more explicit.
- **Dynamic viewport guidance:** `dvh` / `svh` are available for mobile browser-chrome/full-height problems without becoming a universal replacement for `vh`.
- **Calibration against dogma:** no blanket ban on Inter, serif, em dashes, Lucide, gradients, pure black/white, multiple semantic accents, or a single theme. Context and project evidence win.
- **56 behavioral eval cases** now cover v1–v4.1 routing and regression expectations.

Detailed merge rationale: [`TASTE-SKILL-AUDIT.md`](TASTE-SKILL-AUDIT.md).

## Install in 30 seconds

### Codex + Claude Code with `npx skills`

Global:

```bash
npx skills add henriquercz/design-director \
  --skill design-director \
  -g \
  -a codex \
  -a claude-code \
  -y
```

Project only:

```bash
npx skills add henriquercz/design-director \
  --skill design-director \
  -a codex \
  -a claude-code \
  -y
```

One agent only:

```bash
npx skills add henriquercz/design-director --skill design-director -g -a codex -y
npx skills add henriquercz/design-director --skill design-director -g -a claude-code -y
```

The repository follows the open Agent Skills layout at `skills/design-director/SKILL.md`.

## Use it naturally

### Codex

```text
$design-director
This landing page feels generic and weak. Diagnose the real problems, preserve the working product behavior, choose the right treatments yourself, implement them, and verify desktop and mobile.
```

### Claude Code

```text
/design-director
I don't like this dashboard section. Redesign it to feel more professional and easier to operate. Keep the current flows working and choose the right design treatments yourself.
```

### Abstract requests are expected

All of these are valid:

```text
$design-director Make this section feel more professional.
$design-director This hero looks AI-generated. Fix it.
$design-director The mobile version feels cramped and awkward.
$design-director Redesign this landing page without changing the content obligations.
$design-director Make the onboarding easier to understand and more polished.
```

Design Director infers the route. Explicit modes are only scope controls:

```text
$design-director review this dashboard. Do not edit files.
$design-director relayout this hero. Preserve color and typography.
$design-director responsive fix tablet and mobile only.
$design-director surface harden this production dashboard with real states and edge data.
```

## How v4.1 thinks

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
register + internal posture
Brand / Product
variance × motion × density
   ↓
optional product outcome
Acquire / Activate / Retain / Expand / Monetize / Differentiate
   ↓
root-cause diagnosis
   ↓
smallest treatment chain
   ↓
real project primitive / dependency / API lookup
   ↓
component contracts + implementation
   ↓
micro-craft + purposeful motion
   ↓
rendered + behavioral + preservation verification
   ↓
review /100 → bounded repair → finish
```

## Core modes

You normally do not need to name these. The public mode surface remains stable at **23 modes/aliases**.

| Group | Modes |
|---|---|
| Diagnose | `checkup`, `smell`, `review`, `audit` |
| Direction | `setup`, `brief`, `direction` |
| Create / transform | `create`, `build`, `redesign`, `deslop`, `relayout`, `refine` |
| Systems | `typeset`, `recolor`, `interaction`, `motion`, `responsive`, `a11y`, `tokenize` |
| Character / production | `voice`, `surface`, `writing`, `finish` |
| Product outcome | `outcome` plus focused conversion, activation, retention, monetization, experimentation, and feature-discipline references |

Explicit `checkup`, `smell`, and `review` are report-only unless you separately request treatment. A freeform improvement request can diagnose and implement in one pass.

## What makes Design Director different

- **One director, not a pile of prompts.** The user states the goal; routing and specialist selection stay internal.
- **Surface-first composition.** Layout derives from the work rather than defaulting to centered heroes, equal cards, pills, and generic SaaS patterns.
- **Prompt invariants.** Exact names, domain artifacts, proof, constraints, user pressure, and content obligations survive redesigns.
- **Brand vs Product.** Marketing surfaces can spend more expression; repeated-use product UI prioritizes speed, density, state coverage, and predictability.
- **Calibrated design posture.** Variance, motion, and density coordinate direction without becoming arbitrary numeric laws.
- **Design evidence.** Screenshots are not allowed to invent hidden tokens or private component APIs.
- **Official-system honesty.** An aesthetic inspired by a platform is not automatically an official package.
- **Reuse/API-first implementation.** Current project components, types, registries, MCPs, and examples beat model memory.
- **Component contracts.** Dialogs, tooltips, tabs, toasts, forms, collections, loading states, drag interactions, and media are evaluated beyond resting screenshots.
- **Micro-craft.** Optical alignment, nested radii, relationship spacing, media geometry, clipping, depth, explicit transitions, and state geometry receive a final craft pass.
- **Purposeful motion.** Motion is judged by purpose × frequency × input × spatial change × cost; high-frequency actions stay effectively immediate.
- **Responsive recomposition.** The interaction primitive itself can adapt (for example Dialog → Drawer) while preserving task/data/semantics.
- **Production-redesign safety.** Visual modernization does not silently break SEO, analytics, form integrations, consent, URLs, or accessibility.
- **Anti-slop by evidence clusters.** Overused patterns are smells to diagnose, not a blacklist of components/fonts/punctuation.
- **Outcome-aware design.** Conversion, activation, retention, pricing, experimentation, and feature adoption can inform design without overriding user benefit or truthfulness.
- **Truthful completion.** No claim of visual/behavioral correctness without implementation and, when possible, rendered verification.
- **Bounded iteration.** One broad repair pass and one targeted final repair; then expose remaining tradeoffs instead of looping forever.

## Full skillset installer

`npx skills` installs the Design Director core. To install recommended companions too:

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

See [`THIRD_PARTY.md`](THIRD_PARTY.md) for license/provenance boundaries.

## No install: prompt bootstrap

For a one-off session, copy [`PROMPT-INSTALL.md`](PROMPT-INSTALL.md) into the LLM/agent and then state your design request normally.

With the Skills CLI:

```bash
npx skills use henriquercz/design-director@design-director --agent codex
npx skills use henriquercz/design-director@design-director --agent claude-code
```

## Claude on the web

Build the native Skill ZIP:

```bash
python scripts/build-web-bundles.py --claude
```

Output:

```text
dist/claude/design-director-claude-web.zip
```

Upload it in Claude's custom Skills interface and enable **Design Director**. The builder derives the package from the canonical skill so web and coding-agent copies do not drift.

More detail: [`web/claude/README.md`](web/claude/README.md).

## ChatGPT on the web

Build the persistent GPT/Project bundle:

```bash
python scripts/build-web-bundles.py --chatgpt
```

Outputs:

```text
dist/chatgpt/INSTRUCTIONS.md
dist/chatgpt/design-director-knowledge.md
```

Use `INSTRUCTIONS.md` as GPT/Project instructions and upload `design-director-knowledge.md` as Knowledge/project reference material.

More detail: [`web/chatgpt/README.md`](web/chatgpt/README.md).

## Repository map

```text
skills/design-director/
├── SKILL.md                 # portable Agent Skill entrypoint
├── references/              # progressively disclosed design knowledge
├── templates/               # brief/report/decision templates
├── evals/                   # behavioral evaluation cases
└── agents/                  # optional host metadata

scripts/
├── install.sh
├── update.sh
├── uninstall.sh
├── doctor.sh
├── validate.py
├── catalog.py
├── test_validate_v4.py
├── test_taste_integration.py
└── build-web-bundles.py

web/
├── README.md
├── chatgpt/
└── claude/
```

## Validation

```bash
python scripts/test_taste_integration.py .
python scripts/validate.py
python scripts/catalog.py
python scripts/build-web-bundles.py
```

Current catalog target:

```text
36 references
6 templates
56 evaluation cases
23 public modes/aliases
```

Knowledge additions follow a source → distill → calibrate → review → merge/supersede process rather than simply accumulating rules. See [`MAINTAINING.md`](MAINTAINING.md).

## Research / merge notes

- [`MERGE-ANALYSIS.md`](MERGE-ANALYSIS.md) — Command Code design reference analysis and v2 merge rationale.
- [`RCD-REPOSITORY-AUDIT.md`](RCD-REPOSITORY-AUDIT.md) — Revenue-Centric Design audit and v3 rationale.
- [`V4-RESEARCH-AUDIT.md`](V4-RESEARCH-AUDIT.md) — UI Skills, COSS, Design System Checklist, Emil Kowalski, and ReUI research that informed v4.
- [`TASTE-SKILL-AUDIT.md`](TASTE-SKILL-AUDIT.md) — Taste Skill accepted/rejected concepts for v4.1.
- [`THIRD_PARTY.md`](THIRD_PARTY.md) — companion licenses and research-source boundaries.

## License

The Design Director core is released under the [`MIT License`](LICENSE).

Third-party companion skills are not bundled into the MIT core unless their licenses allow it. Upstream terms continue to apply to separately installed companions.
