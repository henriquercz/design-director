# Maintaining Design Director knowledge

v3 adopts a source-of-truth discipline: runtime references are the authoritative knowledge. Documentation and counts should be derived or validated from the files rather than maintained as independent truth.

## Ingestion workflow

```text
discover source → stage source → assess scope/license → distill → human review → merge/supersede → validate → changelog
```

### 1. Discover, do not auto-adopt
Candidate material is a queue, not knowledge. Keep discovery separate from curation.

### 2. Preserve provenance
Keep the original URL/source metadata in maintainer notes. Do not let paraphrased runtime guidance become the only record of where a rule came from.

### 3. Distill into a standard entry
Use `templates/principle-entry.md`:
- principle;
- trigger;
- action;
- evidence level;
- calibration/exceptions;
- verification;
- provenance/license notes.

### 4. Human review before merge
Check truth, scope, ethics, redundancy, license, overly universal numbers, and whether the rule actually improves agent decisions.

### 5. Prefer additive history; supersede explicitly
Do not silently rewrite a prior rule when a new source contradicts it. Mark the old guidance superseded or revise it with a decision note explaining why.

### 6. Runtime stays progressively disclosed
The main `SKILL.md` should route. Detailed knowledge belongs in focused `references/` files and should load only when useful.

### 7. Validate derived structure
Run:

```bash
python scripts/catalog.py
python scripts/validate.py
```

The catalog discovers references/evals directly from the tree; it is not a second manifest.
