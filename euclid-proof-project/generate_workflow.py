"""Generate a self-contained workflow script for a specific Book + Run."""
import json
import sys

def main():
    book_num = int(sys.argv[1])
    run_id = sys.argv[2]

    with open(r"E:\Claude\euclid-proof-project\data\euclid_statements.json", "r", encoding="utf-8") as f:
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
    foundations_js = json.dumps(foundations, ensure_ascii=False)
    props_js = json.dumps(props, ensure_ascii=False)
    prior_js = json.dumps(prior_theorems_text, ensure_ascii=False)

    script = f"""export const meta = {{
  name: 'euclid-book{book_num}-run{run_id}',
  description: 'Prove all {len(props)} propositions of Euclid Book {book_num} (Run {run_id})',
  phases: [
    {{ title: 'Prove', detail: 'Each proposition proved by a dedicated agent' }},
    {{ title: 'Retry', detail: 'Re-prove propositions with ordering violations' }}
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
const foundations = {foundations_js}
const priorTheorems = {prior_js}
const propositions = {props_js}

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

  return `FIRST: Read the file at E:\\\\Claude\\\\euclid-proof-project\\\\SKILL.md using your Read tool. This file contains the authoritative Euclid Proof Protocol. You must follow its Step 2 rules exactly for proving propositions.

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
log('Run ' + runId + ' | Book ' + bookNum + ': proving ' + propositions.length + ' propositions')

const initialResults = await pipeline(
  propositions,
  async (prop) => {{
    const prompt = buildPrompt(prop, false, [])
    const result = await agent(prompt, {{
      label: prop.id,
      phase: 'Prove',
      schema: SCHEMA,
      effort: 'high'
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

  const retryProps = propositions.filter(p => violated.includes(p.id))
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
          effort: 'high'
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

const finalResults = propositions.map(p => {{
  const d = proofs[p.id]
  if (!d) return null
  return {{ prop_id: p.id, statement: p.statement, proof: d.proof, used: d.used }}
}}).filter(Boolean)

log('Done: ' + finalResults.length + '/' + propositions.length + ' propositions')
return finalResults
"""

    out_path = f"E:\\Claude\\euclid-proof-project\\workflow_Run{run_id}_Book{book_num}.js"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(script)

    print(f"Generated: {out_path}")
    print(f"Script size: {len(script)} chars")
    print(f"Propositions: {len(props)}")

if __name__ == "__main__":
    main()
