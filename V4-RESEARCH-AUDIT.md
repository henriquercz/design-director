# Design Director v4 — UI craft research audit

This document records the source review that informed Design Director v4. Runtime guidance was independently distilled, calibrated, and merged into the MIT core; third-party skill/component text or code was not copied into the package.

## Scope

Primary source ecosystems reviewed:

1. UI Skills — https://www.ui-skills.com/
   - catalog/index: https://www.ui-skills.com/llms.txt
   - routing/orchestration skill
   - design-system evidence extraction / design.md workflow
   - micro-craft UI guidance
   - accessibility guidance
   - contrastive variant workflow
2. COSS UI — https://coss.com/ui
   - component catalog / llms index
   - agent/skill usage guidance
   - component composition patterns, including responsive overlay primitives
3. Design System Checklist — https://www.designsystemchecklist.com/pt
   - design language
   - foundations
   - component completeness
   - maintenance/system consistency
4. Emil Kowalski UI writing — https://emilkowal.ski/ui/you-dont-need-animations
   - related motion essays/examples on timing, origin, interruptibility, restraint, and interaction frequency
5. ReUI — https://reui.io/components
   - component catalog / llms index
   - agent skills
   - MCP/registry workflow and usage validation

## What v4 adopts

### UI Skills

**Adopted:**
- route to the smallest useful specialist set rather than loading every skill;
- separate design evidence from design inference;
- do not claim internal tokens/APIs from screenshot appearance;
- contrastive design variants should differ along a meaningful primary axis;
- optical micro-craft deserves an explicit final-quality layer;
- keyboard-only and semantic/accessibility review should be explicit verification passes.

**Calibration:**
- no fixed universal radius formula;
- no universal ban on gradients/custom easing;
- no universal animation duration cap;
- no requirement to produce variants for every request.

### COSS UI

**Adopted:**
- component behavior should be composed from proven primitives when available;
- read the actual current API instead of inventing props from model memory;
- responsive design may adapt interaction primitives (for example modal/dialog-like surfaces to a drawer/sheet) while preserving task semantics;
- component completeness includes focus/keyboard/collision/scroll/disabled/loading/recovery behavior, not only appearance.

**Not adopted as a dependency:**
- COSS is not installed automatically and Design Director does not assume its stack. The principles are registry-agnostic.

### Design System Checklist

**Adopted:**
- durable design memory should capture design-language constitution, not only colors/fonts;
- foundations include spacing/grid, type, semantic color, elevation, z-index, motion posture, iconography, responsive strategy;
- components need family-specific contracts (Dialog, Tooltip, Tabs, Toast, Skeleton, tables/collections, forms, etc.);
- media geometry/fallback/density/alt behavior is design-system quality.

**Calibration:**
- component checklists are loaded only for touched/relevant families;
- a checklist item is not forced when the primitive/product does not require it.

### Emil Kowalski UI motion writing

**Adopted:**
- first ask whether an interaction should animate;
- motion decision uses purpose + frequency + input + spatial change + cost;
- repeated/high-frequency actions have a tiny motion/latency budget;
- origin should preserve causality when an overlay/object emerges from a trigger/source;
- reversible motion should be interruptible;
- normal-speed judgment can be supplemented by a slow diagnostic pass;
- spring/easing choices depend on interaction mechanics rather than trends.

**Calibration:**
- timing ranges remain heuristics, not standards;
- keyboard-triggered actions are not universally forbidden from moving, but repeated keyboard navigation must not wait for decorative motion;
- stillness is always an acceptable motion decision.

### ReUI

**Adopted:**
- separate workflow intelligence from live component/API truth;
- use registry/MCP/current source as authoritative when present;
- `find → inspect API/examples → validate usage → adapt` is a better implementation protocol than inventing plausible component props;
- complex primitives should preferentially reuse proven accessible behavior.

**Not adopted as a dependency:**
- ReUI is not mandatory or bundled. Projects using another stack should use their own registry/library/native primitives.

## New v4 references

### `design-evidence.md`
Prevents false certainty when learning a design system from repositories, URLs, screenshots, or references. Introduces Normative / Observed / Inferred / Unknown confidence.

### `component-contracts.md`
Defines family-level obligations for overlays, forms, async/status, tabs/disclosure, collections, manipulation, and media.

### `micro-craft.md`
Captures optical polish after structure is correct: nested geometry, spacing relationships, icon alignment, media geometry/crop, transitions, stacking/clipping, state geometry.

## Existing v4 upgrades

- `motion.md` — purpose/frequency/input/spatial-change/cost; origin; interruptibility; timing calibration; slow diagnostic pass.
- `implementation.md` — reuse-first, API-first, live-registry truth, complex-primitive reuse.
- `responsive.md` — responsive interaction-primitive adaptation.
- `verification.md` — keyboard-only, semantic/accessibility, component-contract, craft, and motion passes.
- `project-memory.md` — design-language constitution + evidence provenance.
- `routing.md` — evidence-before-system-claims and contrastive direction.
- `companion-routing.md` — 0–3 companion context budget.
- `calibration.md` — prevents source heuristics from becoming universal laws.
- `creation-redesign.md` — contrastive variants on one meaningful axis.

## Rejected universal rules

Design Director v4 explicitly refuses to turn the research into the following house laws:
- "always animate" or "never animate";
- one fixed animation duration/easing for every interaction;
- "never gradients";
- exact nested-radius arithmetic everywhere;
- mandatory 4pt/8pt spacing math across all products;
- one specific component library for all stacks;
- hand-built UI behavior when a healthy project primitive already solves it;
- screenshot appearance as proof of hidden tokens/API;
- loading skeletons everywhere;
- Dialog→Drawer on every mobile interface;
- unlimited specialist/skill fan-out.

## Result

v4 increases decision quality while preserving the original product promise:

```text
user states abstract goal
        ↓
Design Director inspects evidence/product truth
        ↓
routes internally
        ↓
uses real primitives/APIs
        ↓
implements component contracts + craft + motion
        ↓
verifies actual behavior
```

The user still does not need to know internal references or mode names.
