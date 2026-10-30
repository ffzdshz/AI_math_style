export const meta = {
  name: 'euclid-prove-book',
  description: 'Independently prove all propositions in one book of Euclid\'s Elements',
  phases: [
    { title: 'Prove', detail: 'Each proposition proved by a dedicated agent' },
    { title: 'Retry', detail: 'Re-prove propositions with ordering violations' }
  ]
}

const SCHEMA = {
  type: 'object',
  properties: {
    prop_id: { type: 'string', description: 'Proposition ID e.g. 5.12' },
    proof: { type: 'string', description: 'Step-by-step proof text with **Step N.** format' },
    used: { type: 'array', items: { type: 'string' }, description: 'Reference IDs actually cited' }
  },
  required: ['prop_id', 'proof', 'used'],
  additionalProperties: false
}

const { bookNum, runId, foundations, theorems, propositions } = args

log('Run ' + runId + ' | Book ' + bookNum)

function buildPrompt(prop, isRetry, priorViolations) {
  const sameBook = []
  for (const [tid, stmt] of Object.entries(theorems)) {
    const dotIdx = tid.indexOf('.')
    const b = parseInt(tid.substring(0, dotIdx))
    const p = parseInt(tid.substring(dotIdx + 1))
    if (b === bookNum && p < prop.propNum) {
      sameBook.push(tid + ': ' + stmt)
    }
  }

  const otherBooks = {}
  for (const tid of Object.keys(theorems)) {
    const b = parseInt(tid.split('.')[0])
    if (b < bookNum) {
      if (!otherBooks[b]) otherBooks[b] = []
      otherBooks[b].push(tid)
    }
  }
  const otherSummary = Object.keys(otherBooks)
    .map(Number).sort((a, b) => a - b)
    .map(b => 'Book ' + b + ': ' + otherBooks[b].join(', '))
    .join('\n')

  const retryWarning = isRetry
    ? '\n\n!!! RETRY WARNING !!!\nYour previous proof had OUT-OF-ORDER citations: ' + priorViolations.join(', ') +
      '\nThese are FORBIDDEN. You must NOT cite ' + prop.id + ' itself or any proposition >= ' + prop.id +
      ' or from a later book. Double-check EVERY entry in your USED list.\n'
    : ''

  return 'Prove this proposition from Euclid\'s Elements independently.' + retryWarning + '\n\n' +
    'PROPOSITION: ' + prop.id + '\n' +
    'STATEMENT: ' + prop.statement + '\n\n' +
    'RULES:\n' +
    '1. Reason ONLY from the tools listed below - no external content\n' +
    '2. Write a step-by-step proof with explicit citations at each step\n' +
    '3. USED list = only references actually invoked in the reasoning (no insurance citations)\n' +
    '4. Choose the most direct proof route\n' +
    '5. When two equivalent propositions could serve, choose the one naturally reached first and note why\n\n' +
    'STRICT ORDERING: For ' + prop.id + ', you may cite:\n' +
    '- Postulates (P1-P5), Common Notions (CN1-CN5), Definitions (D...) - always valid\n' +
    '- Theorems from Books 1 through ' + (bookNum - 1) + ' (any proposition number)\n' +
    '- Book ' + bookNum + ' theorems with proposition number STRICTLY LESS than ' + prop.propNum + '\n' +
    '- NEVER cite ' + prop.id + ' itself or any ' + bookNum + '.j where j >= ' + prop.propNum + '\n' +
    'CHECK every entry in your USED list before finalizing!\n\n' +
    'FOUNDATIONS (always available):\n' + foundations + '\n\n' +
    'PRECEDING THEOREMS IN BOOK ' + bookNum + ':\n' +
    (sameBook.length > 0 ? sameBook.join('\n') : '(None - this is the first theorem)') + '\n\n' +
    'THEOREMS FROM EARLIER BOOKS (available by ID - you know their content):\n' +
    (otherSummary || '(None - this is Book 1)') + '\n\n' +
    'Return structured output: prop_id="' + prop.id + '", proof (each step as "**Step N.** ..."), used (array of ref IDs like ["P1","CN1","D1.15","1.4"]).'
}

function findViolations(propId, used) {
  const dotIdx = propId.indexOf('.')
  const sb = parseInt(propId.substring(0, dotIdx))
  const sp = parseInt(propId.substring(dotIdx + 1))
  const bad = []
  for (const ref of used) {
    const m = ref.match(/^(\d+)\.(\d+)$/)
    if (!m) continue
    const tb = parseInt(m[1])
    const tp = parseInt(m[2])
    if (tb > sb || (tb === sb && tp >= sp)) {
      bad.push(ref)
    }
  }
  return bad
}

// Phase 1: Prove all propositions
phase('Prove')
log('Book ' + bookNum + ': proving ' + propositions.length + ' propositions')

const initialResults = await pipeline(
  propositions,
  async (prop) => {
    const prompt = buildPrompt(prop, false, [])
    const result = await agent(prompt, {
      label: prop.id,
      phase: 'Prove',
      schema: SCHEMA,
      effort: 'high'
    })
    if (result) {
      log(prop.id + ' proved (' + result.used.length + ' refs)')
    }
    return result
  }
)

// Collect results and find violations
const proofs = {}
for (const r of initialResults.filter(Boolean)) {
  proofs[r.prop_id] = { proof: r.proof, used: r.used, violations: [] }
}

const violated = []
for (const [pid, data] of Object.entries(proofs)) {
  const bad = findViolations(pid, data.used)
  if (bad.length > 0) {
    data.violations = bad
    violated.push(pid)
  }
}

if (violated.length > 0) {
  log('Violations found in: ' + violated.join(', ') + ' - retrying...')

  // Phase 2: Retry violated propositions (up to 3 attempts each)
  phase('Retry')

  const retryProps = propositions.filter(p => violated.includes(p.id))

  const retryResults = await pipeline(
    retryProps,
    async (prop) => {
      let bestResult = proofs[prop.id]
      for (let attempt = 1; attempt <= 3; attempt++) {
        const prompt = buildPrompt(prop, true, bestResult.violations)
        const result = await agent(prompt, {
          label: prop.id + ' retry#' + attempt,
          phase: 'Retry',
          schema: SCHEMA,
          effort: 'high'
        })
        if (!result) break
        const bad = findViolations(prop.id, result.used)
        if (bad.length === 0) {
          log(prop.id + ': resolved on attempt ' + attempt)
          return { ...result, resolved: true }
        }
        if (bad.length < bestResult.violations.length) {
          bestResult = { proof: result.proof, used: result.used, violations: bad }
        }
      }
      log(prop.id + ': UNRESOLVED after 3 attempts')
      return {
        prop_id: prop.id,
        proof: '[UNRESOLVED violations: ' + bestResult.violations.join(', ') + '] ' + bestResult.proof,
        used: bestResult.used,
        resolved: false
      }
    }
  )

  // Update proofs with retry results
  for (const r of retryResults.filter(Boolean)) {
    proofs[r.prop_id] = { proof: r.proof, used: r.used, violations: findViolations(r.prop_id, r.used) }
  }
} else {
  log('No ordering violations found')
}

// Return all proofs
const finalResults = propositions.map(p => {
  const data = proofs[p.id]
  if (!data) return null
  return {
    prop_id: p.id,
    statement: p.statement,
    proof: data.proof,
    used: data.used,
    has_violations: data.violations.length > 0
  }
}).filter(Boolean)

log('Done: ' + finalResults.length + '/' + propositions.length + ' propositions completed')

return finalResults
