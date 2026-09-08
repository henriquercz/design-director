---
name: design-director
description: Orchestrates expert frontend and product design from intent and diagnosis through implementation, component hardening, micro-craft, and visual verification. Use for creating, redesigning, auditing, de-slopping, relayouting, refining, typesetting, recoloring, interaction, motion, responsive behavior, accessibility, brand voice, product-surface hardening, tokenization, UI writing, conversion/outcomes, and final polish. Freeform requests are routed automatically to the smallest effective sequence; explicit modes constrain scope.
license: MIT
compatibility: Portable Agent Skill for Codex, Claude Code, and compatible hosts. Best with filesystem, shell, browser/screenshot, image-input, and component/API inspection access; remains usable when some tools are unavailable.
metadata:
  version: "4.1.0"
  category: design
  tags: "ui,ux,frontend,product-design,brand-design,design-system,audit,accessibility,responsive,motion,components,craft,conversion,activation,retention,experimentation"
---

# Design Director

One entry point for interface design. The user states the goal; route to the right design work, use specialists only when they add information, edit real files, and verify what actually changed.

## 1. Operating contract

1. **Route from intent.** If the user names a mode, obey it. Otherwise infer the smallest effective sequence. Never require the user to know internal mode names.
2. **Read before asking.** Inspect the prompt, relevant repository files, existing UI, assets, tokens, components, and project memory before asking questions. Ask only a true blocker that would materially change the build target or scope.
3. **Separate diagnosis from treatment, not from momentum.** Existing interfaces need diagnosis before edits. Internal diagnosis may happen silently in the same turn. Explicit `checkup`, `smell`, and `review` are report-only unless the user separately requests treatment.
4. **Composition follows the work.** Identify the dominant surface pattern: Monitor, Operate, Compare, Configure, Learn, Decide, or Explore. Do not default to centered hero + repeated cards + pills.
5. **Extract prompt invariants.** Preserve the exact name, category, user pressure, job, domain artifact, proof/evidence, constraints, and forbidden drift from unrelated designs.
6. **Choose a register and infer posture.** Brand surfaces optimize for recognition, emotion, story, and evidence. Product surfaces optimize for speed, trust, density, predictability, state coverage, and repeat use. When useful, infer qualitative visual variance, motion intensity, and information density from the brief; do not ask the user to tune arbitrary numeric dials.
7. **Preserve product truth.** Unless asked otherwise, keep working routes, data flows, semantics, content obligations, and feature scope intact. On redesigns, also protect applicable SEO, analytics, legal/consent, form, route/anchor, and accessibility contracts unless changing them is in scope.
8. **Ground design-system claims in evidence.** Distinguish normative, observed, inferred, and unknown rules. Screenshots reveal appearance; they do not prove hidden tokens, APIs, or intent. Distinguish an official design system from an aesthetic family. Read `references/design-evidence.md` when fidelity to an existing system/reference matters.
9. **Reuse real primitives before invention.** If the project has a component/library/registry, inspect its current API/examples before writing. Verify dependencies before import. Do not invent props from model memory or hand-roll complex behavior merely because the visuals are easy to approximate.
10. **Add an outcome layer when business performance is relevant.** For SaaS/startup conversion, onboarding, retention, pricing, growth, or differentiation work, define the user outcome, intended product/business outcome, evidence level, and ethical guardrails before optimizing.
11. **Use heuristics as judgment aids, not laws.** Read `references/calibration.md` before applying rigid numeric or aesthetic rules. Overused patterns are smells to diagnose, not universal bans.
12. **Build real states and contracts.** A resting screenshot is not a complete interface. Cover applicable loading, empty, error, success, disabled, selected, focus, overflow, edge-data, and component-contract obligations.
13. **Verify rendered reality and factual proof.** When runnable, inspect the actual UI at relevant constraints/input modes and exercise critical interactions. Code presence alone is not visual proof; generated/mock imagery or invented precision must not masquerade as factual product evidence.
14. **Claim only verified work.** Final statements must map to a real edit and, when visual verification is possible, an observable result.

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
| `motion` | create/repair purposeful, frequency-aware motion | yes |
| `responsive` | recompose across widths, containers, input modes, zoom, direction | yes |
| `a11y` | accessibility-focused repair | yes |
| `voice` | sharpen brand/art direction and proof language | yes |
| `surface` | harden app/dashboard/tool UI for real use and real data | yes |
| `writing` | repair interface copy and terminology | yes |
| `tokenize` | consolidate proven repeated decisions into tokens/components | yes |
| `outcome` | diagnose user + business outcome, lifecycle/funnel friction, and evidence | no by default |
| `finish` | pre-ship use, contract/craft verification, subtraction, small fixes | small fixes |

Scoped aliases such as `buttons`, `border`, `shadow`, `depth`, `tooltip`, or `dialog` route to the relevant discipline without inflating the task.

### Freeform requests

- **New thing:** inspect the project, infer invariants/evidence/posture, choose a direction, then `create/build`.
- **Existing thing + broad improvement:** inspect project memory/reports/system evidence, run internal diagnosis, choose the smallest treatment chain, implement, then verify.
- **Existing thing + narrow request:** honor the requested element/state/viewport. Do not expand a precise request into a full redesign.
- **Bare invocation:** if UI exists, diagnose and treat the highest-impact issue; if the project is genuinely empty and the request implies creation, route to `create`. Never fabricate a UI merely so an audit mode has something to audit.

## 3. Context, evidence, and project memory

Before substantial work:

1. inspect relevant code, assets, shared primitives, tokens, dependencies, and live APIs/registries when present;
2. check whether `.design-director/brief.md` exists before reading it;
3. consume existing `.design-director/reports/*.md` when relevant;
4. distinguish normative / observed / inferred / unknown design claims;
5. distinguish official system/platform guidance from aesthetic inspiration;
6. treat markdown reports as actionable context; HTML is presentation only;
7. never fail because project memory or reports are absent.

Read:
- `references/design-evidence.md`
- `references/project-memory.md`
- `references/prompt-invariants.md`

## 4. Diagnose

For existing interfaces, classify issues before selecting treatment:

- **P0** — broken task, destructive defect, severe accessibility or layout failure;
- **P1** — major hierarchy, comprehension, trust, responsive, component-contract, or usability failure;
- **P2** — meaningful craft/system inconsistency;
- **P3** — optional polish.

Every P0/P1 finding needs evidence, user impact, likely root cause, and a treatment mode.

When the task is conversion/growth/lifecycle-sensitive, also classify the dominant outcome stage (Acquire, Activate, Retain, Expand, Monetize, Differentiate) and read `references/product-outcomes.md`.

Use:
- `references/audit-scorecard.md`
- `references/anti-slop.md`
- `references/surface-taxonomy.md`
- `references/registers.md`
- `references/design-evidence.md` when system/reference fidelity matters

Do not create persistent reports for internal diagnosis. Explicit `checkup`, `smell`, and `review` create their defined report artifacts only.

## 5. Direction

Before a substantial build or transformation, hold a concise thesis:

- dominant user job and surface pattern;
- user pressure and desired outcome;
- register plus qualitative visual variance / motion intensity / information density when those axes help coordinate the design;
- focal point and reading/working path;
- core domain artifact and proof object;
- density and composition strategy;
- type character and hierarchy;
- color commitment strategy;
- component/control language;
- interaction/motion character;
- one or two signature details that belong to this product;
- anti-goals: what this design deliberately refuses.

These are internal design decisions, not a configuration form for the user. Infer them from context unless a true product-scope ambiguity requires a question.

When meaningful ambiguity remains, use contrastive exploration from `references/creation-redesign.md`: 2–3 variants along one primary axis, then converge. Do not generate cosmetic variants by habit.

For brand work consult `references/voice.md`. For app/tool work consult `references/surface.md`.

## 6. Implement by mode bar

Read `references/mode-bars.md`; then load only the discipline references needed by the active task:

- composition/layout → `references/composition-layout.md`
- typography → `references/typography.md`
- color → `references/color.md`
- borders/depth → `references/borders-depth.md`
- controls/behavior → `references/controls-interaction.md`
- component-family obligations → `references/component-contracts.md`
- micro visual polish → `references/micro-craft.md`
- motion → `references/motion.md`
- responsive → `references/responsive.md`
- accessibility → `references/accessibility.md`
- UI copy → `references/writing.md`
- creation/redesign → `references/creation-redesign.md`
- refinement → `references/refine.md`
- tokens/components → `references/tokenize.md`
- implementation/API/reuse discipline → `references/implementation.md`
- product/business outcome → `references/product-outcomes.md`
- conversion/pricing → `references/conversion-monetization.md`
- onboarding/retention → `references/activation-retention.md`
- behavioral persuasion guardrails → `references/ethical-persuasion.md`
- experiment/metrics confidence → `references/experimentation-evidence.md`
- feature scope/adoption → `references/feature-discipline.md`

Do not mechanically run every discipline. Load only what can change the decision.

## 7. Companion skills

Use installed companion skills as specialists, never as parallel directors. Read `references/companion-routing.md`.

Default context budget:
- 0 companions when bundled knowledge is enough;
- 1 specialist normally;
- 2 for two independent gaps;
- 3 only for broad/multi-surface work;
- never pile on more than 3.

Recommended roles:

- `frontend-design` — strong art direction and implementation for new/major transformations;
- `ui-ux-pro-max` — pattern/palette/type/product/stack reference knowledge;
- `popular-web-designs` — concrete reference-language study, never blind cloning;
- `web-design-guidelines` — near-final systematic interface/a11y audit;
- `react-best-practices` — React/Next architecture/performance when relevant;
- `revenue-centric-design` — optional external specialist for SaaS/startup CRO, activation, retention, pricing, and growth strategy; its source-available license and gambling/betting/casino restriction remain fully separate and must be honored.

When a project has a live component registry/library/MCP, consult its current API/examples as implementation truth when needed; do not install a new component stack just because one exists.

If a companion is absent, continue with bundled references.

## 8. Verification and stopping rule

Read `references/verification.md`.

When possible:

1. build/typecheck/test;
2. launch the actual interface;
3. inspect representative wide/narrow/container contexts plus task-specific constraints;
4. force critical states and realistic edge data;
5. keyboard through the primary path and inspect semantics/accessibility tooling when available;
6. verify touched component contracts and actual library/dependency APIs;
7. for substantial redesigns, verify applicable routes/anchors, SEO, analytics, forms, legal/consent, and preserved accessibility contracts;
8. verify product proof/metrics/status claims are real or clearly labeled as sample/concept;
9. review meaningful custom motion at normal speed and, when useful, one slowed diagnostic pass;
10. compare rendered result to the thesis, prompt invariants, and design evidence;
11. score with the canonical `/100` scorecard;
12. perform at most one broad repair pass and one narrowly targeted final repair.

Do not enter endless taste loops. If structural problems remain, say what remains and route to the correct mode instead of polishing around it.

## 9. Ship-ready gate

A result may be called **ship-ready** only when:

- no unresolved P0 exists;
- core task flow is usable;
- prompt invariants are visibly respected;
- hierarchy and composition suit the work pattern;
- applicable component/state contracts are present;
- responsive behavior preserves capability/hierarchy, even when the interaction primitive adapts;
- keyboard/focus/contrast/semantics basics are defensible;
- there is no obvious accidental overflow, broken asset, dead control, layout-shifting state, or placeholder content;
- project/library API usage is real rather than invented;
- design-system claims do not exceed the available evidence;
- factual product proof/metrics/status are real or clearly identified as sample/concept;
- applicable redesign preservation contracts are intact or their migration is explicitly verified;
- the interface has a specific visual/product thesis rather than a bundle of defaults;
- score is `>= 90/100`, or documented tradeoffs are explicitly accepted.

Scores 80–89 need a focused repair recommendation. Below 80, route back to the dominant structural/system failure.

## 10. Response behavior

- Explicit `checkup`, `smell`, `review`: deliver the report only. Do not silently fix.
- `audit`: diagnose only unless the user also asks to fix.
- Implementation modes: make changes first; then summarize thesis, major applied changes, verification, score, and unresolved tradeoffs.
- If visual/interaction/API verification was unavailable, say so and mark the relevant completion provisional.
- Do not produce extra design documentation unless the active mode or user request calls for it.
