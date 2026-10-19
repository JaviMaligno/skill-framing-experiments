"""Generate release notes for every (model, condition, case, rep) still missing.

Isolation: --system-prompt replaces Claude Code's default prompt and --setting-sources ""
keeps the user's CLAUDE.md out (checked: with both flags the model cannot quote it).
Outputs are written to a temp file and only promoted if they pass is_valid(), so a
spend-limit or login message never gets scored as a response.

Usage: python run.py [--reps N] [--models opus,sonnet,haiku] [--conds 0,A,B] [--split dev|test|all]
"""
import argparse
import shutil
import subprocess
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from cases import CASES

HERE = Path(__file__).parent
ROOT = HERE.parent
RAW = HERE / "data" / "raw"
SKILLS = ROOT / "skills" / "release-notes"

MODELS = {"opus": "claude-opus-5-5", "sonnet": "claude-sonnet-5-5", "haiku": "claude-haiku-5-5"}
BASE_SYSTEM = "You are a helpful assistant."
NOT_A_RESPONSE = ("spend limit", "usage-credits", "rate limit reached", "Please run /login",
                  "Invalid API key", "quota", "overloaded_error", "API Error")
abort = threading.Event()


def skill_text(cond):
    files = {"A": "A-rules.md", "B": "B-role.md", "A+p": "A-rules+patch.md", "B+p": "B-role+patch.md"}
    return None if cond == "0" else (SKILLS / files[cond]).read_text(encoding="utf-8")


def system_prompt(cond):
    skill = skill_text(cond)
    if skill is None:
        return BASE_SYSTEM
    return f"{BASE_SYSTEM}\n\nThe following skill is loaded for this task. Follow it.\n\n<skill>\n{skill}\n</skill>"


def user_prompt(case):
    items = "\n".join(f"- {c['text']}" for c in case["changes"])
    return (f"Here are the changes merged into Ledgerly this week:\n\n{items}\n\n"
            "Write the release notes for this update. Reply with the release notes only.")


def is_valid(text):
    if not text or len(text.strip()) < 80:
        return False
    return not any(m.lower() in text.lower() for m in NOT_A_RESPONSE)


def generate(model, cond, case, rep, claude):
    dest = RAW / model / cond.replace("+", "_") / f"{case['id']}_{rep}.md"
    if dest.exists() and is_valid(dest.read_text(encoding="utf-8")):
        return "skip"
    if abort.is_set():
        return "aborted"
    dest.parent.mkdir(parents=True, exist_ok=True)
    proc = subprocess.run(
        [claude, "-p", "--model", MODELS[model], "--system-prompt", system_prompt(cond),
         "--setting-sources", "", "--tools", ""],
        input=user_prompt(case).encode("utf-8"), capture_output=True, timeout=300)
    out = proc.stdout.decode("utf-8", errors="replace")
    if not is_valid(out):
        if any(m in out for m in ("spend limit", "usage-credits")):
            abort.set()
        print(f"INVALID {dest.relative_to(RAW)} :: {out[:140]!r} {proc.stderr[:140]!r}", flush=True)
        return "invalid"
    dest.write_text(out, encoding="utf-8")
    print(f"ok      {dest.relative_to(RAW)} ({len(out)} chars)", flush=True)
    return "ok"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--reps", type=int, default=2)
    ap.add_argument("--models", default="haiku,sonnet,opus")
    ap.add_argument("--conds", default="0,A,B")
    ap.add_argument("--split", default="all")
    args = ap.parse_args()
    claude = shutil.which("claude")
    cases = [c for c in CASES if args.split == "all" or c["split"] == args.split]
    jobs = [(m, k, c, r) for m in args.models.split(",") for k in args.conds.split(",")
            for c in cases for r in range(1, args.reps + 1)]
    print(f"{len(jobs)} jobs", flush=True)
    # Two at a time: this machine kills the session when saturated.
    with ThreadPoolExecutor(2) as pool:
        results = list(pool.map(lambda j: generate(*j, claude), jobs))
    print({s: results.count(s) for s in set(results)})
    if abort.is_set():
        print("STOPPED: spend limit hit, jobs left undone")
        sys.exit(1)


if __name__ == "__main__":
    main()
