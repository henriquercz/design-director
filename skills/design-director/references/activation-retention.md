# Activation, onboarding, and retention

Use for first-run flows, empty states, setup, trials, early lifecycle, recurring workflows, cancellation, and recovery.

## Activation thesis

Activation is not completion of onboarding UI. It is the earliest observable moment where the user experiences or creates meaningful value.

Define:

- the first useful outcome;
- the behavior that produces it;
- time-to-value (TTV) or an equivalent latency-to-value measure;
- the minimum setup genuinely required;
- what evidence would distinguish retained from non-retained users.

Do not assume the activation event from convention; infer it from the product job and validate with data when available.

## First-run bar

A first-run experience should:

- orient the user without turning into a feature tour;
- make one useful next action dominant;
- avoid blank, consequence-free dashboards when sample/preview/example state can teach the destination;
- remove administrative work that does not help the current task;
- ask for intent/preferences only when they genuinely personalize or route the experience;
- show real progress when a multi-step setup is unavoidable;
- allow experienced users to skip education that is not required for safety or correctness.

## Empty state bar

An empty state answers:

1. what belongs here;
2. why it matters;
3. what action creates the first useful object;
4. what the result will look like when appropriate.

Use sample data only when clearly labeled and when it helps users understand the target state.

## Friction placement

Do not optimize for minimum clicks. Classify friction:

- **necessary/safety friction** — prevents costly mistakes or establishes required intent;
- **value-producing friction** — configuration that improves the result enough to justify effort;
- **administrative friction** — data collection or steps that mostly serve internal process.

Remove or defer administrative friction first. Preserve necessary friction. Test value-producing friction against TTV and outcome quality.

## Retention and recurring value

Improve retention by making recurring value easy to resume and recognize:

- preserve state and context;
- make next actions clear on return;
- support undo/recovery;
- communicate meaningful changes before they become surprises;
- make accumulated user-created value visible and exportable where appropriate;
- treat repeated support/confusion as product evidence;
- align landing-page promises with the actual first-run experience.

## Cancellation and exit

Cancellation is part of the product surface. It must:

- be findable and understandable;
- state the real consequence and effective date;
- preserve/export data according to policy;
- offer alternatives only when genuinely useful;
- allow a clear path to complete cancellation without obstruction;
- collect reasons optionally and respectfully;
- confirm completion and recovery/reactivation options when available.

Never manufacture retention by making exit confusing or exhausting.
