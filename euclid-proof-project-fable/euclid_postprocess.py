"""Post-processing for Euclid proof workflow results.
Usage: python euclid_postprocess.py <book_num> <run_id> <results_json>

run_id: A, B, or C
Outputs go to ./outputs/ as RunX_BookN_StepByStep_Proofs.md and RunX_BookN_AI_vs_Human_Citations.csv
"""
import sys
import json
import csv
import os

def jaccard(a, b):
    sa, sb = set(a), set(b)
    if not sa and not sb:
        return 1.0
    if not sa or not sb:
        return 0.0
    return len(sa & sb) / len(sa | sb)

def main():
    book_num = int(sys.argv[1])
    run_id = sys.argv[2]
    results_json = sys.argv[3]

    project_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(project_dir, "data")
    output_dir = os.path.join(project_dir, "outputs")
    os.makedirs(output_dir, exist_ok=True)

    with open(results_json, "r", encoding="utf-8") as f:
        raw = json.load(f)
    results = raw["result"] if isinstance(raw, dict) and "result" in raw else raw

    with open(os.path.join(data_dir, "euclid_human_refs.json"), "r", encoding="utf-8") as f:
        all_human_refs = json.load(f)

    with open(os.path.join(data_dir, "euclid_statements.json"), "r", encoding="utf-8") as f:
        statements = json.load(f)

    human_refs_book = {k: v for k, v in all_human_refs.items() if k.startswith(f"{book_num}.")}

    prefix = f"Run{run_id}_Book{book_num}"

    md_lines = [f"# Book {book_num} of Euclid's Elements — Step-by-Step AI Proofs (Run {run_id})\n"]
    csv_rows = []

    for r in sorted(results, key=lambda x: int(x["prop_id"].split(".")[1])):
        pid = r["prop_id"]
        stmt = r["statement"]
        proof = r["proof"]
        ai_used = r["used"]
        hrefs = human_refs_book.get(pid, [])
        j = jaccard(ai_used, hrefs)
        ai_s, h_s = set(ai_used), set(hrefs)

        shared = sorted(ai_s & h_s)
        ai_only = sorted(ai_s - h_s)
        human_only = sorted(h_s - ai_s)

        if j == 1.0:
            divergence = "Perfect match."
        else:
            parts = []
            if ai_only:
                parts.append(f"AI adds {ai_only}")
            if human_only:
                parts.append(f"Human adds {human_only}")
            divergence = "; ".join(parts)

        md_lines.append(f"## Proposition {pid}")
        md_lines.append(f"**Statement:** {stmt}\n")
        for line in proof.strip().split("\n"):
            md_lines.append(line)
        md_lines.append(f"\n**USED:** {', '.join(sorted(ai_s))}")
        md_lines.append(f"**Human refs (from References field):** {', '.join(sorted(h_s))}")
        md_lines.append(f"**Jaccard:** {j:.3f} — {divergence}\n")

        csv_rows.append({
            "Proposition": pid,
            "Statement": stmt[:120].replace('"', "'").replace("\n", " "),
            "AI_USED": "|".join(sorted(ai_s)),
            "Human_Refs": "|".join(sorted(h_s)),
            "Shared": "|".join(shared),
            "AI_Only_Extra": "|".join(ai_only),
            "Human_Only_Missing": "|".join(human_only),
            "Jaccard": round(j, 3),
            "n_AI": len(ai_s),
            "n_Human": len(h_s),
            "n_Shared": len(shared),
            "Proof_Summary": proof[:200].replace("\n", " "),
        })

    md_path = os.path.join(output_dir, f"{prefix}_StepByStep_Proofs.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))

    csv_path = os.path.join(output_dir, f"{prefix}_AI_vs_Human_Citations.csv")
    with open(csv_path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=list(csv_rows[0].keys()))
        writer.writeheader()
        writer.writerows(csv_rows)

    mean_j = sum(r["Jaccard"] for r in csv_rows) / len(csv_rows)
    perfect = sum(1 for r in csv_rows if r["Jaccard"] == 1.0)
    print(f"\n=== Run {run_id} | Book {book_num} ===")
    print(f"  Mean Jaccard: {mean_j:.4f}")
    print(f"  Perfect matches: {perfect}/{len(csv_rows)}")
    print(f"  {md_path}")
    print(f"  {csv_path}")

    diverged = [r for r in csv_rows if r["Jaccard"] < 1.0]
    if diverged:
        print(f"\n  Divergences ({len(diverged)}):")
        for r in diverged:
            print(f"    {r['Proposition']}: J={r['Jaccard']:.3f}"
                  f"  extra=[{r['AI_Only_Extra']}]"
                  f"  missing=[{r['Human_Only_Missing']}]")

if __name__ == "__main__":
    main()
