import json
from pathlib import Path
from diagnose.benchmark import run_benchmark, aggregate

ROOT = Path(__file__).resolve().parent
rows = run_benchmark(ROOT / "cases")
out = {"aggregate": aggregate(rows), "cases": rows}
(ROOT / "outputs" / "benchmark_results.json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out["aggregate"], indent=2))
