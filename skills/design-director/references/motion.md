# Motion

Motion is body language and causal explanation, not a requirement to animate everything. Before choosing duration/easing, decide whether movement improves the task at all.

## Motion decision matrix

Evaluate five dimensions before adding or expanding motion:

### 1. Purpose
Use motion when it clarifies one or more:
- causality: where something came from / returns to;
- state change;
- continuity through navigation, reordering, expansion, or direct manipulation;
- hierarchy or focus shift;
- feedback that confirms contact/result;
- progress/completion;
- rare delight on a moment that already carries emotional value.

If no motion makes the interaction clearer or more meaningful, stillness is valid.

### 2. Frequency
Frequency changes the motion budget.

- **Rare:** onboarding milestone, meaningful completion, one-time reveal can afford more expression.
- **Occasional:** modal/open-detail/navigation transitions should remain concise and interruptible.
- **Routine:** dropdowns, accordions, toggles, repeated actions should resolve quickly.
- **High-frequency:** command palettes, keyboard navigation, dense operator workflows should spend near-zero perceived time on decorative motion.

Repeated motion that the user must wait through is latency, not polish.

### 3. Input
- passive/state-driven changes can use subtle continuity;
- pointer/touch feedback should feel attached to the action;
- direct manipulation should preserve physical continuity and may benefit from spring-like response;
- repeated keyboard navigation should not be delayed by decorative flourish.

Motion may still communicate selection during keyboard use, but it must remain effectively immediate and never make navigation feel queued.

### 4. Spatial change
The larger/farther the visual change, the more continuity can help:
- local control;
- overlay/popover;
- panel/route transition;
- large scene or brand moment.

Small controls generally resolve faster than large scene changes.

### 5. Cost
Check:
- attention/distraction;
- perceived latency;
- paint/composite cost and target hardware;
- vestibular/accessibility risk;
- whether the animation blocks input or obscures state.

## Origin and causality

When an element emerges from a trigger or spatial source, its transform/origin/path should preserve that relationship when useful. A popover that appears from its trigger usually reads more naturally than one that scales from an unrelated center point.

Use this principle for menus, popovers, expanded cards, context surfaces, drawers, shared elements, and drag/drop feedback where the source/target relationship matters.

## Interruptibility

Reversible interactions should reverse gracefully when the user changes intent before motion finishes.

Check hover, accordion, drawer, popover, selection, route-like transitions, and toggles for:
- no queued animation backlog;
- no jump to a stale intermediate state;
- smooth reversal toward the new target;
- input remains available unless the operation truly must lock.

## Register

Product motion should usually be fast, interruptible, and subordinate to task flow. Brand motion can be more expressive when it supports story, recognition, or evidence without harming performance/access.

## Timing and easing

Choose duration/easing from purpose, frequency, distance, visual weight, urgency, and interaction type. Do not hardcode one universal timing system.

Useful tendencies, not laws:
- tiny local feedback often resolves around ~100–150ms;
- routine UI transitions often live around ~150–250ms;
- larger overlays/scene changes often live around ~200–300ms;
- high-frequency navigation may need near-instant visual response.

Easing tendencies:
- entering/leaving from outside a scene often benefits from deceleration / ease-out-like behavior;
- an object already on-screen moving between positions can benefit from ease-in-out-like continuity;
- constant continuous movement is usually linear;
- spring behavior can be excellent for physical/direct manipulation when tuned to the product, but spring is not a default badge of modernity.

Exits can often be faster than entrances because the user has already decided to leave.

## Properties and performance

Prefer compositor-friendly `transform` and `opacity` for frequent motion. Other properties (`clip-path`, grid/size transitions, filters, etc.) are allowed when tested and materially beneficial.

Avoid layout-thrashing animation by default. Avoid paint-heavy blur/shadow animation on large surfaces unless verified on target hardware.

Use explicit transition properties rather than `transition: all` by reflex.

## Reduced motion

Honor `prefers-reduced-motion`. Reduced mode should preserve state meaning while removing/replacing non-essential movement or vestibular motion.

A custom motion preference UI can be useful in motion-heavy products, but it is not mandatory for every site.

Essential content/state must never depend on an entrance animation successfully firing.

## Press / hover

Subtle scale feedback can work, but do not mandate one scale ratio on every control. Use color, surface, border, transform, icon movement, or another cue that fits the product's physical language.

Hover affordances must not gate functionality that touch/keyboard users need.

## Loading

Choose coherent loading behavior based on the task: spinner, determinate progress, skeleton, reserved-space state, optimistic update, etc.

Motion should reassure and communicate real state. Do not imply fake progress or make routine waits theatrical.

## Motion review

For meaningful custom motion, when tooling permits:
1. inspect at normal speed for perceived quality and latency;
2. inspect one slow-motion pass (for example browser/OS tooling around ~10–25% speed) to reveal origin, clipping, stagger, reversal, and timing defects;
3. restore normal speed and judge the real user experience.

Slow motion is a diagnostic tool, not the target experience.

## Verification

Motion work is complete only if:
- the behavior is reachable/visible in the rendered UI;
- it has a named purpose or is intentionally absent;
- high-frequency actions remain effectively immediate;
- origin/continuity make sense where spatial causality matters;
- reversible interactions are interruptible enough for the product;
- nothing delays task flow without a reason;
- reduced-motion behavior preserves meaning;
- target devices remain smooth enough for the product's requirements.
