# Third-party companion skills and research sources

This package's `design-director` skill is original orchestration content under MIT.

The installer may optionally fetch independent third-party Agent Skills from their own repositories:
- Anthropic `frontend-design`
- nextlevelbuilder `ui-ux-pro-max`
- Vercel `web-design-guidelines`
- NousResearch/Hermes `popular-web-designs`
- Vercel `react-best-practices` (optional)
- NousResearch/Hermes `claude-design` (optional)
- heliocosta-dev `revenue-centric-design` (optional via `--revenue`)

Those projects retain their own licenses and terms. They are not bundled into this archive.

## Revenue-Centric Design boundary

`revenue-centric-design` is source-available, not OSI open source. Its upstream terms require attribution, exclude gambling/betting/casino and specified real-money gaming uses, and require copies/derivatives of its material to preserve those terms. For that reason v3 does **not** copy its 101-principle library into the MIT core. The optional installer fetches the upstream skill separately, and Design Director contains only an original outcome-aware routing layer and general ethical/product-design guidance.

## Prior design / research sources

### Command Code design reference

The v2 architecture was informed by a user-supplied full Command Code `/design` reference document. The package synthesizes concepts into a portable, calibrated workflow rather than reproducing Command Code runtime behavior or branding.

### Revenue-Centric Design

The v3 outcome layer was informed by a full audit of `heliocosta-dev/revenue-centric-design`. Because that upstream license is source-available with additional restrictions, its principle library is not copied into the MIT core; the separately licensed skill remains an optional companion.

### UI Skills / COSS / Design System Checklist / Emil Kowalski / ReUI

The v4 craft update was informed by public design-system, interaction, motion, component-contract, and implementation guidance from these sources. Design Director distilled general principles such as evidence-aware system inference, reuse/API-first implementation, component contracts, calibrated motion, and micro-craft instead of reproducing source libraries.

### Taste Skill (Leonxlnx)

Design Director 4.1 was informed by a line-by-line review of `Leonxlnx/taste-skill/skills/taste-skill/SKILL.md` plus its README and license. Taste Skill is MIT licensed (Copyright © 2026 Leonxlnx).

The integration is intentionally selective. It adopts/calibrates general ideas such as qualitative variance/motion/density posture, official-system-vs-aesthetic honesty, production-redesign preservation (SEO/analytics/forms/legal/accessibility), marketing anti-slop signals, product-proof integrity, copy self-audit, dependency verification, high-frequency interaction safeguards, and dynamic viewport guidance.

Design Director does **not** wholesale-copy Taste Skill's runtime or adopt its rigid universal bans/presets. See [`TASTE-SKILL-AUDIT.md`](TASTE-SKILL-AUDIT.md) for the accepted/rejected rationale.

Upstream: https://github.com/Leonxlnx/taste-skill
