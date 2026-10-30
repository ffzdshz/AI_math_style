"""Finalize one Book+Run after the Workflow finished.
Usage: python finalize_run.py <book_num> <run_id> <task_output_json> [workflow_run_id]

Steps (same as done by hand for RunA Book 1):
  1. copy the Workflow task output JSON to proofs/Run{X}_Book{N}_results.json
  2. SKILL.md Step 2.5 checks: out-of-order citations, unknown citation IDs, UNRESOLVED markers, duplicates
  3. run euclid_postprocess.py (Jaccard + the two output files)
  4. append per-agent timings/tokens to outputs/agent_timings.csv
run_id must be a single letter (A/B/C).
"""
import csv, io, json, os, re, shutil, subprocess, sys
from datetime import datetime, timezone

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

def parse_prop(ref):
    m = re.fullmatch(r"(\d+)\.(\d+)", ref)
    return (int(m.group(1)), int(m.group(2))) if m else None

def main():
    book = int(sys.argv[1]); run = sys.argv[2]; src = sys.argv[3]
    if run.lower().startswith("run"):
        raise SystemExit(f"run_id must be a single letter, got {run!r}")
    raw = json.load(io.open(src, encoding="utf-8"))
    res = raw["result"] if isinstance(raw, dict) and "result" in raw else raw
    dst = os.path.join(PROJECT_DIR, "proofs", f"Run{run}_Book{book}_results.json")
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copyfile(src, dst)
    print(f"[1] saved {len(res)} results -> {dst}")

    st = json.load(io.open(os.path.join(PROJECT_DIR, "data", "euclid_statements.json"), encoding="utf-8"))
    expected = sorted([k for k, v in st.items() if v["type"] == "Theorem" and v["book"] == book],
                      key=lambda x: int(x.split(".")[1]))
    ids = sorted([r["prop_id"] for r in res], key=lambda x: int(x.split(".")[1]))
    missing = sorted(set(expected) - set(ids), key=lambda x: int(x.split(".")[1]))
    print(f"[2] propositions: {len(ids)}/{len(expected)}" + (f"  MISSING: {missing}" if missing else "") +
          ("  DUPLICATE IDS" if len(ids) != len(set(ids)) else ""))
    viol, unknown, unresolved, dup = {}, {}, [], []
    for r in res:
        sb, sp = parse_prop(r["prop_id"])
        bad = []
        for u in r["used"]:
            t = parse_prop(u)
            if t and (t[0] > sb or (t[0] == sb and t[1] >= sp)): bad.append(u)
        if bad: viol[r["prop_id"]] = bad
        unk = [u for u in r["used"] if u not in st]
        if unk: unknown[r["prop_id"]] = unk
        if "[UNRESOLVED" in r["proof"]: unresolved.append(r["prop_id"])
        if len(set(r["used"])) != len(r["used"]): dup.append(r["prop_id"])
    print(f"    out-of-order citations: {viol or 'none'}")
    print(f"    unknown citation IDs:   {unknown or 'none'}")
    print(f"    UNRESOLVED markers:     {unresolved or 'none'}")
    print(f"    duplicates in USED:     {dup or 'none'}")
    models = sorted({str(r.get("model")) for r in res}); efforts = sorted({str(r.get("effort")) for r in res})
    print(f"    model(s): {models}  effort(s): {efforts}")
    n = [len(set(r["used"])) for r in res]
    print(f"    USED size: min {min(n)}, mean {sum(n)/len(n):.2f}, max {max(n)}")

    print("[3] post-processing")
    subprocess.run([sys.executable, os.path.join(PROJECT_DIR, "euclid_postprocess.py"), str(book), run, dst], check=True)

    agents = []
    def walk(o):
        if isinstance(o, dict):
            if o.get("type") == "workflow_agent": agents.append(o)
            for v in o.values(): walk(v)
        elif isinstance(o, list):
            for v in o: walk(v)
    walk(raw.get("workflowProgress", {}) if isinstance(raw, dict) else {})
    wf_id = sys.argv[4] if len(sys.argv) > 4 else ""  # optional: workflow run id from the task notification
    m = re.search(r"wf_[0-9a-f]+-[0-9a-f]+", json.dumps(raw.get("logs", "")) + os.path.basename(src)) if isinstance(raw, dict) else None
    if m and not wf_id: wf_id = m.group(0)
    def iso(ms): return datetime.fromtimestamp(ms / 1000, tz=timezone.utc).isoformat()
    rows = []
    for a in agents:
        if a.get("state") != "done" or "startedAt" not in a or "durationMs" not in a: continue
        label = a["label"]; pid = label.split(" ")[0]
        b, p = pid.split(".")
        rows.append({"run": run, "prop_id": pid, "book": int(b), "prop_num": int(p),
                     "duration_s": round(a["durationMs"] / 1000, 1),
                     "start": iso(a["startedAt"]), "end": iso(a["startedAt"] + a["durationMs"]),
                     "wf_id": a.get("wfId") or wf_id or a.get("agentId", ""), "tokens": a.get("tokens"), "label": label})
    rows.sort(key=lambda r: (r["book"], r["prop_num"], r["label"]))
    path = os.path.join(PROJECT_DIR, "outputs", "agent_timings.csv")
    new = not os.path.exists(path)
    with io.open(path, "a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["run", "prop_id", "book", "prop_num", "duration_s", "start", "end", "wf_id", "tokens", "label"])
        if new: w.writeheader()
        w.writerows(rows)
    if rows:
        d = sorted(r["duration_s"] for r in rows); t = [r["tokens"] or 0 for r in rows]
        print(f"[4] timings: {len(rows)} rows appended -> {path}")
        print(f"    duration_s: min {d[0]}, median {d[len(d)//2]}, max {d[-1]} | tokens total {sum(t)}, per agent min {min(t)} max {max(t)}")
        print(f"    slowest: {[(r['prop_id'], r['duration_s']) for r in sorted(rows, key=lambda r: -r['duration_s'])[:3]]}")
        retries = [r["label"] for r in rows if "retry" in r["label"]]
        if retries: print(f"    retry agents: {retries}")
    else:
        print("[4] no per-agent timing data found in task output")

if __name__ == "__main__":
    main()
