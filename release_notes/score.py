"""Deterministic scoring of the release notes in data/raw.

Per response:
  coverage      visible changes mentioned / visible changes          (higher is better)
  internal      internal changes mentioned                           (0 is right; S2)
  kept          required user-facing terms present / required terms  (S5; low = over-generalised S4)
  leaks         internal tokens + engineering vocabulary found       (S4; high = rule not applied)
  action_first  action and date stated in the first third            (S6; only cases with an action)
  words

Usage: python score.py [--split dev|test|all]   -> prints a table and writes data/scores.csv
"""
import argparse
import csv
import re
from collections import defaultdict
from pathlib import Path
from statistics import mean

from cases import CASES

HERE = Path(__file__).parent
RAW = HERE / "data" / "raw"

JARGON = [r"\bendpoints?\b", r"\brefactor", r"\bregression", r"\bnull\b", r"race condition", r"\bback-?end\b",
          r"\bfront-?end\b", r"\bquer(y|ies)\b", r"\bcach(e|ed|ing)\b", r"\bpayload", r"\bschema", r"\bcodebase",
          r"pull request", r"\bPRs?\b", r"stack trace", r"\bexception", r"\bdebounc", r"\bpaginat", r"\blocale\b",
          r"\b[A-Z]{2,4}-\d{2,}\b", r"#\d{3,}"]


def hit(patterns, text):
    return any(re.search(p, text, re.I) for p in patterns)


def score(case, text):
    vis = [c for c in case["changes"] if c["kind"] == "visible"]
    intl = [c for c in case["changes"] if c["kind"] == "internal"]
    required = [r for c in vis for r in c["required"]]
    leak_tokens = [t for c in case["changes"] for t in c["leak"]]
    leaks = sum(t.lower() in text.lower() for t in leak_tokens)
    leaks += sum(len(re.findall(p, text, re.I if not p.startswith(r"\b[A-Z]") else 0)) > 0 for p in JARGON)
    row = dict(
        coverage=sum(hit(c["anchors"], text) for c in vis) / len(vis),
        internal=sum(hit(c["anchors"], text) for c in intl),
        kept=sum(bool(re.search(r, text, re.I)) for r in required) / len(required) if required else None,
        leaks=leaks,
        words=len(text.split()),
        action_first=None,
    )
    if case["action"]:
        # The action is always the first change of its case; it is "first" when what and when
        # both appear before any other visible change is mentioned.
        starts = [m.start() for c in vis[1:] for p in c["anchors"] for m in [re.search(p, text, re.I)] if m]
        head = text[: min(starts)] if starts else text
        row["action_first"] = int(hit(case["action"]["what"], head) and hit(case["action"]["when"], head))
    return row


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--split", default="all")
    args = ap.parse_args()
    by_id = {c["id"]: c for c in CASES}
    rows = []
    for f in sorted(RAW.glob("*/*/*.md")):
        model, cond = f.parent.parent.name, f.parent.name
        case = by_id[f.stem.split("_")[0]]
        if args.split != "all" and case["split"] != args.split:
            continue
        rows.append(dict(model=model, cond=cond, case=case["id"], split=case["split"], file=str(f.relative_to(RAW)),
                         **score(case, f.read_text(encoding="utf-8"))))
    if not rows:
        print("no responses yet")
        return
    with open(HERE / "data" / "scores.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

    metrics = ["coverage", "internal", "kept", "leaks", "action_first", "words"]
    groups = defaultdict(list)
    for r in rows:
        groups[(r["model"], r["cond"])].append(r)
        groups[("ALL", r["cond"])].append(r)
    print(f"{'model':7} {'cond':5} {'n':>3} " + " ".join(f"{m:>12}" for m in metrics))
    for (model, cond), rs in sorted(groups.items()):
        vals = []
        for m in metrics:
            xs = [r[m] for r in rs if r[m] is not None]
            vals.append(f"{mean(xs):12.2f}" if xs else f"{'-':>12}")
        print(f"{model:7} {cond:5} {len(rs):3d} " + " ".join(vals))


if __name__ == "__main__":
    main()
