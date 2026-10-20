"""Blind LLM judge for the narration revisions.

One call per (model, script): the judge sees the original narration and the twelve revisions
(four skill versions x three reps) shuffled under neutral labels. Only what the voice says is
shown: the spoken column of the script table plus any spoken-form notes, so long visual
descriptions do not crowd the prompt.

Usage: python judge.py --judge opus|sol --set fresh|repro [--models opus,astra,haiku,luna]
Output: data/judge/<set>/<judge>/<model>_<script>.json
"""
import argparse
import json
import random
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT / "corrections"))
from run import call, is_valid  # noqa: E402

VERSIONS = ("0993f3d", "4ccc13f", "1c81e93", "2d8f6fa")
SETS = {
    "fresh": dict(raw=HERE / "data" / "raw", originals={p.stem: p for p in (HERE / "drafts").glob("*.md")}),
    "repro": dict(raw=ROOT / "narration_repro" / "data" / "raw",
                  originals={"subagent": ROOT / "narration_repro" / "inputs" / "subagent_v1.1_script.md",
                             "repetition": ROOT / "narration_repro" / "inputs" / "repetition_v1.1_script.md"}),
}
OUT = HERE / "data" / "judge"
SPOKEN_HEADER = re.compile(r"^(EN line|Narration( \(EN\))?|Line|Voice|Spoken|EN)$", re.I)

PROMPT = """You are judging revisions of the narration of a 30-60 second explainer video about an
experiment. The reviser was asked to make the spoken narration follow updated guidance on how
numbers are spoken. Judge each revision on its own merits; several may be equally good or bad.

## What the author wants from the voice
The finding said with its number, naturally, the way you would explain the result to a
colleague. What tires the ear is several unround figures in a row, read out like a table.
Numbers may also appear on screen; here only what the VOICE says matters.

## Original narration (before the revision)
{original}

## Revisions
{responses}

For each revision return:
- "essential": true only if every headline finding that the original said with a number is still
  SAID with a number or an exact fraction ("4 times in 791", "a quarter", "nine in ten", "47%",
  "eight of twelve"). A vague quantifier in its place ("almost never", "more often", "almost every
  time", "far more", "a fraction") or moving it to the screen only does NOT pass.
- "lost": the headline findings whose number is no longer said, short, or [] if none.
- "excess": 0-3, runs of figures in the voice that are hard to follow by ear (several exact or
  unround numbers close together, table-like recitation). 0 none, 1 one such spot, 2 several,
  3 reads like a spreadsheet.
- "errors": true if a spoken number or claim now misstates the original.
- "quality": 1-5, would the author approve this narration as is.
- "reason": one sentence.

Return only a JSON array, one object per revision, in the order given:
[{{"id": "<label>", "essential": true|false, "lost": [...], "excess": 0-3, "errors": true|false,
  "quality": 1-5, "reason": "..."}}]"""


def spoken(text):
    """The spoken column of the first script table, plus spoken-form notes; the whole text if no table."""
    lines, col, out = text.splitlines(), None, []
    for line in lines:
        if not line.strip().startswith("|"):
            if col is not None and out:
                break
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if col is None:
            for i, c in enumerate(cells):
                if SPOKEN_HEADER.match(c):
                    col = i
                    break
            continue
        if set("".join(cells)) <= set("-: "):
            continue
        if col < len(cells):
            out.append(f"{cells[0]} | {cells[col]}")
    notes = [l for l in lines if re.search(r"spoken (as|form)|is spoken", l, re.I)]
    if not out:
        return text[:6000]
    return "\n".join(out + ([""] + notes if notes else []))


def judge_one(judge, set_name, model, script):
    dest = OUT / set_name / judge / f"{model}_{script}.json"
    if dest.exists():
        return "skip"
    cfg = SETS[set_name]
    items = []
    for v in VERSIONS:
        for f in sorted((cfg["raw"] / model / v).glob(f"{script}_*.md")):
            items.append((v, f.stem, spoken(f.read_text(encoding="utf-8"))))
    if not items:
        return "empty"
    random.Random(f"{set_name}/{model}/{script}").shuffle(items)
    labels = [f"X{i + 1}" for i in range(len(items))]
    responses = "\n\n".join(f"### {l}\n<narration>\n{t}\n</narration>" for l, (_, _, t) in zip(labels, items))
    prompt = PROMPT.format(original=spoken(cfg["originals"][script].read_text(encoding="utf-8")),
                           responses=responses)
    out = call(judge, "You are a careful, strict evaluator. Output only what is asked.", prompt,
               dest.with_suffix(".work"))
    start, end = out.find("["), out.rfind("]")
    try:
        rows = json.loads(out[start:end + 1]) if is_valid(out) and start >= 0 else None
    except json.JSONDecodeError:
        rows = None
    key = {l: dict(version=v, file=s) for l, (v, s, _) in zip(labels, items)}
    if not rows or {r.get("id") for r in rows} != set(key):
        print(f"INVALID {dest.name} :: {out[:200]!r}", flush=True)
        return "invalid"
    for r in rows:
        r.update(key[r["id"]], model=model, script=script)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(rows, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"ok      {dest.relative_to(HERE)}", flush=True)
    return "ok"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--judge", default="opus")
    ap.add_argument("--set", default="fresh", choices=list(SETS))
    ap.add_argument("--models", default="opus,astra,haiku,luna")
    args = ap.parse_args()
    results = [judge_one(args.judge, args.set, m, s)
               for m in args.models.split(",") for s in sorted(SETS[args.set]["originals"])]
    print({s: results.count(s) for s in set(results)})


if __name__ == "__main__":
    main()
