# Skill framing: rule vs way of doing it

Does the *form* in which a skill is written change behaviour, holding its content fixed?
The working hypothesis (Oct 2026): a skill written as a role or a way of doing things
generalises better than one written as detailed rules, which the model over-applies until it
becomes a list of prohibitions patched on top of each other.

Not the same question as `agent-scaffolding-experiments` (skill vs no skill). Here every
condition has a skill; only the framing of one part of it changes.

## Where it came from

A narration skill for explainer videos (`agilabs-video-studio/skills/explainer-script`). The
author asked it not to string together non-round numbers; the next video said no numbers at
all; the rule then grew into a natural-language `if`; it was finally fixed by describing a way
of narrating: "as you'd explain it to a colleague". `skills/narration/` holds the four real
commits:

| commit | framing |
|---|---|
| `a84ecb6` | rule: say only the number that carries the point (led to a video with no numbers) |
| `4ccc13f` | corrected rule with exceptions |
| `1c81e93` | natural-language conditional, "judge by ear" |
| `2d8f6fa` | role: "as you'd explain it to a colleague" |

It is the motivating example, not data: it was tested by hand and each version is tuned to
the video that provoked it. Everything below uses fresh material.

## Result in one paragraph

When a correction **caps a quantity** ("say at most the one figure that carries the point"),
writing it as a rule makes every model tested drop the figure the message needed, and the
more capable the model the more often it does (Opus 6/18 and gpt-6-astra 4/18 keep it, against
18/18 with the same correction written as a way of speaking). Written as a way of doing it, the
correction never loses the essential, but it only changes behaviour much on the large models:
the small ones keep reciting exact figures. When the correction is plain **restraint** (be
shorter, drop the caveats), the rule works as well or slightly better. There is no universal
winner; the failure mode of the rule is the cap read to the letter.

## Experiment 2: corrections (`corrections/`)

The original observation was about a **correction** over-applied by Opus on a **graded**
criterion, so the design reproduces that:

- a realistic base skill (several sections) that produces too much of some behaviour X;
- a correction appended either as a **rule** (R) or as a **way of doing it** (W), carrying the
  same content, exception included, within ±10 % length; plus the base alone (0);
- three cases where X is still needed and three where it is not. Over-correction = X gone
  where it was needed.

Five corrections people actually give, all written before any output was seen
(`corrections/tasks.py`):

| task | base skill | rule (R) | way of doing it (W) |
|---|---|---|---|
| numbers | spoken briefing for an internal podcast | "say at most the one figure that carries the point… never several unround numbers in a row" | "say numbers the way you'd tell a colleague over coffee… the only thing to avoid is reading a table aloud" |
| questions | engineering assistant | "stop asking… only ask first if a wrong assumption would be costly" | "work like a senior contractor the team trusts… only pick up the phone when a wrong guess would cost real work" |
| hedging | DIY store chat | "stop hedging… keep a warning only when skipping it could hurt" | "the experienced person behind the counter… the one warning a friend would still give" |
| comments | Python for a billing service | "stop commenting what the code does… only where the reason is not obvious" | "write for the colleague who'll debug this at 2 a.m.… don't narrate it" |
| concise | #updates channel post | "be much more concise… keep only impact, actions, deadlines" | "a message to a busy manager between two meetings" |

Models: Opus 5.5 and gpt-6-astra (large), Haiku 5.5 and gpt-6-luna (small). Three reps per
case for every task; six for numbers and concision. 1,512 responses in total.

### Judging

Each response is judged by an LLM that never sees the condition (`corrections/judge.py`). For
every case, the judge gets the request, a description of a good response, what is essential in
that case, and all the responses for that case shuffled under neutral labels. Per response it
returns:

- **essential**: it gets across what the case needs (for example, in the price-change
  briefing: both the old and the new price, so the listener knows how big the rise is);
- **excess** 0-3: how much of the behaviour the correction was meant to curb;
- **errors**: facts misstated or invented relative to the source;
- **quality** 1-5: would a demanding editor publish it as is.

Two judges from different providers, Opus 5.5 and gpt-6.1-sol. They agree on 97 % of the
essential verdicts (1,512 shared responses), 96 % on excess within one point, 93 % on quality
within one point. Before the full run the judge was checked against responses the author had
judged by hand; it agreed on all of them (a bare "four" without the total fails, "about half
a percent" passes; reason-giving comments are not excess).

### Results

Essential kept, per model (judge Opus; Sol gives the same counts unless noted).

**Numbers** (18 need-responses per cell):

| model | base | rule | way | rule vs way, Fisher p |
|---|---|---|---|---|
| Opus | 18 | **6** | 18 | < 0.0001 |
| Astra | 18 | **4** | 18 | < 0.0001 |
| Haiku | 18 | 11 | 18 | 0.008 |
| Luna | 18 | 11 | 18 | 0.008 |

What the rule drops: the starting price ("going up to twelve euros", never from nine), the
denominator of the audit ("four records had a wrong VAT number", out of how many?), the scale
of an outage ("many payments failed").

Excess of figures (0-3, need cases) and quality (1-5):

| model | excess base → rule → way | quality base / rule / way |
|---|---|---|
| Opus | 2.3 → 0.0 → 0.3 | 2.4 / 3.3 / **4.3** |
| Astra | 2.2 → 0.0 → 0.7 | 2.6 / 2.7 / **3.7** |
| Haiku | 2.4 → 0.0 → 1.8 | 2.7 / **3.6** / 3.1 |
| Luna | 2.3 → 0.0 → 1.4 | 2.6 / **3.5** / 3.4 |

The way-of-speaking correction rounds rather than removes on the large models ("about thirteen
hundred payments… close to fifty thousand euros"); the small ones mostly keep the exact
figures ("1,284 failed payments, of which 1,071…"), so the rule, which at least sounds easy,
scores higher there.

**Comments** (9 need-responses): the external constraint explained in the code.

| model | base | rule | way |
|---|---|---|---|
| Opus | 3 | 9 | 9 |
| Astra | 3 | 5 | 4 |
| Haiku | 3 | 6 | 7 |
| Luna | 3 | 3 | 3 |

Neither version leads to narrating comments. With the 2 a.m. framing Opus also comments the
traps in "trivial" functions (Decimal's default banker's rounding, `datetime` being a subclass
of `date`): reasons, not narration.

**Concision** (18 need-responses, six reps): every condition keeps the actions and deadlines in
every model (judge Opus; Sol fails three of Opus's way-of-doing-it posts that make Support
wait for customers to write in instead of contacting them). The rule trims more on the large
models: excess on Opus 0.9 → 0.0 (rule) vs 0.4 (way), quality 4.4 vs 4.0; Astra and Luna in
the same order; Haiku a tie.

**Hedging**: every condition keeps the warning that matters (fire, toxic gas, load-bearing
wall). Both corrections cut boilerplate on most models; the rule cuts more on Luna, elsewhere they
tie.

**Questions**: no effect of the framing. Failures are the same in every condition (handing over
a ready-to-run delete while asking, or not asking how two tables relate).

### Not supported

- *The way-of-doing-it framing makes Opus invent details.* It looked so at three reps. At six,
  its factual errors in concision are at the base level (11 vs 15 of 36, judge Sol) and the
  rule's lower count (5) comes from cutting text (W vs R, p = 0.16). In numbers it is one
  repeated slip, counting automatically retried payments as collected (p = 0.08 with Sol, 0.36
  with Opus). A lead, not a finding.

### Limits

- One base skill per task, written by us. Corrections in the wild are messier.
- Single-turn responses; no agent loop, no tools.
- Six reps on numbers and concision, three on the rest: the comments and questions tables are
  directional.

## Pilot: release notes (`release_notes/`)

A first pilot compared no skill, rules, patched rules and a role for user-facing release
notes. Any skill cut leaked internal work tenfold; Opus and the other large models solved it
under every framing, and only gpt-6-luna over-applied the rules (p ≈ 0.03). It was too close to
classification to reproduce the original observation, which is why experiment 2 exists.

## Running

Single-turn text. Every runner rejects invalid executions (spend-limit messages, API errors,
empty output) and skips responses already on disk, so any run can be resumed. `--workers`
sets concurrency (this machine runs out of memory above two).

- **Claude** (Opus, Sonnet, Haiku 5.5) via `claude -p --system-prompt … --setting-sources ""
  --tools ""`: replaces Claude Code's default prompt and keeps the user's CLAUDE.md out.
- **Codex** (`gpt-6-astra`, `gpt-6.1-sol`, `gpt-6-luna`) via `codex exec` with a `CODEX_HOME`
  holding only `auth.json` (keeps `~/.codex/AGENTS.md` and config out) and
  `model_instructions_file` (replaces the base instructions). Reasoning effort fixed at medium.

```
cd corrections
python run.py --models opus,astra,haiku,luna --reps 3 --workers 2
python judge.py --judge opus            # and --judge sol; --reps 4-6 for extra batches
python judge_score.py                   # tables + agreement + data/judge_scores.csv
```
