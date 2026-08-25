# Calibration: heuristics are not laws

This file prevents useful design patterns from becoming pseudo-scientific universal rules. Distinguish standards, project contracts, ergonomic targets, observed patterns, and subjective heuristics.

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
- anti-slop detection by clusters rather than banned components;
- use project/live API evidence before model memory;
- screenshot-only evidence must not masquerade as hidden design-system truth.

## Evidence labels are not confidence theater

Use `Normative`, `Observed`, `Inferred`, and `Unknown` only when provenance matters. Do not add labels to every trivial design choice. Their job is to prevent uncertain evidence from becoming permanent project truth.

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
Use a small coherent token scale. A 4/8-derived scale is common and useful, but do not force one arithmetic across every brand/product. Semantic relationship matters more than divisibility.

### Nested radius arithmetic
Outer radius often needs to increase with the inset around an inner rounded surface so corners read concentrically. Treat `outer ≈ inner + inset` as a construction aid, not a mandatory formula.

### Visual mass
Balance size, contrast, position, whitespace, and motion qualitatively. Do not use a fake numeric equilibrium score.

### "Cliffhanger" section reveal
Can help narrative scroll continuity, but should not be universal or use fixed pixel exposure.

### Motion duration ranges
Common UI motion often falls into rough bands such as ~100–150ms for tiny feedback, ~150–250ms for routine transitions, and ~200–300ms for larger overlays/scenes. These are starting regions, not standards. Frequency, distance, input, interruption, visual weight, device performance, and register decide.

### Easing tendencies
Ease-out-like behavior can suit entering/leaving motion; ease-in-out-like behavior can suit objects already moving within the scene; linear suits constant motion; springs can suit physical/direct manipulation. None is a universal default.

### Stagger
Use only where sequence improves comprehension. Deterministic clean timing is preferable to random jitter inserted to seem "human."

### Transform/opacity
Prefer for frequent high-performance animation, but do not ban every other CSS property when a tested alternative is appropriate.

### Button press scale
Optional tactile cue, not a mandatory ratio.

### One primary action
Aim for one dominant action per decision context. Complex products can legitimately contain multiple local primary actions across independent regions.

### Initial tooltip delay
A small delay can reduce accidental hover activation. Subsequent tooltips in an intentional traversal may be near-instant. Tune to device/input and never make keyboard users wait to understand a focused control.

### Dialog → Drawer adaptation
A strong responsive pattern when narrow touch constraints change reach/space while the same task remains intact. It is not mandatory if the original dialog remains usable or another primitive better fits the product.

### Skeleton geometry
Matching the eventual content's shape can reduce layout shift. Do not use skeletons when they hide uncertainty, imply fake progress, or add more distraction than a reserved state/progress message.

### Slow-motion review
Useful for debugging meaningful custom animation. Not required for interfaces without custom motion and not a substitute for judging normal-speed experience.

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
- hard-capping all UI motion to one duration;
- banning gradients, springs, shadows, or custom easing independent of context;
- inferring hidden design tokens/APIs from screenshots;
- hand-rolling complex accessible primitives without checking the project/library first;
- fabricating an interface when an explicit audit is run on an empty project;
- generating multiple diagnostic reports as a prerequisite for every fix.
