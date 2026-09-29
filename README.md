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
 
## Run Log — Before
 
Evidence files, all committed in `results/`:
 
| Criterion | Produced by | File |
|---|---|---|
| 2 (and raw answers) | `run_eval.py::main` → `run_eval.py::run_once` → `generate.py::answer_from_chunks` | `results/run_2026-09-29_0033_before.md` (original, buggy scorer) and `results/run_<TIMESTAMP>_before-scorerfix.md` (re-run, fixed scorer) |
| 1 | `check_retrieval.py` (module-level script) → `store.py::search` | `results/retrieval_check_before.txt` |
| 3 | `run_eval.py::check_out_of_scope`, plus `python app.py ask` for the refusal text | `results/run_2026-09-29_0033_before.md`, `results/refusal_check_before.txt` |
| 4 | `sample_chunks.py` → `chunker.py::split_documents` | `results/chunk_sample_before.txt` |
| 5 | `run_hall_eval.py::main` → `run_eval.py::run_once` | `results/hall_eval_<TIMESTAMP>_before.md` (run started 00:58) |
 
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
### Real output
 
**Criterion 1** — `check_retrieval.py`, retrieval by `store.py::search`, from `results/retrieval_check_before.txt`:
 
```
=== When is the best time to do laundry at Innisfree Hall?
    expects 'Tuesday' -> IN A RETRIEVED CHUNK
    1. housing_innisfree_hall_laundry.txt#0  distance=0.3376
       Laundry in Innisfree Hall  Machines take $1.75 wash, $1.75 dry, app-based. There are eight washers and six dryers for the building, which is the wrong ratio and means the dryers back up on Sunday evenings.  Best time to do laundry here is Tuesday or Wednesday morning. Sunday after 6pm you will wait.
    2. housing_tamsin_court_laundry.txt#0  distance=0.4344
       Laundry in Tamsin Court  Machines take in-unit washer-dryer. There are eight washers and six dryers for the building, which is the wrong ratio and means the dryers back up on Sunday evenings.  Best time to do laundry here is Tuesday or Wednesday morning. Sunday after 6pm you will wait.
    3. housing_aldridge_hall_laundry.txt#0  distance=0.4444
       Laundry in Aldridge Hall  Machines take $1.75 wash, $1.50 dry, card only. There are eight washers and six dryers for the building, which is the wrong ratio and means the dryers back up on Sunday evenings.  Best time to do laundry here is Tuesday or Wednesday morning. Sunday after 6pm you will wait.
```
 
For all five questions, the expected answer was in the **top-ranked** chunk, not just somewhere in the top three.
 
**Criterion 2** — `generate.py::answer_from_chunks` via `run_eval.py::run_once`, run 1 of each question, from `results/run_2026-09-29_0033_before.md`:
 
```
Q: Does the campus store price-match textbooks?
Yes, the campus store price-matches textbooks, though it is not advertised and you have to ask at the counter with the other listing on your phone. 
 
Source: money_textbooks.txt
```
 
```
Q: When do the paths get cleared after snow?
The paths get cleared by 7am on weekdays and considerably later on weekends (winter_gear.txt).
```
 
```
Q: When is the best time to do laundry at Innisfree Hall?
The best time to do laundry at Innisfree Hall is Tuesday or Wednesday morning. 
 
Source: housing_innisfree_hall_laundry.txt
```
 
```
Q: How long is the wait for a first counselling appointment?
The wait for a first counselling session is usually three or four days (health_center.txt).
```
 
```
Q: How is ENGL 205 Writing for the Sciences graded?
ENGL 205 has no exams and is assessed using a portfolio of six revised pieces that is not curved. The portfolio is graded on revision, meaning students are marked on the distance traveled and must keep their drafts (Source: `course_engl_205.txt`, `course_engl_205_exams.txt`).
```
 
**Criterion 3** — `run_eval.py::check_out_of_scope`, from `results/run_2026-09-29_0033_before.md`:
 
| Out-of-scope question | Best distance | Gate |
|---|---|---|
| What is the capital of Mongolia? | 0.825 | refused |
| How do I change the oil in a diesel engine? | 0.934 | refused |
| Who won the 1994 World Cup? | 0.886 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.844 | refused |
| How do I write a for loop in Rust? | 0.896 | refused |
 
And the refusal the user actually sees, from `python app.py ask` (`results/refusal_check_before.txt`):
 
```
  (best distance 0.825, cutoff 0.55)
 
I don't have enough information about that.
 
0 model calls this session
```
 
**Criterion 4** — `sample_chunks.py`, chunks from `chunker.py::split_documents`, from `results/chunk_sample_before.txt`. This is the closest call of the 30:
 
```
--- 1.7  dining_verrill_street_grill_followup.txt#0
Re: Verrill Street Grill
 
Adding to what people have said about Verrill Street Grill. The wait figure of up to 30 minutes on Friday evenings matches what I've seen. If you're trying to eat between classes, go before 11:45 and it's a different building entirely.
 
Also worth saying: one register, so the queue is a single line no matter how busy. Nobody tells you this at orientation.
Standalone?  [x] yes  [ ] no   Reason: BORDERLINE. It's a reply ("Adding to what people have said"), so it points at an earlier post. It still passes because it restates the facts it refers to (up to 30 minutes on Friday evenings, go before 11:45, single register) and names the place, so "How long is the wait at Verrill Street Grill on Fridays?" is answerable from this chunk alone.
```
 
**Criterion 5** — `run_hall_eval.py::main`, answers via `run_eval.py::run_once`, from `results/hall_eval_<TIMESTAMP>_before.md` (run started 00:58). This is the question where two chunks nearly tied:
 
```
### How much does a dryer cost in Morrow House? — run 1
 
- Retrieved: housing_morrow_house.txt#0 (0.322), housing_morrow_house_laundry.txt#0 (0.323), housing_old_brewhouse_laundry.txt#0 (0.490)
 
A dryer in Morrow House costs $1.25. 
 
Source: housing_morrow_house.txt (also mentioned in housing_morrow_house_laundry.txt)
```
 
A try passed only if the answer stated that hall's fact **and** cited that hall's doc **and** cited no other hall's doc. This rule was committed in `run_hall_eval.py` before the run. The ten questions were chosen so each correct answer differs between halls (for example Morrow's $1.25 dryer), because the original laundry test question couldn't detect a wrong-hall answer: the "best time" sentence is identical in every hall's laundry doc.
 
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
 
**I missed nothing.** All five criteria were met on all three runs, so there is no pipeline failure to trace. The one failure my test reported (the laundry question) traced back to the test itself, not the pipeline. Working backwards: the answer was in the top-ranked chunk (so loading, chunking, embedding and retrieval were fine), and the generated answer matched that chunk word for word (so generation was fine). That left the scorer, which was comparing case-sensitively.
 
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
 
**What I changed:** I added `gate.py::relevant`, which keeps only the chunks whose own distance is under the 0.55 cutoff, and called it at the top of `generate.py::build_prompt`. Before the change, the gate only checked the *best* chunk, and every top-k result went into the prompt once that one chunk passed. Now each chunk has to pass the same cutoff on its own. This was the only system change in this unit (commit: "Improvement: drop chunks past the relevance cutoff before generation").
 
**Why I picked it:** My diagnosis found that 4 of the 15 chunks sent to the model were past my own relevance cutoff, because `gate.check` looks only at the best distance. Filtering each chunk against the same cutoff targets exactly that mechanism. I didn't pick hybrid search, because no test failed in a way keyword matching would fix.
 
**The risk I expected:** the 0.55 cutoff was calibrated to decide whether a *question* is answerable, not whether a *supporting chunk* is useful, so the filter could drop a chunk that held part of an answer. I checked for this specifically.
 
**How I measured it:** `check_context.py` replaces the API call with a function that captures the prompt, then runs `generate.py::answer_from_chunks` for every question and counts which chunks actually appear in the prompt. It makes zero model calls and measures the real prompt, not a reconstruction of it, so the same script works before and after the change. I also re-ran all five criteria, three runs each.
 
### Context check — before and after
 
Produced by `check_context.py`, from `results/context_check_before.txt` and `results/context_check_after.txt`:
 
| Measure | Before | After |
|---|---|---|
| Past-cutoff chunks sent to the model (5 test questions) | 4 of 15 | 0 of 11 |
| Past-cutoff chunks sent to the model (10 hall questions) | 0 of 30 | 0 of 30 |
| Questions where the answer chunk still reached the model | 5 of 5 | 5 of 5 |
 
The four chunks removed were exactly the four my diagnosis named:
 
```
BEFORE
=== Does the campus store price-match textbooks?
    sent: money_textbooks.txt  distance=0.2412
    sent: admin_printing_quota.txt  distance=0.5148
    sent: admin_library_holds.txt  distance=0.6519  <-- PAST CUTOFF
 
=== When do the paths get cleared after snow?
    sent: winter_gear.txt  distance=0.4568
    sent: transit_walking.txt  distance=0.7050  <-- PAST CUTOFF
    sent: housing_calder_annexe_noise.txt  distance=0.7815  <-- PAST CUTOFF
 
=== How long is the wait for a first counselling appointment?
    sent: health_center.txt  distance=0.3594
    sent: advising_registration.txt  distance=0.5380
    sent: admin_grade_appeals.txt  distance=0.5832  <-- PAST CUTOFF
 
Test questions (questions.py): 4 of 15 chunks sent to the model were past the 0.55 cutoff
```
 
```
AFTER
=== Does the campus store price-match textbooks?
    sent: money_textbooks.txt  distance=0.2412
    sent: admin_printing_quota.txt  distance=0.5148
 
=== When do the paths get cleared after snow?
    sent: winter_gear.txt  distance=0.4568
 
=== How long is the wait for a first counselling appointment?
    sent: health_center.txt  distance=0.3594
    sent: advising_registration.txt  distance=0.5380
 
Test questions (questions.py): 0 of 11 chunks sent to the model were past the 0.55 cutoff
```
 
### Run Log — After
 
Evidence files, all committed in `results/`: `run_2026-09-29_0146_after.md` (criteria 2 and 3), `retrieval_check_after.txt` (criterion 1), `refusal_check_after.txt` (criterion 3), `chunk_sample_after.txt` (criterion 4), and `hall_eval_<TIMESTAMP>_after.md` (criterion 5, run started 01:47). Same settings as before: top-k 3, cutoff 0.55, caching off.
 
| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Sampled chunks stand alone (revised target) | 10 of 10 | 10/10 | 10/10 | 10/10 | MET |
| 5. Hall questions attributed to the right hall | 8 of 10 | 10/10 | 10/10 | 10/10 | MET |
 
`retrieval_check_after.txt` and `chunk_sample_after.txt` are identical to their before versions, which is expected, because the change doesn't touch retrieval or chunking. The criterion 5 re-run used the stricter checker with Fenwick Court added to the hall list; no answer cited Fenwick.
 
**Reading the after file correctly:** the "Sources retrieved" line in `run_2026-09-29_0146_after.md` still lists three sources for every question, including the past-cutoff ones. That's because `run_eval.py` logs what `store.py::search` *retrieved*, and the filter runs afterwards, inside `build_prompt`. What was actually *sent* to the model is in `context_check_after.txt`.
 
Real output after the change, `generate.py::answer_from_chunks` via `run_eval.py::run_once`, run 1. These are the two questions that lost chunks to the filter:
 
```
Q: When do the paths get cleared after snow?   (context: winter_gear.txt only; 2 chunks removed)
The paths get cleared by 7am on weekdays and considerably later on weekends (winter_gear.txt).
```
 
```
Q: How long is the wait for a first counselling appointment?   (context: 2 chunks; 1 removed)
The wait for a first counselling session is usually three or four days (health_center.txt).
```
 
**Did it help?** It did what it was built to do, and nothing more. Past-cutoff chunks reaching the model went from 4 of 15 to 0 of 11, and the answer chunk survived the filter for every question, so the risk I expected didn't happen. But no criterion changed, because all five were already met, and the answers didn't measurably improve either: the snow and counselling answers are word for word the same as before the change. The irrelevant chunks were never causing wrong answers, so removing them made the context cleaner without making the output better. I know this because I compared the before and after answers for the three questions that lost chunks, and the stated facts and citations are unchanged.
 
Two limits showed up in the after measurement:
 
- **The cutoff isn't a clean relevance line.** Two clearly irrelevant chunks still get through because they sit just under 0.55: `admin_printing_quota.txt` (0.515) for the price-match question and `advising_registration.txt` (0.538) for the counselling question.
- **It does nothing for the wrong-hall risk.** The hall questions had 0 of 30 past-cutoff chunks both before and after, so the filter never touched them, yet those prompts still include other halls' laundry docs well under the cutoff: Innisfree's laundry doc at 0.389 for a Morrow House question, and Fenwick Court's at 0.404 for an Old Brewhouse question. Near-duplicate docs about a different building sit *close* in embedding space, so a distance filter can't separate them.
## What's Still Broken
 
No criterion is missed after the fix, but these problems remain:
 
- **Wrong-hall chunks still reach the model (retrieval stage).** 
- **The gate has never been tested on near-domain questions.** 
- **Irrelevant chunks just under the cutoff still get through** 
- **The model repeats contradictions in the source (generation stage).** 
- **Occasional invented connections between facts.** 
## What I'd Do Differently
 
Knowing what I know now, I'd rewrite three of my five criteria for the next unit:
 
- **Criterion 3:** I'd use near-domain out-of-scope questions. Questions from a completely different world only prove the gate can reject what obviously doesn't belong; they say nothing about the borderline cases a real student would actually ask.
- **Criterion 5:** I'd write the test questions before trusting the one existing laundry question. The "best time" sentence is identical across every hall's laundry doc, so that question could never catch a wrong-hall answer. I'd also include questions that don't name the hall, such as "Which residence hall has $1.25 dryers?", where the near-duplicate docs would really compete. And I'd add a criterion on what reaches the model, not just what comes out of it, since that's where the wrong-hall risk actually lives.
- **Criterion 4:** I'd write a criterion that actually tests the chunker, for example on the few longest documents, rather than one that passes automatically because every document is already a single chunk.
I'd also test the scorer on a known-correct answer before trusting it. A case-sensitivity bug cost me a false failure on my very first run, and I only caught it by reading the answer instead of the verdict.

## How I Used AI

I used AI to help me draft the README as well as go about helping write code. The thinking and how to do it was all done by me only the code and the readme generation was done with the help of AI.