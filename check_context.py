import re

import config
import gate
import generate
from questions import answered
from run_hall_eval import HALL_QUESTIONS
from store import search

captured = {}


def _capture(prompt, system=None, cache=True):
    captured["prompt"] = prompt
    return "(not sent)"


generate.generate = _capture  # answer_from_chunks looks this up at call time


def measure(title, questions):
    sent_total = past_total = 0
    print(f"\n########## {title} ##########")
    for question in questions:
        results = search(question)
        if not gate.check(results).passed:
            print(f"\n=== {question}\n    refused by the gate (nothing sent)")
            continue
        generate.answer_from_chunks(question, results, cache=False)
        sent = re.findall(r"^\[from (.+?)\]$", captured["prompt"], flags=re.M)
        distance = {r.source: r.distance for r in results}
        print(f"\n=== {question}")
        for source in sent:
            d = distance[source]
            flag = "  <-- PAST CUTOFF" if d >= config.THRESHOLD else ""
            print(f"    sent: {source}  distance={d:.4f}{flag}")
            past_total += d >= config.THRESHOLD
        sent_total += len(sent)
    print(f"\n{title}: {past_total} of {sent_total} chunks sent to the model "
          f"were past the {config.THRESHOLD} cutoff")


measure("Test questions (questions.py)", [q["question"] for q in answered()])
measure("Hall questions (run_hall_eval.py)", [q for q, _, _ in HALL_QUESTIONS])