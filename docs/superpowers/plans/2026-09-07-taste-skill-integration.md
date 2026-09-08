# Design Director 4.1 Taste Skill Integration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Integrate high-value Taste Skill ideas into Design Director v4 while preserving freeform routing and calibrated judgment.

**Architecture:** Extend existing progressive-disclosure references rather than adding modes or a large new monolithic reference. Add regression evals for the accepted ideas and for rejected dogmatic rules. Release as v4.1.0.

**Tech Stack:** Agent Skills Markdown, Python validation scripts, GitHub.

**Spec:** `docs/superpowers/specs/2026-09-07-taste-skill-integration-design.md`

## Global Constraints

- Keep the existing 23 public modes.
- Freeform invocation remains the default UX.
- No rigid numeric taste dials exposed to users.
- No blanket bans on fonts, punctuation, palettes, gradients, theme modes, or animation libraries.
- Preserve MIT core and record Taste Skill as MIT research provenance.
- Use TDD for regression enforcement.

---

### Task 1: Add regression test first

**Files:**
- Create: `scripts/test_taste_integration.py`

- [ ] Assert version 4.1.0, posture axes, redesign preservation, system-vs-aesthetic honesty, copy self-audit, dependency verification, dynamic viewport guidance, calibration, preservation verification, and at least 56 eval cases.
- [ ] Run against v4.0 baseline and confirm failure for missing v4.1 markers.

### Task 2: Integrate accepted design knowledge

**Files:**
- Modify: `skills/design-director/SKILL.md`
- Modify focused reference files only.

- [ ] Add qualitative posture axes.
- [ ] Add system-vs-aesthetic evidence discipline.
- [ ] Add redesign preservation envelope.
- [ ] Add marketing anti-slop and proof-asset discipline.
- [ ] Add copy self-audit and CTA intent consistency.
- [ ] Add dependency/high-frequency state safeguards.
- [ ] Add dynamic viewport and cleanup guidance.
- [ ] Add calibration rejections for Taste Skill dogma.

### Task 3: Add behavioral evals

**Files:**
- Modify: `skills/design-director/evals/EVALS.md`
- Modify: `scripts/validate.py`

- [ ] Add cases 47–56 covering the accepted ideas and rejected universal bans.
- [ ] Raise validator eval floor to 56.
- [ ] Run regression test and validator.

### Task 4: Documentation and provenance

**Files:**
- Create: `TASTE-SKILL-AUDIT.md`
- Modify: `README.md`
- Modify: `THIRD_PARTY.md`

- [ ] Document accepted/rejected ideas and MIT provenance.
- [ ] Update README v4.1 section while keeping install/use unchanged.

### Task 5: Publish safely

- [ ] Compare branch to `main`; verify scoped diff and branch is not behind.
- [ ] Run fresh validation evidence.
- [ ] Fast-forward `main` to the verified commit.
- [ ] Fetch `main` HEAD and key files to confirm publication.
