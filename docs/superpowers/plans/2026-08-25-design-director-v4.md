# Design Director v4 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Upgrade Design Director to v4 with evidence-aware design inference, component contracts, micro-craft intelligence, stronger motion/reuse/responsive verification, and unchanged freeform usability.

**Architecture:** Keep `SKILL.md` as a compact router and progressively disclose three new focused references. Update existing references to route through evidence, component contracts, live APIs, and purpose/frequency-aware motion. Expand evals and validation so the new behavior is structurally enforced.

**Tech Stack:** Agent Skills markdown, Python catalog/validator scripts, GitHub repository metadata/docs.

**Spec:** `docs/superpowers/specs/2026-08-25-design-director-v4-design.md`

## Global Constraints
- Freeform invocation remains the default; no new mandatory mode vocabulary.
- The Design Director core remains MIT and does not bundle copied third-party skill text.
- Heuristics remain contextual, not universal laws.
- Design Director remains the single orchestrator; companion use is capped at three.
- `SKILL.md` remains under the recommended 500-line limit.
- Existing install flows for Codex, Claude Code, Claude web, and ChatGPT web remain intact.

---

### Task 1: Add v4 knowledge modules

**Files:**
- Create: `skills/design-director/references/design-evidence.md`
- Create: `skills/design-director/references/component-contracts.md`
- Create: `skills/design-director/references/micro-craft.md`

**Interfaces:**
- Consumes: existing project-memory, implementation, controls, verification references.
- Produces: three reference contracts linked by `SKILL.md` and other references.

- [ ] Write the three focused references from the approved spec.
- [ ] Check that no rule duplicates an existing reference without adding a distinct decision boundary.
- [ ] Check that numeric heuristics are marked contextual rather than normative.

### Task 2: Upgrade routing and implementation behavior

**Files:**
- Modify: `skills/design-director/SKILL.md`
- Modify: `skills/design-director/references/routing.md`
- Modify: `skills/design-director/references/mode-bars.md`
- Modify: `skills/design-director/references/companion-routing.md`
- Modify: `skills/design-director/references/implementation.md`
- Modify: `skills/design-director/references/creation-redesign.md`

**Interfaces:**
- Consumes: Task 1 reference names.
- Produces: freeform routing that consults evidence/contracts/craft only when needed.

- [ ] Bump metadata to `4.0.0` and link the new references from `SKILL.md`.
- [ ] Add evidence extraction before design-system claims.
- [ ] Add reuse-first/API-first/live-registry validation discipline.
- [ ] Add contrastive exploration along one primary axis.
- [ ] Cap companion use at 0–3 and preserve Director ownership.

### Task 3: Upgrade craft, motion, responsive, memory, and verification

**Files:**
- Modify: `skills/design-director/references/motion.md`
- Modify: `skills/design-director/references/responsive.md`
- Modify: `skills/design-director/references/verification.md`
- Modify: `skills/design-director/references/calibration.md`
- Modify: `skills/design-director/references/project-memory.md`

**Interfaces:**
- Consumes: Task 1 contracts.
- Produces: contextual motion, responsive primitive adaptation, richer verification and durable evidence-aware memory.

- [ ] Add purpose × frequency × input × spatial change × cost motion decision model.
- [ ] Add origin-aware and interruptible motion guidance.
- [ ] Add responsive interaction-primitive substitution while preserving task semantics.
- [ ] Add keyboard-only, semantics/accessibility-tree, contract, and slow-motion verification passes.
- [ ] Add design-language constitution fields and evidence confidence to project memory.
- [ ] Calibrate timing/radius/spacing/icon rules as heuristics, not standards.

### Task 4: Add behavioral evals before finalizing release metadata

**Files:**
- Modify: `skills/design-director/evals/EVALS.md`
- Modify: `scripts/validate.py`

**Interfaces:**
- Consumes: v4 expected behaviors.
- Produces: regression expectations and structural enforcement that the three v4 references exist.

- [ ] Add evals for screenshot evidence, live API validation, complex primitive reuse, component contracts, high-frequency motion, tooltip timing, loading geometry, responsive Dialog→Drawer adaptation, contrastive variants, nested craft, media geometry, keyboard-only verification, and companion cap.
- [ ] Update validator required reference set from v3 to v4.
- [ ] Run validator against a local reconstructed tree and confirm it fails when a required v4 reference is removed, then passes when restored.

### Task 5: Update catalog and release documentation

**Files:**
- Modify: `CATALOG.json`
- Modify: `README.md`
- Modify: `QUICKSTART-PTBR.md`
- Modify: `MAINTAINING.md`
- Create: `V4-RESEARCH-AUDIT.md`
- Create: `docs/superpowers/specs/2026-08-25-design-director-v4-design.md`
- Create: `docs/superpowers/plans/2026-08-25-design-director-v4.md`

**Interfaces:**
- Consumes: final reference/eval counts.
- Produces: public v4 documentation and provenance.

- [ ] Regenerate catalog with 36 references and updated eval count.
- [ ] Explain v4 improvements without making usage more complex.
- [ ] Preserve all existing installation methods and web LLM instructions.
- [ ] Document source-by-source merge/rejection rationale and licensing boundary.

### Task 6: Verify and publish

**Files:** all files changed above.

**Interfaces:**
- Consumes: completed v4 tree.
- Produces: verified GitHub commit and promotion to `main`.

- [ ] Run `python scripts/validate.py` on the reconstructed tree.
- [ ] Run `python scripts/catalog.py` and compare output to committed `CATALOG.json`.
- [ ] Verify `SKILL.md` line count < 500 and all referenced files resolve.
- [ ] Review diff for accidental mode-count or installation regressions.
- [ ] Commit v4 to `feat/design-director-v4`.
- [ ] Compare branch to `main`.
- [ ] Fast-forward `main` only after verification succeeds.
