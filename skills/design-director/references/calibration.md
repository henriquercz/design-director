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
- screenshot-only evidence must not masquerade as hidden design-system truth;
- preserve redesign contracts such as routes, SEO, analytics, legal copy, and form semantics unless changing them is explicitly in scope.

## Evidence labels are not confidence theater

Use `Normative`, `Observed`, `Inferred`, and `Unknown` only when provenance matters. Do not add labels to every trivial design choice. Their job is to prevent uncertain evidence from becoming permanent project truth.

## Qualitative posture, not numeric taste theater

Visual variance, motion intensity, and information density are useful coordination axes. Infer them qualitatively from task, audience, risk, register, references, and existing system evidence.

Do not require the user to configure numeric sliders or treat values such as `8 / 6 / 4` as objective design truth. If a team intentionally defines its own numeric scale, use it as a project convention rather than a universal standard.

## Use contextually

### OKLCH
Excellent for authoring new web palettes because of perceptual properties and modern support. Do not migrate an existing healthy palette solely to use it.

### 44–48px touch targets
A strong ergonomic aim for many touch interfaces. It is not the exact WCAG 2.2 AA minimum. WCAG 2.2 SC 2.5.8 uses 24×24 CSS px with exceptions. Design above the floor when context allows.

### 60–30–10 color balance
A composition heuristic, not a requirement. Semantic and brand roles matter more than percentages.

### Accent count / saturation caps
A restrained palette can improve coherence, but "one accent only" and fixed saturation ceilings are not universal rules. Multiple semantic accents may be necessary for state, data, brand, or comparison. Control role and hierarchy matter more than counting hues.

### Light/dark mode
Support both modes when product requirements, user preference, platform conventions, or brand strategy call for it. Do not force dual-theme implementation on every consumer/marketing page. A deliberately light-only or dark-only experience can be correct if accessibility and contrast remain good.

### Pure black / pure white
Off-black/off-white often create softer depth, but `#000` and `#fff` are not inherently wrong. Use rendered contrast, material strategy, brand, display characteristics, and accessibility to decide.

### 60–76ch or similar body measures
Useful starting region for some long-form Latin text, not a universal rule for all languages, typefaces, densities, or product UI.

### Hero line/word limits
Short hero copy can sharpen first-impression clarity, but exact two-line, 20-word, four-element, or top-padding caps are not standards. Fit the value proposition, evidence, CTA, localization, viewport, and brand composition. A hero that hides its primary action or becomes unreadable is a problem; breaking an arbitrary count is not.

### Navigation height / single-line rules
Desktop navigation normally should remain compact and scannable, but exact pixel caps and one-line-only rules depend on IA, locale, accessibility, input mode, and brand. Prevent accidental wrapping/overflow; do not delete meaningful navigation solely to satisfy a number.

### 3-level text hierarchy
Hook/support/detail can be a helpful pattern, but content may need two, four, or more roles. Avoid flattening semantic hierarchy to satisfy a number.

### Typography families
Inter, serif faces, display sans faces, monospace, and mixed-family systems are all valid when the content, brand, language coverage, performance, and hierarchy justify them. Do not blacklist specific fonts because models overuse them; reject reflexive choice, not the typeface itself.

### Punctuation
No blanket ban on em dashes, en dashes, exclamation marks, title case, middle dots, or other punctuation. Use language conventions, localization, voice, readability, and semantics. Decorative separator overuse can be a smell without making the character itself forbidden.

### Icon libraries
Prefer one coherent icon language and reuse the project's existing accessible assets. No library is universally banned or preferred. Hand-drawn/custom icons can be correct for brand or missing domain glyphs when implemented accessibly and consistently.

### Spacing scales
Use a small coherent token scale. A 4/8-derived scale is common and useful, but do not force one arithmetic across every brand/product. Semantic relationship matters more than divisibility.

### Nested radius arithmetic
Outer radius often needs to increase with the inset around an inner rounded surface so corners read concentrically. Treat `outer ≈ inner + inset` as a construction aid, not a mandatory formula.

### Visual mass
Balance size, contrast, position, whitespace, and motion qualitatively. Do not use a fake numeric equilibrium score.

### Section-layout repetition
Repeated layout can create rhythm and system coherence; excessive identical sections can reveal lazy composition. Change the layout when the content relationship changes. Do not enforce a universal "every layout family only once" quota.

### Eyebrows / micro-labels
Small labels can orient, categorize, or provide useful metadata. Repeating them above every section can become templated slop. Judge semantic value and rhythm rather than applying a fixed one-per-three-sections quota.

### Images on marketing pages
Strong imagery can be essential to brand/evidence, but text-led/editorial/minimal compositions can be complete without an arbitrary minimum image count. Never generate imagery merely to satisfy a quota. Product proof and atmospheric art direction are different roles.

### Generated images
Use image generation when the task benefits from custom visual assets and the tool/workflow permits it. It is not a mandatory first step for every landing page. Prefer real product evidence when making product claims.

### `dvh` / viewport units
Dynamic/small viewport units are useful for mobile browser-chrome problems. Do not mechanically replace every `vh` with `dvh`; choose based on the intended viewport behavior and browser support.

### Grid vs flex
CSS Grid and Flexbox solve different layout relationships. Avoid brittle percentage arithmetic, but do not ban Flexbox. Choose the primitive that expresses the content relationship most directly.

### "Cliffhanger" section reveal
Can help narrative scroll continuity, but should not be universal or use fixed pixel exposure.

### Motion duration ranges
Common UI motion often falls into rough bands such as ~100–150ms for tiny feedback, ~150–250ms for routine transitions, and ~200–300ms for larger overlays/scenes. These are starting regions, not standards. Frequency, distance, input, interruption, visual weight, device performance, and register decide.

### Easing tendencies
Ease-out-like behavior can suit entering/leaving motion; ease-in-out-like behavior can suit objects already moving within the scene; linear suits constant motion; springs can suit physical/direct manipulation. None is a universal default.

### GSAP / Motion / CSS animation
Use the smallest capable mechanism already compatible with the project. GSAP, Motion, CSS scroll-driven animations, IntersectionObserver, Web Animations, and other approaches each have valid use cases. Do not mandate one library or canonical skeleton independent of the project/version/task.

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

## Reject as universal mechanisms

- reading-distance equations that produce exact web font sizes;
- random animation jitter to hide "robotic" timing;
- numeric composition mass calculators;
- fixed taste-dial baselines or mandatory numeric design-posture presets;
- mandatory fixed viewport lists for every project;
- forcing animation into a motion pass when stillness is better;
- hard-capping all UI motion to one duration;
- banning gradients, springs, shadows, custom easing, specific fonts, punctuation, icon libraries, or color families independent of context;
- forcing one accent, dual-theme support, one corner system, one image minimum, one hero text formula, or one navigation height across unrelated products;
- requiring image generation, marquees, bento diversity, or section-layout quotas just to appear designed;
- treating `100dvh`, CSS Grid, Tailwind, Motion, GSAP, React, or Next.js as universal implementation defaults;
- inferring hidden design tokens/APIs from screenshots;
- hand-rolling complex accessible primitives without checking the project/library first;
- fabricating product screenshots, metrics, status, or precision and presenting them as evidence;
- fabricating an interface when an explicit audit is run on an empty project;
- generating multiple diagnostic reports as a prerequisite for every fix.
