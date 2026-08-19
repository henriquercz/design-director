# Motion

Motion is body language and causal explanation, not a requirement to animate everything.

## Jobs for motion

Use motion when it clarifies:
- where an element came from / returns to;
- state change;
- hierarchy or focus shift;
- continuity through navigation/reordering;
- direct-manipulation feedback;
- progress or completion.

If no motion makes the interaction clearer, stillness is a valid design decision.

## Register

Product motion should usually be fast, interruptible, and subordinate to task flow. Brand motion can be more expressive when it supports the story and performance/access remain good.

## Timing

Choose duration/easing from distance, mass/visual weight, urgency, and interaction type. Small controls should generally resolve faster than large scene changes. Exits often benefit from being quicker than entrances.

Do not hardcode universal spring tension, damping, three-beat overshoot, or random jitter as a house rule.

## Properties

Prefer compositor-friendly `transform` and `opacity` for frequent motion. Other properties such as `filter`, `clip-path`, grid or size transitions may be valid when tested and when they materially improve the interaction. Avoid layout-thrashing animation by default.

## Reduced motion

Honor the platform's `prefers-reduced-motion` preference. Reduced mode should preserve state meaning while removing/replacing vestibular or non-essential movement.

A custom motion preference UI can be useful in motion-heavy products, but it is not mandatory for every site.

## Press / hover

Subtle scale feedback can work, but do not mandate `0.97–0.98` on every button. Use color, surface, border, transform, or another cue that fits the physical language.

## Loading

Choose one coherent loading behavior per context: spinner, progress, skeleton, reserved-space transition, etc. Motion should reassure, not imply fake progress or make waiting feel longer.

## Verification

Motion work is complete only if:
- the behavior is reachable/visible in the rendered UI;
- it improves causality or feedback;
- it does not delay task flow;
- reduced-motion behavior preserves meaning;
- target devices remain smooth enough for the product's requirements.
