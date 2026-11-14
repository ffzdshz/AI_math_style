# AI Has Its Own Style in Mathematical Proving

Data, prompts, workflows and analysis code for the paper:

> **AI has its own style in mathematical proving**
> Xiaokai Li, Ziyu Zhou, Qibin Cheng, Yangcheng Wu, An Zeng, Ying Fan
> arXiv:2611.16527 (2026)
>
> 📄 Paper: <https://arxiv.org/abs/2611.16527>

We asked large language models to independently reprove all 465 propositions of Euclid's *Elements*, citing only the postulates, common notions, definitions and preceding propositions available at each point in the deductive system. We then compared the AI citation choices with the human baseline given by Heath's classical translation, using Jaccard similarity and complex network analysis.

This repository contains everything needed to inspect and audit the results:

- the complete AI-generated proofs (2,325 proofs across five runs, plus 1,395 proofs from three prompt-robustness experiments);
- the citation set extracted from every proof, alongside Heath's citations;
- the classification of every proof (P / G / D / E), the geometric consistency audit and the expert validation records;
- the citation networks of the human proofs and of every AI run;
- the Claude Code skills and workflows used to generate the Claude proofs and to classify and audit all proofs;
- the notebooks and intermediate tables used to produce the figures in the paper.

---

## Contents

1. [Experimental design at a glance](#1-experimental-design-at-a-glance)
2. [Repository structure](#2-repository-structure)
3. [Core data (`data/`)](#3-core-data-data)
4. [Pipelines](#4-pipelines)
5. [Prompt-robustness experiments (GPT-6 Astra)](#5-prompt-robustness-experiments-gpt-6-astra)
6. [Analysis and figures (`analysis/`)](#6-analysis-and-figures-analysis)
7. [Quick start](#7-quick-start)
8. [Conventions and caveats](#8-conventions-and-caveats)
9. [Citation and license](#9-citation-and-license)

---

## 1. Experimental design at a glance

| Label in files | Model | Runs | Proof-generation project |
|---|---|---|---|
| `RunA`, `RunB`, `RunC` | Claude Opus 4.6 | 3 independent runs | `euclid-proof-project/` |
| `Fable` | Claude Fable 5.1 | 1 run | `euclid-proof-project-fable/` |
| `GPT` | GPT-6 Astra (reasoning effort `xhigh`) | 1 baseline run | `gpt_RunA/` |
| — | GPT-6 Astra | 3 prompt variants | `gpt_Antiground_RunA/`, `gpt_ShuffledTable_RunA/`, `gpt_ReverseTable_RunA/` |

**Proving protocol.** Each proposition is proved by a dedicated, isolated sub-agent that sees only the proposition statement and the resources it is allowed to cite: the five postulates, the five common notions, all definitions up to the current book, and all propositions that strictly precede it. The sub-agent never sees Heath's proof. It returns the proof text and the list of resources it used (`used`), from which the AI citation set is taken.

**Evaluation pipeline.**

1. **Citation comparison**: AI vs Heath citation sets, Jaccard similarity per proposition.
2. **AI check**: automated classification of every proof (P / G / D / E), followed by a geometric configuration consistency audit of D-class proofs in geometric books.
3. **Expert validation**: two experts with mathematical training (the second and third authors) reviewed every flagged error and a random sample of D-class proofs.
4. **Re-prove**: every confirmed error was re-proved by the AI under the same constraints and re-classified.

---

## 2. Repository structure

```
AI_math_style/
├── data/                         # Canonical, analysis-ready data (start here)
│   ├── reference/                # Euclid statements, Heath citations and Heath proofs
│   ├── proofs/                   # Full AI proofs, one file per run, plus error summary
│   ├── citations/                # AI vs Heath citation comparison, one CSV per run
│   ├── classification/           # P/G/D/E classification and reports, one per run
│   ├── geometry_check/           # Geometric consistency audit reports, one per run
│   ├── expert_validation/        # Expert review records and the materials sent to experts
│   └── network/                  # Citation networks (NetworkX DiGraph, pickle)
│
├── analysis/                     # Notebooks and intermediate tables for the figures
│
├── euclid-proof-project/         # Proof generation, Claude Opus 4.6 (Runs A, B, C)
├── euclid-proof-project-fable/   # Proof generation, Claude Fable 5.1
├── euclid-classify-auto/         # Automated classification and re-prove workflows
├── euclid-geometry-check/        # Geometric consistency audit workflows
│
├── gpt_RunA/                     # GPT-6 Astra, baseline prompt
├── gpt_Antiground_RunA/          # GPT-6 Astra, anti-grounding instruction
├── gpt_ShuffledTable_RunA/       # GPT-6 Astra, shuffled resource table
└── gpt_ReverseTable_RunA/        # GPT-6 Astra, reverse-ordered resource table
```

The pipeline folders keep their own working copies of the inputs and outputs so that each pipeline is self-contained. **The files in `data/` are the canonical versions used in the paper**; where the same proofs or tables appear in several folders, use the copy in `data/`.

---

## 3. Core data (`data/`)

### 3.1 `data/reference/` — Euclid's *Elements* and Heath's proofs

| File | Rows | Columns | Content |
|---|---|---|---|
| `Euclid_All_Statements.xlsx` | 607 | `ID`, `Type`, `Book`, `Statement` | 5 postulates, 5 common notions, 132 definitions and 465 propositions |
| `Euclid_Human_References_All465.xlsx` | 465 | `Proposition`, `Book_Name`, `All_References` | Heath's citation set for each proposition (the human baseline) |
| `Euclid_Heath_Proofs.xlsx` | 607 | `ID`, `Proof` | Heath's proof text |

Source: the structured version of Heath's translation hosted on the [Wolfram Data Repository](https://datarepository.wolframcloud.com/resources/Structure-of-Euclids-Elements/).

### 3.2 `data/proofs/` — AI-generated proofs

| File | Content |
|---|---|
| `RunA_All_Books_StepByStep_Proofs_Final.md` | Claude Opus 4.6, Run A, all 465 propositions |
| `RunB_All_Books_StepByStep_Proofs_Final.md` | Claude Opus 4.6, Run B |
| `RunC_All_Books_StepByStep_Proofs_Final.md` | Claude Opus 4.6, Run C |
| `Fable5.1_StepByStep_Proofs.md` | Claude Fable 5.1 |
| `GPT-6-Astra_All_Books_StepByStep_Proofs.md` | GPT-6 Astra (baseline prompt) |
| `AI_Error_Summary.md` | Every error identified in the Opus runs, with the violated claim, failure mode and evidence |

Each proof is written step by step, with the cited resource given for each step. Per-proposition files are available in the `proofs/` sub-folders of each proof-generation project.

### 3.3 `data/citations/` — citation comparison

One CSV per run (`RunA_…_Final.csv`, `RunB_…_Final.csv`, `RunC_…_Final.csv`, `Fable5.1_…csv`, `GPT-6-Astra_…csv`), 465 rows each.

| Column | Description |
|---|---|
| `Proposition` | Proposition identifier, e.g. `1.47` (**read as text**, see §8) |
| `Statement` | Statement of the proposition |
| `AI_USED` | AI citation set, pipe-separated, e.g. `1.4\|1.5\|CN1` |
| `Human_Refs` | Heath's citation set, pipe-separated |
| `Shared` | Citations common to both |
| `AI_Only_Extra` | Citations used only by the AI |
| `Human_Only_Missing` | Citations used only by Heath |
| `Jaccard` | Jaccard similarity, \|AI ∩ Human\| / \|AI ∪ Human\| |

### 3.4 `data/classification/` — P / G / D / E classification

| Code | Category | Meaning |
|---|---|---|
| P | Perfect match | Same key intermediate conclusions, same citation set |
| G | Granularity difference | Same key intermediate conclusions, different citation depth |
| D | Path difference | Different key intermediate conclusions, both logically complete |
| E | AI proof error | A positively identifiable logical defect |

One CSV and one Markdown report per run. CSV columns: `Proposition`, `Book`, `Category`, `Category_Label`, `Error_type`, `Jaccard`, `AI_citations`, `Heath_citations`, `AI_only`, `Heath_only`. The reports give the reasoning behind each verdict. The full protocol, including the forward-dependency gate and the closed list of error modes, is in `euclid-classify-auto/classify_protocol.md`.

The classification at the three stages reported in the paper (Table 1) can be reconstructed from:

| Stage | File |
|---|---|
| After AI check | `data/classification/*` together with `data/geometry_check/*` |
| After expert validation | `analysis/expert_verified_classification.csv` |
| After re-prove (final) | `analysis/final_classification.csv` and `data/classification/*_Final.csv` |

### 3.5 `data/geometry_check/` — geometric configuration audit

One report per run. D-class proofs in geometric books (Books I–IV, VI, X–XIII) were checked for spatial configuration contradictions, i.e. steps that are individually sound but rest on mutually inconsistent assumptions about the positions of points, lines and circles. Each proof receives PASS, FAIL or SKIP (non-geometric proposition). The protocol is in `euclid-geometry-check/geometry_check_protocol.md`.

### 3.6 `data/expert_validation/` — expert review

| File | Content |
|---|---|
| `expert_validation_report_{1,2}.md` | Review of all 29 flagged items in the Opus runs (18 E-class flags and 11 geometry-check FAILs), completed by each of the two experts |
| `expert_validation_d_class_report_{1,2}.md` | Review of a random sample of 18 D-class proofs (random seed 42), completed by each of the two experts |
| `to_expert/` | Materials given to the experts: review instructions, all statements, a guide to the *Elements*, and Heath's proofs |

For each item the experts received the AI proof, Heath's proof and the automated analysis. These records are in Chinese, the language in which the review was conducted.

### 3.7 `data/network/` — citation networks

Directed citation networks stored as pickled NetworkX `DiGraph` objects: `Human_Citation_Network.pkl` and `{RunA,RunB,RunC,Fable,GPT}_AI_Citation_Network_Final.pkl`. Nodes are propositions, definitions, common notions and postulates; an edge points from a proposition to each resource it cites. The human network has 525 nodes and 1,889 edges.

The networks can be rebuilt from the citation CSVs in §3.3 without unpickling (see §7).

---

## 4. Pipelines

The proofs of the Claude models (§4.1) were generated with [Claude Code](https://claude.com/claude-code). The GPT-6 Astra proofs were generated separately with GPT-6 Astra (see §5); all proofs, including those of GPT-6 Astra, were then classified and audited with the same Claude Code pipelines (§4.2–4.3). Each folder contains the instructions (`SKILL.md`, `CLAUDE.md` or protocol file), the workflow scripts, and the per-book inputs and outputs.

### 4.1 Proof generation — `euclid-proof-project/` and `euclid-proof-project-fable/`

| Path | Content |
|---|---|
| `SKILL.md` | The full proving protocol followed by every run |
| `CLAUDE.md` | Entry point and output naming conventions (e.g. `Prove Book 5, RunA`) |
| `generate_workflow.py`, `euclid_prove_book.js` | Generate and run the parallel workflow: one isolated sub-agent per proposition |
| `euclid_postprocess.py` (plus `finalize_run.py` for Fable) | Merge per-proposition results into per-book proof files and citation CSVs |
| `data/` | Statements and Heath citations (`.xlsx` and `.json`) |
| `proofs/{Run}_Book{N}/` | One Markdown file per proposition |
| `outputs/` | Per-book proofs, citation CSVs and raw results (`*_results.json`); `agent_timings.csv` records the start time, end time and duration of every sub-agent |

### 4.2 Classification and re-prove — `euclid-classify-auto/`

| Path | Content |
|---|---|
| `classify_protocol.md` | Classification protocol |
| `.claude/workflows/classify-book.js` | Classifies all propositions of one book for one run |
| `.claude/workflows/classify-reprove.js` | Re-proves and re-classifies a confirmed error |
| `run_config.json`, `reprove_config.json` | Run parameters |
| `scripts/preprocess.py`, `scripts/lookup.py`, `scripts/collect_results.py` | Prepare per-proposition inputs, look up statements and proofs, collect outputs |
| `prepared/{Run}/book{N}/` | Prepared inputs |
| `output/{Run}/` | Per-book classification CSVs and reports |

### 4.3 Geometric consistency audit — `euclid-geometry-check/`

| Path | Content |
|---|---|
| `geometry_check_protocol.md` | Audit protocol (point position, betweenness and configuration consistency) |
| `scripts/geometry_check_workflow.js`, `geometry_check_fable_batch.js` | Audit workflows |
| `scripts/geometry_check_reprove.js`, `geometry_check_reprove_batch.js` | Re-prove workflows for FAIL items |
| `scripts/preprocess.py`, `scripts/collect_results.py` | Input preparation and result collection |
| `data/` | AI proofs, Heath proofs and classification results used as inputs |
| `output/{Run}/` | Per-book audit CSVs and reports |

---

## 5. Prompt-robustness experiments (GPT-6 Astra)

To test whether the citation patterns are an artefact of the prompt, we ran three additional full runs (465 propositions each) with GPT-6 Astra, keeping everything else identical to the baseline. Details and results are given in the Supplementary Information (Supplementary Text and Tables S1–S9).

| Folder | Condition |
|---|---|
| `gpt_RunA/` | Baseline prompt (the GPT-6 Astra run analysed in the main text) |
| `gpt_Antiground_RunA/` | **Anti-grounding**: one added instruction asking the model to avoid "building from the ground up" and to prefer citing mature, previously established results; all other prompt text byte-identical to the baseline |
| `gpt_ShuffledTable_RunA/` | **Shuffled resource table**: citable resources provided through an external table in random order instead of an inline list |
| `gpt_ReverseTable_RunA/` | **Reverse-ordered resource table**: as above, with the table rows in reverse order |

Each package has the same layout:

| Path | Content |
|---|---|
| `outputs/` | 13 per-book proof files, 13 citation CSVs (same columns as §3.3) and 13 execution metadata files |
| `proofs/RunA_Book{N}/` | One Markdown file per proposition |
| `runs/RunA_Book{N}/` | Frozen book results (`book_result.json`), run manifest, ordering audit (no forward citations) and save audit |
| `docs/` | Result index, run reports and export audits |
| `PACKAGE_MANIFEST.json` | Size and SHA-256 hash of every file in the package |

The package-level `README.md` files are in Chinese. Raw model session logs, intermediate prompt contexts and credentials are not included; the packages are result snapshots rather than runnable projects. As described in the Supplementary Information, the two resource-table conditions also change how the citable resources are presented, so they differ from the baseline in more than the ordering alone.

---

## 6. Analysis and figures (`analysis/`)

### 6.1 Notebooks

| Notebook | Figure in the paper |
|---|---|
| `basic_stats.ipynb` | Fig. 2 — network size and degree distributions, proof length and proving time |
| `Jaccard_similarity.ipynb` | Fig. 3 — distributions of pairwise Jaccard similarity among AI runs and between AI and human proofs |
| `category_complexity_6panel.ipynb` | Fig. 4 — classification category versus human-proof complexity, and D-class rate |
| `AI-style_6panel.ipynb` | Fig. 5 — citation type composition, citation distance and human-ancestor overlap |

Fig. 1 is a schematic of the experimental pipeline and is not generated by code.

### 6.2 Intermediate tables

| File | Rows | Content |
|---|---|---|
| `final_classification.csv` | 465 | Final category of every proposition in Runs A, B and C |
| `expert_verified_classification.csv` | 465 | Category after expert validation, before re-proving |
| `human_proof_complexity.csv` | 465 | Heath proof length (words), Heath reference count and number of citable resources |
| `degree_statistics_all_models.csv` | 18 | In- and out-degree statistics of every network |
| `topological_generation_distances.csv` | 22,617 | Citation distance in topological generations for every edge, full and theorem-only networks |
| `proof_timings_all_models.csv` | 2,325 | Proving time of every AI proof |
| `ai_proof_wordcounts_all_models.csv` | 2,325 | Word count of every AI proof |

### 6.3 Running the notebooks

Requirements: Python ≥ 3.10 with `pandas`, `numpy`, `scipy`, `matplotlib`, `networkx` and `openpyxl`.

Each notebook defines its input and output folders in its first code cell (`NET_DIR`, `REF_DIR`, `OUT_DIR`, `DATA_DIR`, `THM_DIR`). Set them to the corresponding folders of this repository before running:

| Variable | Folder |
|---|---|
| `NET_DIR` | `data/network/` |
| `REF_DIR` | `data/reference/` |
| `OUT_DIR`, `DATA_DIR` | `analysis/` |
| `THM_DIR` | folder containing the theorem-only networks and `final_classification.csv` |

---

## 7. Quick start

Reproduce the headline numbers of the paper (mean proposition-level Jaccard similarity) directly from the CSV files. Run from the repository root:

```python
import pandas as pd

def citation_sets(path, column):
    df = pd.read_csv(path, dtype={"Proposition": str})
    split = lambda s: set() if pd.isna(s) else {x.strip() for x in str(s).split("|") if x.strip()}
    return dict(zip(df["Proposition"], df[column].map(split)))

def jaccard(a, b):
    return len(a & b) / len(a | b) if (a | b) else 1.0

def mean_jaccard(x, y):
    return sum(jaccard(x[p], y[p]) for p in x) / len(x)

d = "data/citations/"
run_a = citation_sets(d + "RunA_All_Books_AI_vs_Human_Citations_Final.csv", "AI_USED")
run_b = citation_sets(d + "RunB_All_Books_AI_vs_Human_Citations_Final.csv", "AI_USED")
human = citation_sets(d + "RunA_All_Books_AI_vs_Human_Citations_Final.csv", "Human_Refs")

print(f"Opus Run A vs Run B : {mean_jaccard(run_a, run_b):.3f}")   # 0.683
print(f"Opus Run A vs Heath : {mean_jaccard(run_a, human):.3f}")   # 0.374
```

To build a citation network from a CSV instead of loading the pickle files:

```python
import networkx as nx

G = nx.DiGraph()
for prop, cited in run_a.items():
    G.add_edges_from((prop, c) for c in cited)
```

---

## 8. Conventions and caveats

**Identifiers.**

| Type | Format | Example |
|---|---|---|
| Postulate | `P{n}` | `P1`–`P5` |
| Common notion | `CN{n}` | `CN1`–`CN5` |
| Definition | `D{book}.{n}` | `D1.15`, `D7.6` |
| Proposition | `{book}.{n}` | `1.47`, `9.36` |

Book X definitions come in three groups: `D10.1`–`D10.4`, `D10.2.1`–`D10.2.6` and `D10.3.1`–`D10.3.6`.

**Always read identifiers as text.** Spreadsheet software and default CSV readers parse `1.10` or `7.20` as numbers and silently turn them into `1.1` and `7.2`. With pandas, pass `dtype={"Proposition": str}` (or `dtype={"ID": str}` for the reference files).

**Final files.** Files with the suffix `_Final` include post-hoc corrections of identifier normalisation and of individual citation records; these are the versions used in the paper.

**Pickle files.** Only load pickle files from sources you trust. All networks can be rebuilt from the CSV files (§7).

**Absolute paths.** Some run manifests in the `gpt_*` folders contain absolute paths from the original machine. They are kept for provenance only; all files should be accessed through the relative paths of this repository.

---

## 9. Citation and license

If you use these data or code, please cite the paper (<https://arxiv.org/abs/2611.16527>):

```bibtex
@article{li2026aistyle,
  title   = {AI has its own style in mathematical proving},
  author  = {Li, Xiaokai and Zhou, Ziyu and Cheng, Qibin and Wu, Yangcheng and Zeng, An and Fan, Ying},
  journal = {arXiv preprint arXiv:2611.16527},
  year    = {2026},
  url     = {https://arxiv.org/abs/2611.16527}
}
```

**License:** Code (`.py`, `.js` and `.ipynb` files) is released under the MIT License (see [`LICENSE`](LICENSE)). Data, AI-generated proofs, reports and other non-code content are released under CC BY 4.0 (see [`LICENSE-DATA`](LICENSE-DATA)), except the third-party material derived from the Wolfram Data Repository, which remains subject to the terms of its original source.
