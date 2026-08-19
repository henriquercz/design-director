# Implementation discipline

## Inspect existing system

Before introducing new primitives, find:
- global style/tokens;
- component library;
- typography loading;
- theme/dark mode;
- layout shells;
- icons/images;
- route conventions;
- data/state patterns.

## Prefer semantic reuse

Reuse healthy primitives. Extend them when the new requirement is a real new role. Do not create wrappers/components solely to hide a one-off styling choice.

## Tokens

Use semantic tokens for repeated design roles. Avoid scattering magic values during system-level work, but do not over-tokenize one-off art direction.

## Accessibility stays in the implementation

Keep native semantics, labels, focus, keyboard behavior, and live-region/state communication appropriate to the product.

## Real states in code

Do not leave state designs only in comments. Implement and, when possible, expose test/demo paths for empty/loading/error/success/disabled/etc.

## Responsive behavior

Encode actual recomposition: order, visibility strategy, density, layout, table behavior, container adaptation. Avoid brittle fixed widths.

## Assets

Use real product assets where available. Verify paths/loading and avoid placeholder imagery left in a shippable result.

## Performance

Match visual ambition to target hardware and framework. Optimize obviously expensive media/effects; do not sacrifice user experience merely to maximize a synthetic score.

## Change safety

After edits, run the project's relevant checks (format/lint/typecheck/test/build) and inspect diffs for unrelated changes.
