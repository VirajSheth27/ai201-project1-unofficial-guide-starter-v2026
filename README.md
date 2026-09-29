# The Unofficial Guide

<!-- Replace this line with your name and which corpus you picked. -->

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

The RAG system built over campus_life—a real-world corpus of 88 student-written posts covering housing, dining halls, course workloads, and administrative edge cases. It answers queries like "Does the campus store price-match textbooks?" or "How is ENGL 205 graded?" by identifying the most relevant document chunks and generating a precise response that explicitly cites its source. If a user asks a question outside the scope of the corpus (like general world trivia or unrelated campus topics), the system uses a vector distance threshold ( cutoff at 0.55 ) to politely refuse to answer rather than fabricate information.

## Chunking Strategy

**Chunk size:** No fixed chunk size

**Overlap:** None

The campus_life documents are short (averaging 317 characters, with the longest found at ~550 characters) and single-topic, with each post opening with a self-naming title line (e.g., "Laundry in Innisfree Hall" or "Morrow House — what it's actually like"). I split on paragraph breaks (\n\n) with a 600-character ceiling as a explicit safety net for longer, multi-paragraph documents, rather than relying on a arbitrary default size that happened not to trigger splits.

I confirmed via raw string inspection (repr() on file contents) that paragraphs across both general overview files and specific sub-topic files are consistently separated by \n\n. In practice, this strategy yields one chunk per document across almost all 88 files—a deliberate design choice backed by corpus analysis, since the longest overview document sitting at ~550 characters easily fits under the 600-character ceiling without arbitrary truncation. While I initially considered injecting filename and title headers directly into the chunk text to solve potential context gaps, inspecting raw samples proved that every document already explicitly self-identifies in its first line. Consequently, I kept raw chunk text untouched and rely on the attached metadata payload for downstream citation tracking and source attribution.k

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

**Chunk 1** — source: `admin_add_drop_deadline.txt#0` — produced by: `chunker.py::split_documents`

```
On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other.
```

**Chunk 2** — source: `course_biol_160.txt#0` — produced by: `chunker.py::split_documents`

```
BIOL 160 Cell Biology

I lived here my sophomore year. Format is lecture three times a week with a weekly lab. Assessment: four unit tests and a cumulative final. Not curved.

Expect 9 to 11 hours a week, the heaviest first-year course by reputation.

The one piece of advice: the unit tests come fast, roughly every three weeks; falling behind once is very hard to recover from.
```

**Chunk 3** — source: `course_hist_118_workload.txt#0` — produced by: `chunker.py::split_documents`

```
Workload for HIST 118 Modern World History

People keep asking so: a lot of reading, about 120 pages a week, but no problem sets. That's real time, not optimistic time.

It's front-loaded — the first month is heavier than the rest, partly because you're learning the format.
```

**Chunk 4** — source: `dining_pellew_dining_hall_followup.txt#0` — produced by: `chunker.py::split_documents`

```
Re: Pellew Dining Hall

Adding to what people have said about Pellew Dining Hall. The wait figure of 12 to 18 minutes at peak matches what I've seen. If you're trying to eat between classes, go before 11:45 and it's a different building entirely.

Also worth saying: the furthest hall from anywhere, next to the athletics centre. Nobody tells you this at orientation.
```

**Chunk 5** — source: `housing_innisfree_hall.txt#0` — produced by: `chunker.py::split_documents`

```
Innisfree Hall — what it's actually like

Transferred in last year, so take this with a grain of salt. Built 1991, renovated 2022. Rooms are doubles arranged as pairs sharing one bathroom between two rooms.

The good: the shared-bathroom-between-two-rooms arrangement is the best compromise on campus.

The bad: no air conditioning, which matters for the first three weeks of September.

Laundry costs $1.75 wash, $1.75 dry, app-based. On noise: moderate; the building is L-shaped and the short wing is much quieter.

For each one, ask: could someone answer a question using only this,
without reading what came before or after?
```

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:** Does the campus store price-match textbooks?

**Answer:**

```
Yes, the campus store price-matches, though it is not advertised anywhere and you must ask at the counter with the other listing on your phone. This comes from money_textbooks.txt.
```

**My relevance cutoff:** 0.55

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->

| Question | In corpus? | Best distance |
|---|---|---|
| Does the campus store price-match textbooks?|  Yes | 0.241 |
| How is ENGL 205 graded? |  Yes | 0.303 |
| What is the capital of Mongolia?|  No | 0.825 |
| How do I change the oil in a diesel engine? |  No | 0.934 |

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.** I asked Claude whether I should inject filenames into chunk text to fix a context problem I found in one chunk. It initially agreed a fix was needed, but pushed back when I generalized to 'always inject headers' — sampling 10 chunks showed most already self-identify, so I dropped the header idea and kept chunk text untouched.

**2.** After writing criterion 4 (8 of 10 chunks pass a completeness check) based on reading just 5 chunks, I asked Claude to help me verify the reasoning behind it.

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->

# Unit 2
 
## Run Log — Before
 
Evidence files, all committed in results folder.
 
| Criterion | Produced by | File |
|---|---|---|
| 2 (and raw answers) | `run_eval.py::main` → `run_eval.py::run_once` → `generate.py::answer_from_chunks` | `results/run_2026-09-29_0033_before.md` (original, buggy scorer) and `results/run_<TIMESTAMP>_before-scorerfix.md` (re-run, fixed scorer) |
| 1 | `check_retrieval.py` (module-level script) → `store.py::search` | `results/retrieval_check_before.txt` |
| 3 | `run_eval.py::check_out_of_scope`, plus `python app.py ask` for the refusal text | `results/run_2026-09-29_0033_before.md`, `results/refusal_check_before.txt` |
| 4 | `sample_chunks.py` → `chunker.py::split_documents` | `results/chunk_sample_before.txt` |
| 5 | `run_hall_eval.py::main` → `run_eval.py::run_once` | `results/hall_eval_2026-09-29_0058_before.md` |
 
Settings: corpus `campus_life`, index variant `default`, top-k 3, relevance cutoff 0.55, caching off.
 
| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Sampled chunks stand alone (revised target) | 10 of 10 | 10/10 | 10/10 | 10/10 | MET |
| 5. Hall questions attributed to the right hall | 8 of 10 | 10/10 | 10/10 | 10/10 | MET |
 
Criteria 1 and 3 have one number repeated across all three columns. Retrieval is deterministic (every question got identical distances in all three runs) and the gate is a comparison against a fixed number, so there is one measurement. Criteria 2 and 5 depend on generated answers and were genuinely re-generated each run: the answer wording differs between runs (for example "three or four days (health_center.txt)" vs "three or four days. Source: health_center.txt"), which confirms caching was off. Criterion 4 is three independent seeded random draws of 10 chunks (seeds 1, 2, 3).
 
**Two things that went wrong during testing, both in the test harness rather than the system:**
 
1. **Scorer bug.** The first run (`run_2026-09-29_0033_before.md`) marked the Innisfree laundry question as failing in all three runs. The answer was correct ("Tuesday or Wednesday morning", matching the source doc word for word). `scorer.py::judge` compared `expects.lower()` against the answer without lowercasing the answer, so `"tuesday"` never matched "Tuesday". The other four questions only passed because their expected words happen to be lowercase in the answers. I fixed the scorer, left the original results file untouched as evidence, and re-ran as `before-scorerfix`.
2. **Rate limit.** The first attempt at the criterion 5 run hit the Gemini free-tier limit (15 requests per minute) partway through run 2 and crashed before writing a file. I added a 5-second delay between calls and re-ran all three runs from scratch. The partial results shown on screen were not counted.


## Verdicts
 
| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunk contains the answer | MET | The target was 4 of 5 and all three runs scored 5/5. The expected answer was in the top-ranked chunk for every question, which I confirmed by reading the chunk text, not just trusting the keyword match. |
| 2 | Every answer names a source | MET | The target was 5 of 5 and all 15 generated answers named at least one `.txt` file. The citation format varied (parentheses, "Source:", backticks, italics), and I counted any explicit filename. Refusals aren't counted, since the gate returns them before an answer is generated. |
| 3 | Gate stops out-of-corpus questions | MET | The target was 4 of 5 and all 5 were refused, with the exact refusal message and zero model calls. It wasn't close: the nearest out-of-scope question (0.825) sat 0.275 past the 0.55 cutoff. |
| 4 | Sampled chunks stand alone | MET | The revised target was 10 of 10 per draw and all three seeded draws scored 10/10, judged against a rule written before marking. The closest calls were the two "Re:" follow-up posts, which I passed because they restate every fact they refer to and name the place. |
| 5 | Hall questions attributed to the right hall | MET | The target was 8 of 10 and all three runs scored 10/10. Fenwick Court was missing from the checker's hall list during this run, but I read all 30 answers and none cited it, so no result changes. |
 
No criteria were revised in this unit. All five could be measured and were. Criterion 3 turned out to be too easy, but a target that is too easy isn't a broken measurement, so it stays as written and is discussed below and under What I'd Do Differently. (Criterion 4's revision from 8/10 to 10/10 was made in unit 1, before any results existed, and is recorded in `criteria.md`.)
 
## Diagnoses
 
**I missed nothing.** All five criteria were met on all three runs, so there is no pipeline failure to trace. 
 
**Were my targets set low? Honestly, mostly yes.**
 
- **Criterion 3 is the weakest.** My out-of-scope questions (Mongolia, diesel engines, the World Cup) come from a different world entirely, so they landed at 0.825–0.934, nowhere near the 0.55 cutoff. A real user of a campus guide asks campus questions the corpus doesn't cover, and those would sit much closer to the cutoff. **I'd tighten it to:** "At least 4 of 5 near-domain questions the corpus doesn't cover (for example gym hours, parking permits, the campus Wi-Fi password) are refused." That tests the gate where it could actually fail.
- **Criterion 4 was nearly unmissable.** My chunker never splits anything (88 documents become 88 chunks), and every document opens with a self-naming title line. So this criterion measured how well the corpus is written, not how well my chunker works.
- **Criterion 5 named the hall in every question**, which gives retrieval an easy anchor. **I'd tighten it to:** 8 of 10 on questions that don't name the hall up front, such as "Which residence hall has $1.25 dryers?", where near-identical laundry docs would actually compete.
- **Criterion 2 only checks that a source is named, not that it's the right one.** A stricter version would require the cited file to be one that actually contains the stated fact.
- **Criterion 1 at 4 of 5 left room for a miss the system never needed.** Every answer came from the top-ranked chunk, so 5 of 5 at rank 1 would have been a fairer target.

**Weaknesses my tests surfaced that no criterion captured:**
 
- **Retrieval/gate stage — irrelevant chunks reach the model.** The gate checks only the best distance, and `run_eval.py::run_once` passes all top-k results to `generate.py::answer_from_chunks`. So once the best chunk passes, every retrieved chunk goes to the model, however far away it is. Across my five test questions, **4 of the 15 chunks sent to the model were past the 0.55 cutoff**: `admin_library_holds.txt` (0.652) for the price-match question, `transit_walking.txt` (0.705) and `housing_calder_annexe_noise.txt` (0.782) for the snow question, and `admin_grade_appeals.txt` (0.583) for the counselling question. None caused a wrong answer this time, but the model is being handed text the gate itself would call irrelevant.
- **Generation stage — contradictions copied without comment.** `housing_tamsin_court_laundry.txt` says both "in-unit washer-dryer" and "eight washers and six dryers for the building". All three Tamsin answers repeated both claims without flagging that the source contradicts itself.
- **Generation stage — small invented links.** One Old Brewhouse answer (run 3) said you pay with coins "as the machines take $1.50", connecting two facts the source never connects.
## The Improvement
 
 
**What I changed:** _To fill in after the change._ Planned: filter retrieved chunks individually against the 0.55 cutoff before generation, so only chunks the gate would accept reach the model.
 
**Why I picked it:** My diagnosis found that 4 of the 15 chunks sent to the model were past my own relevance cutoff, because the gate checks only the best distance. Filtering chunks individually targets exactly that mechanism. I didn't pick hybrid search, because no test failed in a way keyword matching would fix.
 
**How I'll measure it:** the number of past-cutoff chunks sent to the model across the five test questions (4 of 15 before), plus all five criteria re-run with three runs each, to check the change didn't break anything.
 
### Run Log — After
 
<!-- TODO: fill in from the after runs. -->
 
| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. Sampled chunks stand alone (revised target) | 10 of 10 |  |  |  |  |
| 5. Hall questions attributed to the right hall | 8 of 10 |  |  |  |  |
 
| Measure | Before | After |
|---|---|---|
| Past-cutoff chunks sent to the model (5 test questions) | 4 of 15 |  |