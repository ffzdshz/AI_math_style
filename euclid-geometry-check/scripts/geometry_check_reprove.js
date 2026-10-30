/**
 * Geometry Configuration Consistency Check — Single Reproved Proposition
 *
 * Checks a single reproved proof markdown file for spatial configuration
 * contradictions, following the same protocol as the batch workflow.
 *
 * Args: { run: "RunA", prop: "1.24" }
 *
 * Input:  E:/Claude/euclid-analysis/output/reprove/{book}_{num}_{Run}_reprove.md
 * Output: E:/Claude/euclid-geometry-check/output/Reprove/{prop}_{Run}_GeometryCheck.json
 *         E:/Claude/euclid-geometry-check/output/Reprove/{prop}_{Run}_GeometryCheck_Report.md
 */

export const meta = {
  name: 'geometry-check-reprove',
  description: 'Check a single reproved Euclid proof for geometric configuration contradictions',
  phases: [
    { title: 'Check', detail: 'Geometry configuration audit on reproved proof' },
    { title: 'Report', detail: 'Save result as JSON and markdown report' },
  ],
}

const CHECK_BASE = 'E:/Claude/euclid-geometry-check'
const REPROVE_BASE = 'E:/Claude/euclid-analysis/output/reprove'

const parsed = (typeof args === 'string') ? JSON.parse(args) : args
const run = parsed.run
const prop = parsed.prop
const parts = prop.split('.')
const book = parts[0]
const num = parts[1]
const filename = `${book}_${num}_${run}_reprove.md`

log(`Checking reproved proof: ${run} ${prop} — file: ${filename}`)

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

// ── Phase 1: Check ────────────────────────────────────────────────────

phase('Check')

const result = await agent(
  `You are a geometry expert performing a spatial configuration consistency check on a reproved AI-generated proof of a proposition from Euclid's Elements.

## Your task

1. Read the checking protocol: ${CHECK_BASE}/geometry_check_protocol.md
2. Read the reproved proof: ${REPROVE_BASE}/${filename}
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
- proposition: "${prop}"
- run: "${run}"
- book: ${book}
- source: "reprove"
- verdict: "PASS" | "FAIL" | "SKIP"
- spatial_claims: array of {step, claim, type} for every spatial claim you extracted
- configuration_map: text description of the configuration
- If FAIL: contradictory_steps, spatial_claim_1, spatial_claim_2, contradiction, fixable, fix_note
- If PASS: pass_reason (brief explanation)
- If SKIP: skip_reason (brief explanation)`,
  {
    label: `check:${prop}`,
    phase: 'Check',
    schema: CHECK_RESULT_SCHEMA,
    effort: 'high',
  }
)

if (!result) {
  log('Check agent returned no result.')
  return { error: 'no result', run, prop }
}

log(`Verdict: ${result.verdict}`)

// ── Phase 2: Report ───────────────────────────────────────────────────

phase('Report')

const outDir = `${CHECK_BASE}/output/Reprove`

await agent(
  `Save the geometry check result and generate a markdown report.

1. Create the directory if it does not exist: ${outDir}

2. Save the raw JSON result to: ${outDir}/${prop}_${run}_GeometryCheck.json

JSON content:
${JSON.stringify(result, null, 2)}

3. Generate a markdown report and save to: ${outDir}/${prop}_${run}_GeometryCheck_Report.md

The report format should be:

# Proposition ${prop} — Geometry Configuration Check (${run}, Reprove)

## Verdict: [PASS|FAIL|SKIP]

[If FAIL, include full contradiction details: contradictory steps, spatial claims 1 and 2, contradiction explanation, fixable status, and fix note.]

[If PASS, include the pass_reason.]

[If SKIP, include the skip_reason.]

## Configuration Map

[configuration_map content]

## Spatial Claims

[List all spatial claims as a numbered list with step and claim.]`,
  { label: 'save-report', phase: 'Report' }
)

log(`Results saved to ${outDir}`)

return result
