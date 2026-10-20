"""Reproduce the narration episode: revise an existing video script under each version of the
real explainer-script skill, and see what happens to the spoken numbers.

The episode (agilabs-video-studio 74eb78b): with the rule version in force, Opus revised two
v1.1 scripts and removed every spoken number, moving them on screen ("4 times in 791" ->
"almost never"). Inputs here are those two v1.1 scripts; the skill versions are the real commits.

Usage: python run.py [--models opus] [--reps 3] [--versions 0993f3d,4ccc13f,1c81e93,2d8f6fa]
"""
import argparse
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent / "corrections"))
from run import call, is_valid  # noqa: E402

SKILLS = HERE.parent / "skills" / "narration"
INPUTS = HERE / "inputs"
RAW = HERE / "data" / "raw"
SCRIPTS = {"subagent": "subagent_v1.1_script.md", "repetition": "repetition_v1.1_script.md"}

ASK = ("The explainer-script skill has been updated, in particular its Voice section on how numbers "
       "are spoken. Revise this script so that its narration follows the current skill. Keep "
       "everything else as it is. Return the full revised script.\n\n{script}")


def system(version):
    skill = (SKILLS / f"{version}.md").read_text(encoding="utf-8")
    return ("You are a helpful assistant.\n\nThe following skill is loaded for this task. Follow it.\n\n"
            f"<skill>\n{skill}\n</skill>")


def generate(model, version, script, rep):
    dest = RAW / model / version / f"{script}_{rep}.md"
    if dest.exists() and is_valid(dest.read_text(encoding="utf-8")):
        return "skip"
    dest.parent.mkdir(parents=True, exist_ok=True)
    text = (INPUTS / SCRIPTS[script]).read_text(encoding="utf-8")
    out = call(model, system(version), ASK.format(script=text), dest.with_suffix(".work"))
    if not is_valid(out):
        print(f"INVALID {dest.relative_to(RAW)} :: {out[:160]!r}", flush=True)
        return "invalid"
    dest.write_text(out, encoding="utf-8")
    print(f"ok      {dest.relative_to(RAW)} ({len(out)} chars)", flush=True)
    return "ok"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", default="opus")
    ap.add_argument("--versions", default="0993f3d,4ccc13f,1c81e93,2d8f6fa")
    ap.add_argument("--reps", type=int, default=3)
    ap.add_argument("--workers", type=int, default=2)
    args = ap.parse_args()
    jobs = [(m, v, s, r) for r in range(1, args.reps + 1) for m in args.models.split(",")
            for v in args.versions.split(",") for s in SCRIPTS]
    print(f"{len(jobs)} jobs", flush=True)
    with ThreadPoolExecutor(args.workers) as pool:
        results = list(pool.map(lambda j: generate(*j), jobs))
    print({s: results.count(s) for s in set(results)})


if __name__ == "__main__":
    main()
