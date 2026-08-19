# Tokenization and component consolidation

Tokenize is consolidation after design intent is understood. It is not a way to avoid making design decisions.

## Extract proven repetition

Look for repeated **meaning**, not merely repeated literal values.

Good tokens/components represent stable roles:
- surface/background levels;
- text roles;
- action/state colors;
- spacing tiers;
- radius/elevation roles;
- type roles;
- control sizes;
- repeated component behavior.

Do not create `--blue-17` or `CardVariant6` just because values repeat.

## Process

1. inventory repeated values/patterns;
2. cluster by semantic role;
3. decide canonical tokens/primitives;
4. migrate real usage;
5. remove redundant/dead variants when safe;
6. test states/themes/responsive contexts;
7. verify rendered behavior did not regress.

## No invention disguised as cleanup

Tokenization should not silently introduce a new color palette, radius language, spacing scale, or component redesign unless the user asked for that broader system change.

If repeated patterns are bad, redesign/refine them first, then tokenize the proven result.

## Naming

Prefer role-based names that survive theme changes: `surface-raised`, `text-muted`, `action-primary`, `space-section`, `radius-control` rather than names tied only to current color/value.
