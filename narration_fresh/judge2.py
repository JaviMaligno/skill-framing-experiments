"""Second blind judge for the narration revisions: is the FINDING still carried, as the article states it?

The first judge (judge.py) failed any revision that replaced a number with words. That conflates
two different things. When the article itself states a finding qualitatively ("it almost never
believes the report"), saying it in words is faithful. The loss that matters is when the finding
IS a size, a comparison or a gap, and the words no longer convey how big it is ("the base is on
another planet" for ~0.10 vs 0.51). This judge gets the source article so it can tell which
findings are which.

Usage: python judge2.py --judge opus|sol --set fresh|repro [--models opus,astra,haiku,luna]
Output: data/judge2/<set>/<judge>/<model>_<script>.json
"""
import argparse
import json
import random
import re

from judge import HERE, ROOT, SETS, VERSIONS, call, is_valid, spoken

OUT = HERE / "data" / "judge2"
ARTICLES = {
    "fresh": {p.stem: p for p in (HERE / "articles").glob("*.md")},
    "repro": {p.stem: p for p in (ROOT / "narration_repro" / "articles").glob("*.md")},
}

PROMPT = """You are judging revisions of the narration of a 30-60 second explainer video about an
experiment. The reviser was asked to make the spoken narration follow updated guidance on how
numbers are spoken. Judge each revision on its own merits; several may be equally good or bad.

## The source article
This is what the video narrates. Use it to decide what each finding actually claims.
<article>
{article}
</article>

## Original narration (before the revision)
{original}

## Revisions
{responses}

## How to judge whether a finding survives
For each headline finding that the original narration said with a number, ask what the article
claims with it:
- If the article's claim is qualitative (for example "it almost never believes the report", "every
  file was checked"), a faithful phrase in words keeps it. "Almost never" for 4 in 791 passes when
  the article's point is that it almost never happens.
- If the claim is a size, a comparison, a gap or a change (X against Y, from A to B, rose to N, N
  times more), the voice must still convey how big it is: the numbers, an exact or near-exact
  fraction or ratio ("nine in ten", "almost half", "five times more", "a quarter"). A vague
  comparative that drops the size does NOT pass ("more often", "far more", "on another planet",
  "did clearly worse", "slightly better") when the size is what the finding says.
Moving a number to the screen only does not count; only what the VOICE says matters.

For each revision return:
- "finding": true only if every headline finding of the original is still carried by the voice, by
  the rule above.
- "lost": the findings that are no longer carried, short, or [] if none.
- "excess": 0-3, runs of figures in the voice that are hard to follow by ear (several exact or
  unround numbers close together, table-like recitation). 0 none, 1 one such spot, 2 several,
  3 reads like a spreadsheet. A single magnitude said naturally ("five times more", "rose to 47%")
  is not excess.
- "errors": true if a spoken number or claim now misstates the article.
- "reason": one sentence.

Return only a JSON array, one object per revision, in the order given:
[{{"id": "<label>", "finding": true|false, "lost": [...], "excess": 0-3, "errors": true|false, "reason": "..."}}]"""


def article_text(path):
    """The article without frontmatter, inline SVG, style blocks or HTML tags."""
    t = path.read_text(encoding="utf-8")
    t = re.sub(r"\A---.*?\n---\n", "", t, flags=re.S)
    t = re.sub(r"<(svg|style|script)\b.*?</\1>", "", t, flags=re.S | re.I)
    t = re.sub(r"<[^>]+>", " ", t)
    return re.sub(r"\n{3,}", "\n\n", t).strip()


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
    random.Random(f"judge2/{set_name}/{model}/{script}").shuffle(items)
    labels = [f"X{i + 1}" for i in range(len(items))]
    responses = "\n\n".join(f"### {l}\n<narration>\n{t}\n</narration>" for l, (_, _, t) in zip(labels, items))
    prompt = PROMPT.format(article=article_text(ARTICLES[set_name][script]),
                           original=spoken(cfg["originals"][script].read_text(encoding="utf-8")),
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
