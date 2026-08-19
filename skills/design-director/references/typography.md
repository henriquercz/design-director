# Typography system

Typography is information architecture plus voice. Font choice is only one part.

## Roles before sizes

Define semantic roles appropriate to the product: display, page title, section heading, subheading, body, label, caption/meta, code/data, numeric emphasis, etc.

Not every text block needs exactly three layers. Use as many distinct roles as the content hierarchy actually requires, while avoiding needless micro-steps.

## Contrast

Adjacent hierarchy levels should be clearly distinguishable through a combination of size, weight, width, case, color, spacing, and placement. Do not force a universal ratio.

## Measure and line height

Readable long-form body copy commonly benefits from a moderate line measure, but tune to typeface, language, device, and task. Dense product UI can be narrower; editorial content can be longer. Avoid rigid universal character counts.

## Register

### Product
System sans faces are legitimate. Optimize for legibility, numeric/data behavior, compact UI, language coverage, loading reliability, and consistent metrics.

### Brand
Typeface can carry more identity. Choose from the product's physical/domain associations, emotional posture, imagery, and content—not from trend reflex.

## Pairing

Use one family well before adding a second. Add another family only when it creates a useful role contrast. Check x-height, width, weight range, punctuation, numerals, and language coverage.

## Data

Use tabular numerals where alignment matters. Prevent changing number widths from causing jitter in dashboards, timers, prices, and tables.

## Real content stress

Test:
- long names;
- short and missing labels;
- large/small numbers;
- multi-line buttons only when unavoidable;
- translated strings;
- RTL scripts if supported;
- dynamic values and truncation.

## Loading and fallback

Verify custom fonts really load. Provide defensible fallback stacks and avoid layout shifts from radically different metrics when possible.

## Dark surfaces

Light-on-dark type can feel optically brighter/thinner depending on typeface. Tune weight, spacing, and contrast by rendered appearance rather than blindly mirroring light-mode values.

## Avoid pseudo-precision

Do not use a "reading distance equation" to generate exact font sizes for arbitrary web UIs. Choose sizes from content role, viewing context, accessibility, device, and the rendered result.
