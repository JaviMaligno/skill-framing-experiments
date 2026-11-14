"""Aggregate the second judge (judge2.py): finding carried, figure runs, and both together.

"ideal" = the finding is still carried AND the voice has no run of figures (excess 0).

Usage: python score2.py [fresh|repro]
"""
import json
import sys
from collections import defaultdict
from pathlib import Path
from statistics import mean

HERE = Path(__file__).parent
NAMES = {"0993f3d": "rule", "4ccc13f": "pile-ups", "1c81e93": "by ear (if)", "2d8f6fa": "colleague"}


def main():
    set_name = sys.argv[1] if len(sys.argv) > 1 else "fresh"
    rows = []
    for f in sorted((HERE / "data" / "judge2" / set_name).glob("*/*.json")):
        for r in json.loads(f.read_text(encoding="utf-8")):
            r["judge"] = f.parent.name
            rows.append(r)
    g = defaultdict(list)
    for r in rows:
        g[(r["judge"], r["model"], r["version"])].append(r)
    print(f"{'judge':5} {'model':6} {'version':12} {'finding':>8} {'ideal':>7} {'excess':>7} {'errors':>7}")
    for (j, m, v), rs in sorted(g.items(), key=lambda kv: (kv[0][0], kv[0][1], list(NAMES).index(kv[0][2]))):
        n = len(rs)
        print(f"{j:5} {m:6} {NAMES[v]:12} {sum(r['finding'] for r in rs):>4}/{n:<3} "
              f"{sum(r['finding'] and r['excess'] == 0 for r in rs):>3}/{n:<3} "
              f"{mean(r['excess'] for r in rs):>7.2f} {sum(r['errors'] for r in rs):>7}")

    by = defaultdict(dict)
    for r in rows:
        by[(r["model"], r["version"], r["file"])][r["judge"]] = r
    pairs = [(v["opus"], v["sol"]) for v in by.values() if "opus" in v and "sol" in v]
    if pairs:
        print(f"\nagreement on {len(pairs)}: finding {mean(x['finding'] == y['finding'] for x, y in pairs):.0%}, "
              f"excess within 1 {mean(abs(x['excess'] - y['excess']) <= 1 for x, y in pairs):.0%}")


if __name__ == "__main__":
    main()
