"""Print the narration column of chosen scenes, per skill version and rep, to read them side by side.

Usage: python show.py subagent 6,10,11,12,13 [model]
"""
import re
import sys
from pathlib import Path

RAW = Path(__file__).parent / "data" / "raw"


def narration(text):
    rows = {}
    for line in text.splitlines():
        m = re.match(r"\|\s*(\d+)\s*\|([^|]*)\|", line)
        if m and m.group(1) not in rows:
            rows[m.group(1)] = m.group(2).strip()
    return rows


def main():
    script, scenes = sys.argv[1], sys.argv[2].split(",")
    model = sys.argv[3] if len(sys.argv) > 3 else "opus"
    src = Path(__file__).parent / "inputs" / f"{script}_v1.1_script.md"
    before = narration(src.read_text(encoding="utf-8"))
    for s in scenes:
        print(f"\n### scene {s}\n  v1.1      : {before.get(s, '-')}")
        for vdir in sorted((RAW / model).iterdir()):
            for f in sorted(vdir.glob(f"{script}_*.md")):
                print(f"  {vdir.name} {f.stem[-1]}: {narration(f.read_text(encoding='utf-8')).get(s, '-')}")


if __name__ == "__main__":
    main()
