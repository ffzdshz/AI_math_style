Read and follow the protocol in ./SKILL.md for all proof tasks.

## Usage

Prove an entire book (specify run):

    Prove Book 5, RunA
    Prove Book 10, RunB

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
- `SKILL.md` — the 4-step Euclid proof protocol
