# Skill framing: role/metaphor vs detailed rules

Does the *form* in which a skill is written change behaviour, holding its content fixed?
The working hypothesis (Oct 2026): a skill written as a role or a way of doing things
generalises better than one written as detailed rules, which the model over-applies
until it becomes a list of prohibitions patched on top of each other.

Not the same question as `agent-scaffolding-experiments` (skill vs no skill). Here every
condition has a skill; only its framing changes.

## Conditions

- **0 · none** — the task alone (control).
- **A · rules** — the guidance as a checklist with explicit prohibitions.
- **C · patched** — rules after successive corrections, ending in a natural-language conditional.
- **B · role** — the same intent as a way of doing it ("as you'd tell a colleague").

## Skills under test

| # | Skill | Kind | Letter vs spirit | Scoring |
|---|---|---|---|---|
| 1 | User-facing release notes | style | "no jargon" vs the one technical term the user needs | jargon count + omissions + blind judge |
| 2 | Client email | communication | "no internal references" vs data the client needs | regex + omissions |
| 3 | Programming tutor | pedagogy | "don't give the answer" vs a trivial fact | refusals of trivia / give-aways |
| 4 | Code review | technical judgement | checklist vs noise | seeded bugs found vs nitpicks |
| 5 | CV tailoring | factual fidelity | "tailor to the role" vs "invent nothing" | claims absent from the source CV |
| 6 | Returns policy | hard constraint | "keep the customer happy" vs saying no | out-of-policy concessions |

Pre-registered prediction: role wins on 1–3, ties on 4, loses on 5–6.

**Patch test:** apply one new piece of feedback to each version and measure regressions on
cases that previously passed.

## Controls

- **Matched length**: the four framings of a skill are written from one content spec and stay
  within ±10 % of each other in characters, so length is not the variable.
- **Fresh cases**: every framing and every test case is written before any output is seen.
  Patches for the patch test come from a dev split; regressions are measured on a held-out
  test split.

## Narration: motivating example only, not data

The narration skill is where the hypothesis came from, and it was already tested by hand:
each version was a fix for a specific video, so the last one is tuned to those cases. It is
kept as the motivating example. `skills/narration/` holds four real commits of `agilabs-video-studio/skills/explainer-script/SKILL.md`,
which went from rule to role while fixing how numbers are spoken:

| commit | framing |
|---|---|
| `a84ecb6` | rule: say only the number that carries the point (led to a video with no numbers) |
| `4ccc13f` | corrected rule with exceptions |
| `1c81e93` | natural-language conditional, "judge by ear" |
| `2d8f6fa` | role: "as you'd explain it to a colleague" |

## Running

Single-turn text via `claude -p`, Opus/Sonnet/Haiku 5.5, N≥3 per cell, run serially.
Every runner rejects invalid executions (spend-limit messages, empty output) before scoring.
