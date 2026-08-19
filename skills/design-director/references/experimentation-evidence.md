# Experimentation and evidence

Use when the user asks to optimize conversion/activation/retention, cites product metrics, or wants confidence that a design change "works".

## Evidence ladder

Label important claims internally as one of:

1. **Observed in this product** — direct analytics, session observation, research, support evidence, or reproducible behavior.
2. **Validated external evidence** — applicable study/standard/credible benchmark with context.
3. **Design heuristic** — useful general pattern with known exceptions.
4. **Hypothesis** — plausible but unverified in this product.

Do not present level 3/4 as product fact.

## Experiment bar

Before an A/B or controlled experiment:

- name the decision the test should inform;
- define primary metric and guardrails;
- specify population/segment and exposure unit;
- estimate whether enough traffic/events exist for a useful test;
- avoid changing many causal mechanisms at once unless testing a deliberately bundled redesign;
- define minimum run conditions before looking at results;
- record material instrumentation changes.

When sample size is insufficient, use qualitative research, usability tests, session evidence, prototypes, or larger directional changes rather than pretending a tiny numeric difference is significant.

## Causality discipline

A before/after change is not automatically causal. Check for:

- traffic-source mix;
- seasonality/time effects;
- simultaneous product/price/campaign changes;
- instrumentation changes;
- novelty effects;
- sample composition;
- regression to the mean.

## Metrics hierarchy

Prefer metrics that represent value over vanity activity. Examples:

- landing page: qualified next-step completion + downstream quality;
- onboarding: first meaningful value + TTV + retained behavior;
- product surface: task completion, error/recovery, repeat success;
- monetization: paid conversion plus activation/retention/refund guardrails;
- retention: recurring valuable behavior, not forced session length.

## Design decision record

For meaningful outcome experiments, capture:

- observation;
- hypothesis/mechanism;
- changed surface;
- expected user behavior;
- primary metric/guardrails;
- evidence confidence;
- result;
- keep/revert/iterate decision.

This can live in the existing design decision log when the project wants persistent documentation.
