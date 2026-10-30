/**
 * Geometry Configuration Consistency Check — Batch Reproved Propositions
 *
 * Checks all reproved proof markdown files for spatial configuration
 * contradictions, following the same protocol as the batch workflow.
 *
 * Args: { items: [{ run: "RunA", prop: "1.24", file: "1_24_RunA_reprove.md" }, ...] }
 *
 * Input:  E:/Claude/euclid-analysis/output/reprove/*.md
 * Output: E:/Claude/euclid-analysis/output/validation/<prop>_<Run>_GeometryCheck.json
 *         E:/Claude/euclid-analysis/output/validation/Reprove_All_GeometryCheck_Report.md
 */

export const meta = {
  name: 'geometry-check-reprove-batch',
  description: 'Check all reproved Euclid proofs for geometric configuration contradictions',
  phases: [
    { title: 'Check', detail: 'Per-proposition geometry configuration audit' },
    { title: 'Report', detail: 'Save results as JSON and generate merged report' },
  ],
}

const CHECK_BASE = 'E:/Claude/euclid-geometry-check'
const REPROVE_BASE = 'E:/Claude/euclid-analysis/output/reprove'
const OUT_DIR = 'E:/Claude/euclid-analysis/output/validation'

const parsed = (typeof args === 'string') ? JSON.parse(args) : args
const items = parsed.items

log(`Batch reprove geometry check: ${items.length} propositions`)

// ── Schema ────────────────────────────────────────────────────────────

const CHECK_RESULT_SCHEMA = {
  type: 'object',
  properties: {
    proposition:        { type: 'string' },
    run:                { type: 'string' },
    book:               { type: 'number' },
    source:             { type: 'string' },
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
    contradiction:     { type: 'string' },
    fixable:           { type: 'boolean' },
    fix_note:          { type: 'string' },
    pass_reason:       { type: 'string' },
    skip_reason:       { type: 'string' },
    configuration_map: { type: 'string' },
  },
  required: ['proposition', 'run', 'verdict'],
}

// ── Prompt builder ────────────────────────────────────────────────────

function buildCheckPrompt(item) {
  const book = item.prop.split('.')[0]
  return `You are a geometry expert performing a spatial configuration consistency check on a reproved AI-generated proof of a proposition from Euclid's Elements.

## Your task

1. Read the checking protocol: ${CHECK_BASE}/geometry_check_protocol.md
2. Read the reproved proof: ${REPROVE_BASE}/${item.file}
   - This is a markdown file containing the full step-by-step reproved AI proof.

3. Follow the protocol precisely:
   **Step A**: Extract every spatial claim from the proof (point positions, ray orderings, angle decompositions, inside/outside claims).
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
- run: "${item.run}"
- book: ${book}
- source: "reprove"
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
    label: `check:${item.prop}_${item.run}`,
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

const jsonBlock = JSON.stringify(valid, null, 2)

await agent(
  `Save geometry check results for reproved propositions.

1. Create the directory if it does not exist: ${OUT_DIR}

2. Save each result as an individual JSON file to: ${OUT_DIR}/<proposition>_<run>_GeometryCheck.json
   For example, proposition "1.24" run "RunA" → ${OUT_DIR}/1.24_RunA_GeometryCheck.json

3. Save all results as a combined JSON array to: ${OUT_DIR}/Reprove_All_GeometryCheck.json

Results (${valid.length} total):

${jsonBlock}

Write each result as a formatted JSON file. Do not modify the content.`,
  { label: 'save-json', phase: 'Report' }
)

await agent(
  `Generate a merged markdown report for all reprove geometry check results and save it.

Save to: ${OUT_DIR}/Reprove_All_GeometryCheck_Report.md

Use this format:

# Reprove — Geometry Configuration Check Report

## Overall Summary

**Total propositions checked**: ${valid.length}

| Verdict | Count | Propositions |
|---|---|---|
| PASS | ${verdicts.PASS} | [list] |
| FAIL | ${verdicts.FAIL} | [list] |
| SKIP | ${verdicts.SKIP} | [list] |

## Detected Contradictions

[For each FAIL result, include full details: contradictory steps, spatial claims, contradiction explanation, fixable status, fix note]

## Passed Propositions

[For each PASS result, include one bullet: proposition (run) — pass_reason]

## Skipped Propositions

[For each SKIP result, include one bullet: proposition (run) — skip_reason]

---

Results data:

${jsonBlock}`,
  { label: 'save-report', phase: 'Report' }
)

log(`All results saved to ${OUT_DIR}`)

return {
  total: items.length,
  completed: valid.length,
  verdicts,
  results: valid,
}
