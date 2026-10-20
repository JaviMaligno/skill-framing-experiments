"""Aggregate the LLM judgments of experiment 2 and compare the two judges.

Usage: python judge_score.py [data/judge_numbers5]   -> table per judge + agreement + <dir>_scores.csv
"""
import csv
import json
import sys
from collections import defaultdict
from pathlib import Path
from statistics import mean

HERE = Path(__file__).parent
JUDGE = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "data" / "judge"


def load():
    rows = []
    for f in sorted(JUDGE.glob("*/*.json")):
        for r in json.loads(f.read_text(encoding="utf-8")):
            r["judge"] = f.parent.name
            rows.append(r)
    return rows


def fmt(xs):
    return f"{mean(xs):.2f}" if xs else "-"


def main():
    rows = load()
    with open(JUDGE.parent / f"{JUDGE.name}_scores.csv", "w", newline="", encoding="utf-8") as fh:
        cols = ["judge", "model", "task", "case", "kind", "cond", "file", "essential", "excess", "errors",
                "quality", "reason"]
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)

    g = defaultdict(list)
    for r in rows:
        g[(r["judge"], r["task"], r["model"], r["cond"])].append(r)
    print(f"{'judge':5} {'task':10} {'model':6} {'cond':4} {'need ok':>8} {'exc need':>9} {'exc noneed':>11} "
          f"{'quality':>8} {'errors':>7} {'n':>3}")
    for (judge, task, model, cond), rs in sorted(g.items()):
        need = [r for r in rs if r["kind"] == "need"]
        noneed = [r for r in rs if r["kind"] == "noneed"]
        print(f"{judge:5} {task:10} {model:6} {cond:4} "
              f"{sum(r['essential'] for r in need):>4}/{len(need):<3} "
              f"{fmt([r['excess'] for r in need]):>9} {fmt([r['excess'] for r in noneed]):>11} "
              f"{fmt([r['quality'] for r in rs]):>8} {sum(r['errors'] for r in rs):>7} {len(rs):>3}")

    # Agreement between judges on the same response.
    by = defaultdict(dict)
    for r in rows:
        by[(r["model"], r["task"], r["cond"], r["file"])][r["judge"]] = r
    judges = sorted({r["judge"] for r in rows})
    if len(judges) == 2:
        a, b = judges
        pairs = [(v[a], v[b]) for v in by.values() if a in v and b in v]
        if pairs:
            ess = mean(x["essential"] == y["essential"] for x, y in pairs)
            exc = mean(abs(x["excess"] - y["excess"]) <= 1 for x, y in pairs)
            qual = mean(abs(x["quality"] - y["quality"]) <= 1 for x, y in pairs)
            print(f"\nagreement {a} vs {b} on {len(pairs)} responses: essential {ess:.0%}, "
                  f"excess within 1 {exc:.0%}, quality within 1 {qual:.0%}")
            for x, y in pairs:
                if x["essential"] != y["essential"]:
                    print(f"  disagree essential: {x['model']} {x['task']} {x['cond']} {x['file']}"
                          f"  {a}={x['essential']} {b}={y['essential']}")


if __name__ == "__main__":
    main()
