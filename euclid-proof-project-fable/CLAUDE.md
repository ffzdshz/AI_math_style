Read and follow the protocol in ./SKILL.md for all proof tasks.

## Usage

Prove an entire book (specify run):

    Prove Book 5, RunA
    Prove Book 10, RunB

## Model and effort

Every proving sub-agent is pinned to model `claude-fable-5-1` and reasoning effort `xhigh`
(`MODEL_ID` and `EFFORT` in `generate_workflow.py`, passed as `model:` / `effort:` to each
`agent()` call; both are recorded in every result item). The Opus 4.6 runs used effort `high`.

## Re-running a single proposition (after an API failure)

- Do NOT use Workflow `resumeFromRunId` to retry one failed proposition: replay is prefix-based, so every
  proposition after the failed one is re-run live (new samples replace already-good proofs, tokens wasted).
- Instead: `python generate_workflow.py <book> <A|B|C> --only <n>` writes `workflow_Run{X}_Book{N}_only{n}.js`
  whose prompt is byte-identical to the full-book script; run it, then merge the result into the saved
  proofs JSON before `finalize_run.py`. Book 8 RunA 8.21 was completed this way (see proofs JSON `provenance`).
- Known API failure: HTTP 400 `Output blocked by content filtering policy` (Fable safety classifier, fires
  during hidden thinking). Same prompt may pass on a later attempt; 8.21 passed on its 5th attempt overall.

## Output naming

All outputs include the run identifier:

- `proofs/RunA_Book5/`  — per-proposition .md files
- `outputs/RunA_Book5_StepByStep_Proofs.md`
- `outputs/RunA_Book5_AI_vs_Human_Citations.csv`

## Project structure

- `data/` — xlsx source files + pre-extracted JSON
- `proofs/` — per-proposition proof files, organized by Run + Book
- `outputs/` — aggregated reports per Run + Book
- `euclid_prove_book.js` — workflow script: parallel per-proposition proving
- `euclid_postprocess.py` — Jaccard computation + output generation
- `finalize_run.py` — post-workflow step: `python finalize_run.py <book> <A|B|C> <task_output_json> [wf_id]`
  (saves proofs/Run{X}_Book{N}_results.json, runs the Step 2.5 checks, calls euclid_postprocess.py,
  appends per-agent timings to outputs/agent_timings.csv)
- `SKILL.md` — the 4-step Euclid proof protocol
