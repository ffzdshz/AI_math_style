"""
Quick lookup for statements or Heath proofs by proposition ID.

Usage:
    python lookup.py statement 1.47
    python lookup.py heath_proof 5.16
    python lookup.py statement D1.15
"""

import sys
import json
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
PREPARED_DIR = PROJECT_DIR / 'prepared'


def main():
    if len(sys.argv) < 3:
        print("Usage: python lookup.py <statement|heath_proof> <prop_id> [prop_id2 ...]")
        sys.exit(1)

    lookup_type = sys.argv[1]
    prop_ids = sys.argv[2:]

    if lookup_type == 'statement':
        data = json.loads((PREPARED_DIR / 'statements.json').read_text(encoding='utf-8'))
        for pid in prop_ids:
            entry = data.get(pid)
            if entry:
                print(f"=== {pid} ({entry['type']}) ===")
                print(entry['statement'])
            else:
                print(f"=== {pid}: NOT FOUND ===")
            print()

    elif lookup_type == 'heath_proof':
        data = json.loads((PREPARED_DIR / 'heath_proofs.json').read_text(encoding='utf-8'))
        for pid in prop_ids:
            proof = data.get(pid)
            if proof:
                print(f"=== Heath proof of {pid} ===")
                print(proof)
            else:
                print(f"=== {pid}: NOT FOUND ===")
            print()

    else:
        print(f"Unknown lookup type: {lookup_type}")
        print("Use 'statement' or 'heath_proof'")
        sys.exit(1)


if __name__ == '__main__':
    main()
