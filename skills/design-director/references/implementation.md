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

## Prefer semantic reuse

Reuse healthy primitives. Extend them when the new requirement introduces a genuine new role. Do not create wrappers/components solely to hide one-off styling or to rename an existing primitive without product value.

Do not force reuse of a broken primitive merely to avoid new code; repair the shared abstraction when the requirement is genuinely shared.

## Component contracts

For touched interactive components, read `component-contracts.md` and implement applicable contract obligations: semantics, states, focus/keyboard, geometry, responsive adaptation, recovery, and API truth.

Do not leave state designs only in comments.

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

## Performance

Match visual ambition to target hardware/framework. Optimize obviously expensive media/effects and large collection behavior.

Do not sacrifice task quality merely to maximize a synthetic score, but do not ignore obvious jank, layout shift, oversized media, or unnecessary client work.

## Change safety

After edits:
- run relevant format/lint/typecheck/test/build;
- inspect diffs for unrelated changes;
- verify imports/props against the actual installed API;
- exercise the affected component contract;
- inspect rendered wide/narrow states when possible.
