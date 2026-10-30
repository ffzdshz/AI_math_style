/**
 * Geometry Configuration Consistency Check — Fable All Books Batch
 *
 * Checks all D-category propositions across all books in a single workflow.
 *
 * Args: { items: [{ book: 2, prop: "2.7" }, ...] }
 *
 * Prerequisites: preprocess.py Fable <book> --categories D (for each book)
 * Post-processing: collect_results.py Fable <book> (for each book)
 */

export const meta = {
  name: 'geometry-check-fable',
  description: 'Check all Fable D-class proofs for geometric configuration contradictions',
  phases: [
    { title: 'Check', detail: 'Per-proposition geometry configuration audit' },
    { title: 'Report', detail: 'Save individual results to JSON files' },
  ],
}

const BASE = 'E:/Claude/euclid-geometry-check'
const RUN = 'Fable'

const parsed = (typeof args === 'string') ? JSON.parse(args) : args
const items = parsed.items

log(`Fable batch geometry check: ${items.length} propositions across ${new Set(items.map(i => i.book)).size} books`)

// ── Schema ────────────────────────────────────────────────────────────

const CHECK_RESULT_SCHEMA = {
  type: 'object',
  properties: {
    proposition:        { type: 'string' },
    run:                { type: 'string' },
    book:               { type: 'number' },
    current_category:   { type: 'string' },
    verdict:            { type: 'string', enum: ['PASS', 'FAIL', 'SKIP'] },
    spatial_claims:     {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          step:  { type: 'string' },
          claim: { type: 'string' },
          type:  { type: 'string' },
        },
        required: ['step', 'claim'],
      },
    },
    contradictory_steps: { type: 'array', items: { type: 'string' } },
    spatial_claim_1: {
      type: 'object',
      properties: {
        step:        { type: 'string' },
        claim:       { type: 'string' },
        required_by: { type: 'string' },
      },
    },
    spatial_claim_2: {
      type: 'object',
      properties: {
        step:        { type: 'string' },
        claim:       { type: 'string' },
        required_by: { type: 'string' },
      },
    },
    contradiction:   { type: 'string' },
    fixable:         { type: 'boolean' },
    fix_note:        { type: 'string' },
    pass_reason:     { type: 'string' },
    skip_reason:     { type: 'string' },
    configuration_map: { type: 'string' },
  },
  required: ['proposition', 'run', 'verdict'],
}

// ── Prompt builder ────────────────────────────────────────────────────

function buildCheckPrompt(item) {
  return `You are a geometry expert performing a spatial configuration consistency check on an AI-generated proof of a proposition from Euclid's Elements.

## Your task

1. Read the checking protocol: ${BASE}/geometry_check_protocol.md
2. Read the proposition data: ${BASE}/prepared/${RUN}/book${item.book}/${item.prop}.json
   - The "ai_proof_text" field contains the full step-by-step AI proof to check.
   - The "heath_proof_text" field contains Heath's proof for reference (do NOT check Heath's proof — only check the AI proof).

3. Follow the protocol precisely:
   **Step A**: Extract every spatial claim from the AI proof (point positions, ray orderings, angle decompositions, inside/outside claims).
   **Step B**: Build a configuration map — for each constructed point, track its claimed position through every step.
   **Step C**: Check pairwise consistency — for each pair of spatial claims involving the same point or figure, verify they can simultaneously be true. Pay special attention to:
     - Claims in different steps
     - Claims that cite different propositions (one requires interior, another requires exterior)
     - Implicit spatial assumptions hidden in angle decompositions
   **Step D**: Verdict — PASS, FAIL, or SKIP per the protocol.

## Critical rules from the protocol

- **Default presumption is PASS.** Only flag FAIL when you can articulate a specific, concrete contradiction. Vague unease is not sufficient.
- **Each step may be individually correct.** The error is in the COMBINATION of spatial claims.
- **Angle decomposition is the #1 error pattern.** Verify the middle ray actually falls between the outer rays given the established geometry.
- **A point inside a triangle** means angles around it sum to 360°, NOT to any single angle. Additive decomposition requires the middle ray BETWEEN the outer two.
- If the proof makes no significant spatial/geometric claims (e.g. purely algebraic), verdict is SKIP.

## Output

Return a structured result with:
- proposition: "${item.prop}"
- run: "${RUN}"
- book: ${item.book}
- current_category: (from the JSON data)
- verdict: "PASS" | "FAIL" | "SKIP"
- spatial_claims: array of {step, claim, type} for every spatial claim you extracted
- configuration_map: text description of the configuration
- If FAIL: contradictory_steps, spatial_claim_1, spatial_claim_2, contradiction, fixable, fix_note
- If PASS: pass_reason (brief explanation)
- If SKIP: skip_reason (brief explanation)`
}

// ── Phase 1: Check ────────────────────────────────────────────────────

phase('Check')

const results = await pipeline(
  items,
  (item) => agent(buildCheckPrompt(item), {
    label: `check:${item.prop}`,
    phase: 'Check',
    schema: CHECK_RESULT_SCHEMA,
    effort: 'high',
  })
)

const valid = results.filter(Boolean)
log(`Completed: ${valid.length}/${items.length} checks`)

const verdicts = { PASS: 0, FAIL: 0, SKIP: 0 }
for (const r of valid) {
  verdicts[r.verdict] = (verdicts[r.verdict] || 0) + 1
}
log(`Verdicts — PASS: ${verdicts.PASS}, FAIL: ${verdicts.FAIL}, SKIP: ${verdicts.SKIP}`)

// ── Phase 2: Report ───────────────────────────────────────────────────

phase('Report')

// Group results by book for saving
const byBook = {}
for (const r of valid) {
  const b = r.book
  if (!byBook[b]) byBook[b] = []
  byBook[b].push(r)
}

const bookDirs = Object.keys(byBook).map(b =>
  `Book ${b}: ${BASE}/prepared/${RUN}/book${b}/results/`
).join('\n')

await agent(
  `Save each geometry check result as individual JSON files, organized by book.

For each result, save to: ${BASE}/prepared/${RUN}/book<BOOK>/results/<proposition>.json

Create the results/ subdirectory under each book directory if it does not exist.

Books and their directories:
${bookDirs}

Results to save (${valid.length} total):

${JSON.stringify(valid, null, 2)}

Write each result as a formatted JSON file. Do not modify the content.`,
  { label: 'save-results', phase: 'Report' }
)

log('Results saved by book')

return {
  run: RUN,
  total: items.length,
  completed: valid.length,
  verdicts,
  results: valid,
}
