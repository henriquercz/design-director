# Brand vs Product register

Two design registers need different permissions.

## Brand
Typical surfaces: marketing pages, launches, campaigns, portfolios, editorial experiences.

Optimize for:
- recognition and point of view;
- emotional arrival;
- memorable composition;
- strong proof/evidence;
- art-directed type, image, color, and motion;
- deliberate pacing and section character.

Brand can tolerate higher visual variance if coherence and usability remain intact.

## Product
Typical surfaces: apps, dashboards, admin panels, work tools, repeated-use workflows.

Optimize for:
- speed and predictability;
- stable component semantics;
- useful density;
- state coverage;
- data resilience;
- keyboard/touch efficiency;
- feedback and recovery;
- low cognitive tax during repeated use.

Product distinctiveness should usually come from precise hierarchy, domain-native artifacts, density choices, interaction quality, and a restrained identity system rather than spectacle.

## Mixed
A product may have brand moments inside onboarding or empty states; a marketing page may embed a product demo. Apply the register per region, but keep the overall visual DNA coherent.

## Design posture axes

For substantial visual work, infer a small internal posture before choosing layout details. These are coordination axes, not user-facing configuration and not pseudo-scientific scores.

### Visual variance
How far the composition can move from predictable symmetry and standard section rhythm.

- **Low:** stable alignment, familiar structure, low surprise; useful for trust-critical, regulated, accessibility-sensitive, or repeated-use contexts.
- **Medium:** controlled asymmetry, varied section rhythm, selective overlap or scale changes.
- **High:** stronger asymmetry, editorial/kinetic composition, unusual spatial relationships; appropriate only when Brand context, content, and usability can carry it.

### Motion intensity
How much movement the experience can spend without becoming latency or distraction.

- **Low:** state feedback and essential continuity only.
- **Medium:** concise transitions, selected reveals, stronger spatial continuity.
- **High:** authored narrative/physics/scroll choreography reserved for moments where motion is part of the experience.

Read `motion.md`; high frequency and task pressure can force motion intensity down even on expressive brands.

### Information density
How much meaningful information should occupy a viewport/component.

- **Low:** gallery/editorial pacing, fewer objects, larger relationship spacing.
- **Medium:** ordinary product/marketing density with clear grouping.
- **High:** operator/cockpit density where scan speed and comparison matter more than spectacle.

## Infer posture from the brief

Use evidence, not a fixed baseline. Read:
- page/surface kind;
- audience and user pressure;
- task frequency and risk;
- explicit vibe/brand words;
- reference signals;
- existing brand/design-system evidence;
- accessibility, performance, platform, and regulatory constraints.

The same project can use different posture by surface, but differences need a reason. Product truth, accessibility, clarity, and performance override aesthetic ambition.

Do not ask the user to tune numeric dials unless they explicitly want that control. Normally the user states an abstract goal and Design Director infers the posture internally.