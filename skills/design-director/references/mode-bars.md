# Mode bars and completion criteria

A mode is complete only when it makes the kind of change its name promises. v4 internal references increase quality without adding mandatory user-facing modes.

## setup / brief
- inspect repository and existing design system using `design-evidence.md` when needed;
- create/update `.design-director/brief.md` with durable facts and confidence/provenance for uncertain rules;
- do not turn setup into a long interview if facts are inferable.

## checkup
Fast six-vital evidence scan: intentionality, readability, usability, responsiveness, performance feel, accessibility.
Output: `.design-director/reports/checkup.md` only by default.
No product edits.

## smell
Detect generic/generated reflexes with evidence and severity.
Output: `.design-director/reports/smell.md` only by default.
No product edits.

## review
Deep experience critique: first impression, prompt fidelity, primary flow, hierarchy/composition, system quality, interaction/responsive/access, component contracts, craft/specificity, priorities.
Output: `.design-director/reports/review.md` only by default.
No product edits.

## audit
Working diagnosis for a task. Persistent report optional only when user asks.
No edits unless user also asks for treatment.

## direction
Produce a coherent thesis and treatment plan. A list of trends is not direction.
When meaningful ambiguity remains, 2–3 contrastive variants may explore one primary axis at a time; cosmetic swaps do not count as distinct directions.

## create / build
Build a usable real surface, not a mockup. Include realistic content, applicable component contracts/non-happy states, responsive behavior, and verified implementation.

## redesign
Change the visual world and spatial premise end-to-end while preserving the product's core job/content/flow unless scope says otherwise. Repainting the same layout is not redesign.

## refine
Choose a named character move and make it visibly change the result: push, settle, strip, proof, activate, texture, or push-past-limits. One tiny detail does not count unless explicitly scoped.

## deslop
Replace generic defaults with product-specific decisions. Do not merely remove gradients or swap a purple palette for another cliché. Fix causes in priority order: composition → identity/color → type → depth → component language → motion → decoration, adjusted to evidence.

## relayout
Must include at least one visible structural change: focal point, section composition/order, text-proof relationship, control/nav placement, grid/table/split/stack/flow structure, or responsive order. Spacing-only changes do not count.

## typeset
Define and apply roles, hierarchy, measures, wrapping behavior, numeric/data behavior, and loading/fallbacks where applicable. A single font-size change does not count.

## recolor
Define/apply semantic roles for canvas, surface, text, muted text, border, actions, focus, selection, success/warning/error, disabled, and domain states. One accent swap does not count.

## interaction
Repair applicable hover/active/focus, keyboard path, touch/pointer target behavior, disabled/loading/empty/error/success/selected/overflow, destructive recovery, overlays, focus return, and feedback. Apply relevant `component-contracts.md`; hover polish alone does not count.

## motion
Use the purpose/frequency/input/spatial-change/cost model. Add or repair only motion that communicates causality, state, hierarchy, continuity, feedback, or justified delight. A valid motion pass may deliberately reduce/remove motion. High-frequency actions must not wait for decorative motion.

## responsive
Recompose across content constraints, containers, viewport widths, input modes, zoom, safe areas, and text direction. Responsive adaptation may change the interaction primitive while preserving the same task/data/state. Desktop stacked vertically is not automatically a responsive solution.

## a11y
Repair concrete access barriers: semantics, labels, keyboard/focus, target size/spacing, contrast, non-color cues, reduced motion, zoom/reflow, alternative text, form errors, direction/localization as relevant.

## voice
Change the brand lane visibly through art direction, domain evidence, imagery/material choices, typography, color, composition, and copy posture. Do not import a reference brand wholesale.

## surface
Harden a product UI under real use: density, real/edge data, component contracts, state coverage, selection, commands, shortcuts, tables/lists, overlays, feedback, recovery, performance feel, responsive behavior.

## writing
Make controls, errors, empty states, loading, labels, help, terminology, and localization behavior more specific and operational. Preserve brand tone without sacrificing clarity.

## tokenize
Extract only proven repeated intent. Consolidate values/components, migrate actual use, remove dead duplicates, and verify the rendered result is unchanged except for intended consistency improvements.

## finish
Use the product like a user, force rough states, run keyboard/semantics/component-contract/craft checks as relevant, remove unnecessary decoration/copy/motion, repair small remaining inconsistencies, verify claims against diff + render. If composition is wrong, route back to relayout/redesign instead of pretending finish can polish it away.

## outcome
Diagnose the user outcome, intended product/business outcome, lifecycle stage, evidence confidence, and ethical constraints. This mode does not need to edit by itself. It routes the resulting problem into existing implementation modes and reads the relevant outcome references. Completion requires a specific outcome hypothesis, evidence/unknowns, guardrails, and the smallest design treatment likely to affect the mechanism.
