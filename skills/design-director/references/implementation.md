# Implementation discipline

Design quality includes using the project's real system correctly. Do not invent a parallel component/API universe because it is easy for the model to write plausible code.

## Inspect existing system

Before introducing new primitives, find:
- global styles/tokens/theme;
- component library and shared primitives;
- registry/MCP/design-system tooling when present;
- typography loading;
- theme/dark mode;
- layout shells;
- icons/images;
- route conventions;
- data/state patterns;
- storybook/examples/tests/demos that reveal real APIs.

When making design-system claims, read `design-evidence.md`.

## Dependency verification

Before importing or recommending a third-party package:

1. inspect the actual dependency manifest/lockfile and framework version;
2. confirm whether the dependency already exists;
3. if absent, decide whether adding it is justified by the task rather than convenience;
4. verify the current package/API/import path from project types/source/registry or current documentation when available;
5. state/install the dependency deliberately rather than writing code that assumes it is present.

Do not silently introduce a second design/component/animation system just to implement one visual idea.

## Reuse-first protocol

Before creating a component/interaction from scratch:

1. **Find** — does the project already have a primitive or component for this job?
2. **Read** — inspect its actual current source/API/types/examples rather than relying on model memory.
3. **Validate** — confirm planned props, composition, states, and required behavior exist.
4. **Adapt** — compose/extend the primitive using the project's established patterns.
5. **Invent only for a real gap** — hand-roll new behavior when the existing system cannot express the requirement cleanly.

This is especially important for complex primitives such as dialogs, comboboxes, calendars, data grids, trees, sortable/drag interactions, command palettes, and virtualized collections.

A visually correct approximation with broken semantics/focus/keyboard behavior is not a successful implementation.

## Live registry/API truth

If the project exposes a live component registry, MCP, package documentation, type definitions, or installed source:

- treat the live/current API as authoritative;
- do not invent props/variants from remembered versions;
- retrieve real examples when composition is non-trivial;
- validate usage before writing large amounts of code when tooling supports it.

Model memory is fallback context, not current API truth.

## Design-system coherence

Prefer one coherent component/design-system language per interaction surface. Multiple systems can coexist during migrations, embedded ecosystems, or deliberate interoperability, but the boundary should be explicit.

Do not mix systems merely because different libraries have attractive individual components. Mixing can create incompatible tokens, focus behavior, density, theming, and semantics even when screenshots look fine.

## Prefer semantic reuse

Reuse healthy primitives. Extend them when the new requirement introduces a genuine new role. Do not create wrappers/components solely to hide one-off styling or to rename an existing primitive without product value.

Do not force reuse of a broken primitive merely to avoid new code; repair the shared abstraction when the requirement is genuinely shared.

## Component contracts

For touched interactive components, read `component-contracts.md` and implement applicable contract obligations: semantics, states, focus/keyboard, geometry, responsive adaptation, recovery, and API truth.

Do not leave state designs only in comments.

## High-frequency interaction data

Pointer position, scroll progress, drag physics, gesture progress, and other frame-by-frame values should not cause avoidable full-tree re-renders.

When the framework/library provides motion values, signals, animation timelines, observers, refs, or imperative animation primitives, prefer those for high-frequency values and keep ordinary application state for semantic state that the UI actually needs to render.

In React-like systems, repeatedly calling component state setters on every scroll/pointer frame is a performance smell unless the affected render is intentionally tiny and measured. Isolate highly interactive/motion-heavy behavior into the smallest practical client/interactive leaf.

Any listener/effect/observer/animation setup must have lifecycle cleanup when the platform requires it.

## Tokens

Use semantic tokens for repeated design roles. Avoid scattering magic values during system-level work, but do not over-tokenize one-off art direction.

Tokenize proven intent after the desired system is stable; do not freeze a bad design into abstractions.

## Accessibility stays in the implementation

Keep native semantics, labels, focus, keyboard behavior, live-region/state communication, reduced-motion, and accessible names appropriate to the product.

Prefer native elements/semantics before adding ARIA. ARIA repairs semantics; it does not make a generic `div` implementation automatically correct.

## Real states in code

Implement and, when possible, expose test/demo paths for applicable:
- empty;
- loading/in-flight;
- error/recovery;
- success/confirmation;
- disabled/read-only;
- selected/current;
- overflow/truncation;
- slow/no network or large-data behavior where relevant.

Preserve geometry during async state changes when possible so controls/content do not jump without purpose.

## Responsive behavior

Encode actual recomposition: order, disclosure, density, control placement, navigation model, table behavior, container adaptation, safe areas, and input mode.

The responsive solution may change the interaction primitive (for example Dialog → Drawer) while preserving the same task/data/semantics. Read `responsive.md`.

Avoid brittle fixed widths.

## Assets

Use real product assets where available. Verify paths/loading and avoid placeholder imagery left in a shippable result.

Reserve media geometry before load when possible and validate crop/fallback/alt behavior. Read `micro-craft.md` for media polish.

If a visual is presented as **product proof**, prefer a real screenshot/artifact or an actual executable preview. Generated/editorial visuals are valid art direction, but do not present them as factual product evidence without labeling.

## Performance

Match visual ambition to target hardware/framework. Optimize obviously expensive media/effects and large collection behavior.

Do not sacrifice task quality merely to maximize a synthetic score, but do not ignore obvious jank, layout shift, oversized media, or unnecessary client work.

## Change safety

After edits:
- run relevant format/lint/typecheck/test/build;
- inspect diffs for unrelated changes;
- verify imports/props against the actual installed API;
- confirm new third-party imports exist in the dependency graph or are intentionally added;
- exercise the affected component contract;
- inspect rendered wide/narrow states when possible;
- confirm high-frequency interaction code does not create avoidable render churn;
- confirm listeners/effects/observers are cleaned up where required.
