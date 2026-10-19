"""Score experiment 2.

Per response, two numbers:
  ok   on "need" cases: the behaviour the correction targets is still there where it is
       needed (key number said / question asked / warning given / reason commented / action
       and deadline kept). ok=0 on a need case is an OVER-CORRECTION.
  x    how much of the targeted behaviour there is (numbers said / asked a question /
       hedging phrases / comment lines / words). On "noneed" cases a lower x is the point
       of the correction.

Usage: python score.py   -> table + data/scores.csv
"""
import csv
import re
from collections import defaultdict
from pathlib import Path
from statistics import mean

from tasks import TASKS

HERE = Path(__file__).parent
RAW = HERE / "data" / "raw"

NUMBER_WORDS = (r"\b(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|"
                r"sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|"
                r"hundred|thousand|million|half|quarter|percent)\b")
HEDGES = [r"consult", r"professional", r"it depends", r"depending on", r"be careful", r"\bsafety\b", r"make sure",
          r"disclaimer", r"note that", r"keep in mind", r"\bcaution", r"if (you'?re )?(unsure|in doubt|not sure)"]


def prose(text):
    return re.sub(r"```.*?```", " ", text, flags=re.S)


def code(text):
    blocks = re.findall(r"```[a-zA-Z]*\n(.*?)```", text, flags=re.S)
    return "\n".join(blocks) if blocks else text


def numbers_said(text):
    return len(re.findall(r"\d[\d,.:]*", text)) + len(re.findall(NUMBER_WORDS, text, re.I))


def score(task, case, text):
    keys = case.get("key", [])
    if task == "numbers":
        return dict(ok=all(re.search(k, text, re.I) for k in keys) if keys else None, x=numbers_said(text))
    if task == "questions":
        asked = "?" in prose(text)
        return dict(ok=asked if case["kind"] == "need" else None, x=int(asked))
    if task == "hedging":
        return dict(ok=all(re.search(k, text, re.I) for k in keys) if case["kind"] == "need" else None,
                    x=sum(bool(re.search(h, text, re.I)) for h in HEDGES))
    if task == "comments":
        src = code(text)
        comments = re.findall(r"#\s*(.*)", src)
        docstrings = re.findall(r'"""(.*?)"""', src, flags=re.S)
        explained = " ".join(comments + docstrings)
        return dict(ok=all(re.search(k, explained, re.I) for k in keys) if case["kind"] == "need" else None,
                    x=len(comments))
    if task == "concise":
        return dict(ok=all(re.search(k, text, re.I) for k in keys), x=len(text.split()))
    raise ValueError(task)


def main():
    rows = []
    for f in sorted(RAW.glob("*/*/*/*.md")):
        model, task, cond = f.parts[-4], f.parts[-3], f.parts[-2]
        case = next(c for c in TASKS[task]["cases"] if c["id"] == f.stem.split("_")[0])
        s = score(task, case, f.read_text(encoding="utf-8"))
        rows.append(dict(model=model, task=task, cond=cond, case=case["id"], kind=case["kind"],
                         file=str(f.relative_to(RAW)), ok="" if s["ok"] is None else int(s["ok"]), x=s["x"]))
    if not rows:
        print("no responses yet")
        return
    with open(HERE / "data" / "scores.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

    g = defaultdict(list)
    for r in rows:
        g[(r["task"], r["model"], r["cond"])].append(r)
    print(f"{'task':10} {'model':6} {'cond':4} {'need ok':>8} {'x need':>7} {'x noneed':>9} {'n':>4}")
    for (task, model, cond), rs in sorted(g.items()):
        oks = [r["ok"] for r in rs if r["ok"] != ""]
        xn = [r["x"] for r in rs if r["kind"] == "need"]
        xo = [r["x"] for r in rs if r["kind"] == "noneed"]
        f = lambda xs: f"{mean(xs):.2f}" if xs else "-"
        print(f"{task:10} {model:6} {cond:4} {f(oks):>8} {f(xn):>7} {f(xo):>9} {len(rs):4d}")


if __name__ == "__main__":
    main()
