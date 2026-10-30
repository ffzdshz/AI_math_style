"""
Preprocess Euclid data files into per-proposition JSON for workflow agents.

Usage:
    python preprocess.py <run_prefix> <book_num>
    python preprocess.py RunA 1

Produces:
    prepared/statements.json        — all 607 statements (created once)
    prepared/heath_proofs.json       — all Heath proof texts (created once)
    prepared/<run>/book<N>/manifest.json   — list of prop IDs
    prepared/<run>/book<N>/<prop_id>.json  — per-proposition data
"""

import sys
import os
import re
import json
import pandas as pd
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / 'data'
PREPARED_DIR = PROJECT_DIR / 'prepared'

STMTS_XLSX = DATA_DIR / 'Euclid_All_Statements.xlsx'
HEATH_XLSX = DATA_DIR / 'Euclid_Heath_Proofs.xlsx'


def prepare_statements():
    out = PREPARED_DIR / 'statements.json'
    if out.exists():
        return json.loads(out.read_text(encoding='utf-8'))
    df = pd.read_excel(STMTS_XLSX, dtype={'ID': str})
    BOOK_NAME_TO_NUM = {
        'Book I': 1, 'Book II': 2, 'Book III': 3, 'Book IV': 4,
        'Book V': 5, 'Book VI': 6, 'Book VII': 7, 'Book VIII': 8,
        'Book IX': 9, 'Book X': 10, 'Book XI': 11, 'Book XII': 12, 'Book XIII': 13,
    }
    stmts = {}
    for _, row in df.iterrows():
        book_val = row['Book'] if not pd.isna(row['Book']) else ''
        book_num = BOOK_NAME_TO_NUM.get(str(book_val).strip(), 0)
        stmts[row['ID']] = {
            'type': row['Type'],
            'book': book_num,
            'statement': str(row['Statement']) if not pd.isna(row['Statement']) else '',
        }
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(stmts, ensure_ascii=False, indent=1), encoding='utf-8')
    print(f"  statements.json: {len(stmts)} entries")
    return stmts


def prepare_heath_proofs():
    out = PREPARED_DIR / 'heath_proofs.json'
    if out.exists():
        return json.loads(out.read_text(encoding='utf-8'))
    df = pd.read_excel(HEATH_XLSX, dtype={'ID': str})
    proofs = {}
    for _, row in df.iterrows():
        pid = str(row['ID'])
        proof = '' if pd.isna(row['Proof']) else str(row['Proof'])
        proofs[pid] = proof
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(proofs, ensure_ascii=False, indent=1), encoding='utf-8')
    print(f"  heath_proofs.json: {len(proofs)} entries")
    return proofs


def parse_ai_proof_texts(path: Path) -> dict:
    text = path.read_text(encoding='utf-8')
    result = {}
    blocks = re.split(r'\n## Proposition ', text)
    for block in blocks[1:]:
        m_id = re.match(r'(\d+\.\d+)', block)
        if not m_id:
            continue
        pid = m_id.group(1)
        result[pid] = block.strip()
    return result


def load_citations(run_prefix: str) -> dict:
    csv_path = DATA_DIR / f'{run_prefix}_All_Books_AI_vs_Human_Citations.csv'
    if not csv_path.exists():
        xlsx_path = DATA_DIR / f'{run_prefix}_All_Books_AI_vs_Human_Citations.xlsx'
        if xlsx_path.exists():
            df = pd.read_excel(xlsx_path, dtype={'Proposition': str})
        else:
            raise FileNotFoundError(f"Cannot find citations file for {run_prefix}")
    else:
        df = pd.read_csv(csv_path, dtype={'Proposition': str})

    cits = {}
    for _, r in df.iterrows():
        prop = str(r['Proposition'])

        def split_pipe(val):
            if pd.isna(val) or str(val).strip() in ('', 'nan'):
                return []
            return [x.strip() for x in str(val).split('|') if x.strip()]

        cits[prop] = {
            'ai_used': split_pipe(r.get('AI_USED', '')),
            'heath_refs': split_pipe(r.get('Human_Refs', '')),
            'ai_only': split_pipe(r.get('AI_Only_Extra', '')),
            'heath_only': split_pipe(r.get('Human_Only_Missing', '')),
            'jaccard': float(r.get('Jaccard', 0)),
            'proof_summary': str(r.get('Proof_Summary', '')) if not pd.isna(r.get('Proof_Summary', '')) else '',
        }
    return cits


def prepare_book(run_prefix: str, book_num: int):
    print(f"\nPreparing {run_prefix} Book {book_num}...")

    stmts = prepare_statements()
    heath_proofs = prepare_heath_proofs()

    md_path = DATA_DIR / f'{run_prefix}_All_Books_StepByStep_Proofs.md'
    if not md_path.exists():
        # try alternative naming
        for alt in DATA_DIR.glob(f'{run_prefix}*StepByStep*.md'):
            md_path = alt
            break
    ai_texts = parse_ai_proof_texts(md_path)

    cits = load_citations(run_prefix)

    book_prefix = f'{book_num}.'
    props = sorted(
        [pid for pid in cits if pid.startswith(book_prefix)],
        key=lambda x: int(x.split('.')[1])
    )

    if not props:
        print(f"  WARNING: No propositions found for Book {book_num}")
        return

    out_dir = PREPARED_DIR / run_prefix / f'book{book_num}'
    out_dir.mkdir(parents=True, exist_ok=True)

    manifest = {'run': run_prefix, 'book': book_num, 'propositions': props}
    (out_dir / 'manifest.json').write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')

    for pid in props:
        cit = cits.get(pid, {})
        prop_data = {
            'proposition': pid,
            'book': book_num,
            'statement': stmts.get(pid, {}).get('statement', ''),
            'heath_proof': heath_proofs.get(pid, ''),
            'ai_proof_text': ai_texts.get(pid, ''),
            'ai_used': cit.get('ai_used', []),
            'heath_refs': cit.get('heath_refs', []),
            'ai_only': cit.get('ai_only', []),
            'heath_only': cit.get('heath_only', []),
            'jaccard': cit.get('jaccard', 0),
            'proof_summary': cit.get('proof_summary', ''),
        }
        prop_file = out_dir / f'{pid}.json'
        prop_file.write_text(
            json.dumps(prop_data, ensure_ascii=False, indent=2), encoding='utf-8')

    print(f"  Prepared {len(props)} propositions: {props[0]} .. {props[-1]}")
    print(f"  Output dir: {out_dir}")


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python preprocess.py <run_prefix> <book_num>")
        print("       python preprocess.py RunA 1")
        sys.exit(1)

    run_prefix = sys.argv[1]
    book_num = int(sys.argv[2])
    prepare_book(run_prefix, book_num)
    print("\nDone.")
