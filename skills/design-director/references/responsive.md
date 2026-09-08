# Responsive, adaptive, and international layout

Responsive design is recomposition across constraints, not merely shrinking desktop.

## Test from content, not device labels

Use breakpoints where content/layout begins to fail. Include representative narrow, medium, wide, and edge widths relevant to the project rather than blindly requiring one universal viewport gauntlet.

Container size can matter more than viewport size for reusable components.

## Recompose

Ask what changes under tighter or different constraints:
- order;
- grouping;
- disclosure;
- control placement;
- table/list strategy;
- navigation model;
- action reach;
- information density;
- interaction primitive.

Preserve capability whenever possible. If a feature truly cannot exist in a context, explain the product constraint instead of hiding it casually.

## Responsive primitive adaptation

The same user task may legitimately use a different interaction primitive across contexts.

Examples, when the job/evidence supports them:
- centered Dialog → bottom/side Drawer or Sheet on narrow touch screens;
- anchored Popover → reachable Sheet when viewport/keyboard constraints make anchoring brittle;
- persistent two-pane inspector → drill-in/detail route with a clear return path;
- dense toolbar → grouped reachable action bar / overflow command surface;
- wide comparison table → priority columns + preserved horizontal comparison or summary + drill-down.

The data, semantics, action consequences, and current state should remain consistent across the adaptation. Do not create two unrelated product experiences for desktop and mobile.

## Input modes

Use media features such as `pointer` and `hover` where useful. Never put essential functionality behind hover.

Touch can require larger targets/reachable actions; keyboard can require stable focus/shortcuts; pointer can use hover affordances. Input mode is a design constraint, not merely a CSS detail.

## Containers

Reusable components should adapt to the space they actually receive. Container queries can be preferable when the same component appears in sidebar/main/split contexts.

Do not assume viewport breakpoints solve nested component constraints.

## Dynamic viewport height

Mobile browser chrome, virtual keyboards, and installed-app contexts can make classic `100vh` behave differently from the actually visible area.

For full-height heroes, sheets, onboarding panels, or edge-to-edge surfaces where this matters:
- consider modern dynamic/small viewport units (`dvh`, `svh`, etc.) or a platform-specific measured strategy;
- choose the unit based on whether the surface should track the currently visible viewport or remain stable to a smaller safe viewport;
- test browser chrome expansion/collapse and orientation changes;
- do not turn `100dvh` into a universal replacement for every `vh` usage.

A full-height visual should not hide a primary action behind browser chrome merely because desktop viewport math looked correct.

## Safe areas and virtual keyboards

Support notches/home indicators where edge-to-edge layouts or fixed actions require it via `env(safe-area-inset-*)` and appropriate viewport configuration.

Check fixed/sticky controls and dialogs against mobile virtual keyboards; the commit action must not become unreachable.

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
- stacked row details only when cross-row comparison is no longer primary;
- split view;
- alternative summary + drill-down.

Do not convert every table to isolated cards if comparison alignment is the user job.

## Edge data

Test long strings, empty values, huge lists, narrow cells, translations, numbers, timestamps, slow/no network states, sticky controls, overlays near viewport edges, browser chrome changes, and virtual-keyboard intrusion where relevant.
