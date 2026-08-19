# Interface writing

Words are controls, state, orientation, and recovery.

## Buttons and commands

Prefer labels that name what happens: "Archive report", "Send invite", "Start import". Use short generic labels only where convention/context makes the action unambiguous.

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

## Hierarchy

Remove filler that repeats headings or delays the useful information. But do not adopt blanket punctuation bans. Em dashes, exclamation marks, title case, and other voice choices can be valid when the brand/context earns them.

## Localization

Allow for expansion, different word order, plural rules, number/date formats, line breaking, and RTL. Do not make narrow fixed-width labels that only survive English.

## Brand vs product

Brand copy can carry more rhythm and personality. Product copy should prioritize clarity, consequence, and predictable terminology. Both should sound specific to the product rather than generated filler.
