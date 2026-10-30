"""
Collect geometry check results into CSV and Markdown report.

Usage:
    python collect_results.py <run_prefix> <book_num>
    python collect_results.py RunA 1

Reads:
    prepared/<run>/book<N>/results/*.json

Produces:
    output/<run>/Book<N>_GeometryCheck.csv
    output/<run>/Book<N>_GeometryCheck_Report.md
"""

import sys
import json
import csv
from pathlib import Path
from collections import Counter

PROJECT_DIR = Path(__file__).resolve().parent.parent
PREPARED_DIR = PROJECT_DIR / 'prepared'
OUTPUT_DIR = PROJECT_DIR / 'output'


def collect(run_prefix: str, book_num: int):
    results_dir = PREPARED_DIR / run_prefix / f'book{book_num}' / 'results'
    if not results_dir.exists():
        print(f"No results directory found: {results_dir}")
        return

    results = []
    for f in sorted(results_dir.glob('*.json')):
        try:
            data = json.loads(f.read_text(encoding='utf-8'))
            results.append(data)
        except Exception as e:
            print(f"  WARNING: Failed to read {f.name}: {e}")

    if not results:
        print("No results found.")
        return

    results.sort(key=lambda r: (int(r['proposition'].split('.')[0]),
                                 int(r['proposition'].split('.')[1])))

    out_dir = OUTPUT_DIR / run_prefix
    out_dir.mkdir(parents=True, exist_ok=True)

    csv_path = out_dir / f'Book{book_num}_GeometryCheck.csv'
    fieldnames = [
        'Proposition', 'Book', 'Run', 'Current_Category', 'Verdict',
        'Contradictory_Steps', 'Contradiction_Summary', 'Fixable',
    ]
    with open(csv_path, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in results:
            steps = r.get('contradictory_steps', [])
            if isinstance(steps, list):
                steps = ' | '.join(steps)
            writer.writerow({
                'Proposition': r.get('proposition', ''),
                'Book': r.get('book', book_num),
                'Run': r.get('run', run_prefix),
                'Current_Category': r.get('current_category', ''),
                'Verdict': r.get('verdict', ''),
                'Contradictory_Steps': steps,
                'Contradiction_Summary': r.get('contradiction', ''),
                'Fixable': r.get('fixable', ''),
            })
    print(f"CSV written: {csv_path}")

    md_path = out_dir / f'Book{book_num}_GeometryCheck_Report.md'
    counts = Counter(r.get('verdict', 'UNKNOWN') for r in results)

    lines = [f'# Book {book_num} — Geometry Configuration Check ({run_prefix})\n']

    lines.append('## Summary\n')
    lines.append(f'**Total propositions checked**: {len(results)}\n')
    lines.append('| Verdict | Count | Propositions |')
    lines.append('|---|---|---|')
    for verdict in ['PASS', 'FAIL', 'SKIP']:
        props = [r['proposition'] for r in results if r.get('verdict') == verdict]
        lines.append(f'| {verdict} | {counts.get(verdict, 0)} | {", ".join(props)} |')
    lines.append('')

    fails = [r for r in results if r.get('verdict') == 'FAIL']
    if fails:
        lines.append('## Detected Contradictions\n')
        for r in fails:
            lines.append(f'### Proposition {r["proposition"]}\n')
            steps = r.get('contradictory_steps', [])
            if isinstance(steps, list):
                steps = ', '.join(steps)
            lines.append(f'**Contradictory steps**: {steps}\n')

            sc1 = r.get('spatial_claim_1', {})
            sc2 = r.get('spatial_claim_2', {})
            if sc1:
                lines.append(f'**Spatial claim 1** ({sc1.get("step", "")}): {sc1.get("claim", "")}')
                lines.append(f'  - Required by: {sc1.get("required_by", "")}\n')
            if sc2:
                lines.append(f'**Spatial claim 2** ({sc2.get("step", "")}): {sc2.get("claim", "")}')
                lines.append(f'  - Required by: {sc2.get("required_by", "")}\n')

            lines.append(f'**Contradiction**: {r.get("contradiction", "")}\n')
            lines.append(f'**Fixable**: {r.get("fixable", "")}')
            if r.get('fix_note'):
                lines.append(f'  - {r["fix_note"]}')
            lines.append('')

    passes = [r for r in results if r.get('verdict') == 'PASS']
    if passes:
        lines.append('## Passed Propositions\n')
        for r in passes:
            lines.append(f'- **{r["proposition"]}**: {r.get("pass_reason", "All spatial claims mutually consistent.")}')
        lines.append('')

    skips = [r for r in results if r.get('verdict') == 'SKIP']
    if skips:
        lines.append('## Skipped Propositions\n')
        for r in skips:
            lines.append(f'- **{r["proposition"]}**: {r.get("skip_reason", "No significant geometric configuration claims.")}')
        lines.append('')

    md_path.write_text('\n'.join(lines), encoding='utf-8')
    print(f"Report written: {md_path}")

    print(f"\nBook {book_num} ({run_prefix}): "
          f"PASS={counts.get('PASS', 0)} FAIL={counts.get('FAIL', 0)} "
          f"SKIP={counts.get('SKIP', 0)}  total={len(results)}")


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python collect_results.py <run_prefix> <book_num>")
        sys.exit(1)
    collect(sys.argv[1], int(sys.argv[2]))
