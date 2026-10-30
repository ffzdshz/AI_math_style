"""
Collect classification results from agent output JSONs into CSV and Markdown.

Usage:
    python collect_results.py <run_prefix> <book_num>
    python collect_results.py RunA 1

Reads:
    prepared/<run>/book<N>/results/*.json

Produces:
    output/<run>/Book<N>_Classification.csv
    output/<run>/Book<N>_Classification_Report.md
"""

import sys
import os
import json
import csv
from pathlib import Path
from collections import Counter

PROJECT_DIR = Path(__file__).resolve().parent.parent
PREPARED_DIR = PROJECT_DIR / 'prepared'
OUTPUT_DIR = PROJECT_DIR / 'output'

CATEGORY_LABEL = {
    'P': 'Perfect match',
    'G': 'Granularity difference',
    'D': 'Path difference',
    'E': 'AI proof error',
}


def collect(run_prefix: str, book_num):
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

    # Write CSV
    csv_path = out_dir / f'Book{book_num}_Classification.csv'
    fieldnames = ['Proposition', 'Book', 'Category', 'Category_Label',
                  'Error_type', 'Jaccard', 'AI_citations', 'Heath_citations',
                  'AI_only', 'Heath_only']
    with open(csv_path, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in results:
            cat = r.get('category', 'G')
            writer.writerow({
                'Proposition': r['proposition'],
                'Book': book_num,
                'Category': cat,
                'Category_Label': CATEGORY_LABEL.get(cat, cat),
                'Error_type': r.get('error_type', ''),
                'Jaccard': round(r.get('jaccard', 0), 3),
                'AI_citations': r.get('ai_citations', ''),
                'Heath_citations': r.get('heath_citations', ''),
                'AI_only': r.get('ai_only', ''),
                'Heath_only': r.get('heath_only', ''),
            })
    print(f"CSV written: {csv_path}")

    # Write Markdown report
    md_path = out_dir / f'Book{book_num}_Classification_Report.md'
    counts = Counter(r.get('category', 'G') for r in results)
    errors = [r for r in results if r.get('category') == 'E']

    lines = [f'# Book {book_num} — Classification Report ({run_prefix})\n']

    lines.append('## Summary\n')
    lines.append('| Category | Count | Propositions |')
    lines.append('|---|---|---|')
    for cat in ['P', 'G', 'D', 'E']:
        props = [r['proposition'] for r in results if r.get('category') == cat]
        lines.append(f'| {CATEGORY_LABEL[cat]} ({cat}) | {counts.get(cat, 0)} | {", ".join(props)} |')
    lines.append(f'\n**Total**: {len(results)} propositions\n')

    if errors:
        lines.append('## Error Details\n')
        lines.append('| Proposition | Error type | Details |')
        lines.append('|---|---|---|')
        for r in errors:
            lines.append(f'| {r["proposition"]} | {r.get("error_type", "")} | {r.get("audit_record", "").replace(chr(10), " ")[:200]} |')
        lines.append('')

    lines.append('## Per-Proposition Analysis\n')
    for r in results:
        cat = r.get('category', 'G')
        lines.append(f'### {r["proposition"]}')
        lines.append(f'**Category**: {CATEGORY_LABEL.get(cat, cat)}')
        lines.append(f'**Jaccard**: {r.get("jaccard", 0):.3f}')
        lines.append(f'**Analysis**: {r.get("analysis", "")}')
        if r.get('audit_record'):
            lines.append(f'**Audit Record**: {r["audit_record"]}')
        lines.append('')

    md_path.write_text('\n'.join(lines), encoding='utf-8')
    print(f"Report written: {md_path}")

    print(f"\nBook {book_num}: P={counts.get('P',0)} G={counts.get('G',0)} "
          f"D={counts.get('D',0)} E={counts.get('E',0)}  total={len(results)}")


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python collect_results.py <run_prefix> <book_num>")
        sys.exit(1)
    book_arg = sys.argv[2]
    try:
        book_arg = int(book_arg)
    except ValueError:
        pass  # keep as string for non-numeric book identifiers
    collect(sys.argv[1], book_arg)
