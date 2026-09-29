# Criterion 5: hall attribution — before

- Produced by: `run_hall_eval.py::main` (answers via `run_eval.py::run_once`, caching off)
- top-k: 3 · cutoff: 0.55 · When: 2026-09-29 00:58
- Pass = correct fact AND cites that hall's doc AND cites no other hall's doc.

## Run 1

| Question | Fact | Attribution | Cited | Verdict |
|---|---|---|---|---|
| How much does a wash cost in Calder Annexe? | ✓ | ✓ | housing_calder_annexe.txt, housing_calder_annexe_laundry.txt | pass |
| How much does a dryer cost in Aldridge Hall? | ✓ | ✓ | housing_aldridge_hall.txt, housing_aldridge_hall_laundry.txt | pass |
| How do you pay for laundry in Aldridge Hall? | ✓ | ✓ | housing_aldridge_hall.txt, housing_aldridge_hall_laundry.txt | pass |
| How much does a dryer cost in Morrow House? | ✓ | ✓ | housing_morrow_house.txt, housing_morrow_house_laundry.txt | pass |
| How much does a wash cost in Morrow House? | ✓ | ✓ | housing_morrow_house.txt, housing_morrow_house_laundry.txt | pass |
| How do you pay for laundry in Old Brewhouse? | ✓ | ✓ | housing_old_brewhouse.txt, housing_old_brewhouse_laundry.txt | pass |
| How much does a dryer cost in Old Brewhouse? | ✓ | ✓ | housing_old_brewhouse.txt, housing_old_brewhouse_laundry.txt | pass |
| How much does a dryer cost in Innisfree Hall? | ✓ | ✓ | housing_innisfree_hall.txt, housing_innisfree_hall_laundry.txt | pass |
| How do you pay for laundry in Innisfree Hall? | ✓ | ✓ | housing_innisfree_hall.txt, housing_innisfree_hall_laundry.txt | pass |
| What laundry machines does Tamsin Court have? | ✓ | ✓ | housing_tamsin_court_laundry.txt | pass |

**Run 1: 10/10**

## Run 2

| Question | Fact | Attribution | Cited | Verdict |
|---|---|---|---|---|
| How much does a wash cost in Calder Annexe? | ✓ | ✓ | housing_calder_annexe.txt, housing_calder_annexe_laundry.txt | pass |
| How much does a dryer cost in Aldridge Hall? | ✓ | ✓ | housing_aldridge_hall.txt, housing_aldridge_hall_laundry.txt | pass |
| How do you pay for laundry in Aldridge Hall? | ✓ | ✓ | housing_aldridge_hall.txt, housing_aldridge_hall_laundry.txt | pass |
| How much does a dryer cost in Morrow House? | ✓ | ✓ | housing_morrow_house.txt, housing_morrow_house_laundry.txt | pass |
| How much does a wash cost in Morrow House? | ✓ | ✓ | housing_morrow_house.txt, housing_morrow_house_laundry.txt | pass |
| How do you pay for laundry in Old Brewhouse? | ✓ | ✓ | housing_old_brewhouse.txt, housing_old_brewhouse_laundry.txt | pass |
| How much does a dryer cost in Old Brewhouse? | ✓ | ✓ | housing_old_brewhouse.txt, housing_old_brewhouse_laundry.txt | pass |
| How much does a dryer cost in Innisfree Hall? | ✓ | ✓ | housing_innisfree_hall.txt, housing_innisfree_hall_laundry.txt | pass |
| How do you pay for laundry in Innisfree Hall? | ✓ | ✓ | housing_innisfree_hall.txt, housing_innisfree_hall_laundry.txt | pass |
| What laundry machines does Tamsin Court have? | ✓ | ✓ | housing_tamsin_court.txt, housing_tamsin_court_laundry.txt | pass |

**Run 2: 10/10**

## Run 3

| Question | Fact | Attribution | Cited | Verdict |
|---|---|---|---|---|
| How much does a wash cost in Calder Annexe? | ✓ | ✓ | housing_calder_annexe.txt, housing_calder_annexe_laundry.txt | pass |
| How much does a dryer cost in Aldridge Hall? | ✓ | ✓ | housing_aldridge_hall.txt, housing_aldridge_hall_laundry.txt | pass |
| How do you pay for laundry in Aldridge Hall? | ✓ | ✓ | housing_aldridge_hall.txt, housing_aldridge_hall_laundry.txt | pass |
| How much does a dryer cost in Morrow House? | ✓ | ✓ | housing_morrow_house.txt, housing_morrow_house_laundry.txt | pass |
| How much does a wash cost in Morrow House? | ✓ | ✓ | housing_morrow_house.txt, housing_morrow_house_laundry.txt | pass |
| How do you pay for laundry in Old Brewhouse? | ✓ | ✓ | housing_old_brewhouse.txt, housing_old_brewhouse_laundry.txt | pass |
| How much does a dryer cost in Old Brewhouse? | ✓ | ✓ | housing_old_brewhouse.txt, housing_old_brewhouse_laundry.txt | pass |
| How much does a dryer cost in Innisfree Hall? | ✓ | ✓ | housing_innisfree_hall.txt, housing_innisfree_hall_laundry.txt | pass |
| How do you pay for laundry in Innisfree Hall? | ✓ | ✓ | housing_innisfree_hall.txt, housing_innisfree_hall_laundry.txt | pass |
| What laundry machines does Tamsin Court have? | ✓ | ✓ | housing_tamsin_court.txt, housing_tamsin_court_laundry.txt | pass |

**Run 3: 10/10**

---

## Real output

### How much does a wash cost in Calder Annexe? — run 1

- Retrieved: housing_calder_annexe_laundry.txt#0 (0.229), housing_calder_annexe.txt#0 (0.372), housing_old_brewhouse_laundry.txt#0 (0.526)

```
A wash costs $2.00 in Calder Annexe (housing_calder_annexe.txt and housing_calder_annexe_laundry.txt).
```

### How much does a dryer cost in Aldridge Hall? — run 1

- Retrieved: housing_aldridge_hall_laundry.txt#0 (0.356), housing_aldridge_hall.txt#0 (0.470), housing_calder_annexe.txt#0 (0.526)

```
A dryer costs $1.50 in Aldridge Hall. 

Source: housing_aldridge_hall.txt (also found in housing_aldridge_hall_laundry.txt)
```

### How do you pay for laundry in Aldridge Hall? — run 1

- Retrieved: housing_aldridge_hall_laundry.txt#0 (0.293), housing_aldridge_hall.txt#0 (0.431), housing_innisfree_hall_laundry.txt#0 (0.459)

```
Laundry in Aldridge Hall is card only. 

Source: housing_aldridge_hall_laundry.txt (also mentioned in housing_aldridge_hall.txt)
```

### How much does a dryer cost in Morrow House? — run 1

- Retrieved: housing_morrow_house.txt#0 (0.322), housing_morrow_house_laundry.txt#0 (0.323), housing_old_brewhouse_laundry.txt#0 (0.490)

```
A dryer in Morrow House costs $1.25. 

Source: housing_morrow_house.txt (also mentioned in housing_morrow_house_laundry.txt)
```

### How much does a wash cost in Morrow House? — run 1

- Retrieved: housing_morrow_house_laundry.txt#0 (0.218), housing_morrow_house.txt#0 (0.257), housing_innisfree_hall_laundry.txt#0 (0.388)

```
A wash in Morrow House costs $1.50 (housing_morrow_house.txt and housing_morrow_house_laundry.txt).
```

### How do you pay for laundry in Old Brewhouse? — run 1

- Retrieved: housing_old_brewhouse_laundry.txt#0 (0.255), housing_old_brewhouse.txt#0 (0.378), housing_fenwick_court_laundry.txt#0 (0.404)

```
Laundry in Old Brewhouse is coin only. 

Source: `housing_old_brewhouse_laundry.txt` (also mentioned in `housing_old_brewhouse.txt`).
```

### How much does a dryer cost in Old Brewhouse? — run 1

- Retrieved: housing_old_brewhouse_laundry.txt#0 (0.355), housing_old_brewhouse.txt#0 (0.355), housing_calder_annexe_laundry.txt#0 (0.510)

```
A dryer in Old Brewhouse costs $1.50 (housing_old_brewhouse_laundry.txt and housing_old_brewhouse.txt).
```

### How much does a dryer cost in Innisfree Hall? — run 1

- Retrieved: housing_innisfree_hall_laundry.txt#0 (0.331), housing_innisfree_hall.txt#0 (0.361), housing_calder_annexe.txt#0 (0.505)

```
A dryer in Innisfree Hall costs $1.75. This comes from `housing_innisfree_hall.txt` and `housing_innisfree_hall_laundry.txt`.
```

### How do you pay for laundry in Innisfree Hall? — run 1

- Retrieved: housing_innisfree_hall_laundry.txt#0 (0.268), housing_innisfree_hall.txt#0 (0.342), housing_aldridge_hall_laundry.txt#0 (0.463)

```
Laundry in Innisfree Hall is app-based. 

Sources: `housing_innisfree_hall_laundry.txt` and `housing_innisfree_hall.txt`
```

### What laundry machines does Tamsin Court have? — run 1

- Retrieved: housing_tamsin_court_laundry.txt#0 (0.323), housing_tamsin_court.txt#0 (0.506), housing_old_brewhouse_laundry.txt#0 (0.511)

```
According to *housing_tamsin_court_laundry.txt*, Tamsin Court has in-unit washer-dryer machines, with a total of eight washers and six dryers for the building. *(housing_tamsin_court_laundry.txt)*
```

### How much does a wash cost in Calder Annexe? — run 2

- Retrieved: housing_calder_annexe_laundry.txt#0 (0.229), housing_calder_annexe.txt#0 (0.372), housing_old_brewhouse_laundry.txt#0 (0.526)

```
A wash costs $2.00 in Calder Annexe. 

Source: housing_calder_annexe.txt (and housing_calder_annexe_laundry.txt)
```

### How much does a dryer cost in Aldridge Hall? — run 2

- Retrieved: housing_aldridge_hall_laundry.txt#0 (0.356), housing_aldridge_hall.txt#0 (0.470), housing_calder_annexe.txt#0 (0.526)

```
A dryer in Aldridge Hall costs $1.50. 

Source: housing_aldridge_hall_laundry.txt (also mentioned in housing_aldridge_hall.txt)
```

### How do you pay for laundry in Aldridge Hall? — run 2

- Retrieved: housing_aldridge_hall_laundry.txt#0 (0.293), housing_aldridge_hall.txt#0 (0.431), housing_innisfree_hall_laundry.txt#0 (0.459)

```
Laundry in Aldridge Hall is paid using card only. 

Source: housing_aldridge_hall_laundry.txt (also mentioned in housing_aldridge_hall.txt)
```

### How much does a dryer cost in Morrow House? — run 2

- Retrieved: housing_morrow_house.txt#0 (0.322), housing_morrow_house_laundry.txt#0 (0.323), housing_old_brewhouse_laundry.txt#0 (0.490)

```
A dryer costs $1.25 in Morrow House (housing_morrow_house.txt and housing_morrow_house_laundry.txt).
```

### How much does a wash cost in Morrow House? — run 2

- Retrieved: housing_morrow_house_laundry.txt#0 (0.218), housing_morrow_house.txt#0 (0.257), housing_innisfree_hall_laundry.txt#0 (0.388)

```
A wash costs $1.50 in Morrow House. This information comes from `housing_morrow_house_laundry.txt` and `housing_morrow_house.txt`.
```

### How do you pay for laundry in Old Brewhouse? — run 2

- Retrieved: housing_old_brewhouse_laundry.txt#0 (0.255), housing_old_brewhouse.txt#0 (0.378), housing_fenwick_court_laundry.txt#0 (0.404)

```
You pay for laundry in Old Brewhouse using coins only (housing_old_brewhouse_laundry.txt and housing_old_brewhouse.txt).
```

### How much does a dryer cost in Old Brewhouse? — run 2

- Retrieved: housing_old_brewhouse_laundry.txt#0 (0.355), housing_old_brewhouse.txt#0 (0.355), housing_calder_annexe_laundry.txt#0 (0.510)

```
A dryer in Old Brewhouse costs $1.50 (housing_old_brewhouse_laundry.txt and housing_old_brewhouse.txt).
```

### How much does a dryer cost in Innisfree Hall? — run 2

- Retrieved: housing_innisfree_hall_laundry.txt#0 (0.331), housing_innisfree_hall.txt#0 (0.361), housing_calder_annexe.txt#0 (0.505)

```
A dryer in Innisfree Hall costs $1.75. This comes from `housing_innisfree_hall_laundry.txt` and `housing_innisfree_hall.txt`.
```

### How do you pay for laundry in Innisfree Hall? — run 2

- Retrieved: housing_innisfree_hall_laundry.txt#0 (0.268), housing_innisfree_hall.txt#0 (0.342), housing_aldridge_hall_laundry.txt#0 (0.463)

```
You pay for laundry in Innisfree Hall using an app-based system. 

Source: housing_innisfree_hall_laundry.txt (also mentioned in housing_innisfree_hall.txt)
```

### What laundry machines does Tamsin Court have? — run 2

- Retrieved: housing_tamsin_court_laundry.txt#0 (0.323), housing_tamsin_court.txt#0 (0.506), housing_old_brewhouse_laundry.txt#0 (0.511)

```
Tamsin Court has in-unit washer-dryer machines (source: *housing_tamsin_court_laundry.txt* and *housing_tamsin_court.txt*). There are eight washers and six dryers for the building (*housing_tamsin_court_laundry.txt*).
```

### How much does a wash cost in Calder Annexe? — run 3

- Retrieved: housing_calder_annexe_laundry.txt#0 (0.229), housing_calder_annexe.txt#0 (0.372), housing_old_brewhouse_laundry.txt#0 (0.526)

```
A wash costs $2.00 in Calder Annexe (housing_calder_annexe.txt and housing_calder_annexe_laundry.txt).
```

### How much does a dryer cost in Aldridge Hall? — run 3

- Retrieved: housing_aldridge_hall_laundry.txt#0 (0.356), housing_aldridge_hall.txt#0 (0.470), housing_calder_annexe.txt#0 (0.526)

```
A dryer in Aldridge Hall costs $1.50. 

Source: housing_aldridge_hall.txt (and housing_aldridge_hall_laundry.txt)
```

### How do you pay for laundry in Aldridge Hall? — run 3

- Retrieved: housing_aldridge_hall_laundry.txt#0 (0.293), housing_aldridge_hall.txt#0 (0.431), housing_innisfree_hall_laundry.txt#0 (0.459)

```
You pay for laundry using a card only. 

Source: housing_aldridge_hall_laundry.txt (and housing_aldridge_hall.txt)
```

### How much does a dryer cost in Morrow House? — run 3

- Retrieved: housing_morrow_house.txt#0 (0.322), housing_morrow_house_laundry.txt#0 (0.323), housing_old_brewhouse_laundry.txt#0 (0.490)

```
A dryer costs $1.25 in Morrow House (housing_morrow_house.txt and housing_morrow_house_laundry.txt).
```

### How much does a wash cost in Morrow House? — run 3

- Retrieved: housing_morrow_house_laundry.txt#0 (0.218), housing_morrow_house.txt#0 (0.257), housing_innisfree_hall_laundry.txt#0 (0.388)

```
A wash costs $1.50 in Morrow House. This information comes from the documents `housing_morrow_house_laundry.txt` and `housing_morrow_house.txt`.
```

### How do you pay for laundry in Old Brewhouse? — run 3

- Retrieved: housing_old_brewhouse_laundry.txt#0 (0.255), housing_old_brewhouse.txt#0 (0.378), housing_fenwick_court_laundry.txt#0 (0.404)

```
You pay for laundry in Old Brewhouse using coins only, as the machines take $1.50 for a wash and $1.50 for a dry (*housing_old_brewhouse_laundry.txt* and *housing_old_brewhouse.txt*).
```

### How much does a dryer cost in Old Brewhouse? — run 3

- Retrieved: housing_old_brewhouse_laundry.txt#0 (0.355), housing_old_brewhouse.txt#0 (0.355), housing_calder_annexe_laundry.txt#0 (0.510)

```
A dryer costs $1.50 in Old Brewhouse. 

Source: `housing_old_brewhouse_laundry.txt` (also mentioned in `housing_old_brewhouse.txt`)
```

### How much does a dryer cost in Innisfree Hall? — run 3

- Retrieved: housing_innisfree_hall_laundry.txt#0 (0.331), housing_innisfree_hall.txt#0 (0.361), housing_calder_annexe.txt#0 (0.505)

```
A dryer in Innisfree Hall costs $1.75. 

Source: housing_innisfree_hall_laundry.txt (also mentioned in housing_innisfree_hall.txt)
```

### How do you pay for laundry in Innisfree Hall? — run 3

- Retrieved: housing_innisfree_hall_laundry.txt#0 (0.268), housing_innisfree_hall.txt#0 (0.342), housing_aldridge_hall_laundry.txt#0 (0.463)

```
You pay for laundry in Innisfree Hall using an app, as it is app-based (housing_innisfree_hall_laundry.txt and housing_innisfree_hall.txt).
```

### What laundry machines does Tamsin Court have? — run 3

- Retrieved: housing_tamsin_court_laundry.txt#0 (0.323), housing_tamsin_court.txt#0 (0.506), housing_old_brewhouse_laundry.txt#0 (0.511)

```
Tamsin Court has in-unit washer-dryer machines, with a total of eight washers and six dryers for the building. 

Source: `housing_tamsin_court_laundry.txt` and `housing_tamsin_court.txt`
```
