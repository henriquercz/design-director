# Interface writing

Words are controls, state, orientation, evidence, and recovery.

## Buttons and commands

Prefer labels that name what happens: "Archive report", "Send invite", "Start import". Use short generic labels only where convention/context makes the action unambiguous.

## CTA intent consistency

For the same user intent, prefer one stable label unless a different context truly changes the action or commitment.

Avoid accidental synonym drift such as using "Get started", "Try free", and "Create account" for the exact same destination/commitment merely to make sections sound varied. Variation in visual rhythm does not require variation in command meaning.

Different actions may legitimately use different labels. Preserve consequence clarity over slogan consistency.

## Errors

An error should help recovery:
- what happened;
- why, when useful;
- what the user can do next;
- preserve input/work when possible.

Do not blame the user for the system's failure.

## Empty states

Teach the space:
- what belongs here;
- why it matters;
- how to create/import/find the first item.

"No items" is rarely enough when the user needs orientation.

## Loading

Name the real work when useful: uploading, analyzing, syncing, importing. Show measurable progress when the system actually knows it.

## Terminology

Use one term for one concept. Do not switch between workspace/project/team/account if they are not genuinely different.

## Evidence and precision

Numbers and factual claims inherit the same evidence rules as visual proof.

- use real metrics/specifications when provided or verifiable;
- label sample/mock values as sample/mock when they exist to exercise the design;
- do not invent precise percentages, dimensions, customer counts, version strings, availability, or performance claims merely because precision looks credible;
- do not turn decorative metadata into implied product facts.

## Hierarchy

Remove filler that repeats headings or delays the useful information. But do not adopt blanket punctuation bans. Em dashes, exclamation marks, title case, and other voice choices can be valid when the brand/context earns them.

## Copy self-audit

Before ship on a writing-heavy or substantially redesigned surface, re-read **every visible string that changed** (and the surrounding strings needed for context):

- headline/subhead/eyebrow;
- CTA and nav labels;
- body copy/captions;
- empty/loading/error/success text;
- form labels/helper/error text;
- alt text/accessibility labels when edited;
- social proof, stats, metadata, footer text.

Flag and repair:
- grammatically broken or ambiguous sentences;
- unclear referents ("it", "that", "we stay that way") without a clear antecedent;
- hallucinated/fake factual claims;
- forced metaphors or cute copy whose meaning does not track;
- generic filler verbs such as "elevate", "unleash", "revolutionize" when a concrete verb would say more;
- performative micro-meta that exists to sound designed rather than communicate;
- inconsistent terminology or CTA intent;
- mismatches between copy promise and actual behavior.

When personality and clarity conflict, rewrite toward clarity first, then restore voice without losing meaning.

## Localization

Allow for expansion, different word order, plural rules, number/date formats, line breaking, and RTL. Do not make narrow fixed-width labels that only survive English.

## Brand vs product

Brand copy can carry more rhythm and personality. Product copy should prioritize clarity, consequence, and predictable terminology. Both should sound specific to the product rather than generated filler.
