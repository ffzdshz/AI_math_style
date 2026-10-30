# Euclid Proof Classification Protocol

Classify each AI-generated proof against Heath's proof for the same proposition. Follow this protocol exactly.

> **E must be reproducible across runs.** G vs D may vary at the margin; E may not. The hardened standard in Q1(b) governs every E verdict and overrides any softer reading elsewhere.

| Code | Category | Meaning |
|---|---|---|
| P | Perfect match | Same key intermediate conclusions, same citation set |
| G | Granularity difference | Same key intermediate conclusions, different citation depth |
| D | Path difference | Different key intermediate conclusions, both logically complete |
| E | AI proof error | A *positively identifiable* logical defect (closed list of 5 modes — see Q1) |

---

## Forward-dependency gate (automated, binding)

Pure arithmetic on citation labels — run first.

A Theorem citation b.n is forward for proposition B.N iff b > B, or (b == B and n >= N).
Definitions (D...), Common Notions (CN...), Postulates (P...) are NEVER forward.

If any forward dependency is found → **E (forward dependency)**, no further judgment needed.

---

## Pre-processing

**P1 — Heath data.** Read the Heath proof as an argumentative narrative: the constructions performed, the key geometric facts established, the logical chain to the conclusion. Scan the statement and proof for multi-case markers ("either…or", "first…again", "the one…the other") and list the required cases before proceeding.

**P2 — AI data.** Read the AI proof text. Use the pre-computed citation data (ai_only, heath_only, jaccard) for diagnostic comparison.

**P3 — Diagnostic citation comparison.** Use ai_only / heath_only only to *narrow the search* for where the proofs might diverge — they are a prior, never a verdict:
- Large symmetric difference → divergence more likely; small → granularity more likely.
- ai_only postulates / construction props (P1–P5, I.1–I.3, I.9–I.12) / common notions → suggests over-citation (G). Substantive props → suggests path divergence (D).
- heath_only substantive props that the AI does not cite → either under-citation (G) or a missing step (E); resolved by reading the text in Q1/Q2.
- When heath_only holds substantive props and the AI cites one higher-level proposition that may cover the same ground, defer to the **proof-tree containment test in Q2** — do not decide here.

> A shallow citation diff (small symmetric difference, or ai_only only construction/axioms) makes G a *hypothesis*, not a verdict. The backbones must still be compared in Q2.

---

## Classification

**Governing rule:** The AI proof text is the *only* evidence of what the AI proved. Never infer intent or supply a step a reasonable prover "would" have written — if it is not in the text, it is not in the proof. When a discrepancy appears, re-read both proof texts verbatim; the P3 citation lists narrow the search, they do not replace it.

> **Do not automate the judgment.** Answer each question by reading the texts and writing plain-text reasoning. **Sole exception:** the forward_dependency_check gate (numeric only) is binding and runs first.

Order of operations: **gate → Q1 → Q2 → Q3 → perfect-match check.** Stop at the first definitive answer.

---

### Question 1 — Is the AI proof logically complete?

**Read the AI proof text only. Do not consult Heath yet.**

#### 1(a) Case coverage (multi-case propositions only)

For each required case from P1, verify the text *addresses* it — by a dedicated argument or by a single general argument that demonstrably covers it. A case is *absent* only if neither a dedicated nor a covering argument exists.

→ Genuinely absent case → **E (missing case)**. Stop.

#### 1(b) Conclusion establishment check — hardened standard

**Default presumption: the AI proof is valid.** E is assigned only when a defect can be *positively named*. Terse text, skipped algebra, or a summary-style proof is never by itself an error.

**E triggers only under this closed list of five modes:**

| Mode | Triggers E when… | Does NOT trigger (→ G or D) |
|---|---|---|
| **Unsupported assertion** | The claim has **no supporting step AND no citation** that could license it. | Terse / skips algebra **but** cites or plainly invokes a proposition that licenses it. |
| **Circular / vacuous citation** | The only justification is an item that **merely names or defines** the thing to be proved. | The cited item is a genuine prior result bearing on the claim. |
| **Invalid inference** | AI infers Q from cited P where **P does not entail Q**. | P entails Q and AI merely compressed steps; or the inference is informal but sound. |

**Lenience rule (binding):** when weighing "unsupported" vs "terse-but-supported", or "invalid" vs "compressed-but-sound", the answer is **NOT-E**. Lack of rigour is a G/D matter.

**Mandatory audit record** — emit before assigning *any* E. If any field cannot be completed convincingly, the verdict defaults to **NOT-E** (reclassify G/D):

```
CANDIDATE E — <prop_id>
  violated_claim : <the exact claim that fails>
  failure_mode   : <unsupported_assertion | circular_citation | invalid_inference | missing_case | forward_dependency>
  missing_is     : <support | expansion>   # "expansion" ⇒ NOT an error; reclassify
  evidence       : <AI text span, and the cited ref if any, that you checked>
  why_not_terse  : <one sentence: why this is a genuine logical gap, not mere brevity>
```

`missing_is` is the crux: a missing *expansion of a supported step* is G/D; only a missing *support relation* is E.

→ A claim fails under one mode **and** the audit record completes convincingly → **E**. Stop. Otherwise proceed to Q2.

---

### Question 2 — Do both proofs argue through the same key intermediate conclusions?

Read both proof texts as narratives and identify each one's sequence of **key intermediate conclusions** — the indispensable geometric facts forming the logical backbone. Constructive sub-steps (drawing a line, placing a point) are not key conclusions.

**Case A — same backbone, different citation depth.** Both proofs establish the same key conclusions (verified by reading, not inferred from the citation diff). For each ai_only / heath_only item, confirm by reading that either (a) the underlying fact is present in both proofs at the same logical position, or (b) it satisfies the containment test:

> **Proof-tree containment test.** When heath_only holds substantive props (not definitions/CN/postulates) and the AI cites a single higher-level proposition X covering the same ground:
> - If the heath_only items appear **inside Heath's proof of X** → AI cites X as a unit while Heath re-derives X's internals inline. Citation-depth difference → **G**.
> - If the items are **not inside X** → the items form an independent route from another domain → genuine **D**.

If any ai_only/heath_only item is a substantive fact argued in one proof but absent from the other, Case A fails.

→ Case A holds → **Granularity difference (G)**. Stop.

**Case B — different backbone** → proceed to Q3.

---

### Question 3 — Is the AI's different path valid?

**(a) Positional validity** — already decided by the gate. If you reached Q3, (a) holds.

**(b) Logical completeness** — the AI's chain must run from premises to conclusion. A gap here is E **only under the hardened 1(b) standard**. A sound-but-terse chain is **not** a gap.

- (b) holds → **Path difference (D)**.
- (b) fails under 1(b) → **E**.
- Cannot complete the audit record → default **Path difference (D)**.

---

### Perfect match check

If no category was assigned by the gate or Q1–Q3 and the AI ai_used set equals the Heath heath_refs set exactly → **Perfect match (P)**. Otherwise → **Granularity difference (G)**.
