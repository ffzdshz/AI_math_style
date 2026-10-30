"""
Preprocess: extract D-category propositions from geometric books for geometry check.

Usage:
    python preprocess.py <run_prefix> <book_num> [--categories D,G]
    python preprocess.py RunA 1
    python preprocess.py RunA 3 --categories D

Reads:
    data/classification_results/<run>_All_Books_Classification.csv
    data/ai_proofs/<run>_All_Books_StepByStep_Proofs.md
    data/heath_proofs/Euclid_Heath_Proofs.xlsx  (optional)

Produces:
    prepared/<run>/book<N>/manifest.json
    prepared/<run>/book<N>/<prop_id>.json   (per-proposition data)
"""

import sys
import os
import re
import json
import csv
import argparse
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / 'data'
PREPARED_DIR = PROJECT_DIR / 'prepared'

GEOMETRIC_BOOKS = {1, 3, 4, 6, 11, 12}


def parse_ai_proof_texts(path: Path) -> dict:
    text = path.read_text(encoding='utf-8')
    result = {}
    blocks = re.split(r'\n## Proposition ', text)
    for block in blocks[1:]:
        m_id = re.match(r'(\d+\.\d+)', block)
        if not m_id:
            continue
        pid = m_id.group(1)
        result[pid] = f"## Proposition {block.strip()}"
    return result


def load_classification(run_prefix: str) -> dict:
    csv_path = DATA_DIR / 'classification_results' / f'{run_prefix}_All_Books_Classification.csv'
    if not csv_path.exists():
        raise FileNotFoundError(f"Classification CSV not found: {csv_path}")

    results = {}
    with open(csv_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            prop = row['Proposition']
            results[prop] = {
                'book': int(row['Book']),
                'category': row['Category'],
                'category_label': row.get('Category_Label', ''),
                'error_type': row.get('Error_type', ''),
                'jaccard': float(row.get('Jaccard', 0)),
            }
    return results


def load_heath_proofs() -> dict:
    xlsx_path = DATA_DIR / 'heath_proofs' / 'Euclid_Heath_Proofs.xlsx'
    if not xlsx_path.exists():
        print(f"  WARNING: Heath proofs xlsx not found at {xlsx_path}, skipping.")
        return {}
    try:
        import openpyxl
        wb = openpyxl.load_workbook(xlsx_path, read_only=True, data_only=True)
        ws = wb.active
        headers = [cell.value for cell in next(ws.iter_rows(min_row=1, max_row=1))]
        id_col = headers.index('ID') if 'ID' in headers else 0
        proof_col = headers.index('Proof') if 'Proof' in headers else 1

        proofs = {}
        for row in ws.iter_rows(min_row=2, values_only=True):
            pid = str(row[id_col]) if row[id_col] else ''
            proof = str(row[proof_col]) if row[proof_col] else ''
            if pid:
                proofs[pid] = proof
        wb.close()
        return proofs
    except ImportError:
        print("  WARNING: openpyxl not installed, skipping Heath proofs.")
        return {}
    except Exception as e:
        print(f"  WARNING: Failed to load Heath proofs: {e}")
        return {}


def prepare_book(run_prefix: str, book_num: int, categories: set):
    print(f"\nPreparing {run_prefix} Book {book_num} (categories: {', '.join(sorted(categories))})...")

    if book_num not in GEOMETRIC_BOOKS:
        print(f"  WARNING: Book {book_num} is not a geometric book. Geometric books: {sorted(GEOMETRIC_BOOKS)}")

    classifications = load_classification(run_prefix)

    target_props = sorted(
        [pid for pid, info in classifications.items()
         if info['book'] == book_num and info['category'] in categories],
        key=lambda x: int(x.split('.')[1])
    )

    if not target_props:
        print(f"  No propositions found for Book {book_num} with categories {categories}")
        return

    print(f"  Found {len(target_props)} propositions: {', '.join(target_props)}")

    md_path = DATA_DIR / 'ai_proofs' / f'{run_prefix}_All_Books_StepByStep_Proofs.md'
    if not md_path.exists():
        for alt in (DATA_DIR / 'ai_proofs').glob(f'{run_prefix}*StepByStep*.md'):
            md_path = alt
            break
    if not md_path.exists():
        raise FileNotFoundError(f"AI proofs markdown not found for {run_prefix}")

    ai_texts = parse_ai_proof_texts(md_path)
    heath_proofs = load_heath_proofs()

    out_dir = PREPARED_DIR / run_prefix / f'book{book_num}'
    out_dir.mkdir(parents=True, exist_ok=True)

    manifest = {
        'run': run_prefix,
        'book': book_num,
        'categories': sorted(categories),
        'propositions': target_props,
    }
    (out_dir / 'manifest.json').write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')

    missing_proofs = []
    for pid in target_props:
        cls_info = classifications[pid]
        ai_text = ai_texts.get(pid, '')
        if not ai_text:
            missing_proofs.append(pid)

        prop_data = {
            'proposition': pid,
            'book': book_num,
            'run': run_prefix,
            'current_category': cls_info['category'],
            'ai_proof_text': ai_text,
            'heath_proof_text': heath_proofs.get(pid, ''),
        }
        prop_file = out_dir / f'{pid}.json'
        prop_file.write_text(
            json.dumps(prop_data, ensure_ascii=False, indent=2), encoding='utf-8')

    if missing_proofs:
        print(f"  WARNING: Missing AI proof text for: {', '.join(missing_proofs)}")

    print(f"  Prepared {len(target_props)} propositions → {out_dir}")
    print(f"  Manifest: {out_dir / 'manifest.json'}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Preprocess propositions for geometry check')
    parser.add_argument('run', help='Run prefix (RunA, RunB, RunC)')
    parser.add_argument('book', type=int, help='Book number')
    parser.add_argument('--categories', default='D',
                        help='Comma-separated categories to include (default: D)')
    args = parser.parse_args()

    categories = set(args.categories.split(','))
    prepare_book(args.run, args.book, categories)
    print("\nDone.")
