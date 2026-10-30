export const meta = {
  name: 'classify-reprove',
  description: 'Classify a single reproved AI proof against Heath',
  whenToUse: 'When the user wants to classify a reproved proof for a specific proposition',
  phases: [
    { title: 'Prepare', detail: 'Read config and extract citation data' },
    { title: 'Classify', detail: 'Run classification protocol on the reproved proof' },
  ],
}

const RESULT_SCHEMA = {
  type: 'object',
  properties: {
    proposition: { type: 'string', description: 'Proposition ID e.g. "1.24"' },
    run: { type: 'string', description: 'Run identifier e.g. "RunA"' },
    category: { type: 'string', enum: ['P', 'G', 'D', 'E'], description: 'Classification category' },
    category_label: { type: 'string', description: 'Full category name' },
    error_type: { type: 'string', description: 'Error mode if E, else empty string' },
    analysis: { type: 'string', description: 'One paragraph explaining which question decided the classification and why' },
    jaccard: { type: 'number', description: 'Computed Jaccard similarity' },
    ai_citations: { type: 'string', description: 'Pipe-separated AI citations' },
    heath_citations: { type: 'string', description: 'Pipe-separated Heath citations' },
    ai_only: { type: 'string', description: 'Pipe-separated AI-only citations' },
    heath_only: { type: 'string', description: 'Pipe-separated Heath-only citations' },
    audit_record: { type: 'string', description: 'Audit record text if E was considered, else empty string' },
  },
  required: ['proposition', 'run', 'category', 'category_label', 'error_type', 'analysis',
             'jaccard', 'ai_citations', 'heath_citations', 'ai_only', 'heath_only', 'audit_record'],
  additionalProperties: false,
}

const PROJECT_DIR = 'E:/Claude/euclid-classify-auto'
const REPROVE_DIR = 'E:/Claude/euclid-analysis/output/reprove'
const OUTPUT_DIR = `${PROJECT_DIR}/output/Reprove`

phase('Prepare')

const configResult = await agent(
  `Read the file ${PROJECT_DIR}/reprove_config.json and return its contents as structured data.
The file contains "proposition" (e.g. "1.24") and "run" (e.g. "RunA").`,
  {
    label: 'read-config',
    phase: 'Prepare',
    schema: {
      type: 'object',
      properties: {
        proposition: { type: 'string' },
        run: { type: 'string' },
      },
      required: ['proposition', 'run'],
      additionalProperties: false,
    },
  }
)

const propId = configResult.proposition
const run = configResult.run
const proofPath = `${REPROVE_DIR}/${propId.replace('.', '_')}_${run}_reprove.md`
log(`Classifying reproved proof: ${propId} (${run}) from ${proofPath}`)

phase('Classify')

const classifyPrompt = `You are classifying a REPROVED AI proof of Euclid's Elements proposition ${propId} against Heath's proof.

## Your task

1. Read the classification protocol from: ${PROJECT_DIR}/classify_protocol.md
2. Read the reproved AI proof from: ${proofPath}
3. Look up Heath's proof by running:
   python "${PROJECT_DIR}/scripts/lookup.py" heath_proof ${propId}
4. Look up the proposition statement by running:
   python "${PROJECT_DIR}/scripts/lookup.py" statement ${propId}
5. If you need to look up what a cited proposition states, run:
   python "${PROJECT_DIR}/scripts/lookup.py" statement <prop_id>
6. If you need to check Heath's proof of a cited proposition (for the containment test in Q2), run:
   python "${PROJECT_DIR}/scripts/lookup.py" heath_proof <prop_id>

## Citation extraction

The reproved proof text should contain a USED line listing the citations.
Extract the AI citations from this line.
Look up Heath's citations by checking Heath's proof text.
Compute:
- ai_only: citations in AI but not in Heath
- heath_only: citations in Heath but not in AI
- jaccard: |intersection| / |union| of the two citation sets

## Process

Follow the protocol EXACTLY in this order:

### Step 1: Forward dependency gate
Check if any citation in the AI proof is a forward dependency for proposition ${propId}.
A theorem citation b.n is forward if b > B or (b == B and n >= N) where B.N is the current proposition.
Definitions (D...), Common Notions (CN...), Postulates (P...) are NEVER forward.
If forward dependency found → category E, error_type "Forward dependency". STOP.

### Step 2: Pre-processing (P1, P2, P3)
- P1: Read the Heath proof. Note multi-case markers.
- P2: Read the AI proof text. Note the citation comparison data.
- P3: Analyze ai_only and heath_only as diagnostic pointers only.

### Step 3: Q1 — Is the AI proof logically complete?
- 1(a): Check case coverage for multi-case propositions.
- 1(b): Apply the hardened standard. E only for: unsupported assertion, circular citation, invalid inference.
  Default presumption is VALID. Terse or summary-style proofs are NOT errors.
  If E: complete the audit record. If audit record cannot be completed convincingly → NOT-E.

### Step 4: Q2 — Same key intermediate conclusions?
- Case A (same backbone, different depth) → G
- Case B (different backbone) → proceed to Q3
- Use the proof-tree containment test when heath_only has substantive props.

### Step 5: Q3 — Is the AI's different path valid?
- Valid different path → D
- Invalid under 1(b) standard → E
- Cannot complete audit record → default D

### Step 6: Perfect match check
- If no category assigned AND ai_used == heath_refs exactly → P
- Otherwise → G

## Output requirements

Save your result to a JSON file at: ${OUTPUT_DIR}/${propId.replace('.', '_')}_${run}_reprove.json

Before writing, ensure the directory exists: mkdir -p "${OUTPUT_DIR}"

Then return your structured classification result.

The "analysis" field should be one paragraph explaining which question decided the classification and why.
For ai_citations, heath_citations, ai_only, heath_only: use pipe-separated format.
For error_type: use one of "Forward dependency", "Unsupported assertion", "Circular citation", "Invalid inference", "Missing case", or "" if not E.
For audit_record: include the full CANDIDATE E record if you considered E, otherwise empty string "".`

const result = await agent(classifyPrompt, {
  label: `classify:${propId}`,
  phase: 'Classify',
  schema: RESULT_SCHEMA,
  effort: 'high',
})

if (result) {
  log(`Result: ${propId} → ${result.category} (${result.category_label}), Jaccard=${result.jaccard}`)
} else {
  log(`ERROR: Classification failed for ${propId}`)
}

return {
  proposition: propId,
  proof_path: proofPath,
  result,
}
