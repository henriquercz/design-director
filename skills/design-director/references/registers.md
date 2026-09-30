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

## Do not import marketing grammar into product UI

The two registers fail in opposite directions, and each failure is common.

- A **brand** surface that borrows product grammar becomes a dashboard: equal-weight card grids, uniform section rhythm, neutral copy, no art direction, no memorable arrival. It explains features and forgets to persuade.
- A **product** surface that borrows brand grammar becomes a landing page: centered hero, oversized display type, decorative numbering, scroll-reveal choreography, marketing proof blocks, and marketing spacing. It looks promotional and scans slowly.

Classify the register from the dominant user job before choosing composition. If the dominant job is repeated use, the marketing instincts are the wrong instincts even when they would "look more designed". If the job is arrival and persuasion, product minimalism wastes the surface.

### Spend Brand variance inside the category, not beside it

A category's own visual language is not a cliché to escape. Escaping into an **adjacent** register to prove restraint is its own kind of generated default.

- **Luxury / premium / heritage:** variance belongs in editorial craft — scale contrast, negative space, image treatment, restraint of color, a distinctive display voice. Neither the extreme close-up nor the monochrome technical register is a default here.
- **Precision / engineering / technical:** variance belongs in system legibility, data density, instrument honesty, mechanism as proof.
- **Playful / expressive:** variance belongs in illustration, motion personality, and typographic play.

Choosing a register that is *adjacent to but not* the brief's category produces a page that is disciplined and tonally wrong. It reads as a competent engineering brochure for a fashion house, or an austere German instrument panel for a lifestyle brand.

Before committing, name the category's inherited visual language out loud, then decide which parts you are keeping on purpose. Escaping is a decision that needs a reason; keeping is the default.

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