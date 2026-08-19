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

## State and command placement

Keep actions near objects and feedback near actions. Preserve user context after filters, sorts, selection, refreshes, dialogs, and errors.

## Tables/lists

Protect alignment when comparison matters. Support sort/filter/search, stable headers/context, selected/hover/focus states, overflow, and keyboard paths where relevant.

## Empty/loading/error

These are core product states. They should teach, preserve work, explain progress, or offer recovery—not simply display decoration.

## Product motion

Use restrained motion for feedback, continuity, state change, and direct manipulation. Routine operations should not become performances.

## Surface bar

A hardened surface remains usable under real data, non-happy states, keyboard/touch, narrow/wide layouts, and repeated use. It should feel faster and more trustworthy after the pass, not merely prettier.
