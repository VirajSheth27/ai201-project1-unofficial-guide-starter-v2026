"""Evidence for criterion 1: does a retrieved chunk contain the expected answer?"""
from questions import answered
from store import search

for q in answered():
    results = search(q["question"])
    hit = any(q["expects"].lower() in r.text.lower() for r in results)
    print(f"\n=== {q['question']}")
    print(f"    expects {q['expects']!r} -> {'IN A RETRIEVED CHUNK' if hit else 'NOT IN ANY CHUNK'}")
    for rank, r in enumerate(results, 1):
        print(f"    {rank}. {r.label}  distance={r.distance:.4f}")
        print("       " + r.text.replace("\n", " ")[:300])