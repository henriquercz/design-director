# Prompt invariants and drift control

Before designing, extract the things the visible result must prove came from **this** task.

## Invariants

### Exact identity
Use the supplied product, brand, venue, feature, person, or project name exactly unless the user asks for naming work.

### Category
The first meaningful viewport or working region should make it understandable what kind of thing this is.

### User pressure
Know why the user is here now: urgency, uncertainty, comparison, repetitive work, learning, purchase anxiety, coordination, etc.

### Job
What must the user monitor, operate, compare, configure, learn, decide, or explore?

### Core artifact
Find the concrete object from the domain: schedule, contract, map, room, queue, invoice, route, chart, lesson, playlist, order, file, canvas, match, workout, inventory object, etc.

The UI should be shaped around this artifact rather than generic SaaS furniture.

### Proof / evidence
What visible evidence would make the user believe the product works? Examples: a real itinerary, before/after state, live status, example contract, actual chart, route, result, preview, comparison, testimonial tied to an outcome.

### Constraints
Preserve technical, content, brand, accessibility, performance, legal, and product-scope limits.

### Forbidden drift
Refuse accidental carryover from:
- previous generated screens;
- unrelated templates;
- category stereotypes;
- remembered sample names/copy;
- a reference brand that was meant only as inspiration.

## Divergence check

Before shipping a newly generated surface, compare it with recent design shapes in context. If the new task repeats the same spatial premise, proof-object type, alignment habit, button family, headline pattern, palette mood, or navigation shape without a task-specific reason, change the premise rather than merely changing the accent color.

## Generic-proof test

If the main proof object could be dropped into an unrelated product after changing only the logo/headline, it is too generic. Replace it with a domain-native artifact.
