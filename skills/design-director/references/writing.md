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

## Brand copy that carries value

Brand copy is not decoration and not filler. It is the fastest channel for communicating what a product is, who it is for, and why it is worth attention. Slop appears here when copy stops carrying value and starts performing.

**Value, not adjectives.** Every claim should answer a buyer question: what does this do, for whom, versus what, and how do I know? "Elevate your workflow" carries no value; "Reconcile three payment providers against one ledger" does. Prefer the concrete verb and the specific object over the category noun.

**Specific beats sweeping.** Name the actual constraint, workflow, or condition the product addresses. Vague superlatives ("the best", "seamless", "powerful") are unearned and read as interchangeable filler. When a real number, limit, or condition exists, use it; when it does not, describe the mechanism instead of inventing precision.

**Earn the flourish.** Rhythm, wit, metaphor, and a distinctive voice are what keep brand copy from reading like a template. They are earned by the specific idea, not applied on top of a generic one. If the sentence would fit any product in the category, it is decoration — rewrite around what only this product can say.

**Say the hard thing.** Premium and luxury claims are the highest-risk zone for slop: restraint, exclusivity, precision, and heritage are easy to assert and easy to render as empty adjectives. Name the concrete reason for the premium — the material, the tolerance, the constraint, the person — rather than the adjective that labels it.

**One claim per surface.** Do not stack overlapping promises in adjacent sections; repetition reads as an inability to choose. Vary composition and rhythm without varying the underlying claim.

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
