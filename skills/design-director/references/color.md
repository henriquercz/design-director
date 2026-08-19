# Color system

Color carries atmosphere, hierarchy, status, and action. A palette is a role system, not a collection of attractive swatches.

## Decide emotional arc first

Think about:
- arrival: what should be felt before reading;
- decision/action: where signal must peak;
- completion: how progress or relief is confirmed;
- risk: how danger/uncertainty appears;
- rest: where the eye can stop working.

## Commitment strategies

Use as descriptive options, not rigid formulas:
- **Whisper:** mostly neutral surface, rare meaningful accent; common in product UI.
- **Statement:** one authored hue owns substantial visual territory.
- **Conversation:** several named semantic/brand roles.
- **Flood:** color itself becomes a section/hero environment; usually brand-led.

Do not enforce 60/30/10 percentages. Balance is contextual.

## Semantic roles

At minimum when relevant:
- canvas/background;
- elevated/sunken surfaces;
- primary/secondary text;
- muted text;
- borders/dividers;
- primary/secondary actions;
- focus;
- selection;
- success/warning/error/info;
- disabled;
- domain-specific status/category colors.

## Color space

For a new web palette, OKLCH is a strong choice for authored perceptual lightness/chroma relationships when project support allows it. Preserve an existing healthy token system rather than converting color space for fashion.

Control chroma near very light/dark extremes. Slightly tinted neutrals can create cohesion when appropriate.

## Grayscale / non-color test

The hierarchy must still work when hue information is removed. Do not encode status by red/green alone; add text, icon, shape, pattern, position, or another cue.

## Dark mode

Treat dark mode as a designed theme, not inversion:
- depth often comes from surface lightness differences;
- accents may need reduced chroma;
- borders and text need authored values;
- shadows may play a smaller role.

## Domain default trap

Do not choose navy because it is finance/legal, terminal black because it is developer tooling, or teal because it is health. The brief and evidence should justify the palette.

## Recolor bar

A recolor pass must define and apply semantic roles across real components and edge states. An accent swap alone is not a system pass unless explicitly scoped.
