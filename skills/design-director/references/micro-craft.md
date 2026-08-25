# Micro-craft and optical polish

Micro-craft is the layer where a coherent design stops feeling assembled and starts feeling intentionally finished. It does not rescue a wrong composition. Use it after structure, hierarchy, and component behavior are sound.

## Optical judgment beats arithmetic

Small visual relationships are often perceived rather than mathematically equal. Correct by rendered appearance while preserving a coherent system.

Examples:
- icons may need optical rather than purely geometric centering;
- text and icon baselines can require slight adjustment;
- nested corners should read concentrically even if exact arithmetic is not visually perfect;
- visual weight may require a quieter divider or stronger local contrast than a token's nominal value.

Do not scatter arbitrary one-off nudges. If the same correction repeats, determine whether it belongs in the primitive/system.

## Nested radii

Inner and outer rounded surfaces should feel physically related. A useful construction is for outer radius to increase with the inset/padding around the inner surface, but this is a heuristic, not a formula.

Avoid:
- unrelated radii nested closely;
- pills inside modest-radius containers without semantic reason;
- different corner languages for equivalent components.

## Spacing as relationship

Spacing communicates grouping before decoration does.

- same semantic relationship should usually share a gap token/rhythm;
- internal component spacing is typically tighter than spacing between independent groups;
- large empty wrappers should not create dead margins merely to look premium;
- balance density against task frequency: operational UI can be compact; brand/editorial surfaces can spend more space.

Use a small coherent scale, not random values. Do not force every project onto one universal 4/8 or 1-4-9 arithmetic.

## Icons

- use one visual family unless a deliberate exception exists;
- match stroke/fill weight to neighboring typography/control density;
- align optically inside hit targets, not only by SVG viewBox math;
- maintain accessible names for icon-only actions;
- direction-encoded icons respond correctly to RTL; universal symbols/brand marks do not mirror blindly.

## Dividers and edges

Use the least boundary necessary to preserve grouping/scanning.

- repeated dense rows can need subtle separators;
- headers/pinned context can need stronger separation;
- spacing may be enough between simple content groups;
- avoid border + heavy shadow + tinted surface all competing for the same containment job.

## Media geometry

- reserve aspect ratio/size before load to reduce layout shift;
- choose crop and object position around the subject/evidence, not arbitrary center-crop;
- verify low-resolution, missing, transparent, dark/light, and portrait/landscape edge cases where relevant;
- use realistic media rather than placeholders in ship-ready surfaces.

## Transitions

Animate only properties that need to change. Prefer explicit transition properties over `transition: all` by reflex.

Use `will-change` sparingly and temporarily where it solves a measured rendering problem; permanent promotion of many elements can waste memory.

Motion timing belongs in `motion.md`; this file only enforces that the visual result remains crisp and consistent.

## Stacking and clipping

Keep z-index/elevation semantic and bounded:
- base content;
- sticky/local overlays;
- menus/popovers;
- modal layer;
- critical global surface when the product truly needs one.

Avoid arbitrary escalating z-index values. Check overflow/clip paths so focus rings, menus, shadows, and dragged objects are not accidentally cut off.

## Text details

- avoid awkward orphaned single words in prominent display text when a natural line break can fix it;
- avoid truncating information the task depends on;
- use tabular numerals when changing numeric width would create jitter;
- align labels, metadata, and control text consistently inside repeated rows.

## State geometry

Hover, selected, loading, error, and focus treatments should not cause accidental layout shift unless movement itself is the intended interaction.

Prefer reserving border/indicator space or using outlines/box-shadows/backgrounds/transforms that preserve geometry when appropriate.

## Craft review

Before calling finish:
- squint: do the intended hierarchy masses still read?
- inspect 1× and high-density rendering when possible;
- scan repeated rows/components for one-off drift;
- inspect nested corners and icon/text alignment;
- ensure media crop/fallbacks are intentional;
- remove tiny decorative details whose job cannot be explained.
