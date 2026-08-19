# Canonical audit and scoring system

Use one canonical `/100` score across deep review and final verification to avoid conflicting `/60`, `/50`, and inverted smell scores.

## Weights

| Dimension | Points |
|---|---:|
| Task / surface fit, prompt fidelity, and outcome fit | 15 |
| Information hierarchy | 15 |
| Composition and spatial logic | 15 |
| Typography | 10 |
| Color and semantic signaling | 10 |
| Interaction and state coverage | 10 |
| Responsive/container/input adaptation | 10 |
| Accessibility | 10 |
| Craft, specificity, and coherence | 5 |
| **Total** | **100** |

## Interpretation

- **90–100:** candidate for ship-ready if no P0 and verification is real.
- **80–89:** good but one focused repair should be named.
- **70–79:** meaningful structural/system issue remains.
- **<70:** direction or composition likely needs rethink.

Do not inflate scores to be polite. The explanation matters more than the number.

## Severity

### P0
Blocks completion or safe access. Examples: unreachable primary action, keyboard trap, severe overflow hiding controls, destructive operation with broken recovery.

### P1
Major harm to comprehension, trust, hierarchy, responsiveness, or repeated usability.

### P2
System/craft defect with visible user impact.

### P3
Optional polish.

## Evidence requirement

Every major finding must state:
1. what was observed;
2. where/how it was observed;
3. user impact;
4. root cause hypothesis;
5. treatment mode;
6. verification needed after treatment.

If a check cannot be performed, mark it **unverified** rather than healthy.

## Fast checkup status

For `checkup`, use **Healthy / Watch / Critical / Unverified** for six vitals:
- intentionality;
- readability;
- usability;
- responsiveness;
- performance feel;
- accessibility.

The status is more useful than forcing another numeric denominator.

## Smell severity

For `smell`, list tells as `none / faint / clear / dominant` with evidence. Do not turn absence of smells into an inverted score that can be confused with quality. A page can be non-generic and still be bad.


## Outcome-aware extension

When business performance is explicitly part of the task, the first 15-point dimension also asks:
- is the intended user outcome explicit?
- is the requested product/business outcome compatible with that user outcome?
- is the primary action aligned to a genuine value step?
- are proof and commitment truthful?
- are important outcome claims measured, externally supported, heuristic, or merely hypotheses?

Do not award outcome-fit points for higher conversion produced by deception, hidden commitment, obstructed exit, or accessibility regressions.
