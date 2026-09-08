# Creation and redesign

## Before asking anything

Read the project, existing routes/components/assets, project memory, prompt, and relevant evidence. If enough is known to identify goal, user, core artifact, constraints, and outcome, build. Style uncertainty is a design decision, not automatically a question.

When reverse-engineering an existing system/reference, read `design-evidence.md` before turning observations into project rules.

## Build layers

A useful order:
1. semantic structure and information architecture;
2. composition and spacing;
3. type/color/surface system;
4. component contracts, states, and interaction;
5. responsive/container behavior;
6. purposeful motion;
7. micro-craft;
8. visual/behavior verification and repair.

Do not treat this as a waterfall. If iteration reveals a structural issue, return to the earlier layer that caused it.

## Realistic content

Use real data if available. Otherwise use realistic extremes rather than `John Doe` / `Lorem ipsum`. Long content reveals design failures.

Do not invent precise metrics/specifications as decoration. If numbers are mock/sample content, label them accordingly rather than letting visual polish imply factual evidence.

## New surface bar

A build should include:
- prompt invariants;
- task-derived composition;
- real/realistic content;
- primary path;
- applicable component contracts and non-happy states;
- relevant responsive behavior;
- accessible semantics;
- verified implementation.

A happy-path screenshot alone fails the bar.

## Contrastive exploration

When the direction is materially ambiguous and choosing wrong would cause meaningful rework, explore 2–3 alternatives that differ along **one primary axis at a time**.

Useful axes:
- **Structure** — order, columns, grouping, text/evidence relationship;
- **Density** — compact/operator vs spacious/editorial;
- **Emphasis** — what dominates/recedes;
- **Type** — typographic voice/hierarchy posture;
- **Voice** — copy/art-direction posture.

Do not present cosmetic color swaps as three design directions. The purpose is to learn which premise is strongest, not to multiply options.

Once a direction wins, converge. Do not keep multiple competing systems alive in implementation.

For small/local requests, skip variant exploration and make the strongest decision directly.

## Redesign vs relayout

### Relayout
Content and identity are largely right; spatial organization is wrong.

### Redesign
The product should feel like a different visual system while preserving its job. Change the spatial premise plus the necessary type/color/depth/component/motion language.

A redesign that merely repaints the old layout is not a redesign.

## Preserve vs overhaul

For an existing interface, decide the redesign posture before changing structure:

- **Preserve / targeted evolution:** brand, information architecture, content, and core behavior remain recognizable; repair the visual/system debt with the smallest risk.
- **Overhaul:** a new visual world is explicitly desired, but product truth and preservation contracts still remain unless the user expands scope.

Do not interpret "make it look completely different" as permission to silently change URLs, analytics, legal language, data semantics, or form contracts.

## Redesign preservation envelope

Before substantial redesign work, inspect and preserve these unless the user explicitly requests a change or the project requirement proves one is necessary:

- **URL structure / route slugs** and deep-link behavior;
- **anchor IDs / fragment targets** used by links, docs, campaigns, or accessibility navigation;
- **information architecture** and primary navigation labels when the task is visual modernization rather than IA redesign;
- **SEO baseline:** titles/descriptions, canonical behavior, indexability, structured data, important internal links, social/OG metadata, and ranking-critical content obligations where applicable;
- **analytics/telemetry contracts:** event names, data attributes, tracking IDs, experiment hooks, conversion events, and meaningful section/control identifiers;
- **form contracts:** field names, autocomplete semantics, data binding, validation obligations, and submission behavior; preserve field order when changing it would affect task flow, autofill, analytics, compliance, or integration;
- **legal / consent / cookie / disclosure copy** and acceptance mechanics;
- **brand logo/wordmark** and protected brand assets unless rebranding is in scope;
- **existing accessibility wins:** semantic headings/landmarks, labels, alt text, focus order, keyboard behavior, announcements, contrast fixes, reduced-motion behavior;
- **public API/data semantics** consumed by the page or downstream systems.

If one of these must change, call out the migration impact instead of treating it as a cosmetic edit.

## Modernization risk ladder

For preserve-style redesigns, prefer the lowest-risk lever that solves the real problem:

1. typography/hierarchy and copy clarity;
2. spacing/rhythm and composition cleanup;
3. color/depth/edge recalibration inside brand constraints;
4. component/state/interaction hardening;
5. purposeful motion and responsive adaptation;
6. hero/key-section recomposition;
7. full block replacement;
8. information-architecture or route changes only when explicitly in scope.

This is a risk ladder, not a mandatory sequence. Structural problems should still be fixed at their actual layer.

## Visual-world reset

For redesign, articulate:
- new spatial premise;
- new focal/evidence strategy;
- new type voice;
- new color commitment;
- new edge/depth language;
- component/control language;
- motion posture;
- responsive interaction posture;
- what remains invariant from the product.

## Reuse without inheriting bad direction

Preserve healthy implementation primitives/APIs even when visual direction changes. Redesign does not require throwing away accessible components or data/state behavior.

Conversely, do not preserve a shared primitive whose API/behavior is the cause of the design failure merely because it is shared. Repair the abstraction when the problem is systemic.

## Complexity matches ambition

Maximal art direction requires code/asset/performance investment. Minimal work requires precision in type, space, content, interaction, and craft.

Do not promise spectacle with trivial implementation or call unconsidered emptiness minimalism.
