# Project design memory

Use `.design-director/brief.md` as durable project design memory when the repository benefits from consistent future design work.

## Rules

- The file is optional. Confirm it exists before reading it.
- Absence is normal and must not block work.
- `setup` creates or updates it after reading the repository first.
- Do not silently overwrite meaningful existing decisions. Preserve valid constraints and record intentional changes.
- Store durable facts, not transient audit observations.

## Recommended fields

- product / brand name;
- category and register: Brand, Product, or mixed;
- users and user pressures;
- dominant surface patterns by major screen;
- primary jobs and core domain artifacts;
- proof/evidence objects;
- brand traits and anti-traits;
- existing visual system: type, color, spacing, radius, depth, icon/illustration language;
- interaction character and motion posture;
- density and responsive expectations;
- accessibility/performance constraints;
- supported locales/direction/input modes;
- existing component/design-system constraints;
- deliberate anti-patterns / forbidden drift;
- stable references and accepted tradeoffs.

## Reports

Persistent diagnostic reports live under `.design-director/reports/`.
Suggested names:
- `checkup.md`
- `smell.md`
- `review.md`

Markdown is the source for follow-up work. HTML, if generated, is a presentation artifact only and must never become visual inspiration for the product itself.

Internal diagnosis should not create these files automatically.
