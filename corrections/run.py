"""Generate responses for experiment 2 (corrections). Same isolation as release_notes/run.py.

Usage: python run.py [--reps N] [--models opus,astra] [--conds 0,R,W] [--tasks numbers,questions,...]
Codex models need CODEX_ISOLATED_HOME (a CODEX_HOME holding only auth.json).
"""
import argparse
import os
import shutil
import subprocess
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from tasks import TASKS

HERE = Path(__file__).parent
RAW = HERE / "data" / "raw"
MODELS = {"opus": "claude-opus-5-5", "sonnet": "claude-sonnet-5-5", "haiku": "claude-haiku-5-5",
          "astra": "gpt-6-astra", "sol": "gpt-6.1-sol", "luna": "gpt-6-luna"}
CODEX = {"astra", "sol", "luna"}
CODEX_HOME = os.environ.get("CODEX_ISOLATED_HOME")
BASE_SYSTEM = "You are a helpful assistant."
NOT_A_RESPONSE = ("spend limit", "usage-credits", "rate limit reached", "Please run /login",
                  "Invalid API key", "quota", "overloaded_error", "API Error")
abort = threading.Event()


def system_prompt(task, cond):
    t = TASKS[task]
    skill = t["base"] + ("" if cond == "0" else "\n" + t[cond])
    return f"{BASE_SYSTEM}\n\nThe following skill is loaded for this task. Follow it.\n\n<skill>\n{skill}\n</skill>"


def is_valid(text):
    if not text or len(text.strip()) < 40:
        return False
    return not any(m.lower() in text.lower() for m in NOT_A_RESPONSE)


def call(model, system, prompt, work):
    if model in CODEX:
        if not CODEX_HOME:
            raise SystemExit("CODEX_ISOLATED_HOME is not set")
        work.mkdir(parents=True, exist_ok=True)
        (work / "system.md").write_text(system, encoding="utf-8")
        last = work / "last.md"
        proc = subprocess.run(
            [shutil.which("codex"), "exec", "-m", MODELS[model],
             "-c", f"model_instructions_file='{(work / 'system.md').resolve().as_posix()}'",
             "-c", 'model_reasoning_effort="medium"', "--skip-git-repo-check", "--ephemeral",
             "-s", "read-only", "-C", str(work), "-o", str(last), "-"],
            input=prompt.encode("utf-8"), capture_output=True, timeout=600,
            env={**os.environ, "CODEX_HOME": CODEX_HOME})
        out = last.read_text(encoding="utf-8") if last.exists() else proc.stderr.decode("utf-8", "replace")
        shutil.rmtree(work, ignore_errors=True)
        return out
    proc = subprocess.run(
        [shutil.which("claude"), "-p", "--model", MODELS[model], "--system-prompt", system,
         "--setting-sources", "", "--tools", ""],
        input=prompt.encode("utf-8"), capture_output=True, timeout=300)
    return proc.stdout.decode("utf-8", "replace")


def generate(model, task, cond, case, rep):
    dest = RAW / model / task / cond / f"{case['id']}_{rep}.md"
    if dest.exists() and is_valid(dest.read_text(encoding="utf-8")):
        return "skip"
    if abort.is_set():
        return "aborted"
    dest.parent.mkdir(parents=True, exist_ok=True)
    out = call(model, system_prompt(task, cond), TASKS[task]["ask"].format(src=case["src"]),
               dest.with_suffix(".work"))
    if not is_valid(out):
        if any(m in out for m in ("spend limit", "usage-credits")):
            abort.set()
        print(f"INVALID {dest.relative_to(RAW)} :: {out[:160]!r}", flush=True)
        return "invalid"
    dest.write_text(out, encoding="utf-8")
    print(f"ok      {dest.relative_to(RAW)} ({len(out)} chars)", flush=True)
    return "ok"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--reps", type=int, default=3)
    ap.add_argument("--models", default="opus,astra")
    ap.add_argument("--conds", default="0,R,W")
    ap.add_argument("--tasks", default=",".join(TASKS))
    ap.add_argument("--workers", type=int, default=2)
    args = ap.parse_args()
    jobs = [(m, t, k, c, r) for r in range(1, args.reps + 1) for m in args.models.split(",")
            for t in args.tasks.split(",") for k in args.conds.split(",") for c in TASKS[t]["cases"]]
    print(f"{len(jobs)} jobs", flush=True)
    # Few at a time: this machine kills the session when saturated.
    with ThreadPoolExecutor(args.workers) as pool:
        results = list(pool.map(lambda j: generate(*j), jobs))
    print({s: results.count(s) for s in set(results)})
    if abort.is_set():
        print("STOPPED: spend limit hit, jobs left undone")
        sys.exit(1)


if __name__ == "__main__":
    main()
