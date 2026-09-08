# Verification and truthful completion

A design claim is valid only when it maps to actual implementation and, when possible, rendered behavior.

## Pre-ship use pass

Use the interface like a person:
- click/tap;
- tab and use keyboard;
- type and submit;
- wait;
- trigger failure;
- resize/recompose;
- search/filter/sort;
- open/close overlays;
- perform destructive/reversible actions when safe;
- refresh/return where relevant.

## Force rough states

Inspect applicable:
- empty;
- loading;
- error;
- success;
- disabled/read-only;
- selected/current;
- focus;
- overflow;
- long/short/zero/huge data;
- slow/no network when testable;
- narrow/wide container;
- dark/light themes if supported;
- RTL/localization if supported.

## Keyboard-only pass

For an interactive surface, traverse the primary task without a pointer when feasible:
- focus is visible;
- order is logical;
- overlays enter/exit/restore focus correctly;
- composite widgets follow their intended keyboard model;
- essential drag/pointer actions have a non-pointer alternative where required;
- repeated keyboard actions are not delayed by decorative motion.

## Semantics / accessibility pass

When browser/accessibility tooling permits, inspect native roles, accessible names, labels/descriptions, state relationships, live announcements, and tree order.

Do not infer semantic accessibility from visuals alone.

## Component-contract pass

For every substantially touched interactive primitive, consult `component-contracts.md` and verify the applicable contract: states, geometry, focus/keyboard, collision/scroll, loading footprint, responsive adaptation, recovery, and real API usage.

## Redesign preservation pass

For substantial redesigns of an existing production/public surface, compare the changed result against the preservation envelope in `creation-redesign.md`.

When applicable verify:
- route slugs and deep links still resolve;
- important anchor/fragment IDs remain valid or are deliberately migrated;
- page title/description/canonical/indexability/structured data/OG-social metadata and important internal links did not disappear accidentally;
- analytics/telemetry event names, tracking attributes, experiment hooks, and conversion events still fire with intended semantics;
- form field names, autocomplete/data binding, validation, order obligations, and submission behavior remain compatible;
- legal/consent/cookie/disclosure text and acceptance mechanics are intact;
- brand logo/wordmark/protected assets were not silently replaced;
- existing accessibility wins (headings, landmarks, labels, alt text, focus, keyboard, announcements, reduced motion, contrast) did not regress;
- public API/data semantics used by the surface remain compatible.

If a preservation contract changed intentionally, call out the migration and verification rather than hiding it inside a visual redesign summary.

## Proof / factual-claim pass

On brand/marketing surfaces, verify that visual credibility is not built from fabricated facts:
- product screenshots/artifacts shown as real are actually real or executable;
- concept/generated/mock previews are labeled when they could be mistaken for real product evidence;
- metrics/specifications/customer counts/availability/status claims are provided or verifiable, or clearly identified as sample/mock data;
- company/customer logos and testimonial attribution are truthful/authorized for the intended use rather than invented proof.

Atmospheric generated imagery can be excellent art direction; it just must not masquerade as factual product proof.

## Rendered proof

If you say:
- "relayouted" → composition must visibly differ, not just padding;
- "animated" → reachable motion must exist in rendered UI;
- "fixed focus" → keyboard focus must be observable;
- "added loading/error/empty state" → there must be a way to trigger or inspect it;
- "responsive" → inspect actual narrow/wide result and any changed interaction model;
- "recolored" → real components must use semantic roles;
- "tokenized" → migrated usage must resolve through tokens/components;
- "matched the design system" → evidence must support the claimed rules; screenshot similarity alone is insufficient;
- "reused the component library" → imports/props/composition must match the current real API;
- "preserved the production redesign contracts" → verify the applicable SEO/analytics/forms/legal/routes/accessibility behaviors rather than assuming a visual diff cannot affect them.

If implemented but not triggerable in the current environment, say exactly that instead of claiming full visual verification.

## Motion inspection

For meaningful custom motion, when tooling permits:
- inspect at normal speed for latency/quality;
- use one slowed diagnostic pass to reveal origin, clipping, stagger, reversal, and interrupted-state defects;
- verify reduced-motion behavior;
- verify high-frequency actions remain effectively immediate.

Do not run slow-motion review for pages with no meaningful custom motion.

## Visual craft pass

Read `micro-craft.md` for touched/high-visibility surfaces and inspect:
- nested radii/edges;
- icon/text optical alignment;
- repeated spacing drift;
- media crop/fallback/geometry;
- focus rings and shadows clipped by overflow;
- state changes that accidentally shift layout.

## Copy pass

For writing-heavy or substantially redesigned surfaces, read `writing.md` and re-read the changed visible strings in context. Verify grammar, referents, terminology, CTA intent, factual precision, error/recovery language, and alignment between copy promise and actual behavior.

## Subtraction pass

Remove things whose purpose cannot be explained:
- decorative borders/shadows;
- filler copy;
- motion with no behavioral job;
- redundant color roles;
- wrappers that create dead space;
- duplicate controls/headings;
- bespoke primitives that duplicate a healthy project component without need;
- decorative marketing metadata/status/precision that implies meaning it does not have.

## Regression checks

- product behavior still works;
- prompt invariants remain intact;
- no new accessibility failure;
- no new overflow/layout shift;
- no new anti-slop smell introduced;
- performance feel has not visibly degraded;
- actual library APIs are respected;
- project memory was not polluted with unproven inferred rules;
- redesign preservation contracts remain intact or have an explicit migration;
- proof/copy does not invent factual credibility.

## Stop rule

After the first implementation:
1. one broad repair pass is allowed for meaningful issues;
2. one targeted final repair is allowed;
3. then stop and surface remaining structural/tradeoff issues.

Do not keep redesigning because subjective improvements are always possible.

## Verification status

Use one of:
- **Verified:** rendered and exercised sufficiently for the claim.
- **Partially verified:** code/tests plus limited visual/interaction access.
- **Provisional:** source-level implementation only; visual environment unavailable.
