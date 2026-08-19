# Revenue-Centric Design repository audit → Design Director v3

Source reviewed: `heliocosta-dev/revenue-centric-design`, branch `main`, as available on 2026-08-14.

## Method

This audit did not treat the README as a summary substitute. I:

1. inventoried the root, `references/`, `assets/`, `updater/`, and `updater/prompts/` trees;
2. read every line of every root Markdown/config file;
3. read every line of all 10 runtime reference files and classified all 101 principle entries;
4. read the maintainer README and distillation spec line-by-line;
5. reviewed each updater Python script from its raw GitHub representation, including discovery, extraction/media normalization, staging, distillation, delta detection, metadata derivation, and refresh logic;
6. checked the current asset inventory and traced every `Visual` reference from the 101 principles to its asset filename;
7. compared each runtime idea against Design Director v2 for novelty, duplication, calibration risk, manipulation risk, and license compatibility.

See `RCD-SOURCE-FILE-INVENTORY.md` for the per-file textual/code traversal record. Binary assets have no text lines. They were assessed through the complete asset inventory plus every textual `Visual` description/reference; see `RCD-ASSET-INVENTORY.md`. The current asset directory contains 68 media files (the changelog records 66 at v1.0 plus two added later); 37 unique assets are explicitly referenced by final principle entries. The rest are source/context media and do not add runtime knowledge once the principle has been distilled.

## Executive conclusion

The repository is highly useful, but it solves a different layer than Design Director v2:

- Design Director v2: **visual/product experience quality** — composition, typography, color, state coverage, interaction, responsive behavior, accessibility, voice, surface hardening, verification.
- Revenue-Centric Design: **product outcome mechanics** — acquisition, activation, retention, monetization, experimentation, positioning, feature discipline, and behavioral levers.

The best merge is therefore not to paste 101 principles into the visual skill. v3 adds an original **Outcome Layer** that lets Design Director recognize and route these problems, plus focused first-party references for ethical product design. The upstream RCD skill remains an optional external specialist.

## Critical license decision

The upstream repository is source-available, not OSI open source. Its terms require attribution, prohibit use of its material for gambling/betting/casino and specified real-money gaming contexts, and require copies/derivatives to preserve those terms.

Therefore v3 deliberately does **not** vendor or copy the 101-principle library into the MIT core. Instead:

- original general-purpose outcome/product-design guidance was written for v3;
- `revenue-centric-design` can be installed separately with `--revenue`;
- companion routing preserves the upstream restrictions;
- `THIRD_PARTY.md` makes the boundary explicit.

This avoids accidentally relicensing restricted source material as MIT.

---

# File-by-file assessment

## Root `.gitignore`

**Useful:** clear separation between tracked skill knowledge and untracked secrets/regenerable updater artifacts.

**Merged idea:** v3 maintainer guidance keeps runtime knowledge separate from staging/source ingestion. No need to copy the exact ignore file.

## Root `CHANGELOG.md`

**Useful:** distinguishes release date from source-coverage date and records principle-count changes.

**Merged idea:** future Design Director knowledge updates should record meaningful knowledge changes, not bump metadata merely because tooling ran.

## Root `LICENSE`

**Essential:** changes the merge strategy. See license decision above.

**Not copied:** upstream restricted content remains external.

## Root `README.md`

Strong architecture:

- concise mission and trigger conditions;
- progressive disclosure rather than loading all 101 principles;
- theme counts and clear routing table;
- a small conceptual spine;
- provenance and update coverage;
- explicit usage boundary.

**Merged:** progressive outcome routing, companion boundary, maintainer/source-of-truth discipline.

**Not merged literally:** the 9 RCD principles and RCD terminology are upstream material.

## Root `SKILL.md`

Strongest runtime ideas:

- activates on product outcome questions rather than only visual-design words;
- routes to one/few relevant theme files;
- uses a stable principle schema (trigger → action → evidence/source);
- values named mechanisms and evidence;
- keeps a hard source-license boundary in the runtime instruction.

**Merged:** v3 adds outcome-sensitive routing and evidence confidence, while keeping Design Director as the visual/UX director.

**Changed:** named behavioral mechanisms are not automatically treated as good tactics; v3 runs them through an ethical-persuasion gate first.

---

# Runtime reference themes

## `references/conversion-and-landing-pages.md` — 16 entries

### High-value ideas merged

- diagnose audience/buying context and awareness before cosmetic CTA changes;
- treat hero/message/proof/visual positioning as a causal chain rather than isolated style choices;
- CTA copy should make the next action and commitment predictable;
- qualification belongs in product/page architecture when it improves lead quality;
- social proof should be specific and verifiable;
- copy/layout/contrast/trust interact; copy is not an isolated layer;
- avoid cloning visible layouts while ignoring customer research and product context;
- design for rapid comprehension and scanning;
- evaluate landing changes using actual outcome evidence when available.

### Calibrated rather than copied

- exact star-rating ranges are context-sensitive, not a universal design target;
- "5-second" is kept as a fast comprehension test, not literal scientific law for every page;
- "ugly converts" becomes **performance does not excuse weak visual craft, and beauty does not prove outcome**;
- cold-vs-warm traffic is treated as a segmentation/confounding issue, not a universal exact baseline correction.

### Rejected as universal rules

- kill all outbound links;
- use aggressive scarcity as a default conversion lever;
- repeat CTA/urgency simply because it can raise clicks;
- any numeric conversion case study as a general expected uplift.

### v3 destination

`product-outcomes.md`, `conversion-monetization.md`, `ethical-persuasion.md`, `experimentation-evidence.md`.

## `references/onboarding-and-activation.md` — 19 entries

### High-value ideas merged

- onboarding should drive useful behavior/value rather than narrate features;
- distinguish signups/tour completion from meaningful activation;
- define a first useful outcome and time/latency to value;
- blank first-run states need orientation and a dominant next action;
- observe real user journeys instead of trusting designed flow diagrams;
- separate useful/necessary friction from administrative friction;
- deliver value before teaching all mechanics;
- reduce TTV by reordering/removing steps before inventing features;
- onboarding pattern depends on user context and flow complexity;
- use sample/preview state when it genuinely demonstrates the destination.

### Calibrated

- benchmark numbers for activation/TTV/retention remain external context, never hard quality gates;
- card-upfront trial and mandatory onboarding are not assumed to be beneficial;
- progress bars do not start at an arbitrary nonzero percentage unless that percentage is truthful;
- a single retained-user behavior can be useful evidence, but not assumed causal without validation.

### Rejected

- forced commitment or Zeigarnik-like unfinished loops when the purpose is compulsion rather than useful progress;
- universal claims that early churn is always onboarding rather than product, audience, pricing, reliability, or expectation mismatch.

### v3 destination

`activation-retention.md`, `product-outcomes.md`, `experimentation-evidence.md`, `ethical-persuasion.md`.

## `references/churn-and-retention.md` — 9 entries

### High-value ideas merged

- acquisition economics and retention are connected;
- recurring value should compound through workflow, history, personalization, collaboration, and user-created artifacts;
- communicate meaningful product/plan changes proactively;
- cancellation is a designed product surface, not an afterthought;
- expectation mismatch can begin before signup;
- repeated support confusion is product-design evidence;
- plain language reduces avoidable support/friction;
- one-time jobs may require a different product/business model rather than fake engagement.

### Reframed for safety/ethics

Upstream material sometimes frames switching cost and retention in aggressively revenue-oriented language. v3 reframes this as **compounding user value with appropriate portability**, never artificial lock-in.

### Rejected

- engineering "addiction" as a product goal;
- intentionally making leaving harder;
- deliberately withholding/export-blocking user-created data to create retention.

### v3 destination

`activation-retention.md`, `ethical-persuasion.md`, `product-outcomes.md`.

## `references/pricing-and-monetization.md` — 11 entries

### High-value ideas merged

- pricing structure should reflect value/economics rather than copying the cheapest competitor;
- freemium/trial design depends on cost-to-serve, TTV, intent, and downstream quality;
- pricing tables need a coherent comparison/value axis;
- upgrade moments are strongest when contextual to a real capability/usage boundary;
- trial length should reflect time to meaningful value, not a conventional number of days;
- comparison order and hierarchy matter.

### Calibrated

- Good/Better/Best is an optional comparison structure, not a universal pricing architecture;
- anchoring and decoys can clarify comparison, but are high-risk when used to trick rather than inform;
- requiring a card can alter user quality and conversion but is not assumed superior;
- the "middle plan" does not automatically deserve forced visual dominance.

### Rejected

- hiding a free option specifically to manipulate comparison;
- engineered deceptive decoys;
- concealed auto-renewal/commitment;
- optimizing paid conversion while ignoring activation, retention, refunds, complaints, or informed consent.

### v3 destination

`conversion-monetization.md`, `ethical-persuasion.md`, `experimentation-evidence.md`.

## `references/behavioral-science-toolkit.md` — 7 entries

### High-value ideas merged

- founders/designers suffer from expert blindness; test comprehension with unfamiliar users;
- defaults have behavioral power;
- post-action reassurance can reduce uncertainty;
- accumulated value can be made visible;
- specificity can improve credibility when true;
- hierarchy should direct attention;
- cognitive load is finite.

### Major v3 improvement

Behavioral science is no longer treated as a toolbox where every lever is inherently desirable. `ethical-persuasion.md` classifies reversible/truthful uses versus high-risk/dark-pattern uses.

### Rejected/calibrated

- fabricated precision;
- defaults that silently assume payment/consent;
- loss aversion as a license for pressure;
- artificial lock-in;
- reducing choice so far that alternatives become hidden.

## `references/product-strategy-and-features.md` — 7 entries

### High-value ideas merged

- a feature has cognitive/IA/support/maintenance cost after it ships;
- low adoption may be a context/discoverability/timing problem rather than a communication problem;
- feature scope should strengthen the product's core job/claim;
- attention is a finite budget;
- all-in-one expansion can dilute clarity.

### Calibrated

- fixed feature-count thresholds and a fixed "Swiss Knife Index" are treated as optional heuristics, not laws;
- low usage alone is insufficient to delete a feature (rare but critical workflows exist).

### v3 destination

`feature-discipline.md`.

## `references/revenue-centric-design.md` — 13 entries

### High-value ideas merged at architecture level

- design should account for both user value and sustainable product outcome;
- design owns flows/behavior, not only surface styling;
- find the leak/root cause before redesigning;
- refactor/redesign should solve a verified problem;
- preserve useful learned cognitive maps during major redesigns;
- treat interface changes as hypotheses when outcome data exists;
- operational dashboards should help the user determine a next action.

### Calibrated

- product-stage prescriptions are useful lenses, not hard rules about when design "matters";
- claims that better design beats better tech are context-dependent;
- outcome metrics do not replace accessibility, trust, product correctness, or qualitative research.

### v3 destination

`product-outcomes.md`, existing `surface.md`, `verification.md`, and `experimentation-evidence.md`.

## `references/positioning-icp-and-gtm.md` — 8 entries

### Useful for Design Director

- define ICP by real buying/usage criteria rather than shallow demographics;
- positioning specificity reduces generic design/copy;
- distinguish a distribution problem from an on-surface experience problem before redesigning;
- funnel math can expose where visual work is unlikely to be the bottleneck.

### Kept outside core runtime design

- TAM/SAM/SOM modeling;
- referral-program incentive strategy;
- founder sales/pricing tactics;
- channel-selection/Bullseye framework;
- rigid PLG qualification thresholds.

These belong in a growth/GTM specialist, not a universal interface director. The optional RCD companion can cover them.

## `references/ai-era-differentiation.md` — 7 entries

### High-value ideas merged

- faster implementation does not solve weak activation or user value;
- identical underlying technology can still differentiate via workflow/UX/domain fit;
- feature-list parity creates commoditization;
- attention and cognitive load become more important as products become easier to build;
- product proof should show actual use/value rather than generic AI claims;
- avoid source-of-truth drift across design/code tooling;
- recovery, reliability, content truth, and human context distinguish polished product from a generated shell.

### v3 destination

`product-outcomes.md`, existing `voice.md`, `surface.md`, `implementation.md`.

## `references/metrics-and-experimentation.md` — 4 entries

### High-value ideas merged

- signups/activity are not automatically value/traction;
- underpowered A/B tests should not be overinterpreted;
- signal quality matters more than vanity count;
- translate outcome changes into the metric that actually drives the decision.

### v3 destination

`experimentation-evidence.md` and outcome-aware scorecard.

---

# Assets audit

The repo uses assets as source evidence/visual context, not as the primary runtime knowledge store.

Current directory: 68 media files (67 JPGs + 1 MP4 by directory inspection). Runtime principle files explicitly reference 37 unique asset files through `Visual` fields.

### What is useful for our super skill

The **pattern** is useful: keep an image only when it carries information that text would lose (framework, chart, annotated good/bad UI, interaction sequence). Decorative analogy/source images should not be copied merely because they existed in the source post.

### What v3 does

No RCD assets are bundled. Reasons:

1. upstream license boundary;
2. many are source-specific examples rather than universal runtime inputs;
3. the upstream companion can load them when installed;
4. Design Director should prefer project screenshots/real UI over generic source imagery during actual work.

---

# Maintainer/updater audit

## `updater/README.md`

This is one of the most useful files in the repository architecturally.

### Merged ideas

- runtime reference files are the source of truth;
- discovery and curation are separate steps;
- fetch/stage only the delta so updates are idempotent;
- LLM distillation is a draft, human review is the curation gate;
- updates are additive by default;
- framework supersession is explicit rather than silently overwriting history;
- metadata/counts are derived from actual content;
- secrets and bulk source data stay outside runtime skill footprint.

### v3 result

Added `MAINTAINING.md`, `templates/principle-entry.md`, and `scripts/catalog.py`.

## `updater/prompts/distill.md`

### Strong pattern

A knowledge item has a stable shape: reusable principle, trigger, concrete action, optional evidence/visual/voice, provenance, and exactly one routing theme.

### v3 adaptation

Our schema is deliberately stricter for general-purpose agent guidance:

`Principle → Trigger → Action → Evidence level → Calibration → Verification → Provenance/license`

The added **Calibration** field prevents numeric anecdotes from becoming universal laws; **Verification** tells the agent what observable result should confirm the rule.

## `updater/discover_new.py`

### Useful

- discover all candidates after coverage cutoff;
- optional model ranking is triage, not automatic inclusion;
- human curation remains separate.

### v3 principle

Never let a crawler/search result auto-write runtime design doctrine.

## `updater/fetch_posts.py`

### Useful

- preserve raw source fidelity before distillation;
- resolve quoted/related content;
- preserve media and alt/context information;
- normalize source into a model-readable staged representation;
- separate raw/source data from final curated knowledge.

### v3 principle

For future knowledge ingestion, preserve provenance and raw material separately from the runtime paraphrase.

## `updater/update.py`

### Useful

- compute delta against already-included material;
- make re-runs safe/idempotent;
- stage new material instead of directly mutating references;
- move only approved informational assets into runtime.

### v3 principle

Updates should be staged and reviewable before they touch runtime references.

## `updater/distill.py`

### Useful

- structured output (theme + entry) rather than uncontrolled prose;
- validates model output before it enters the library;
- separates automated draft from human approval.

### v3 principle

Machine-generated doctrine is a candidate, not authority.

## `updater/skill_lib.py`

### Excellent architecture

- derives included IDs/counts/coverage from the actual reference files;
- avoids a second manifest that can drift;
- deterministic metadata logic is separate from editorial judgment.

### v3 result

`scripts/catalog.py` now discovers references, templates, evals, and explicit modes from the skill tree itself.

## `updater/refresh_meta.py`

### Useful

- computed metadata can be checked before mutation;
- idempotent/no-op updates should not imply editorial change;
- update date is an editorial decision, not just filesystem activity.

### v3 principle

Do not claim a new knowledge version because a formatter/catalog script ran.

## `updater/.env.example`

### Useful

- credentials are explicitly separated from tracked repo content;
- required vs optional API credentials are documented.

No runtime change needed.

## `updater/requirements.txt`

### Useful

- core tooling remains stdlib-only; LLM dependency is optional.

This supports a small maintenance footprint. v3's catalog/validator likewise uses stdlib where possible (validator still optionally uses PyYAML when available).

## `updater/posts.txt`

A rebuild/source manifest, not runtime knowledge. Useful for reproducibility but not something Design Director should load.

## `updater/new_posts.txt`

A human-curated staging input, not runtime knowledge. The separation itself is useful; the URLs are not.

---

# Rules deliberately NOT imported as doctrine

These source ideas are useful only with strong calibration, or are inappropriate as general-purpose Design Director defaults:

- fake or manufactured scarcity;
- obstructive cancellation;
- artificial switching cost;
- compulsion/addiction engineering;
- hiding a cheaper/free plan to force comparison;
- card-required trial as universal best practice;
- Good/Better/Best as universal pricing structure;
- fixed activation/TTV/retention benchmark cutoffs as quality laws;
- exact review-star targets as universal conversion rules;
- "all outbound links lose conversion";
- "ugly pages convert better" as a visual prescription;
- fixed feature-count/index thresholds as deletion laws;
- one observed correlation treated as causal activation behavior;
- funnel/PLG/GTM thresholds presented as universal product-design facts.

v3 retains the useful causal question while removing the dogma.

---

# Net changes to Design Director v3

## New runtime references

1. `product-outcomes.md`
2. `ethical-persuasion.md`
3. `activation-retention.md`
4. `conversion-monetization.md`
5. `experimentation-evidence.md`
6. `feature-discipline.md`

## Updated runtime files

- `SKILL.md` — outcome-aware activation and specialist routing;
- `routing.md` — lifecycle/outcome routing;
- `companion-routing.md` — separately licensed RCD specialist;
- `audit-scorecard.md` — outcome fit folded into the existing 15-point task/surface dimension;
- `EVALS.md` — 12 new growth/outcome/ethics test cases.

## New maintenance files

- `MAINTAINING.md`
- `templates/principle-entry.md`
- `scripts/catalog.py`

## Installer

`--revenue` optionally installs `heliocosta-dev/revenue-centric-design` from upstream without bundling it.

---

# Final judgment

**Worth merging? Yes, strongly — but as an outcome layer, not as a replacement visual philosophy.**

The source's strongest contribution is making Design Director ask a second class of questions:

- "Is this interface well designed?" **and**
- "Is it solving the right user/product outcome, with evidence, without manipulation?"

That combination is materially stronger than either skill alone.
