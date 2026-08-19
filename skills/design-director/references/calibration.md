# Calibration: heuristics are not laws

This file prevents design prompts from turning useful patterns into pseudo-scientific universal rules.

## Keep as strong defaults

- diagnose before treating;
- composition from user work pattern;
- exact prompt invariants and domain-native artifacts;
- semantic color roles and non-color cues;
- visible focus and keyboard paths;
- real state coverage;
- responsive recomposition and input-mode awareness;
- reduced-motion support;
- visual verification and truthful completion;
- realistic edge data;
- anti-slop detection by clusters rather than banned components.

## Use contextually

### OKLCH
Excellent for authoring new web palettes because of perceptual properties and modern support. Do not migrate an existing healthy palette solely to use it.

### 44–48px touch targets
A strong ergonomic aim for many touch interfaces. It is not the exact WCAG 2.2 AA minimum. WCAG 2.2 SC 2.5.8 uses 24×24 CSS px with exceptions. Design above the floor when context allows.

### 60–30–10 color balance
A composition heuristic, not a requirement. Semantic and brand roles matter more than percentages.

### 60–76ch or similar body measures
Useful starting region for some long-form Latin text, not a universal rule for all languages, typefaces, densities, or product UI.

### Scale ratios
Useful for establishing hierarchy, but no fixed ratio should override rendered optical judgment or available space.

### 3-level text hierarchy
Hook/support/detail can be a helpful pattern, but content may need two, four, or more roles. Avoid flattening semantic hierarchy to satisfy a number.

### Spacing scales
Use a small coherent token scale. Do not force a universal `1-4-9` multiple rule across all projects.

### Visual mass
Balance size, contrast, position, whitespace, and motion qualitatively. Do not use a fake numeric equilibrium score.

### "Cliffhanger" section reveal
Can help narrative scroll continuity, but should not be universal or use fixed pixel exposure.

### Motion timing/springs
Tune from interaction, distance, urgency, visual weight, device performance, and product register. Do not hardcode one tension/damping model or three-beat overshoot everywhere.

### Stagger
Use only where sequence improves comprehension. Deterministic clean timing is preferable to random jitter inserted to seem "human."

### Transform/opacity
Prefer for frequent high-performance animation, but do not ban every other CSS property when a tested alternative is appropriate.

### Button press scale
Optional tactile cue, not a mandatory 0.97–0.98 rule.

### One primary action
Aim for one dominant action per decision context. Complex products can legitimately contain multiple local primary actions across independent regions.

### Motion settings UI
Always honor OS/browser reduced-motion preference. A custom No/Reduced/Standard/Enhanced slider is optional, not a baseline requirement.

### Punctuation bans
No blanket ban on em dashes, exclamation marks, or title case. Use voice and clarity appropriate to the brand/product.

## Reject as universal mechanisms

- reading-distance equations that produce exact web font sizes;
- random animation jitter to hide "robotic" timing;
- numeric composition mass calculators;
- mandatory fixed viewport lists for every project;
- forcing animation into a motion pass when stillness is better;
- fabricating an interface when an explicit audit is run on an empty project;
- generating multiple diagnostic reports as a prerequisite for every fix.
