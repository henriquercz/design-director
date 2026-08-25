# Project design memory

Use `.design-director/brief.md` as durable project design memory when the repository benefits from consistent future design work.

## Rules

- The file is optional. Confirm it exists before reading it.
- Absence is normal and must not block work.
- `setup` creates or updates it after reading the repository first.
- Do not silently overwrite meaningful existing decisions. Preserve valid constraints and record intentional changes.
- Store durable facts, not transient audit observations.
- When a rule is not explicitly proven, store its evidence confidence/provenance rather than presenting inference as fact. Read `design-evidence.md`.

## Recommended fields

### Product and work
- product / brand name;
- category and register: Brand, Product, or mixed;
- users and user pressures;
- dominant surface patterns by major screen;
- primary jobs and core domain artifacts;
- proof/evidence objects;
- outcome stages/measures when business performance is relevant.

### Design language constitution
- product/brand vision or design principles when explicit;
- brand traits and anti-traits;
- tone / voice / terminology conventions;
- existing type roles/families/loading/fallback posture;
- semantic color roles and theme/dark-mode posture;
- spacing/grid/container rhythm;
- radius, border, elevation, shadow, and z-index/depth model;
- iconography/illustration/media language and naming/usage conventions;
- interaction character and motion posture/tokens;
- density expectations;
- responsive/container strategy and deliberate interaction adaptations;
- component primitive/library/registry family and stable API constraints.

### Constraints and tradeoffs
- accessibility/performance constraints;
- supported locales/direction/input modes;
- deliberate anti-patterns / forbidden drift;
- stable references;
- accepted tradeoffs/debt;
- known docs-vs-implementation inconsistencies.

## Evidence notation

Use a compact confidence tag only where it prevents future drift:

```text
Button radius: radius-md token — Normative (theme/tokens.css)
Row spacing: 8/12 appears across tables — Observed, not confirmed global token
Hero crop: left-biased portrait reference — Inferred from approved visual
```

Do not annotate every obvious fact. The purpose is to prevent a model inference from becoming a false constitutional rule.

## Setup behavior

When building memory:
1. read explicit docs and tokens first;
2. inspect shared primitives/current APIs;
3. sample representative real consumers;
4. compare rendered behavior where available;
5. record only durable facts;
6. label unresolved contradictions instead of silently choosing one source.

## Reports

Persistent diagnostic reports live under `.design-director/reports/`.
Suggested names:
- `checkup.md`
- `smell.md`
- `review.md`

Markdown is the source for follow-up work. HTML, if generated, is a presentation artifact only and must never become visual inspiration for the product itself.

Internal diagnosis should not create these files automatically.
