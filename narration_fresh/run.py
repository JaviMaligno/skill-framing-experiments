"""The narration episode on fresh material.

Stage 1 (draft): Opus writes a v1 script for each article with the skill as it was before any
numbers guidance (d658477), once. These drafts are the fixed inputs, as the v1.1 scripts were in
the original episode.
Stage 2 (revise): every model revises every draft under each version of the skill.

Articles are the author's own experiment write-ups that never had a video.

Usage: python run.py draft
       python run.py revise [--models opus,astra,haiku,luna] [--reps 3] [--workers 2]
"""
import argparse
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent / "corrections"))
from run import call, is_valid  # noqa: E402

SKILLS = HERE.parent / "skills" / "narration"
ARTICLES = HERE / "articles"
DRAFTS = HERE / "drafts"
RAW = HERE / "data" / "raw"
DRAFT_SKILL = "d658477"
VERSIONS = ("0993f3d", "4ccc13f", "1c81e93", "2d8f6fa")

DRAFT_ASK = "Write the explainer video script for this article.\n\n<article>\n{article}\n</article>"
REVISE_ASK = ("The explainer-script skill has been updated, in particular its Voice section on how "
              "numbers are spoken. Revise this script so that its narration follows the current skill. "
              "Keep everything else as it is. Return the full revised script.\n\n{script}")


def system(version):
    skill = (SKILLS / f"{version}.md").read_text(encoding="utf-8")
    return ("You are a helpful assistant.\n\nThe following skill is loaded for this task. Follow it.\n\n"
            f"<skill>\n{skill}\n</skill>")


def job(dest, model, version, prompt):
    if dest.exists() and is_valid(dest.read_text(encoding="utf-8")):
        return "skip"
    dest.parent.mkdir(parents=True, exist_ok=True)
    out = call(model, system(version), prompt, dest.with_suffix(".work"))
    if not is_valid(out):
        print(f"INVALID {dest} :: {out[:160]!r}", flush=True)
        return "invalid"
    dest.write_text(out, encoding="utf-8")
    print(f"ok      {dest.relative_to(HERE)} ({len(out)} chars)", flush=True)
    return "ok"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("stage", choices=["draft", "revise"])
    ap.add_argument("--models", default="opus,astra,haiku,luna")
    ap.add_argument("--reps", type=int, default=3)
    ap.add_argument("--workers", type=int, default=2)
    args = ap.parse_args()
    articles = sorted(p.stem for p in ARTICLES.glob("*.md"))
    if args.stage == "draft":
        jobs = [(DRAFTS / f"{a}.md", "opus", DRAFT_SKILL,
                 DRAFT_ASK.format(article=(ARTICLES / f"{a}.md").read_text(encoding="utf-8"))) for a in articles]
    else:
        jobs = [(RAW / m / v / f"{a}_{r}.md", m, v,
                 REVISE_ASK.format(script=(DRAFTS / f"{a}.md").read_text(encoding="utf-8")))
                for r in range(1, args.reps + 1) for m in args.models.split(",") for v in VERSIONS for a in articles]
    print(f"{len(jobs)} jobs", flush=True)
    with ThreadPoolExecutor(args.workers) as pool:
        results = list(pool.map(lambda j: job(*j), jobs))
    print({s: results.count(s) for s in set(results)})


if __name__ == "__main__":
    main()
