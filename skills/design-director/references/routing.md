# Routing and execution policy

The user should be able to invoke `design-director` with ordinary language. Internal mode names are optional controls, not required vocabulary.

## Decision tree

### 1. Parse explicit scope first

If the user names a mode or a precise target, that instruction wins.

Examples:
- "review only, don't edit" → `review`
- "fix mobile only" → `responsive` scoped to narrow viewports
- "change only the hero composition" → `relayout` scoped to hero
- "make the whole product feel different" → `redesign`

Never inflate a narrow request into a full-system pass.

### 2. Determine whether the target exists

Inspect the filesystem rather than assuming:
- interface files and routes;
- package/framework clues;
- component directories;
- styles/tokens;
- screenshots/assets.

If no target exists but the request clearly asks for a new page/component/feature, route to `create`.

If no target exists and the user explicitly asked for `checkup`, `smell`, `review`, or `audit`, report that there is no interface to inspect. Do **not** invent `index.html` to satisfy the audit.

### 3. For an existing interface, absorb prior context

If `.design-director/brief.md` exists, read it.
If `.design-director/reports/*.md` exists, read relevant reports before treatment.
Existing reports inform the next pass; they do not replace active-mode judgment.

### 4. Choose diagnosis depth

- obvious generated/generic complaint → internal smell scan;
- quick health question → checkup lens;
- broad "make it better" → review lens + anti-slop scan as needed;
- clear local defect → inspect only enough to establish root cause.

Internal diagnosis is working state, not a required artifact.

### 5. Choose the smallest effective treatment

Map root cause to mode:

| Root cause | Treatment |
|---|---|
| wrong spatial premise / focal path | `relayout` |
| identity/world fundamentally wrong | `redesign` |
| generic generated reflexes | `deslop` |
| design character too weak/loud/cluttered/brittle | `refine` |
| type hierarchy/measure/font behavior | `typeset` |
| palette/semantic roles/contrast | `recolor` |
| controls/states/recovery/feedback | `interaction` |
| transition/causality/continuity | `motion` |
| mobile/container/input/direction adaptation | `responsive` |
| semantic/focus/assistive-access issue | `a11y` |
| brand recognition/proof/art direction | `voice` |
| app density/data/states/operability | `surface` |
| interface copy/terminology | `writing` |
| repeated inconsistent values/components | `tokenize` |
| only small residual friction remains | `finish` |

Treat structural causes before cosmetic symptoms.

### 6. Multi-mode chains

A broad request may need a short chain. Typical examples:

- generic landing page → internal review → `deslop` + `relayout` → `voice` → `finish`
- brittle dashboard → internal review → `surface` + `responsive` → `interaction` → `finish`
- visually incoherent mature product → `tokenize` only after the desired system is proven, never before redesign decisions
- full transformation → `redesign` already owns composition, color, type, depth, components, and motion; do not redundantly run every subsystem as separate modes

Prefer 1–3 treatment modes. More than that should be justified by distinct root causes.

## Explicit report modes

`checkup`, `smell`, and `review` are strict report boundaries when named explicitly:
- inspect;
- generate their markdown report under `.design-director/reports/`;
- optionally generate HTML only if configured/requested;
- do not edit product UI in the same invocation.

Why: explicit diagnosis should remain inspectable and reversible.

A freeform "improve this" may run the same diagnostics internally and continue directly into treatment without generating report files.

## Bare invocation

With no mode and no freeform instructions:
- if a real interface exists, run a lightweight internal diagnosis and fix the single highest-impact design issue, then verify;
- if the repo is empty, explain that a creation target is needed unless the surrounding task already establishes one.

Do not show a mode menu unless the user asks for one.

## Ask-vs-decide

Decide without asking:
- spacing, radius, shade, font weight, microcopy details;
- exact layout mechanics inside a known goal;
- which reference files to consult;
- common edge-state handling;
- ordinary design tradeoffs.

Ask one focused question only for a true blocker:
- missing target or goal;
- contradictory constraints;
- inaccessible required source/input;
- destructive ambiguity;
- a choice that changes product/feature scope rather than design execution.

Before asking, perform an "answered already" pass across prompt + repo + project memory.

## Outcome-sensitive routing (v3)

When the request involves SaaS/startup conversion, onboarding, pricing, retention/churn, expansion, feature adoption, growth, or differentiation, activate the outcome layer before choosing visual treatment:

1. Read `product-outcomes.md`.
2. Classify dominant stage: Acquire, Activate, Retain, Expand, Monetize, or Differentiate.
3. Identify user outcome + product/business outcome + evidence confidence.
4. Read only the relevant specialist reference:
   - acquisition/conversion/pricing → `conversion-monetization.md`;
   - onboarding/retention → `activation-retention.md`;
   - product metrics/testing → `experimentation-evidence.md`;
   - feature scope/adoption → `feature-discipline.md`;
   - persuasive mechanisms/defaults/urgency → `ethical-persuasion.md`.
5. Then route to the smallest existing implementation mode (`voice`, `writing`, `relayout`, `surface`, `interaction`, `refine`, etc.).

`outcome` is a diagnostic/strategy alias. It does not override visual modes; it determines what the design pass should optimize and which evidence would prove success.

Do not optimize a business metric through deceptive defaults, hidden commitment, artificial scarcity, obstructed cancellation, artificial lock-in, or compulsion engineering. Read `ethical-persuasion.md` whenever the requested mechanism can surprise or pressure the user.
