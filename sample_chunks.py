"""Evidence for criterion 4: three separate random draws of 10 chunks each."""
import random
from ingest import load_documents
from chunker import split_documents

chunks = split_documents(load_documents())
print(f"{len(chunks)} chunks total, produced by {chunks[0].produced_by}\n")

for run, seed in enumerate([1, 2, 3], 1):
    sample = random.Random(seed).sample(chunks, 10)
    print(f"########## Run {run} (seed {seed}) ##########")
    for i, c in enumerate(sample, 1):
        print(f"\n--- {run}.{i}  {c.label}")
        print(c.text)
        print("Standalone?  [ ] yes  [ ] no   Reason:")
    print()