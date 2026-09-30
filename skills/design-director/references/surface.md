# Product surface hardening

Use `surface` for apps, dashboards, admin panels, editors, operations tools, and repeated-use interfaces.

## Product is an instrument

Distinctiveness should not slow routine work. Optimize for fast scanning, stable semantics, density appropriate to expertise, clear state, predictable control placement, and recovery.

## Real-data bar

Test with realistic extremes:
- long identifiers/names;
- zero, one, many, huge counts;
- missing/partial data;
- stale/fresh/live states;
- permission limitations;
- slow/no network;
- selection and bulk actions;
- concurrent or conflict states when relevant.

## Density

Dense is not automatically cluttered; sparse is not automatically clear. Choose density from frequency, expertise, comparison needs, display size, and consequences of missed information.

## Spacing is the density instrument

Spacing, not card count, is how a product surface expresses density. Before adding or removing a container, decide the spacing budget.

Tighten when: the user compares many values, scans a repeated row, or works in a fixed viewport for long stretches. Widen when: content is read once, decisions are consequential, or the user is unfamiliar with the surface.

Prefer, in order:
- consistent rhythm from a small token scale rather than one-off values;
- space that separates by relationship (group, sequence, scope), not space that decorates;
- alignment and dividers for grouping before extra padding;
- whitespace around a region to signal "this is done" rather than inside it to inflate it.

A dashboard usually needs fewer containers and better spacing than it has. Nesting a card inside a card inside a padded panel to create hierarchy inverts the rule: use one surface, spacing, and type weight. Marketing-page spacing habits — large empty hero bands, one-section-per-screen — make product UI slower to scan, not more premium.

## State and command placement

Keep actions near objects and feedback near actions. Preserve user context after filters, sorts, selection, refreshes, dialogs, and errors.

## Tables/lists

Protect alignment when comparison matters. Support sort/filter/search, stable headers/context, selected/hover/focus states, overflow, and keyboard paths where relevant.

## Empty/loading/error

These are core product states. They should teach, preserve work, explain progress, or offer recovery—not simply display decoration.

## Not a landing page

Product surfaces do not import marketing grammar. Marketing optimizes for a first impression that persuades; a tool optimizes for the two hundredth use. A landing page's centered hero, oversized display type, decorative section numbering, scroll-reveal choreography, and marketing proof blocks are usually wrong here — they cost scanning speed and imply a visitor who is not the actual user.

Keep for product: real navigation and wayfinding, dense but organized information, tables and lists that support comparison, visible state, restrained motion, and copy that prioritizes clarity.

## Product motion

Use restrained motion for feedback, continuity, state change, and direct manipulation. Routine operations should not become performances.

## Surface bar

A hardened surface remains usable under real data, non-happy states, keyboard/touch, narrow/wide layouts, and repeated use. It should feel faster and more trustworthy after the pass, not merely prettier.
