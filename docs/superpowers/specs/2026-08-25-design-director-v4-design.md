# Design Director v4 Design Specification

## Goal
Upgrade Design Director's craft, component, evidence, motion, responsive, and implementation intelligence without changing the core user experience: the user states an abstract design goal and the skill routes/executes the smallest effective treatment chain automatically.

## User-facing contract
- Freeform invocation remains the default. Users do not need to know internal modes or references.
- Explicit modes continue to constrain scope when requested.
- No new mandatory commands are introduced in v4.
- Design Director remains the single director; specialists and references are subordinate.

## Architecture
v4 adds three progressively disclosed references:
1. `design-evidence.md` — confidence/provenance when deriving a design system from repositories, rendered DOM, screenshots, and references.
2. `component-contracts.md` — behavior/access/state/geometry obligations by component family.
3. `micro-craft.md` — optical polish, nested geometry, icon alignment, media geometry, transitions, stacking, and fine visual coherence.

Existing references are strengthened rather than replaced:
- `motion.md`: purpose × frequency × input × spatial change × cost, origin-aware motion, interruptibility, frequency-sensitive timing.
- `implementation.md`: reuse-first, API-first, live-registry truth, validate before coding, avoid hand-rolling complex interaction primitives when a healthy project primitive exists.
- `verification.md`: keyboard-only walk, semantics/accessibility pass, component-contract verification, slow-motion inspection for meaningful custom motion.
- `responsive.md`: responsive recomposition may change interaction primitive while preserving the task.
- `project-memory.md`: design-language constitution and evidence status.
- `calibration.md`: demote numeric craft/motion rules to contextual heuristics.
- `routing.md`: evidence extraction before design-system claims; contrastive exploration for ambiguous directions.
- `companion-routing.md`: cap specialist use at 0–3; no specialist pile-on.
- `creation-redesign.md` / `mode-bars.md`: contrastive variants explore one primary axis at a time.

## Evidence model
Design-system claims use one of four confidence labels:
- `normative`: explicit docs/tokens/shared API define the rule.
- `observed`: repeated real implementation or computed/rendered behavior supports it.
- `inferred`: plausible pattern but not proven as a rule.
- `unknown`: evidence is insufficient.

Evidence precedence when available:
1. explicit project/design-system documentation;
2. semantic tokens/theme/global styles;
3. shared primitives/components and their public APIs;
4. repeated consumers in production code;
5. rendered DOM/computed styles/accessibility tree;
6. screenshots/video/reference imagery;
7. inference.

Screenshot appearance never proves hidden token names, component APIs, or exact internal intent.

## Component contracts
Component quality is evaluated as a contract across semantics, states, interaction, geometry, responsive adaptation, accessibility, and failure/recovery. Contracts are grouped rather than implemented as a component library:
- overlays: dialog, sheet/drawer, popover, menu, tooltip;
- forms/controls: button, field, combobox, select, switch, slider, date controls;
- navigation/disclosure: tabs, accordion, breadcrumbs, command/navigation structures;
- async/status: loading button, skeleton, progress, toast, empty/error states;
- collections: table/data-grid/list/tree/virtualized collections;
- manipulation: drag/drop/sortable/kanban-like interactions;
- media: image/video/avatar/thumbnail geometry, fallback, alt, density.

When a project already has an accessible primitive/library/registry, Design Director reads and validates its real API before adapting it. Complex behavior should not be hand-rolled merely because the model can approximate the visuals.

## Motion decision model
Before adding motion, evaluate:
- purpose: causality, state, continuity, feedback, hierarchy, or rare delight;
- frequency: rare, occasional, routine, high-frequency;
- input: passive, pointer/touch, direct manipulation, repeated keyboard;
- spatial change: local, overlay, route, large scene;
- cost: attention, perceived latency, performance, vestibular/accessibility.

High-frequency operations must spend near-zero perceived time on decorative motion. Origin should preserve trigger/target causality when appropriate. Reversible interactions should be interruptible. Stillness remains valid.

## Craft model
Micro-craft is contextual polish, not numerology:
- nested radii should read concentrically;
- icon optical alignment/weight should match neighboring type/control language;
- spacing encodes relationship and should be consistent by semantic relationship;
- media should reserve geometry before load when possible;
- transitions should name the properties that actually need to animate rather than `transition: all` by reflex;
- stacking/depth should use a coherent model;
- dividers/borders should reinforce grouping/scanning rather than decorate emptiness;
- crop/focal point and placeholder/fallback behavior are part of design quality.

## Contrastive exploration
When direction is materially ambiguous, produce 2–3 meaningfully different variants along one primary axis at a time (structure, density, emphasis, type, or voice). Do not present cosmetic color swaps as design alternatives. Once one direction wins, converge and implement one system.

## Companion policy
- 0 companions is normal when bundled knowledge is enough.
- 1 companion is the common specialist case.
- 2 companions require two independent knowledge gaps.
- 3 companions are reserved for broad review/redesign/multi-surface work.
- More than 3 is rejected as context/routing dilution.

## Verification
v4 adds checks for:
- keyboard-only primary path;
- semantics/accessibility-tree when tools permit;
- component contract obligations for touched primitives;
- loading geometry and state reachability;
- responsive interaction-model adaptation;
- actual API/registry usage when a component system is present;
- slow-motion review of meaningful custom motion when tooling permits;
- no hidden claims from screenshot-only evidence.

## Non-goals
- No new visual house style.
- No mandatory ReUI, COSS, UI Skills, or any third-party component library.
- No hardcoded universal animation timings, radii formulas, spacing grids, or component choices.
- No expansion of user-facing mode vocabulary purely to expose internal knowledge.
- No duplication of third-party copyrighted skill text.

## Sources informing v4
- UI Skills: routing discipline, design-evidence separation, contrastive variants, micro-craft/accessibility patterns.
- COSS UI: component composition and API-first reuse discipline.
- Design System Checklist: design-language foundations and component completeness contracts.
- Emil Kowalski UI essays: purpose/frequency-aware motion, origin, interruptibility, restraint.
- ReUI: skill-as-workflow + live registry/API as implementation truth.

All runtime guidance is independently distilled and calibrated into the MIT Design Director core rather than copied verbatim.
