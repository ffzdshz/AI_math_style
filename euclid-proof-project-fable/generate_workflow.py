"""Generate a self-contained workflow script for a specific Book + Run.

Usage: python generate_workflow.py <book_num> <run_id> [--only N[,M,...]]
  --only  prove only the listed proposition numbers, e.g. --only 21 or --only 1-50 or --only 3,7,12
          (single-item re-runs after an API failure, or splitting a large book into parts).
          The prompt for each proposition is identical to the full-book script: the preceding-theorem list is
          still built from the complete book, only the set of propositions actually proved is restricted.
"""
import json
import os
import sys

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(PROJECT_DIR, "data")
SKILL_PATH = os.path.join(PROJECT_DIR, "SKILL.md")
MODEL_ID = "claude-fable-5-1"  # every proving sub-agent is pinned to this model
EFFORT = "xhigh"  # reasoning effort for every proving sub-agent (low|medium|high|xhigh|max)

def main():
    book_num = int(sys.argv[1])
    run_id = sys.argv[2]
    only = None
    if "--only" in sys.argv:
        sel = set()
        for part in sys.argv[sys.argv.index("--only") + 1].split(","):
            if "-" in part:
                lo, hi = part.split("-"); sel.update(range(int(lo), int(hi) + 1))
            else:
                sel.add(int(part))
        only = sorted(sel)

    with open(os.path.join(DATA_DIR, "euclid_statements.json"), "r", encoding="utf-8") as f:
        statements = json.load(f)

    # Build foundations
    lines = ["POSTULATES:"]
    for sid, s in statements.items():
        if s["type"] == "Postulate":
            lines.append(f"{sid}: {s['statement']}")
    lines.append("")
    lines.append("COMMON NOTIONS:")
    for sid, s in statements.items():
        if s["type"] == "Common Notion":
            lines.append(f"{sid}: {s['statement']}")
    lines.append("")
    lines.append("DEFINITIONS:")
    for sid, s in statements.items():
        if s["type"] == "Definition":
            lines.append(f"{sid}: {s['statement']}")
    foundations = "\n".join(lines)

    # Build propositions for target book
    props = []
    for sid, s in statements.items():
        if s["type"] == "Theorem" and s["book"] == book_num:
            props.append({"id": sid, "propNum": int(sid.split(".")[1]), "statement": s["statement"]})
    props.sort(key=lambda x: x["propNum"])
    targets = [p for p in props if only is None or p["propNum"] in only]
    if only is not None and len(targets) != len(only):
        raise SystemExit(f"--only: propositions not found in Book {book_num}: {sorted(set(only) - {p['propNum'] for p in targets})}")
    contiguous = only is not None and len(only) > 1 and only == list(range(only[0], only[-1] + 1))
    only_tag = "" if only is None else ("only" + (f"{only[0]}-{only[-1]}" if contiguous else "_".join(str(n) for n in only)))
    range_desc = "" if only is None else (f"{book_num}.{only[0]}-{book_num}.{only[-1]}" if contiguous else ", ".join(p["id"] for p in targets))
    desc = (f"Prove all {len(props)} propositions of Euclid Book {book_num} (Run {run_id}, model {MODEL_ID}, effort {EFFORT})"
            if only is None else
            f"Prove {len(targets)} of {len(props)} propositions of Euclid Book {book_num}: {range_desc} (Run {run_id}, model {MODEL_ID}, effort {EFFORT}; partial run, prompts identical to the full-book script)")

    # Build prior-book theorem ID ranges
    prior_books = {}
    for sid, s in statements.items():
        if s["type"] == "Theorem" and s["book"] < book_num:
            b = s["book"]
            if b not in prior_books:
                prior_books[b] = []
            prior_books[b].append(sid)

    prior_lines = []
    for b in sorted(prior_books.keys()):
        ids = sorted(prior_books[b], key=lambda x: int(x.split(".")[1]))
        prior_lines.append(f"Book {b}: {', '.join(ids)}")
    prior_theorems_text = "\n".join(prior_lines) if prior_lines else "(None — this is Book 1)"

    # Embed as JSON strings in JS
    foundations_js = json.dumps(foundations, ensure_ascii=True)  # ASCII-only, see note below
    props_js = json.dumps(props, ensure_ascii=True)
    targets_js = json.dumps(targets, ensure_ascii=True)
    prior_js = json.dumps(prior_theorems_text, ensure_ascii=True)
    # NOTE: ensure_ascii=True keeps the generated .js free of non-ASCII control characters (some Book 10
    # statements carry U+0080/U+009C/U+009D mojibake residue), which the Workflow permission layer rejects.
    # JS decodes the unicode escapes at runtime, so sub-agents receive exactly the same prompt text as before.
    skill_js = json.dumps(SKILL_PATH, ensure_ascii=False)
    model_js = json.dumps(MODEL_ID)
    effort_js = json.dumps(EFFORT)

    script = f"""export const meta = {{
  name: 'euclid-book{book_num}-run{run_id}{("-" + only_tag) if only_tag else ""}',
  description: '{desc}',
  phases: [
    {{ title: 'Prove', detail: 'Each proposition proved by a dedicated agent', model: '{MODEL_ID}' }},
    {{ title: 'Retry', detail: 'Re-prove propositions with ordering violations', model: '{MODEL_ID}' }}
  ]
}}

const SCHEMA = {{
  type: 'object',
  properties: {{
    prop_id: {{ type: 'string' }},
    proof: {{ type: 'string' }},
    used: {{ type: 'array', items: {{ type: 'string' }} }}
  }},
  required: ['prop_id', 'proof', 'used'],
  additionalProperties: false
}}

const bookNum = {book_num}
const runId = "{run_id}"
const skillPath = {skill_js}
const modelId = {model_js}
const effortLevel = {effort_js}
const foundations = {foundations_js}
const priorTheorems = {prior_js}
const propositions = {props_js}
const targets = {targets_js}  // subset actually proved; prompts still see the full book

function findViolations(propId, used) {{
  const dotIdx = propId.indexOf('.')
  const sb = parseInt(propId.substring(0, dotIdx))
  const sp = parseInt(propId.substring(dotIdx + 1))
  const bad = []
  for (const ref of used) {{
    const m = ref.match(/^(\\d+)\\.(\\d+)$/)
    if (!m) continue
    const tb = parseInt(m[1])
    const tp = parseInt(m[2])
    if (tb > sb || (tb === sb && tp >= sp)) {{
      bad.push(ref)
    }}
  }}
  return bad
}}

function buildPrompt(prop, isRetry, priorViolations) {{
  const sameBook = []
  for (const p of propositions) {{
    if (p.propNum < prop.propNum) {{
      sameBook.push(p.id + ': ' + p.statement)
    }}
  }}

  const retryWarning = isRetry
    ? '\\n\\n!!! RETRY — your previous proof had OUT-OF-ORDER citations: ' + priorViolations.join(', ') +
      '. These are FORBIDDEN. Do NOT cite ' + prop.id + ' itself or any proposition >= ' + prop.id + '. Double-check EVERY entry in your USED list.\\n'
    : ''

  return `FIRST: Read the file at ${{skillPath}} using your Read tool. This file contains the authoritative Euclid Proof Protocol. You must follow its Step 2 rules exactly for proving propositions.

After reading SKILL.md, prove the following proposition according to its Step 2 requirements.${{retryWarning}}

PROPOSITION: ${{prop.id}}
STATEMENT: ${{prop.statement}}

STRICT ORDERING: For ${{prop.id}} you may cite:
- Postulates (P1-P5), Common Notions (CN1-CN5), Definitions (D...) — always valid${{bookNum > 1 ? '\\n- Theorems from Books 1 through ' + (bookNum - 1) + ' (any proposition)' : ''}}
- Book ${{bookNum}} theorems with proposition number STRICTLY LESS than ${{prop.propNum}}
- NEVER cite ${{prop.id}} itself or any ${{bookNum}}.j where j >= ${{prop.propNum}}
CHECK every entry in your USED list before finalizing!

CRITICAL — CLEAN PROOF ONLY:
Think through the proof internally BEFORE writing your structured output. If you hit a dead end or need to revise your approach, work that out in your own reasoning first. The "proof" field in your structured output must contain ONLY the final, clean, polished proof — no backtracking, no "let me reconsider", no "this is wrong", no abandoned attempts, no corrections. Each step should flow logically to the next. Number steps consecutively with no gaps. A reader should see a clean finished proof, not a reasoning trace.

FOUNDATIONS (always available):
${{foundations}}

PRECEDING THEOREMS IN BOOK ${{bookNum}}:
${{sameBook.length > 0 ? sameBook.join('\\n') : '(None — this is the first theorem)'}}

THEOREMS FROM EARLIER BOOKS (available by ID):
${{priorTheorems}}

Return structured output: prop_id="${{prop.id}}", proof (each step as "**Step N.** ..."), used (array of ref IDs like ["P1","CN1","D1.15","1.4"]).`
}}

phase('Prove')
log('Run ' + runId + ' | Book ' + bookNum + ' | model ' + modelId + ' | effort ' + effortLevel + ': proving ' + targets.length + ' of ' + propositions.length + ' propositions')

const initialResults = await pipeline(
  targets,
  async (prop) => {{
    const prompt = buildPrompt(prop, false, [])
    const result = await agent(prompt, {{
      label: prop.id,
      phase: 'Prove',
      schema: SCHEMA,
      model: modelId,
      effort: effortLevel
    }})
    if (result) {{
      log(prop.id + ' proved (' + result.used.length + ' refs)')
    }}
    return result
  }}
)

const proofs = {{}}
for (const r of initialResults.filter(Boolean)) {{
  proofs[r.prop_id] = {{ proof: r.proof, used: r.used, violations: findViolations(r.prop_id, r.used) }}
}}

const violated = Object.entries(proofs).filter(([_, d]) => d.violations.length > 0).map(([pid]) => pid)

if (violated.length > 0) {{
  log('Violations in: ' + violated.join(', ') + ' — retrying...')
  phase('Retry')

  const retryProps = targets.filter(p => violated.includes(p.id))
  const retryResults = await pipeline(
    retryProps,
    async (prop) => {{
      let best = proofs[prop.id]
      for (let attempt = 1; attempt <= 3; attempt++) {{
        const prompt = buildPrompt(prop, true, best.violations)
        const result = await agent(prompt, {{
          label: prop.id + ' retry#' + attempt,
          phase: 'Retry',
          schema: SCHEMA,
          model: modelId,
          effort: effortLevel
        }})
        if (!result) break
        const bad = findViolations(prop.id, result.used)
        if (bad.length === 0) {{
          log(prop.id + ': resolved on attempt ' + attempt)
          return result
        }}
        if (bad.length < best.violations.length) {{
          best = {{ proof: result.proof, used: result.used, violations: bad }}
        }}
      }}
      log(prop.id + ': UNRESOLVED after 3 attempts')
      return {{ prop_id: prop.id, proof: '[UNRESOLVED: ' + best.violations.join(',') + '] ' + best.proof, used: best.used }}
    }}
  )

  for (const r of retryResults.filter(Boolean)) {{
    proofs[r.prop_id] = {{ proof: r.proof, used: r.used, violations: findViolations(r.prop_id, r.used) }}
  }}
}} else {{
  log('No ordering violations found')
}}

const finalResults = targets.map(p => {{
  const d = proofs[p.id]
  if (!d) return null
  return {{ prop_id: p.id, statement: p.statement, proof: d.proof, used: d.used, model: modelId, effort: effortLevel }}
}}).filter(Boolean)

log('Done: ' + finalResults.length + '/' + targets.length + ' propositions')
return finalResults
"""

    out_path = os.path.join(PROJECT_DIR, f"workflow_Run{run_id}_Book{book_num}{('_' + only_tag) if only_tag else ''}.js")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:  # LF only: CR is a control char the Workflow tool rejects
        f.write(script)

    print(f"Generated: {out_path}")
    print(f"SKILL.md for sub-agents: {SKILL_PATH}")
    print(f"Model pinned for sub-agents: {MODEL_ID}")
    print(f"Effort for sub-agents: {EFFORT}")
    print(f"Script size: {len(script)} chars")
    print(f"Propositions: {len(props)}" + (f" | targets: {[p['id'] for p in targets]}" if only is not None else ""))

if __name__ == "__main__":
    main()
