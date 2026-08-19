# Responsive, adaptive, and international layout

Responsive design is recomposition across constraints, not merely shrinking desktop.

## Test from content, not device labels

Use breakpoints where the content/layout begins to fail. Include representative narrow, medium, wide, and edge widths relevant to the project rather than blindly requiring one universal six-viewport gauntlet.

## Recompose

Ask what changes at smaller containers:
- order;
- grouping;
- disclosure;
- control placement;
- table/list strategy;
- navigation model;
- action reach;
- information density.

Preserve capability whenever possible. If a feature truly cannot exist on a context, explain the product constraint instead of hiding it casually.

## Input modes

Use media features such as `pointer` and `hover` where useful. Never put essential functionality behind hover.

## Containers

Reusable components should adapt to the space they actually receive. Container queries can be preferable when the same component appears in sidebar/main/split contexts.

## Safe areas

Support notches/home indicators where edge-to-edge layouts or fixed actions require it via `env(safe-area-inset-*)` and appropriate viewport configuration.

## Zoom and reflow

Do not disable pinch zoom to solve layout problems. Check reflow/zoom behavior and avoid fixed dimensions that clip essential content.

## iOS form zoom

On iOS Safari, focusing controls below 16px rendered font size may auto-zoom the viewport. Keep `input`, `select`, and `textarea` at 16px or larger on narrow screens where this applies; scale them down at larger breakpoints only if desired.

## Text direction

Use logical properties (`inline-start`, `block-end`, etc.) when the product supports multiple directions. Test real `dir="rtl"` rather than assuming mirrored CSS.

Mirror icons only when direction is semantic (back/forward chevrons). Do not mirror universal symbols or brand marks without reason.

## Tables and dense data

Choose based on the comparison job:
- horizontal scroll with pinned identifiers;
- responsive column priority;
- stacked row details;
- split view;
- alternative summary + drill-down.

Do not convert every table to isolated cards if comparison alignment is the user job.

## Edge data

Test long strings, empty values, huge lists, narrow cells, translations, numbers, timestamps, and slow/no network states.
