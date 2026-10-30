/**
 * Geometry Configuration Consistency Check Workflow
 *
 * Three-phase pipeline:
 *   1. Discover — read manifest of D-category propositions
 *   2. Check   — per-proposition geometry configuration check (parallel agents)
 *   3. Report  — save results and generate summary
 *
 * Args: { run: "RunA", book: 1 }
 *
 * Prerequisites:
 *   python scripts/preprocess.py <run> <book> --categories D
 *
 * Post-processing:
 *   python scripts/collect_results.py <run> <book>
 */

export const meta = {
  name: 'geometry-check',
  description: 'Check D-class Euclid proofs for geometric configuration contradictions',
  phases: [
    { title: 'Discover', detail: 'Read manifest of propositions to check' },
    { title: 'Check', detail: 'Per-proposition geometry configuration audit' },
    { title: 'Report', detail: 'Save individual results to JSON files' },
  ],
}

const BASE = 'E:/Claude/euclid-geometry-check'

const parsed = (typeof args === 'string') ? JSON.parse(args) : args
const run = parsed.run
const book = parsed.book
log(`args received: run=${run}, book=${book}`)

// ── Schema ────────────────────────────────────────────────────────────

const MANIFEST_SCHEMA = {
  type: 'object',
  properties: {
    run: { type: 'string' },
    book: { type: 'number' },
    propositions: { type: 'array', items: { type: 'string' } },
  },
  required: ['propositions'],
}

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

function buildCheckPrompt(prop) {
  return `You are a geometry expert performing a spatial configuration consistency check on an AI-generated proof of a proposition from Euclid's Elements.

## Your task

1. Read the checking protocol: ${BASE}/geometry_check_protocol.md
2. Read the proposition data: ${BASE}/prepared/${run}/book${book}/${prop}.json
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
- proposition: "${prop}"
- run: "${run}"
- book: ${book}
- current_category: (from the JSON data)
- verdict: "PASS" | "FAIL" | "SKIP"
- spatial_claims: array of {step, claim, type} for every spatial claim you extracted
- configuration_map: text description of the configuration
- If FAIL: contradictory_steps, spatial_claim_1, spatial_claim_2, contradiction, fixable, fix_note
- If PASS: pass_reason (brief explanation)
- If SKIP: skip_reason (brief explanation)`
}

// ── Phase 1: Discover ─────────────────────────────────────────────────

phase('Discover')

const manifest = await agent(
  `Read the file ${BASE}/prepared/${run}/book${book}/manifest.json and return its contents. The file is a JSON object with fields: run, book, propositions (array of proposition ID strings like "1.24", "3.5").`,
  { label: 'read-manifest', schema: MANIFEST_SCHEMA }
)

if (!manifest || !manifest.propositions || manifest.propositions.length === 0) {
  log('No propositions found in manifest. Did you run preprocess.py first?')
  return { error: 'empty manifest', run, book }
}

log(`${run} Book ${book}: ${manifest.propositions.length} propositions to check — ${manifest.propositions.join(', ')}`)

// ── Phase 2: Check ────────────────────────────────────────────────────

phase('Check')

const results = await pipeline(
  manifest.propositions,
  (prop) => agent(buildCheckPrompt(prop), {
    label: `check:${prop}`,
    phase: 'Check',
    schema: CHECK_RESULT_SCHEMA,
    effort: 'high',
  })
)

const valid = results.filter(Boolean)
log(`Completed: ${valid.length}/${manifest.propositions.length} checks`)

const verdicts = { PASS: 0, FAIL: 0, SKIP: 0 }
for (const r of valid) {
  verdicts[r.verdict] = (verdicts[r.verdict] || 0) + 1
}
log(`Verdicts — PASS: ${verdicts.PASS}, FAIL: ${verdicts.FAIL}, SKIP: ${verdicts.SKIP}`)

// ── Phase 3: Report ───────────────────────────────────────────────────

phase('Report')

const resultsDir = `${BASE}/prepared/${run}/book${book}/results`
const resultsSummary = valid.map(r =>
  `${r.proposition}: verdict=${r.verdict}` +
  (r.verdict === 'FAIL' ? ` contradiction="${r.contradiction || ''}"` : '')
).join('\n')

await agent(
  `Save each of the following geometry check results as individual JSON files.

Create the directory if it does not exist: ${resultsDir}

For each result object below, save it to: ${resultsDir}/<proposition>.json
(e.g., ${resultsDir}/1.24.json)

Results to save (${valid.length} total):

${JSON.stringify(valid, null, 2)}

Write each result as a formatted JSON file. Do not modify the content, just save each one to its own file.`,
  { label: 'save-results', phase: 'Report' }
)

log(`Results saved to ${resultsDir}`)

return {
  run,
  book,
  total: manifest.propositions.length,
  completed: valid.length,
  verdicts,
  results: valid,
}
