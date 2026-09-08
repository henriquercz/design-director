# Taste Skill → Design Director 4.1 Audit

Source reviewed: `Leonxlnx/taste-skill/skills/taste-skill/SKILL.md` plus its repository README and MIT license.

Taste Skill is a strongly opinionated anti-slop frontend skill aimed mainly at landing pages, portfolios, and redesigns. Design Director has a wider scope (Brand + Product surfaces), so this merge intentionally extracts transferable principles instead of importing Taste Skill's full rulebook.

## What was added

### 1. Qualitative design posture
Taste Skill's variance / motion / density dials are useful as coordination dimensions. Design Director now infers the same three concepts qualitatively from audience, task pressure, risk, references, register, and existing design evidence.

The user does **not** configure numeric dials. Freeform invocation remains the default.

### 2. Official design system vs aesthetic honesty
Taste Skill correctly distinguishes official ecosystems/packages from visual aesthetics. Design Director now requires current evidence before claiming an official package/system exists for a target platform, and labels web recreations/inspirations as approximations when appropriate.

### 3. Redesign preservation envelope
Taste Skill's redesign section highlighted an important production risk: a visual redesign can accidentally damage non-visual contracts. Design Director 4.1 explicitly checks preservation of applicable:

- routes/slugs and deep links;
- anchor IDs;
- information architecture/navigation when not in scope;
- SEO metadata, canonical/indexability, structured data, OG/social metadata, and important internal links;
- analytics/telemetry/experiment/conversion hooks;
- form field/data/autocomplete/submission contracts;
- legal/consent/cookie/disclosure copy and mechanics;
- logo/wordmark/protected brand assets;
- existing accessibility wins;
- public API/data semantics.

### 4. Marketing anti-slop cluster
The anti-slop reference now recognizes several common marketing-page tells when they are unearned or repeated:

- eyebrow/micro-label on every section;
- decorative section numbering;
- fake operational chrome (weather/time/build/version/sync metadata);
- decorative state dots with no real state;
- fake product UI presented as proof;
- fabricated precision/metrics;
- repeated section-layout loops;
- performative "craft" microcopy.

These are **signals**, not universal bans.

### 5. Product proof vs atmospheric imagery
Generated/editorial imagery remains valid for art direction, but it cannot masquerade as factual product evidence. Real product screenshots/artifacts or executable previews are preferred when a visual is presented as product proof; concepts/mocks must be clear when they could be mistaken for reality.

### 6. Copy self-audit
Writing-heavy and redesigned surfaces now include a final copy pass for:

- broken grammar/unclear referents;
- hallucinated or forced "thoughtful" language;
- inconsistent terminology/CTA intent;
- unsupported precise claims;
- mismatch between copy promise and actual behavior.

### 7. Implementation safeguards
Design Director now more explicitly verifies dependencies before imports, avoids casually mixing component/design systems, keeps high-frequency pointer/scroll/gesture values off expensive full-tree render paths where possible, and requires listener/effect cleanup.

### 8. Dynamic viewport guidance
`dvh`/`svh` are recognized as useful tools for mobile browser-chrome/full-height problems, but not as universal replacements for `vh`.

## What was deliberately NOT imported as universal policy

Taste Skill contains many rules that can be useful in a narrow landing-page workflow but would reduce Design Director's correctness if applied globally. Design Director 4.1 explicitly rejects these as universal laws:

- numeric taste baselines such as a mandatory variance/motion/density preset;
- zero em/en dashes;
- bans on Inter, serif, Lucide, emoji, gradients, pure black/white, or custom easing;
- exactly one accent color or fixed saturation caps;
- mandatory dark + light modes for every consumer page;
- fixed hero line/word counts and navigation height caps;
- mandatory image counts or image-generation-first workflow;
- universal `100dvh` or CSS Grid;
- universal Motion/GSAP/Tailwind/React/Next defaults;
- one-use-only layout-family quotas or mechanical eyebrow ratios;
- mandatory marquees/bento diversity/motion because a style dial says so.

The calibrated rule is: **overused patterns are diagnostic smells; project evidence, user job, accessibility, platform, brand, and rendered outcome decide whether a pattern is actually wrong.**

## License / provenance

Taste Skill is MIT licensed (Copyright © 2026 Leonxlnx). Design Director does not bundle or reproduce the 87 KB upstream skill wholesale. This integration is a selective, calibrated synthesis of general design/implementation concepts, with provenance recorded here and in `THIRD_PARTY.md`.

Upstream: https://github.com/Leonxlnx/taste-skill
