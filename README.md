# Skill framing: rule vs way of doing it

Does the *form* in which a skill is written change behaviour, holding its content fixed?
The working hypothesis (Oct 2026): a skill written as a role or a way of doing things
generalises better than one written as detailed rules, which the model over-applies until it
becomes a list of prohibitions patched on top of each other.

Not the same question as `agent-scaffolding-experiments` (skill vs no skill). Here every
condition has a skill; only the framing of one part of it changes.

## Where it came from

A narration skill for explainer videos (`agilabs-video-studio/skills/explainer-script`). The
author asked it not to string together non-round numbers; the next revision of two scripts said
no numbers at all; the rule then grew into a natural-language `if`; it was finally fixed by
describing a way of narrating: "as you'd explain it to a colleague". `skills/narration/` holds
the real commits (all 2026-10-19 except the first):

| commit | version | numbers line |
|---|---|---|
| `d658477` | before | no numbers guidance (used to write the fresh drafts in experiment 3) |
| `a84ecb6` | rule, introduced | "say the one number that carries the point… leave the rest on screen or out" |
| `0993f3d` | **rule** | same line, in force when the scripts were revised |
| `4ccc13f` | **pile-ups** | "the problem is the pile-up, not the number" |
| `1c81e93` | **if, by ear** | case by case; when awkward, say what it means in words |
| `2d8f6fa` | **colleague** | "the way you would explaining the result to a colleague" |

Experiment 3 reproduces the episode with these versions and then tests them on fresh scripts.
Experiment 2 asks the same question on simpler material, written from scratch.

## Result in one paragraph

On the real narration skill, revising fresh scripts, the rule and the patched `if` drop the
finding's number and "colleague" never does: Opus keeps it in 1/18 revisions under the rule,
4/18 under the `if`, 18/18 under "colleague" (judge Opus; Sol 0, 0, 18). The more obedient the
model, the worse the rule: Astra and Haiku survive the `if`, Opus doesn't. The same holds for a
rule that **caps a quantity** in a spoken briefing written from scratch (Opus 6/18, gpt-6-astra
4/18 keep the essential figure, against 18/18 written as a way of speaking). A rule **without**
the cap or the "move it elsewhere" outlet keeps the essential 17-18/18 in every model and
removes recitation better. When the correction is plain **restraint** (be shorter, drop the
caveats), the rule works as well or slightly better. There is no universal winner; the rule
fails when it offers a cap or another place to put the thing, and a capable model applies it
to every instance.

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

The rule above has a cap ("at most the one figure"), and these cases need two. Two more rules
without the cap, same length (`NUMBERS_S`: "do not string numbers together… round when the
source allows"; `NUMBERS_E`: the same plus "keep the figures the point depends on"), judged
together with the other three conditions (`data/judge_numbers5/`):

| model | essential S / E (judge Opus) | excess S / E / way | quality S / E / way |
|---|---|---|---|
| Opus | 18 / 18 | 0.0 / 0.2 / 0.3 | 4.4 / 4.3 / 4.1 |
| Astra | 18 / 18 | 0.0 / 0.3 / 0.9 | 4.3 / 4.2 / 3.5 |
| Haiku | 18 / 18 | 0.4 / 0.4 / 1.8 | 3.9 / 4.3 / 2.9 |
| Luna | 17 / 17 | 0.6 / 1.1 / 1.3 | 3.8 / 3.6 / 3.4 |

Sol gives the same essential counts except Luna E 18. Sol's Luna cells hold 27 of 36 responses.
Without the cap the rule keeps the essential and trims the recitation better than the way of
speaking.

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

### Limits

- One base skill per task, written by us. Corrections in the wild are messier.
- Single-turn responses; no agent loop, no tools (the original episode happened inside an
  agent session).
- Six reps on numbers and concision, three on the rest: the comments and questions tables are
  directional.

## Experiment 3: the real narration skill (`narration_repro/`, `narration_fresh/`)

Experiment 2 did not reproduce the original episode with a cap-free rule. What it lacked was
the real setup: the actual skill, a second channel for numbers ("leave the rest on screen"),
and **revision** of a script that already has them.

**Reproduction** (`narration_repro/`). The two v1.1 scripts from the episode
(`agilabs-video-studio` at `74eb78b^`), revised by Opus under each of the four versions, three
times. The headline "4 times in 791":

| version | what the three revisions say |
|---|---|
| rule | "almost never" ×2, "only 4 times" ×1 (no 791) |
| pile-ups | "4 times in 791" ×3 |
| if, by ear | "almost never" ×3 |
| colleague | "4 times in 791" ×3 |

The rule also turns "47% with long context" into "more often" every time. Read by the author
line by line; this is what the judge below was calibrated on.

**Fresh material** (`narration_fresh/`). Six articles with experimental results that never had a
video (`articles/`). Opus wrote one draft each with `d658477` (no numbers guidance); the drafts
are fixed (`drafts/`). Four models revised every draft under each version, three times: 288
revisions. Two blind judges (Opus, gpt-6.1-sol) read only the spoken column. **Essential** =
every finding the draft said with a number is still said with a number or an exact fraction;
"almost never", "more often", or moving it to the screen fail.

Essential kept, of 18 (judge Opus · judge Sol):

| model | rule | pile-ups | if, by ear | colleague |
|---|---|---|---|---|
| Opus | 1 · 0 | 9 · 6 | 4 · 0 | 18 · 18 |
| Astra | 3 · 0 | 9 · 3 | 18 · 14 | 18 · 18 |
| Haiku | 5 · 4 | 9 · 7 | 14 · 14 | 18 · 18 |
| Luna | 18 · 18 | 18 · 18 | 18 · 18 | 18 · 18 |

Rule vs colleague: Fisher p < 0.0001 for Opus, Astra and Haiku under both judges; `if` vs
colleague p < 0.0001 for Opus only. Luna barely revises: it returns the draft nearly unchanged
under every version. Judges agree on 92 % of essential verdicts, 99 % on excess within one
point, 93 % on quality within one point.

Leftover figure-reading (excess, 0-3) is higher under "colleague" (Opus 1.4, Astra 1.4-1.7)
than under the rule (0). That score was **not** calibrated against the author's reading, and
in the video the author made with the colleague version no pile-up is heard, so it is reported
here without a conclusion.

`python narration_fresh/score.py` prints the full table (excess, quality, errors) and the tests.

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
  The isolation is not perfect: one Haiku response out of 1,512 named the account holder, who
  appears in no prompt (`corrections/data/raw/haiku/concise/0/s3_4.md`, name redacted). Some
  account context still reaches the model.
- **Codex** (`gpt-6-astra`, `gpt-6.1-sol`, `gpt-6-luna`) via `codex exec` with a `CODEX_HOME`
  holding only `auth.json` (keeps `~/.codex/AGENTS.md` and config out) and
  `model_instructions_file` (replaces the base instructions). Reasoning effort fixed at medium.

```
cd corrections
python run.py --models opus,astra,haiku,luna --reps 3 --workers 2
python judge.py --judge opus            # and --judge sol; --reps 4-6 for extra batches
python judge_score.py                   # tables + agreement + data/judge_scores.csv
```
