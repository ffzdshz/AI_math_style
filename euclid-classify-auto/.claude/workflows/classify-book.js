export const meta = {
  name: 'classify-book',
  description: 'Classify AI proofs for one book of Euclid, one proposition at a time',
  whenToUse: 'When the user wants to classify AI proofs for a specific book and run (e.g. "classify book 1 for RunA")',
  phases: [
    { title: 'Prepare', detail: 'Preprocess data files into per-proposition JSON' },
    { title: 'Classify', detail: 'One agent per proposition, following the classification protocol' },
    { title: 'Collect', detail: 'Combine results into CSV and Markdown report' },
  ],
}

const RESULT_SCHEMA = {
  type: 'object',
  properties: {
    proposition: { type: 'string', description: 'Proposition ID e.g. "1.1"' },
    category: { type: 'string', enum: ['P', 'G', 'D', 'E'], description: 'Classification category' },
    category_label: { type: 'string', description: 'Full category name' },
    error_type: { type: 'string', description: 'Error mode if E, else empty string' },
    analysis: { type: 'string', description: 'One paragraph explaining which question decided the classification and why' },
    jaccard: { type: 'number', description: 'Pre-computed Jaccard similarity' },
    ai_citations: { type: 'string', description: 'Pipe-separated AI citations' },
    heath_citations: { type: 'string', description: 'Pipe-separated Heath citations' },
    ai_only: { type: 'string', description: 'Pipe-separated AI-only citations' },
    heath_only: { type: 'string', description: 'Pipe-separated Heath-only citations' },
    audit_record: { type: 'string', description: 'Audit record text if E was considered, else empty string' },
  },
  required: ['proposition', 'category', 'category_label', 'error_type', 'analysis',
             'jaccard', 'ai_citations', 'heath_citations', 'ai_only', 'heath_only', 'audit_record'],
  additionalProperties: false,
}

const PROJECT_DIR = 'E:/Claude/euclid-classify-auto'

// Phase 1: Prepare data (includes reading config)
phase('Prepare')

// Read parameters from run_config.json (args passthrough unreliable)
const configResult = await agent(
  `Read the file ${PROJECT_DIR}/run_config.json and return its contents as structured data. The file may contain optional "start" and "end" fields for proposition range filtering.`,
  {
    label: 'read-config',
    phase: 'Prepare',
    schema: {
      type: 'object',
      properties: {
        run: { type: 'string' },
        book: { type: 'number' },
        start: { type: 'number', description: 'Optional start proposition number (inclusive)' },
        end: { type: 'number', description: 'Optional end proposition number (inclusive)' },
      },
      required: ['run', 'book'],
      additionalProperties: false,
    },
  }
)
const run = configResult.run
const book = String(configResult.book)
const rangeStart = configResult.start || null
const rangeEnd = configResult.end || null
log(`Config loaded: run=${run}, book=${book}${rangeStart ? `, range=${rangeStart}-${rangeEnd}` : ''}`)
const BOOK_DIR = `${PROJECT_DIR}/prepared/${run}/book${book}`
const RESULTS_DIR = `${BOOK_DIR}/results`
const OUTPUT_CSV = `${PROJECT_DIR}/output/${run}/Book${book}_Classification.csv`
const OUTPUT_MD = `${PROJECT_DIR}/output/${run}/Book${book}_Classification_Report.md`

log(`Preprocessing ${run} Book ${book}...`)

const prepResult = await agent(
  `Run the preprocessing script to prepare per-proposition data for classification.

Execute this command:
  python "${PROJECT_DIR}/scripts/preprocess.py" ${run} ${book}

Then read the manifest file at:
  ${PROJECT_DIR}/prepared/${run}/book${book}/manifest.json

Return the list of proposition IDs from the manifest.`,
  {
    label: 'preprocess',
    phase: 'Prepare',
    schema: {
      type: 'object',
      properties: {
        propositions: {
          type: 'array',
          items: { type: 'string' },
          description: 'List of proposition IDs for this book',
        },
        count: { type: 'number' },
      },
      required: ['propositions', 'count'],
      additionalProperties: false,
    },
  }
)

if (!prepResult || !prepResult.propositions || prepResult.propositions.length === 0) {
  log('ERROR: Preprocessing failed or no propositions found.')
  return { error: 'Preprocessing failed', run, book }
}

let props = prepResult.propositions
if (rangeStart && rangeEnd) {
  props = props.filter(p => {
    const n = parseInt(p.split('.')[1])
    return n >= rangeStart && n <= rangeEnd
  })
  log(`Filtered to range ${rangeStart}-${rangeEnd}: ${props.length} propositions`)
}
log(`Found ${props.length} propositions to classify: ${props[0]} .. ${props[props.length - 1]}`)

// Phase 2: Classify each proposition
phase('Classify')

const classifyPrompt = (propId) => `You are classifying AI proof of Euclid's Elements proposition ${propId} against Heath's proof.

## Your task

1. Read the classification protocol from: ${PROJECT_DIR}/classify_protocol.md
2. Read the proposition data from: ${PROJECT_DIR}/prepared/${run}/book${book}/${propId}.json
3. If you need to look up what a cited proposition states, run:
   python "${PROJECT_DIR}/scripts/lookup.py" statement <prop_id>
4. If you need to check Heath's proof of a cited proposition (for the containment test in Q2), run:
   python "${PROJECT_DIR}/scripts/lookup.py" heath_proof <prop_id>
   You can look up multiple IDs at once: python "${PROJECT_DIR}/scripts/lookup.py" heath_proof 5.16 5.22 5.7

## Process

Follow the protocol EXACTLY in this order:

### Step 1: Forward dependency gate
Check if any citation in ai_used is a forward dependency for proposition ${propId}.
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

After you have determined your classification, you MUST save your result to a JSON file:
  Write the result JSON to: ${RESULTS_DIR}/${propId}.json

The JSON must have these fields: proposition, category, category_label, error_type, analysis, jaccard, ai_citations, heath_citations, ai_only, heath_only, audit_record.

Then return your structured classification result.

The "analysis" field should be one paragraph explaining which question decided the classification and why. If you considered E at any point, include the full audit record in the "audit_record" field.

For ai_citations, heath_citations, ai_only, heath_only: use pipe-separated format (e.g. "CN1|D1.15|P3").
For error_type: use one of "Forward dependency", "Unsupported assertion", "Circular citation", "Invalid inference", "Missing case", or "" if not E.
For audit_record: include the full CANDIDATE E record if you considered E, otherwise empty string "".

IMPORTANT: Before writing the result file, ensure the directory exists by running: mkdir -p "${RESULTS_DIR}"`

const results = await pipeline(
  props,
  (propId) => agent(classifyPrompt(propId), {
    label: `classify:${propId}`,
    phase: 'Classify',
    schema: RESULT_SCHEMA,
    effort: 'high',
  })
)

// Count valid results
const validResults = results.filter(Boolean)
log(`Classified ${validResults.length}/${props.length} propositions (results already saved by each agent)`)

// Phase 3: Collect — just run the Python script, no data transfer needed
phase('Collect')

const collectResult = await agent(
  `Run the collection script to generate CSV and Markdown report from the individual result files.

Execute:
  python "${PROJECT_DIR}/scripts/collect_results.py" ${run} ${book}

Expected output CSV: ${OUTPUT_CSV}
Expected output report: ${OUTPUT_MD}

Report the summary statistics from the script output.`,
  {
    label: 'collect-results',
    phase: 'Collect',
    schema: {
      type: 'object',
      properties: {
        csv_path: { type: 'string' },
        report_path: { type: 'string' },
        summary: { type: 'string' },
      },
      required: ['csv_path', 'report_path', 'summary'],
      additionalProperties: false,
    },
  }
)

log(`Done! Results saved.`)
if (collectResult) {
  log(`CSV: ${collectResult.csv_path}`)
  log(`Report: ${collectResult.report_path}`)
  log(`Summary: ${collectResult.summary}`)
}

return {
  run,
  book,
  totalPropositions: props.length,
  classified: validResults.length,
  results: collectResult,
}
