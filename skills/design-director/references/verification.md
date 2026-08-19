# Verification and truthful completion

A design claim is valid only when it maps to actual implementation and, when possible, the rendered behavior.

## Pre-ship use pass

Use the interface like a person:
- click/tap;
- tab and use keyboard;
- type and submit;
- wait;
- trigger failure;
- resize;
- search/filter/sort;
- open/close overlays;
- perform destructive/reversible actions when safe;
- refresh/return where relevant.

## Force rough states

Inspect applicable:
- empty;
- loading;
- error;
- success;
- disabled/read-only;
- selected/current;
- focus;
- overflow;
- long/short/zero/huge data;
- slow/no network when testable;
- narrow/wide container;
- dark/light themes if supported;
- RTL/localization if supported.

## Rendered proof

If you say:
- "relayouted" → composition must visibly differ, not just padding;
- "animated" → reachable motion must exist in rendered UI;
- "fixed focus" → keyboard focus must be observable;
- "added loading/error/empty state" → there must be a way to trigger or inspect it;
- "responsive" → inspect actual narrow/wide result;
- "recolored" → real components must use semantic roles;
- "tokenized" → migrated usage must resolve through tokens/components.

If implemented but not triggerable in the current environment, say exactly that instead of claiming full visual verification.

## Subtraction pass

Remove things whose purpose cannot be explained:
- decorative borders/shadows;
- filler copy;
- motion with no behavioral job;
- redundant color roles;
- wrappers that create dead space;
- duplicate controls or headings.

## Regression checks

- product behavior still works;
- prompt invariants remain intact;
- no new accessibility failure;
- no new overflow or layout shift;
- no new anti-slop smell introduced;
- performance feel has not visibly degraded.

## Stop rule

After the first implementation:
1. one broad repair pass is allowed for meaningful issues;
2. one targeted final repair is allowed;
3. then stop and surface remaining structural/tradeoff issues.

Do not keep redesigning because subjective improvements are always possible.

## Verification status

Use one of:
- **Verified:** rendered and exercised sufficiently for the claim.
- **Partially verified:** code/tests plus limited visual/interaction access.
- **Provisional:** source-level implementation only; visual environment unavailable.
