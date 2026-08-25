# Component contracts

A component is not complete because its resting screenshot looks right. Each primitive owes a contract across semantics, state, interaction, geometry, responsive behavior, accessibility, failure/recovery, and integration with the project's real component system.

Load this reference when creating, redesigning, hardening, or reviewing interactive component families.

## Contract template

For a touched component, ask only what applies:

1. **Purpose and semantics** — what role does it play and what native/accessible primitive best represents it?
2. **Trigger / entry** — how is it reached by pointer, touch, keyboard, programmatic state, or route?
3. **States** — resting, hover, pressed, focus, selected, disabled/read-only, loading, error, success, empty, overflow as relevant.
4. **Geometry** — size, hit area, content growth, long data, loading footprint, collision, scroll.
5. **Keyboard / focus** — navigation model, focus entry, trap/roving behavior if required, escape, restore focus.
6. **Responsive adaptation** — does the same task need a different primitive/layout under another constraint?
7. **Feedback / recovery** — confirmation, errors, undo, retry, preservation of user input/state.
8. **API truth** — are props/composition based on the current project/library API rather than model memory?

Do not force irrelevant states onto every primitive; do not omit an applicable obligation merely because the default state looks polished.

## Buttons and action controls

- one dominant action per decision context when appropriate;
- labels describe the action/object when useful;
- preserve footprint during loading to avoid layout jump;
- prevent accidental duplicate submission;
- disabled/read-only communicate truthfully;
- destructive actions expose consequence/recovery;
- icon-only controls have accessible names and usable hit areas.

## Fields and forms

- persistent labels; placeholder is supplementary, not the only label;
- description/error association remains programmatically available;
- preserve input after recoverable validation errors;
- use meaningful autocomplete/inputmode where appropriate;
- do not block paste by default;
- distinguish disabled from read-only;
- narrow-screen controls avoid iOS form zoom where applicable.

## Dialog / sheet / drawer

- trigger and accessible name/description are clear;
- focus enters intentionally and is contained when modality requires it;
- Escape/close/outside-interaction behavior matches the primitive;
- closing restores focus sensibly;
- scrolling works with long content and keyboards/virtual keyboards;
- destructive/commit actions remain understandable;
- on constrained screens, the same task may adapt from centered dialog to sheet/drawer if that improves reach/space without changing product semantics.

## Popover / menu / context menu

- preserves a clear spatial relationship to its trigger when that relationship matters;
- handles viewport collision/edge placement;
- keyboard navigation and dismissal follow the primitive's interaction model;
- focus does not disappear behind the overlay;
- selection and current state remain visible.

## Tooltip

- supplements rather than replaces essential visible labels when the action would otherwise be ambiguous;
- appears on keyboard focus as well as pointer hover when relevant;
- initial hover delay can prevent accidental activation;
- when a user is intentionally traversing a tooltip group, subsequent tooltips may become near-instant to avoid repeated waiting;
- positioning handles viewport collision;
- tooltip timing never blocks the underlying action.

## Tabs / segmented view switchers

- selected tab and controlled panel relationship are programmatic and visible;
- keyboard model is intentional; for conventional tabs, Arrow keys and Home/End should work as expected when the chosen primitive/library supports that model;
- focus and selection behavior are not confused;
- responsive collapse/overflow still preserves the active context.

## Accordion / disclosure

- trigger communicates expanded/collapsed state;
- keyboard focus remains stable;
- content remains accessible when motion is reduced/disabled;
- height animation does not make content unreachable or trap focus.

## Toast / transient status

- communicate semantic priority without relying on color alone;
- timeout is appropriate to message/action complexity;
- actionable toasts remain keyboard reachable;
- timeout should pause while the user is interacting/focusing when dismissal would otherwise remove the action;
- stacking does not obscure critical controls;
- undo/retry is preferred when it improves recovery.

## Skeleton / loading placeholder

- approximates the geometry of the content it replaces so loading does not create avoidable layout shift;
- animation is optional and reduced-motion safe;
- do not use skeletons when a reserved blank area/progress/status is more truthful;
- avoid fake progress or decorative shimmer that suggests work unrelated to real state.

## Table / data grid / list / tree

- preserve the user's scanning/comparison job;
- selection, sort, filter, pagination/virtualization, keyboard, sticky context, and overflow are explicit when present;
- screen reader semantics match the actual structure;
- high-volume behavior does not destroy performance;
- do not replace a comparison table with isolated mobile cards if alignment across criteria is still the task.

## Drag / drop / sortable / kanban-like behavior

- use stable object identity;
- communicate draggable/drop targets/state;
- provide a keyboard/non-drag alternative when the operation is essential;
- handle cancel/revert and invalid drops;
- touch targets and scroll interaction remain usable;
- prefer proven project/library primitives for complex manipulation instead of hand-rolling an approximate accessible implementation.

## Media

- reserve geometry before load with known dimensions/aspect ratio where possible;
- choose crop/focal point intentionally;
- provide appropriate fallback/broken-state behavior;
- alternative text follows communicative purpose, not filename;
- responsive sources/density are used when they materially affect quality/performance;
- lazy loading must not hide immediately important visual evidence.

## Reuse before invention

If the project already has a healthy component, registry, library, design-system primitive, or accessible foundation:

1. locate it;
2. read its actual current API/examples;
3. validate planned props/composition;
4. extend/adapt only where the requirement is genuinely new.

Do not hand-roll complex interaction behavior merely because the model can recreate the appearance.

## Verification

A component contract is complete only when applicable obligations are visible in code and, where possible, reachable in the rendered UI. If a state cannot be triggered in the environment, say it is implemented but not fully exercised.
