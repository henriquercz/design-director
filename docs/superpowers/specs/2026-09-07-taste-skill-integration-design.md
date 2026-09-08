# Design Director 4.1 Taste Skill Integration Design

## Goal

Integrate the genuinely complementary ideas from Leonxlnx/taste-skill into Design Director without changing the one-command freeform UX, expanding the mode surface, or importing Taste Skill's rigid aesthetic dogma.

## Source scope

Primary source reviewed line-by-line:
- `Leonxlnx/taste-skill/skills/taste-skill/SKILL.md` (MIT)

Supporting repository context reviewed:
- README and LICENSE
- skill directory structure (the active `taste-skill` runtime is a single `SKILL.md`)

## Keep

1. **Design posture axes**
   - infer visual variance, motion intensity, and information density from brief/audience/constraints;
   - keep them qualitative and internal; no mandatory numeric baseline or user setup.

2. **System vs aesthetic honesty**
   - distinguish an official design system/ecosystem from an aesthetic reference;
   - verify current package/API/docs before claiming a system is official;
   - label web approximations as approximations rather than inventing official packages.

3. **Redesign preservation envelope**
   - protect URL/route slugs, anchor IDs, information architecture, SEO metadata/structured data/OG, analytics identifiers, form semantics, legal/consent copy, logo/wordmark, and existing accessibility wins unless change is explicit.

4. **Marketing anti-slop tells**
   - repeated eyebrows/micro-labels;
   - decorative section numbering/version stamps/status dots;
   - fake operational chrome such as weather/time/build metadata;
   - fake product previews presented as proof;
   - repeated section layout families without narrative reason;
   - fabricated precise metrics/specifications.

5. **Asset/proof discipline**
   - prefer real product screenshots, real brand assets, or real executable previews when something is presented as product evidence;
   - generated/editorial imagery is valid for art direction but must not masquerade as actual product proof.

6. **Copy self-audit**
   - review every visible string for unclear referents, hallucinated poetic filler, inconsistent terminology/CTA intent, and fake precision.

7. **Implementation/performance safeguards**
   - verify dependencies before import;
   - avoid competing component/design systems without a migration/interop reason;
   - keep high-frequency pointer/scroll animation values off full-tree render state paths where the stack provides motion values/signals/imperative primitives;
   - clean up listeners/effects;
   - use dynamic viewport units when mobile browser chrome makes fixed viewport height brittle.

## Explicitly reject as universal rules

- zero em-dashes;
- ban Inter, serif, Lucide, emojis, gradients, pure black/white, or custom easing;
- exactly one accent color;
- mandatory dark + light mode for every consumer page;
- universal 20-word hero subcopy / 2-line hero / 80px nav;
- mandatory image count for minimalist/editorial pages;
- universal `min-h: 100dvh` or CSS Grid;
- automatic GSAP/Motion selection;
- fixed numeric `DESIGN_VARIANCE / MOTION_INTENSITY / VISUAL_DENSITY` presets;
- one layout family only once per page;
- mandatory eyebrow ratios or other mechanical style bans.

These may be useful observations in a particular brief, but Design Director's calibration layer must keep them contextual.

## Architecture

No new public mode. Keep 23 modes.

Modify focused references:
- `registers.md`
- `design-evidence.md`
- `creation-redesign.md`
- `anti-slop.md`
- `writing.md`
- `implementation.md`
- `responsive.md`
- `calibration.md`
- `verification.md`

Update:
- `SKILL.md` metadata/version and direction wording
- `evals/EVALS.md` with regression cases
- `README.md`, `THIRD_PARTY.md`
- add `TASTE-SKILL-AUDIT.md`

Release as v4.1.0.

## Compatibility

User invocation remains:

`$design-director <freeform request>`

The user never has to set posture axes or name internal modes.

## Verification

- regression test must fail against v4.0 content before changes;
- regression test passes after integration;
- validator passes with >=56 evals;
- `SKILL.md` remains under 500 lines;
- no new reference file required;
- GitHub branch diff is scoped and main is fast-forwarded only after verification.
