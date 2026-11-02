# AI Has Its Own Style in Mathematical Proving

Data and analysis code for the paper:

> **AI has its own style in mathematical proving**
> Xiaokai Li, Ziyu Zhou, Qibin Cheng, Yangcheng Wu, An Zeng, Ying Fan

## Overview

We asked three large language models to independently reprove all 465 propositions of Euclid's *Elements* and compared their citation choices against Heath's human-proof baseline through Jaccard similarity and complex network analysis. This repository contains the complete AI-generated proof texts, citation data, classification results, expert validation records, and analysis scripts.

## Data format

### Citation comparison CSV

Each row corresponds to one proposition. Key columns:

| Column | Description |
|--------|-------------|
| `Proposition` | Proposition identifier (e.g. `1.47`) |
| `AI_USED` | AI citation set, pipe-separated (e.g. `1.4\|1.5\|CN1`) |
| `Human_Refs` | Human citation set, pipe-separated |
| `Shared` | Citations common to both |
| `AI_Only_Extra` | Citations used only by AI |
| `Human_Only_Missing` | Citations used only by human |
| `Jaccard` | Jaccard similarity coefficient |

### Citation identifiers

- Postulates: `P1`–`P5`
- Common notions: `CN1`–`CN5`
- Definitions: `D{book}.{number}` (e.g. `D1.15`, `D10.2.1`)
- Propositions: `{book}.{number}` (e.g. `1.47`, `9.36`)

### Citation networks

Directed graphs stored as Python `pickle` files (NetworkX `DiGraph`). Nodes represent propositions, definitions, common notions, or postulates; directed edges point from each proposition to the elements it cites.

### Classification categories

| Code | Category | Description |
|------|----------|-------------|
| P | Perfect match | Citation set identical to Heath's |
| G | Granularity difference | Same proof backbone, different citation depth |
| D | Path difference | Valid alternative proof route |
| E | Error | Positively identifiable logical defect |

## Source data

The structured Euclid dataset is from the [Wolfram Data Repository](https://datarepository.wolframcloud.com/resources/Structure-of-Euclids-Elements/).
}
```

## License

To be added.
