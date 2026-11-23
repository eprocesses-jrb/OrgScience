import argparse, json
from pathlib import Path
from .pipeline import run

def main():
    p = argparse.ArgumentParser(description="Run the DIAGNOSE proof-of-concept pipeline.")
    p.add_argument("case", help="Path to a case JSON file")
    p.add_argument("--out", help="Output JSON path")
    args = p.parse_args()
    case = json.loads(Path(args.case).read_text())
    result = run(case)
    text = json.dumps(result, indent=2)
    if args.out:
        Path(args.out).write_text(text + "\n")
    else:
        print(text)

if __name__ == "__main__":
    main()
