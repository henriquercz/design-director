# Accessibility baseline

Accessibility is part of design quality, not a late compliance garnish.

## Semantics

Use native elements and landmarks where they express the behavior. Do not simulate buttons/links/forms with generic elements unless a real constraint demands it and full semantics are restored.

## Keyboard and focus

- all core actions reachable without pointer-only gestures;
- visible, consistent focus indication;
- sensible tab order;
- no keyboard traps;
- focus moves/restores intentionally around dialogs, route changes, errors, and dynamic content.

## Target size

WCAG 2.2 AA Success Criterion 2.5.8 defines a 24×24 CSS px minimum target rule with exceptions including sufficient spacing. For touch comfort, larger targets around 44–48 CSS px are often desirable. Treat these as different concepts: compliance floor vs ergonomic design target.

## Contrast and non-color cues

Use defensible text/component contrast. Never make hue the only carrier of status or instruction. Support with label, shape, icon, position, pattern, or other cues.

## Forms

- persistent labels;
- programmatic associations;
- specific errors and recovery;
- preserve entered data on failure where possible;
- group related controls semantically;
- do not suppress mobile zoom to avoid layout issues.

## Motion

Honor `prefers-reduced-motion`. Replace or remove non-essential panning/scaling/large movement while preserving state and progress information.

## Images and media

Use useful alternative text for informative images; empty alt for genuinely decorative imagery when appropriate. Captions/transcripts belong where the content requires them.

## Responsive access

Check zoom/reflow, narrow layouts, input mode, safe areas, text expansion, and RTL/localization requirements.

## Evidence

Never mark accessibility healthy from appearance alone. Perform the checks the environment supports and mark the rest unverified.

## Standards note

Standards evolve. If the user asks for formal conformance or a legal claim, verify the current applicable WCAG/platform requirements rather than relying only on this skill.
