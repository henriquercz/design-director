# Borders, radius, shadows, and depth

Edges answer what belongs together, what is separate, and what state is active. Depth answers what sits above/below and what deserves attention.

## Border jobs

Every visible edge should primarily serve one or more:
- separation;
- containment;
- focus;
- selection/state;
- density/scanning.

If spacing and alignment already communicate grouping, another border may be noise.

## Border roles

Define a small semantic ladder: subtle, default, strong/interactive, focus, error/state. Dark themes need authored edge values; do not invert light borders.

## Radius

Radius is a product physical language. Keep nested radii visually coherent. Pills belong to shapes whose semantics or brand language support pills—tags, chips, segmented controls, certain CTAs—not every rectangle by default.

## Focus

Focus treatment must remain visible against nearby surfaces and avoid clipping. Never remove an outline without an equivalent or better focus indicator.

## Tables and lists

Prefer the least boundary necessary for scanning. Header separation often deserves more clarity than every cell. Dense data may need stronger row/column structure.

## Inputs

Support default, hover where applicable, focus, error, disabled, read-only, and validation/recovery states. Border color alone is often insufficient for focus or errors.

## Depth strategy

Choose a coherent primary containment/depth model:
- flat + spacing/dividers;
- border-led;
- layered surfaces;
- shadow-led elevation;
- intentional translucency/glass.

Heavy border + heavy shadow on every component usually creates noise.

## Shadows

Use elevation semantically: menus, popovers, dialogs, floating controls, dragged objects, sticky surfaces, etc. Keep light direction and softness coherent. Avoid decorative shadow proliferation.

On dark themes, surface value differences often communicate elevation better than large black shadows.

## Performance

Avoid expensive continuously animated shadows/blur without a real benefit. Prefer transforms/opacity for frequent motion; verify paint-heavy effects on target hardware.
