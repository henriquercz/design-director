# Design Director Skillset v3

A portable design workflow for **Codex**, **Claude Code**, and compatible Agent Skills hosts.

v3 keeps the visual/product-design orchestration from v2 and adds an **outcome-aware product layer** for SaaS/startup work: conversion, activation, retention, monetization, experimentation, feature discipline, and ethical persuasion.

## What v3 adds

- outcome stages: Acquire, Activate, Retain, Expand, Monetize, Differentiate;
- dual-outcome framing: user progress + business/product outcome;
- explicit evidence levels and experimentation discipline;
- onboarding/activation/TTV and retention/cancellation hardening;
- conversion/pricing/upgrade/trial guidance without deceptive CRO;
- feature-scope/adoption discipline;
- ethical-persuasion guardrails for defaults, urgency, social proof, cancellation, lock-in, and compulsion;
- optional separately licensed `revenue-centric-design` companion via `--revenue`;
- self-derived catalog tooling and a maintainer ingestion protocol;
- expanded eval suite for outcome-sensitive design.

## Architecture

```text
user goal
   ↓
design-director
   ├─ prompt invariants + project memory
   ├─ surface + Brand/Product register
   ├─ optional outcome stage + evidence level
   ├─ internal diagnosis
   ├─ smallest treatment chain
   ├─ bundled disciplines / optional companions
   ├─ implementation with real states
   └─ rendered verification + /100 score + stop rule
```

## Install

```bash
unzip design-director-skillset-v3.zip
cd design-director-skillset-v3
chmod +x scripts/*.sh

./scripts/install.sh --global --agents codex,claude-code --react
./scripts/doctor.sh
python scripts/validate.py
```

To additionally install the **separately licensed** Revenue-Centric Design specialist:

```bash
./scripts/install.sh --global --agents codex,claude-code --react --revenue
```

That companion is fetched from its own repository and is **not bundled** in this MIT archive. Its upstream attribution and field-of-use restrictions remain in force.

## Use

Normally just state the goal.

Codex:

```text
$design-director Improve this SaaS onboarding. Find the real activation friction, preserve the product's functionality, fix the highest-impact design issues, and verify the result.
```

Claude Code:

```text
/design-director Improve this pricing page. Make the plans easier to compare and improve qualified conversion without deceptive tactics.
```

Explicit modes are still available when you want scope control (`review`, `relayout`, `surface`, `voice`, `outcome`, etc.).

## Repository-analysis rationale

- `MERGE-ANALYSIS.md` — Command Code → v2 analysis.
- `RCD-REPOSITORY-AUDIT.md` — line-by-line/file-by-file assessment of `heliocosta-dev/revenue-centric-design` and what v3 did with it.
- `MAINTAINING.md` — v3 knowledge-ingestion and source-of-truth protocol.
- `THIRD_PARTY.md` — companion licenses/boundaries.
