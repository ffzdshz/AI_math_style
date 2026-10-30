---
name: euclid-proof
description: "Use this skill whenever the user asks to prove theorems from Euclid's Elements, compare AI-generated proofs with Heath's human references, compute Jaccard similarity between citation sets, or run the standardized Euclid proof protocol on any book. Triggers include: 'prove Book N', 'compare AI and human proofs', 'Euclid citation comparison', 'Jaccard for Euclid', 'run the proof protocol', or any mention of Euclid_All_Statements.xlsx or Euclid_Human_References_All465.xlsx. Always use this skill for these tasks — do not improvise the four-step workflow from scratch."
---

# Euclid Proof Protocol — Standardized Execution

This skill governs the standardized workflow for comparing AI-generated proofs of Euclid's *Elements* with human (Heath) references, book by book. Follow this skill exactly; do not deviate between sessions.

---

## Background and Objective

**Research question**: When an AI reproves Euclidean propositions under constraints, how much does its citation set overlap with the human citation set from Heath's English translation?

**Core metric**: Jaccard similarity = |AI ∩ Human| / |AI ∪ Human|

**Data files** (bundled in `data/` — no upload needed):
- `data/Euclid_All_Statements.xlsx` — 607 entries: 5 postulates, 5 common notions, 132 definitions, 465 theorems (ID + statement)
- `data/Euclid_Human_References_All465.xlsx` — 465 theorems with human citation lists from Heath's References field

To locate the data files at runtime, resolve them relative to this SKILL.md:

```python
from pathlib import Path
SKILL_DIR = Path(__file__).parent  # works when skill is installed
# fallback: SKILL_DIR = Path('/mnt/skills/user/euclid-proof')
STATEMENTS_PATH = SKILL_DIR / 'data' / 'Euclid_All_Statements.xlsx'
HUMAN_REFS_PATH = SKILL_DIR / 'data' / 'Euclid_Human_References_All465.xlsx'
```

If the skill is not yet installed and only the xlsx files are uploaded to the session, fall back to reading from `/mnt/user-data/uploads/`.

> ⚠️ **ID format warning**: Both files contain IDs such as `1.10`, `D1.20`, `10.11`. Excel parses these as decimals and truncates trailing zeros (`1.10` → `1.1`). Files use xlsx format with the first column set as text. When reading with pandas, **always** pass `dtype={'ID': str}` (or `dtype={'Proposition': str}`) — never omit this.

**Citation code conventions** (consistent across both files):

| Type | Format | Example |
|---|---|---|
| Postulate | `P{N}` | `P1`, `P5` |
| Common Notion | `CN{N}` | `CN1`, `CN3` |
| Definition | `D{book}.{number}` | `D1.15`, `D7.6`, `D10.2.1` |
| Theorem | `{book}.{prop}` | `1.47`, `7.30`, `9.36` |

Book X definitions use three numbered groups: Group I `D10.1`–`D10.4`, Group II `D10.2.1`–`D10.2.6`, Group III `D10.3.1`–`D10.3.6`.

---

## The Four-Step Workflow

### Step 1 — Load statements

```python
import pandas as pd
from pathlib import Path

SKILL_DIR = Path('/mnt/skills/user/euclid-proof')
STATEMENTS_PATH = SKILL_DIR / 'data' / 'Euclid_All_Statements.xlsx'
if not STATEMENTS_PATH.exists():
    STATEMENTS_PATH = Path('/mnt/user-data/uploads/Euclid_All_Statements.xlsx')

df = pd.read_excel(STATEMENTS_PATH, dtype={'ID': str})
statements = {}
for _, row in df.iterrows():
    statements[row['ID']] = {
        'type':      row['Type'],
        'book':      row['Book'],
        'statement': row['Statement'],
    }

BOOK_NUM = 1  # change to target book number

target = {k: v for k, v in statements.items()
          if v['type'] == 'Theorem' and k.startswith(f'{BOOK_NUM}.')}
target_sorted = sorted(target.keys(), key=lambda x: int(x.split('.')[1]))

for prop in target_sorted:
    print(f"{prop}: {statements[prop]['statement']}")
```

The **available tool inventory** for proving proposition `N.k` consists of:
- All postulates (Type = Postulate)
- All common notions (Type = Common Notion)
- All definitions (Type = Definition)
- All theorems from books 1 through N−1 (Type = Theorem, book number < N)
- Theorems within book N with proposition number < k

**Do not** load `Euclid_Human_References_All465.xlsx` in Steps 1 or 2.

---

### Step 2 — Independent proofs (before seeing any human references)

**Rules**:
- Reason only from postulates, common notions, definitions, and preceding theorems
- Use no external proof content
- For each proposition, output: step-by-step proof + USED list
- USED lists only tools actually invoked in the reasoning — no precautionary citations
- When two equivalent propositions could serve (e.g. 1.37 vs 1.38), choose the one naturally reached first and note the reason
- When a divergence in proof path exists, choose the most direct route and flag it

**Output format per proposition**:

```
## Proposition N.k
**Statement:** [full statement]

**Step 1.** ...
**Step 2.** ...

**USED:** ref1, ref2, ref3
```

---

### Step 2.5 — Out-of-order citation check and retry

After completing all proofs in Step 2, run the following check **before** loading human references. A citation `N.k → M.j` is a violation if:
- M == N and j >= k (same book, citing an equal or later proposition), or
- M > N (citing a proposition from a later book)

Postulates (`P{n}`), common notions (`CN{n}`), and definitions (`D...`) are always valid and must not be flagged.

```python
import re

MAX_RETRIES = 3

def parse_prop(ref):
    """Return (book, prop) if ref is a theorem citation like '7.13', else None."""
    m = re.fullmatch(r'(\d+)\.(\d+)', ref)
    if m:
        return int(m.group(1)), int(m.group(2))
    return None

def find_violations(prop, ai_used):
    """Return list of out-of-order refs in ai_used for the given prop."""
    sb, sp = parse_prop(prop)
    bad = []
    for ref in ai_used:
        t = parse_prop(ref)
        if t is None:
            continue  # postulate / CN / definition — always valid
        tb, tp = t
        if tb > sb or (tb == sb and tp >= sp):
            bad.append(ref)
    return bad

# Check all proofs; collect violations
violations_found = {}
for prop, (ai_used, note) in ai_proofs.items():
    bad = find_violations(prop, ai_used)
    if bad:
        violations_found[prop] = bad

if violations_found:
    print(f"Out-of-order citations detected in: {list(violations_found.keys())}")
    print("Re-proving affected propositions (max 3 attempts each)...\n")
```

For each proposition flagged in `violations_found`, re-prove it independently, applying the ordering rule with explicit emphasis:

> **STRICT ORDERING RULE**: For proposition `N.k`, your USED list must contain only references with theorem index strictly less than k within book N, or from any book with number less than N. Citing `N.k` itself or any `N.j` where j ≥ k is forbidden. Check every entry in your USED list before finalising.

Retry up to `MAX_RETRIES` times. After each retry, re-run `find_violations` on the new USED list. If a proposition still has violations after all retries, flag it as `UNRESOLVED` and record the best attempt (fewest violations).

```python
for prop in list(violations_found.keys()):
    for attempt in range(1, MAX_RETRIES + 1):
        # [Re-prove proposition `prop` here, following the strict ordering rule above]
        # Update ai_proofs[prop] with the new (ai_used, note)
        new_used, new_note = ai_proofs[prop]  # placeholder: replace with actual re-proof
        bad = find_violations(prop, new_used)
        if not bad:
            print(f"  {prop}: resolved on attempt {attempt}")
            break
        if attempt == MAX_RETRIES:
            print(f"  {prop}: UNRESOLVED after {MAX_RETRIES} attempts — flagged, best attempt kept")
            new_note = f"[UNRESOLVED violations: {bad}] " + new_note
            ai_proofs[prop] = (new_used, new_note)
```

Only proceed to Step 3 once all violations are resolved or flagged as UNRESOLVED.

---

### Step 3 — Load human references (after all proofs are complete)

```python
import pandas as pd

HUMAN_REFS_PATH = SKILL_DIR / 'data' / 'Euclid_Human_References_All465.xlsx'
if not HUMAN_REFS_PATH.exists():
    HUMAN_REFS_PATH = Path('/mnt/user-data/uploads/Euclid_Human_References_All465.xlsx')

# Columns: Proposition (str ID), Book_Name (e.g. 'Book I'), All_References (pipe-separated)
df_h = pd.read_excel(HUMAN_REFS_PATH, dtype={'Proposition': str})
human_refs = {}
for _, row in df_h.iterrows():
    prop = row['Proposition']
    refs = [r for r in str(row['All_References']).split('|') if r and r != 'nan']
    human_refs[prop] = refs

# Filter by book — two equivalent methods (use whichever is clearer):
#   Method A: prefix match on Proposition ID (e.g. '3.' for Book III)
human_refs_book = {k: v for k, v in human_refs.items() if k.startswith(f'{BOOK_NUM}.')}
#   Method B: use Book_Name column (e.g. 'Book III') — useful for Book 10 where IDs can be ambiguous
# book_name_map = {1:'Book I', 2:'Book II', 3:'Book III', 4:'Book IV', 5:'Book V',
#                  6:'Book VI', 7:'Book VII', 8:'Book VIII', 9:'Book IX', 10:'Book X',
#                  11:'Book XI', 12:'Book XII', 13:'Book XIII'}
# df_book = df_h[df_h['Book_Name'] == book_name_map[BOOK_NUM]]
# human_refs_book = {row['Proposition']: [r for r in str(row['All_References']).split('|') if r and r != 'nan']
#                    for _, row in df_book.iterrows()}
```

The human references come from the **References structural field** of `xiaofanzhang_Structure-of-Euclids-Elements.json` (not from Proof bracket text). This field is more complete and includes implicit premises not always marked in Heath's proof brackets.

---

### Step 4 — Compute Jaccard and generate outputs

```python
import csv

def jaccard(a, b):
    sa, sb = set(a), set(b)
    if not sa and not sb: return 1.0
    if not sa or not sb: return 0.0
    return len(sa & sb) / len(sa | sb)

# ai_proofs = { 'N.k': (['ref1', 'ref2', ...], 'proof summary'), ... }
# human_refs_book = { 'N.k': ['ref1', 'ref2', ...], ... }

rows = []
for prop in sorted(ai_proofs.keys(), key=lambda x: int(x.split('.')[1])):
    ai_used, note = ai_proofs[prop]
    hrefs = human_refs_book.get(prop, [])
    j = jaccard(ai_used, hrefs)
    ai_s, h_s = set(ai_used), set(hrefs)
    rows.append({
        'Proposition':        prop,
        'Statement':          statements[prop]['statement'][:120].replace('"', "'").replace('\n', ' '),
        'AI_USED':            '|'.join(sorted(ai_s)),
        'Human_Refs':         '|'.join(sorted(h_s)),
        'Shared':             '|'.join(sorted(ai_s & h_s)),
        'AI_Only_Extra':      '|'.join(sorted(ai_s - h_s)),
        'Human_Only_Missing': '|'.join(sorted(h_s - ai_s)),
        'Jaccard':            round(j, 3),
        'n_AI':               len(ai_s),
        'n_Human':            len(h_s),
        'n_Shared':           len(ai_s & h_s),
        'Proof_Summary':      note,
    })

out_csv = f'Book{BOOK_NUM}_AI_vs_Human_Citations.csv'
with open(out_csv, 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    writer.writeheader()
    writer.writerows(rows)

mean_j  = sum(r['Jaccard'] for r in rows) / len(rows)
perfect = sum(1 for r in rows if r['Jaccard'] == 1.0)
print(f"Mean Jaccard: {mean_j:.4f},  Perfect: {perfect}/{len(rows)}")
for r in rows:
    if r['Jaccard'] < 1.0:
        print(f"  {r['Proposition']}: J={r['Jaccard']:.3f}"
              f"  extra=[{r['AI_Only_Extra']}]"
              f"  missing=[{r['Human_Only_Missing']}]")
```

---

## Output File Specifications

### BookN_StepByStep_Proofs.md

```markdown
# Book N of Euclid's Elements — Step-by-Step AI Proofs (Genuine reasoning)

## Proposition N.k
**Statement:** [full statement]

**Step 1.** ...
**Step 2.** ...

**USED:** ref1, ref2, ref3
**Human refs (from References field):** ref1, ref2
**Jaccard:** 0.xxx — [explanation of divergence: what AI adds, what human adds, why]
```

### BookN_AI_vs_Human_Citations.csv — column specification

```
Proposition, Statement, AI_USED, Human_Refs, Shared,
AI_Only_Extra, Human_Only_Missing, Jaccard,
n_AI, n_Human, n_Shared, Proof_Summary
```

Multiple references separated by `|` (e.g. `1.4|1.8|CN2`).

Both files must be produced for every book run.

---

## Fixed Execution Rules

| Rule | Specification |
|---|---|
| No early peek at human refs | Steps 1 and 2 must complete before loading `Euclid_Human_References_All465.xlsx` |
| Independent reasoning | Proofs use only postulates / common notions / definitions / preceding theorems — no external proof content |
| Cite only what is used | USED lists record tools actually invoked; no precautionary or "insurance" citations |
| Flag path choices | When equivalent proof routes exist, choose the most direct and note the reason |
| Both files mandatory | Every book run must produce both `.md` and `.csv` outputs |
| Fixed sequence | Load statements → independent proofs → **violation check + retry** → load human refs → compute and output |
| String dtype enforcement | Always pass `dtype={'ID': str}` and `dtype={'Proposition': str}` when reading xlsx files |
| Out-of-order check mandatory | Step 2.5 must run before Step 3; no proposition may enter Jaccard computation with unresolved violations unless flagged UNRESOLVED |
| Retry limit | Maximum 3 re-proof attempts per flagged proposition; exceeded attempts are marked `[UNRESOLVED violations: ...]` in Proof_Summary |

---

---

## Data Source Note

Human references in `Euclid_Human_References_All465.xlsx` come from the **References structural field** of the source JSON, not from Proof bracket text. The two differ:
- **References field**: compiled structured list; more complete; includes compound-bracket and implicit-premise citations
- **Proof brackets**: explicit `[I. N]` markers in Heath's main text; occasionally incomplete (especially in Book X)

The References field is the standard source for human citations in this experiment.
