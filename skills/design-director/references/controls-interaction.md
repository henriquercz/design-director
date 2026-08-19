# Controls and interaction

Interaction design is behavior under pressure: pointer, touch, keyboard, typing, waiting, errors, recovery, selection, and overflow.

## Control lifecycle

For each control/system, cover applicable states:
- idle;
- hover (when hover exists);
- active/pressed;
- focus-visible;
- selected/current;
- disabled/read-only;
- loading/in-flight;
- success/confirmation;
- error/recovery;
- empty/no-result;
- overflow/truncation.

Do not force irrelevant states onto every primitive, but do not design only the resting state.

## Button hierarchy

Use a consistent hierarchy: primary, secondary, tertiary/quiet, and danger where needed.

Prefer one **dominant** action per decision context, not a universal rule that an entire complex dashboard can have only one primary-looking control anywhere.

Button labels should name the action and object when useful. Avoid vague labels when a specific verb is available.

## Hit targets

Design comfortable targets for the device/context. Aim around 44–48 CSS px for common touch actions when practical, while understanding that WCAG 2.2 AA Target Size (Minimum) is 24×24 CSS px with listed exceptions. Spacing and alternative controls matter too.

## Focus and keyboard

- preserve logical tab order;
- show focus clearly;
- do not trap keyboard users;
- return focus sensibly after closing overlays;
- provide keyboard alternatives for drag-only interactions;
- expose shortcuts only when they do not steal normal typing/navigation.

## Destructive actions

Prefer reversible operations and undo when appropriate. Require confirmation when consequences are difficult/irreversible, financial, legal, bulk, or otherwise high-risk. Name the object/consequence clearly.

## Loading

Keep the action anchored and prevent accidental duplicate submission. Preserve footprint to avoid layout jumps. Show progress when genuinely measurable. Routine waits do not need theatrical animation.

Avoid gimmicks such as button-width "breathing" merely to look alive.

## Overlays

Dialogs, menus, popovers, and tooltips need:
- correct trigger relationship;
- focus management;
- escape/close behavior;
- outside-interaction behavior appropriate to the control;
- collision/viewport handling;
- restore-focus behavior.

## Forms

Labels remain available; placeholder text is not the sole label. Errors explain recovery and preserve user input where possible.

On iOS Safari, form controls with rendered font sizes below 16px can trigger viewport zoom on focus; use at least 16px on narrow screens where this behavior is relevant rather than disabling user zoom.
