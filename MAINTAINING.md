# Maintaining Design Director knowledge

v4 uses a source-of-truth discipline: runtime references are the authoritative knowledge. Documentation and counts should be derived or validated from files rather than maintained as independent truth.

## Ingestion workflow

```text
discover source → stage source → assess scope/license → distill → calibrate → human review → merge/supersede → validate → provenance/changelog
```

### 1. Discover, do not auto-adopt
Candidate material is a queue, not knowledge. Keep discovery separate from curation.

### 2. Preserve provenance
Keep original URL/source metadata in maintainer notes (for example `V4-RESEARCH-AUDIT.md`). Do not let paraphrased runtime guidance become the only record of where a rule came from.

### 3. Separate evidence from inference
When a source claims a project/system behavior, distinguish:
- normative contract/standard;
- observed implementation/pattern;
- heuristic;
- hypothesis/inference.

Do not promote screenshots, anecdotes, or one implementation to universal truth without calibration.

### 4. Distill into a standard entry
Use `templates/principle-entry.md`:
- principle;
- trigger;
- action;
- evidence level;
- calibration/exceptions;
- verification;
- provenance/license notes.

### 5. Human review before merge
Check truth, scope, ethics, redundancy, license, overly universal numbers, dependency assumptions, and whether the rule actually improves agent decisions.

### 6. Prefer additive history; supersede explicitly
Do not silently rewrite a prior rule when a new source contradicts it. Mark the old guidance superseded or revise it with a decision note explaining why.

### 7. Runtime stays progressively disclosed
The main `SKILL.md` should route. Detailed knowledge belongs in focused `references/` files and should load only when useful.

A new reference is justified only when it introduces a distinct decision boundary. Otherwise strengthen an existing reference.

### 8. Keep companions bounded
Do not add a third-party skill merely because it has useful content. Prefer distilled core principles when licensing allows independent guidance; use external companions only for live/specialist knowledge the core should not duplicate.

### 9. Validate derived structure
Run:

```bash
python scripts/catalog.py > CATALOG.json
python scripts/validate.py
```

The catalog discovers references/evals directly from the tree; it is not a second hand-maintained manifest.

### 10. Verify web packaging after knowledge changes
The Claude/ChatGPT builders derive from canonical `skills/design-director/`. After major knowledge changes, run:

```bash
python scripts/build-web-bundles.py
```

Confirm the new references appear in both generated knowledge packages before publishing a release artifact.
