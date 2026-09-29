"""
Evidence for criterion 5: hall-specific questions, attribution checked.

A try PASSES only if all three hold:
  1. the answer states the fact from that hall's own doc,
  2. it cites at least one file belonging to that hall,
  3. it cites no file belonging to a different hall.
The rule was committed before any results existed.
"""
import argparse
import datetime as dt
import re
import time

import config
from run_eval import run_once

DELAY_SECONDS = 5

HALLS = ["innisfree_hall", "aldridge_hall", "tamsin_court",
         "morrow_house", "calder_annexe", "old_brewhouse"]

# (question, hall, acceptable ways the correct fact could appear)
HALL_QUESTIONS = [
    ("How much does a wash cost in Calder Annexe?",     "calder_annexe",  ("$2.00", "$2 ")),
    ("How much does a dryer cost in Aldridge Hall?",    "aldridge_hall",  ("$1.50",)),
    ("How do you pay for laundry in Aldridge Hall?",    "aldridge_hall",  ("card",)),
    ("How much does a dryer cost in Morrow House?",     "morrow_house",   ("$1.25",)),
    ("How much does a wash cost in Morrow House?",      "morrow_house",   ("$1.50",)),
    ("How do you pay for laundry in Old Brewhouse?",    "old_brewhouse",  ("coin",)),
    ("How much does a dryer cost in Old Brewhouse?",    "old_brewhouse",  ("$1.50",)),
    ("How much does a dryer cost in Innisfree Hall?",   "innisfree_hall", ("$1.75",)),
    ("How do you pay for laundry in Innisfree Hall?",   "innisfree_hall", ("app",)),
    ("What laundry machines does Tamsin Court have?",   "tamsin_court",   ("in-unit",)),
]

CITED_FILE = re.compile(r"[\w\-]+\.txt")


def judge(answer: str, hall: str, expects: tuple[str, ...]):
    text = answer or ""
    cited = sorted(set(CITED_FILE.findall(text)))
    cited_halls = {h for h in HALLS for f in cited if f.startswith(f"housing_{h}")}
    fact_ok = any(e.lower() in text.lower() for e in expects)
    attribution_ok = hall in cited_halls and cited_halls <= {hall}
    return fact_ok, attribution_ok, cited


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--runs", type=int, default=3)
    parser.add_argument("--label", default="")
    args = parser.parse_args()

    top_k, threshold, corpus = config.TOP_K, config.THRESHOLD, config.CORPUS
    label = f" — {args.label}" if args.label else ""
    lines = [
        f"# Criterion 5: hall attribution{label}", "",
        "- Produced by: `run_hall_eval.py::main` (answers via `run_eval.py::run_once`, caching off)",
        f"- top-k: {top_k} · cutoff: {threshold} · When: {dt.datetime.now():%Y-%m-%d %H:%M}",
        "- Pass = correct fact AND cites that hall's doc AND cites no other hall's doc.", "",
    ]
    transcript, totals = [], []

    for run in range(1, args.runs + 1):
        print(f"\nRun {run}")
        lines += [f"## Run {run}", "",
                  "| Question | Fact | Attribution | Cited | Verdict |",
                  "|---|---|---|---|---|"]
        passed = 0
        for question, hall, expects in HALL_QUESTIONS:
            answer, results, decision = run_once(question, top_k, threshold, corpus, "default")
            time.sleep(DELAY_SECONDS)
            fact_ok, attr_ok, cited = judge(answer, hall, expects)
            ok = fact_ok and attr_ok
            passed += ok
            print(f"  {'pass' if ok else 'FAIL'}  {question}")
            lines.append(f"| {question} | {'✓' if fact_ok else '✗'} | "
                         f"{'✓' if attr_ok else '✗'} | {', '.join(cited) or 'none'} | "
                         f"{'pass' if ok else 'FAIL'} |")
            transcript.append((run, question, answer,
                               [(r.label, r.distance) for r in results]))
        totals.append(passed)
        lines += ["", f"**Run {run}: {passed}/{len(HALL_QUESTIONS)}**", ""]

    lines += ["---", "", "## Real output", ""]
    for run, question, answer, retrieved in transcript:
        lines += [f"### {question} — run {run}", "",
                  "- Retrieved: " + ", ".join(f"{l} ({d:.3f})" for l, d in retrieved),
                  "", "```", answer, "```", ""]

    config.RESULTS_DIR.mkdir(exist_ok=True)
    suffix = f"_{args.label}" if args.label else ""
    path = config.RESULTS_DIR / f"hall_eval_{dt.datetime.now():%Y-%m-%d_%H%M}{suffix}.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nTotals per run: {totals}  ->  wrote {path}")


if __name__ == "__main__":
    main()