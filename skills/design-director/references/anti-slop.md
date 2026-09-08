# Anti-slop diagnostic

Generated-looking design usually comes from a bundle of unearned defaults, not one forbidden component. Detect patterns in context and replace them with decisions rooted in the prompt invariants and surface job.

## Core tells

### Tech gradient
Blue/purple/cyan gradients used as a generic signal of modernity.
Fix: choose a color strategy tied to product emotion, proof, and semantic roles.

### Generic tech hue
Indigo/cyan CTA and status language applied because the product is "tech".
Fix: choose authored hue/value relationships or intentionally restrained neutrals.

### Equal feature tiles
A repeated three/four-card grid with equal weight despite unequal importance.
Fix: expose hierarchy, sequence, comparison, or a stronger domain-native proof object.

### Accent rail
A colored side stripe used as instant "visual interest" without structural meaning.
Fix: clarify hierarchy with layout, type, state, or semantic edge treatment.

### Unearned blur / glass
Blur used because depth was never decided.
Fix: choose a depth model: flat/border-led, surface-led, shadow-led, or intentionally glassy where context supports it.

### Monument stat
A giant number exists to fill space rather than answer a user question.
Fix: connect metrics to change, target, comparison, threshold, or action.

### Icon topper
Every card starts with an icon in a rounded square regardless of content.
Fix: use icons only when they improve scanning or recognition; let stronger artifacts lead.

### Center stack
Everything centered because alignment was never decided.
Fix: derive alignment and reading/working path from task and evidence.

### Default type
A familiar web font chosen by reflex with no product reason, especially on brand surfaces.
Fix: select type by content, register, physical/domain associations, availability, and hierarchy needs.

### Wrong surface
A dashboard behaves like a landing page, a settings screen like a gallery, or a compare task like isolated cards.
Fix: return to surface taxonomy.

## Additional frequent tells

- bento layout without task-based grouping;
- pills everywhere rather than where shape semantics support them;
- gradient text as identity substitute;
- dark terminal/mono treatment for any developer product;
- navy serif for every legal/finance product;
- white/teal for every health product;
- decorative glow/noise/grid backgrounds with no content relationship;
- duplicated headline/subheadline prose that says little;
- every section using the same left-copy/right-card composition;
- nested cards used to solve hierarchy;
- stock proof objects that could belong to another product.

## Marketing / portfolio tells

Brand surfaces often accumulate a separate class of generated-looking decoration. Treat these as **signals to inspect**, not blanket bans:

### Repeated eyebrow / micro-label rhythm
Every section starts with tiny uppercase, wide-tracked metadata even when the label adds no orientation.
Fix: keep labels only where they genuinely categorize, sequence, or orient; let headings stand alone elsewhere.

### Decorative section numbering
`01 / CAPABILITIES`, `002 · WORK`, image counters, and pseudo-index labels are added because the model wants graphic structure rather than because sequence matters.
Fix: use numbering only when the sequence is meaningful to the story/task.

### Fake operational chrome
Weather, city/time strips, build/version strings, sync timestamps, availability/status dots, terminal metadata, or "live" indicators appear on a marketing page without a product/content reason.
Fix: remove decorative operations metadata; keep only real state that changes user understanding/action.

### Decorative status dots
Colored dots precede nav items, labels, feature rows, or badges without representing actual status.
Fix: reserve state indicators for semantic state.

### Fake product preview
A dashboard, terminal, task list, or "screenshot" is fabricated from decorative rectangles and presented as product proof.
Fix: use an actual product screenshot/artifact, a real executable mini-preview, or clearly label a concept/mock. Generated/illustrated atmosphere is not product evidence.

### Fabricated precision
Metrics, percentages, specs, reservations, customer counts, or performance numbers exist mainly to make the composition feel credible.
Fix: use real data, clearly labeled sample/mock values, or no number.

### Section-layout loop
Multiple adjacent sections repeat the same image/text split, equal-card row, eyebrow-headline-body stack, or symmetric rhythm despite different content jobs.
Fix: vary composition when the content relationship changes; repetition is good when it is a system, bad when it is the model's only idea.

### Decorative craft copy
Poetic micro-meta, fake workshop/archive language, invented field notes, atmospheric version stamps, or clever labels create a "designed" mood but say little.
Fix: use concrete product/brand language unless the actual editorial voice earns the flourish.

## Diagnosis rules

- One tell is not a conviction. Look for co-occurrence and unearned repetition.
- Never ban a pattern just because AI often uses it. A centered composition, glass surface, Inter, serif, card grid, eyebrow, status dot, em dash, or dark theme can be correct when the task earns it.
- Domain stereotypes count as smells when they substitute for a current-brief decision.
- Prompt drift is a stronger smell than fashion: wrong name, wrong artifact, wrong proof, or reused copy/layout from another task.
- Marketing proof must obey `design-evidence.md`: atmosphere and mockups are not automatically factual product evidence.

## Treatment order

Fix the highest-leverage cause first. Typical order:
1. prompt fidelity / surface mismatch;
2. composition and hierarchy;
3. proof object and identity;
4. color/type system;
5. depth/edges/components;
6. motion and decorative effects;
7. residual polish.

## Verification

After deslop:
- stranger test: does it still read instantly as generic generated UI?
- regression test: did removing tells create incoherence or usability loss?
- evidence test: are product screenshots/metrics/status claims real or clearly labeled as sample/concept?
- repetition test: are micro-labels, dots, metadata, and section layouts serving meaning rather than decorating every region the same way?
- reality test: are changes visible in actual files/render?
- judgment test: can each conspicuous choice be explained by the product?

Do not require three persistent reports before deslop. Use existing reports when present; otherwise run the necessary diagnostics internally.
