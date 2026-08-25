# Design evidence and confidence

Design Director must distinguish what the project **declares**, what the implementation **shows repeatedly**, and what the model is merely **inferring**. Visual similarity is useful evidence, but it is not permission to invent hidden design-system rules.

## Confidence labels

Use these labels in working notes/project memory when provenance matters:

- **Normative** — explicit project/design-system documentation, semantic tokens, theme contracts, or a shared public component API defines the rule.
- **Observed** — repeated production usage, rendered DOM/computed styles, or behavior consistently demonstrates the pattern.
- **Inferred** — the pattern is plausible and useful as a working hypothesis, but the project does not prove it as a rule.
- **Unknown** — available evidence is insufficient. Do not manufacture certainty.

## Evidence precedence

When sources conflict, prefer the source closest to actual project truth:

1. explicit design-system/project documentation;
2. semantic tokens, themes, global styles, variables, type loading;
3. shared primitives/components and their current public APIs;
4. repeated real consumers in production code;
5. rendered DOM, computed styles, accessibility tree, actual interaction behavior;
6. screenshots, video, design references, visual examples;
7. model inference.

A lower source can reveal drift from a higher source. Do not silently erase that conflict: record it as implementation drift, stale documentation, or an open inconsistency.

## Repository inspection

Before claiming a project has a design rule, inspect the strongest available evidence:

- tokens/theme/global styles;
- shared layout shells and primitives;
- component variants and public props;
- icon and asset conventions;
- typography loading/fallbacks;
- representative real consumers;
- test/demo/storybook/registry examples when present.

Repeated one-off values do not automatically become a token. A wrapper used twice does not automatically become a component family.

## URL / rendered interface inspection

A live page can reveal:

- DOM structure and semantics;
- computed sizes/colors/type/spacing;
- CSS variables exposed to the client;
- responsive behavior;
- focus/keyboard states;
- loading/error/selection behavior that can be triggered;
- repeated visual relationships.

A live page generally cannot prove:

- hidden token names;
- private component APIs;
- source-level intent;
- whether two visually identical elements share implementation;
- why a value was chosen.

Phrase conclusions accordingly: "observed 16px gaps across these controls" is different from "the system spacing token is 16px."

## Screenshot / image inspection

Use screenshots for composition, hierarchy, proportion, visual language, density, alignment, imagery, and visible states.

Do **not** claim exact internal values, tokens, breakpoints, component names, semantics, or interaction rules from pixels alone. Measurements from an image are approximate unless the source provides scale/context.

If reconstruction is required, mark values as inferred and validate against the rendered result rather than pretending they were extracted exactly.

## Reference designs

A reference is evidence of a useful principle, not a command to clone implementation or brand identity. Extract the transferable idea:

- density;
- composition premise;
- proof strategy;
- navigation model;
- type contrast;
- interaction relationship;
- motion causality;
- component contract.

Then adapt it to the current product invariants.

## Writing project memory

Store durable rules as normative only when project evidence supports them. Store uncertain observations with their confidence/provenance, for example:

```text
Spacing rhythm: 4/8/12/16/24 appears repeatedly — Observed, not confirmed token set.
Dialog primitive: BaseDialog from src/ui/dialog.tsx — Normative shared API.
Hero radius: ~28px from screenshot reference — Inferred; verify in implementation.
```

Do not let an inferred aesthetic choice become permanent project truth merely because an earlier model generated it.

## Completion check

Evidence work is good enough when:

- design-system claims have an appropriate confidence level;
- hidden APIs/tokens were not invented from screenshots;
- conflicts between docs and implementation are visible rather than silently reconciled;
- the current prompt/project outranks unrelated reference patterns;
- implementation decisions can be traced to project truth, observation, or an explicitly labeled design judgment.
