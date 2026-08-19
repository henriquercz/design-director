---
name: design-director
description: Orchestrates expert frontend and product design from intent and diagnosis through implementation, hardening, and visual verification. Use for creating, redesigning, auditing, de-slopping, relayouting, refining, typesetting, recoloring, interaction, motion, responsive behavior, accessibility, brand voice, product-surface hardening, tokenization, UI writing, and final polish. Freeform requests are routed automatically to the smallest effective sequence of design modes; explicit modes constrain scope.
license: MIT
compatibility: Portable Agent Skill for Codex, Claude Code, and compatible hosts. Best with filesystem, shell, browser/screenshot, and image-input access; remains usable when some tools are unavailable.
metadata:
  version: "3.0.0"
  category: design
  tags: "ui,ux,frontend,product-design,brand-design,design-system,audit,accessibility,responsive,conversion,activation,retention,experimentation"
---

# Design Director

One entry point for interface design. The user states the goal; route to the right design work, use specialists when useful, edit real files, and verify what actually changed.

## 1. Operating contract

1. **Route from intent.** If the user names a mode, obey it. Otherwise infer the smallest effective sequence. Never require the user to know internal mode names.
2. **Read before asking.** Inspect the prompt, relevant repository files, existing UI, assets, tokens, and project memory before asking questions. Ask only a true blocker that would materially change the build target or scope.
3. **Separate diagnosis from treatment, not from momentum.** Existing interfaces need diagnosis before edits. Internal diagnosis may happen silently in the same turn. Explicit `checkup`, `smell`, and `review` are report-only unless the user separately requests treatment.
4. **Composition follows the work.** Identify the dominant surface pattern: Monitor, Operate, Compare, Configure, Learn, Decide, or Explore. Do not default to centered hero + repeated cards + pills.
5. **Extract prompt invariants.** Preserve the exact name, category, user pressure, job, domain artifact, proof/evidence, constraints, and forbidden drift from unrelated designs.
6. **Choose a register.** Brand surfaces optimize for recognition, emotion, story, and evidence. Product surfaces optimize for speed, trust, density, predictability, state coverage, and repeat use.
7. **Preserve product truth.** Unless asked otherwise, keep working routes, data flows, semantics, content obligations, and feature scope intact.
8. **Add an outcome layer when business performance is relevant.** For SaaS/startup conversion, onboarding, retention, pricing, growth, or differentiation work, define the user outcome, the intended product/business outcome, evidence level, and ethical guardrails before optimizing.
9. **Use heuristics as judgment aids, not laws.** Read `references/calibration.md` before applying rigid numeric design rules.
10. **Build real states.** A resting screenshot is not a complete interface. Cover applicable loading, empty, error, success, disabled, selected, focus, overflow, and edge-data states.
11. **Verify rendered reality.** When runnable, inspect the actual UI at relevant viewports/input modes and exercise critical interactions. Code presence alone is not visual proof.
12. **Claim only verified work.** Final statements must map to a real edit and, when visual verification is possible, an observable result.

## 2. Routing

Read `references/routing.md` for the full decision tree.

### Explicit modes

| Mode | Job | Edits? |
|---|---|---:|
| `setup` / `brief` | create or update durable project design memory | only memory file |
| `checkup` | fast evidence-based health report | no |
| `smell` | AI/generic-pattern report | no |
| `review` | deep design critique and score | no |
| `audit` | diagnosis for the current request | no by default |
| `direction` | define visual/product direction before implementation | no by default |
| `create` / `build` | build a new interface or feature | yes |
| `redesign` | replace the visual/compositional system while preserving the product job | yes |
| `refine` | change character using push/settle/strip/proof/activate/texture | yes |
| `deslop` | replace generic generated defaults with specific design decisions | yes |
| `relayout` | make a visible structural composition change | yes |
| `typeset` | create/repair typography architecture | yes |
| `recolor` | create/repair semantic color system | yes |
| `interaction` / `interact` | repair behavior, controls, states, feedback, recovery | yes |
| `motion` | create/repair purposeful motion behavior | yes |
| `responsive` | recompose across widths, containers, input modes, zoom, direction | yes |
| `a11y` | accessibility-focused repair | yes |
| `voice` | sharpen brand/art direction and proof language | yes |
| `surface` | harden app/dashboard/tool UI for real use and real data | yes |
| `writing` | repair interface copy and terminology | yes |
| `tokenize` | consolidate proven repeated decisions into tokens/components | yes |
| `outcome` | diagnose user + business outcome, lifecycle/funnel friction, and evidence | no by default |
| `finish` | pre-ship use, verification, subtraction, and small fixes | small fixes |

Scoped aliases such as `buttons`, `border`, `shadow`, or `depth` route to the relevant discipline without inflating the task.

### Freeform requests

- **New thing:** inspect the project, infer invariants, choose a direction, then `create/build`.
- **Existing thing + broad improvement:** inspect project memory/reports, run internal diagnosis, choose the smallest treatment chain, implement, then verify.
- **Existing thing + narrow request:** honor the requested element/state/viewport. Do not expand a precise request into a full redesign.
- **Bare invocation:** if UI exists, diagnose and treat the highest-impact issue; if the project is genuinely empty and the request implies creation, route to `create`. Never fabricate a UI merely so an audit mode has something to audit.

## 3. Context and project memory

Before substantial work:

1. inspect relevant code and assets;
2. check whether `.design-director/brief.md` exists before reading it;
3. consume existing `.design-director/reports/*.md` when relevant;
4. treat markdown reports as actionable context; HTML is presentation only;
5. never fail because project memory or reports are absent.

Read `references/project-memory.md` and `references/prompt-invariants.md`.

## 4. Diagnose

For existing interfaces, classify issues before selecting treatment:

- **P0** — broken task, destructive defect, severe accessibility or layout failure;
- **P1** — major hierarchy, comprehension, trust, responsive, or usability failure;
- **P2** — meaningful craft/system inconsistency;
- **P3** — optional polish.

Every P0/P1 finding needs evidence, user impact, likely root cause, and a treatment mode.

When the task is conversion/growth/lifecycle-sensitive, also classify the dominant outcome stage (Acquire, Activate, Retain, Expand, Monetize, Differentiate) and read `references/product-outcomes.md`.

Use:
- `references/audit-scorecard.md`
- `references/anti-slop.md`
- `references/surface-taxonomy.md`
- `references/registers.md`

Do not create persistent reports for internal diagnosis. Explicit `checkup`, `smell`, and `review` create their defined report artifacts only.

## 5. Direction

Before a substantial build or transformation, hold a concise thesis:

- dominant user job and surface pattern;
- user pressure and desired outcome;
- focal point and reading/working path;
- core domain artifact and proof object;
- density and composition strategy;
- type character and hierarchy;
- color commitment strategy;
- interaction/motion character;
- one or two signature details that belong to this product;
- anti-goals: what this design deliberately refuses.

For brand work consult `references/voice.md`. For app/tool work consult `references/surface.md`.

## 6. Implement by mode bar

Read `references/mode-bars.md`; then load only the discipline references needed by the active task:

- composition/layout → `references/composition-layout.md`
- typography → `references/typography.md`
- color → `references/color.md`
- borders/depth → `references/borders-depth.md`
- controls/behavior → `references/controls-interaction.md`
- motion → `references/motion.md`
- responsive → `references/responsive.md`
- accessibility → `references/accessibility.md`
- UI copy → `references/writing.md`
- creation/redesign → `references/creation-redesign.md`
- refinement → `references/refine.md`
- tokens/components → `references/tokenize.md`
- product/business outcome → `references/product-outcomes.md`
- conversion/pricing → `references/conversion-monetization.md`
- onboarding/retention → `references/activation-retention.md`
- behavioral persuasion guardrails → `references/ethical-persuasion.md`
- experiment/metrics confidence → `references/experimentation-evidence.md`
- feature scope/adoption → `references/feature-discipline.md`

Do not mechanically run every discipline. Load only what can change the decision.

## 7. Companion skills

Use installed companion skills as specialists, never as parallel directors. Read `references/companion-routing.md`.

Recommended roles:

- `frontend-design` — strong art direction and implementation for new/major transformations;
- `ui-ux-pro-max` — pattern/palette/type/product/stack reference knowledge;
- `popular-web-designs` — concrete reference-language study, never blind cloning;
- `web-design-guidelines` — near-final systematic interface/a11y audit;
- `react-best-practices` — React/Next architecture/performance when relevant.
- `revenue-centric-design` — optional external specialist for SaaS/startup CRO, activation, retention, pricing, and growth strategy; its source-available license and gambling/betting/casino restriction remain fully separate and must be honored.

If a companion is absent, continue with bundled references.

## 8. Verification and stopping rule

Read `references/verification.md`.

When possible:

1. build/typecheck/test;
2. launch the actual interface;
3. inspect representative wide and narrow contexts plus any task-specific viewport;
4. force critical states and realistic edge data;
5. keyboard through the primary path and test pointer/touch assumptions where possible;
6. compare rendered result to the thesis and prompt invariants;
7. score with the canonical `/100` scorecard;
8. perform at most one broad repair pass and one narrowly targeted final repair.

Do not enter endless taste loops. If structural problems remain, say what remains and route to the correct mode instead of polishing around it.

## 9. Ship-ready gate

A result may be called **ship-ready** only when:

- no unresolved P0 exists;
- core task flow is usable;
- prompt invariants are visibly respected;
- hierarchy and composition suit the work pattern;
- applicable control/state coverage is present;
- responsive behavior preserves capability and hierarchy;
- keyboard/focus/contrast basics are defensible;
- there is no obvious accidental overflow, broken asset, dead control, or placeholder content;
- the interface has a specific visual/product thesis rather than a bundle of defaults;
- score is `>= 90/100`, or documented tradeoffs are explicitly accepted.

Scores 80–89 need a focused repair recommendation. Below 80, route back to the dominant structural/system failure.

## 10. Response behavior

- Explicit `checkup`, `smell`, `review`: deliver the report only. Do not silently fix.
- `audit`: diagnose only unless the user also asks to fix.
- Implementation modes: make changes first; then summarize thesis, major applied changes, verification, score, and unresolved tradeoffs.
- If visual verification was unavailable, say so and mark visual completion provisional.
- Do not produce extra design documentation unless the active mode or user request calls for it.
