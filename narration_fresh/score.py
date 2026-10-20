"""Aggregate the narration judgments per judge, model and skill version, and compare the judges.

Usage: python score.py [fresh|repro]
"""
import json
import sys
from collections import defaultdict
from math import comb
from pathlib import Path
from statistics import mean

HERE = Path(__file__).parent
NAMES = {"0993f3d": "rule", "4ccc13f": "pile-ups", "1c81e93": "by ear (if)", "2d8f6fa": "colleague"}


def fisher(a, n1, b, n2):
    k, n = a + b, n1 + n2
    p = lambda x: comb(n1, x) * comb(n2, k - x) / comb(n, k)
    obs = p(a)
    return sum(p(x) for x in range(max(0, k - n2), min(k, n1) + 1) if p(x) <= obs * (1 + 1e-9))


def main():
    set_name = sys.argv[1] if len(sys.argv) > 1 else "fresh"
    rows = []
    for f in sorted((HERE / "data" / "judge" / set_name).glob("*/*.json")):
        for r in json.loads(f.read_text(encoding="utf-8")):
            r["judge"] = f.parent.name
            rows.append(r)
    g = defaultdict(list)
    for r in rows:
        g[(r["judge"], r["model"], r["version"])].append(r)
    print(f"{'judge':5} {'model':6} {'version':12} {'essential':>10} {'excess':>7} {'quality':>8} {'errors':>7}")
    for (j, m, v), rs in sorted(g.items(), key=lambda kv: (kv[0][0], kv[0][1], list(NAMES).index(kv[0][2]))):
        print(f"{j:5} {m:6} {NAMES[v]:12} {sum(r['essential'] for r in rs):>6}/{len(rs):<3} "
              f"{mean(r['excess'] for r in rs):>7.2f} {mean(r['quality'] for r in rs):>8.2f} "
              f"{sum(r['errors'] for r in rs):>7}")

    print("\nrule vs colleague, essential, Fisher p:")
    for j in sorted({r["judge"] for r in rows}):
        for m in sorted({r["model"] for r in rows}):
            a, b = g[(j, m, "0993f3d")], g[(j, m, "2d8f6fa")]
            c = g[(j, m, "1c81e93")]
            ea, eb, ec = (sum(r["essential"] for r in x) for x in (a, b, c))
            print(f"  {j:5} {m:6} rule {ea}/{len(a)} vs colleague {eb}/{len(b)} p={fisher(ea, len(a), eb, len(b)):.4f}"
                  f" | if {ec}/{len(c)} vs colleague p={fisher(ec, len(c), eb, len(b)):.4f}")

    by = defaultdict(dict)
    for r in rows:
        by[(r["model"], r["version"], r["file"])][r["judge"]] = r
    pairs = [(v["opus"], v["sol"]) for v in by.values() if "opus" in v and "sol" in v]
    if pairs:
        print(f"\nagreement on {len(pairs)}: essential {mean(x['essential'] == y['essential'] for x, y in pairs):.0%}, "
              f"excess within 1 {mean(abs(x['excess'] - y['excess']) <= 1 for x, y in pairs):.0%}, "
              f"quality within 1 {mean(abs(x['quality'] - y['quality']) <= 1 for x, y in pairs):.0%}")


if __name__ == "__main__":
    main()
