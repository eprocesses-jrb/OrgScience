import json
from pathlib import Path
from diagnose.pipeline import run
from diagnose.perturb import strip_evidence_labels

ROOT = Path(__file__).resolve().parent

def summarize(result):
    return {
        "case_id": result["case_id"],
        "top_diagnosis": result["rival_diagnoses"][0]["mechanism"],
        "evidence_sufficiency": result["evidence_sufficiency"]["status"],
        "rival_diversity": result["epistemic_performance_measures"]["rival_diagnosis_diversity"],
        "traceability": result["epistemic_performance_measures"]["evidence_traceability"]["diagnosis_reference_coverage"],
        "adc_proxy": result["epistemic_performance_measures"]["artificial_diagnostic_certainty_proxy"]["adc_proxy"],
    }

print("DIAGNOSE v0.4A reviewer demo")
print("=" * 32)

case = json.loads((ROOT / "cases" / "SYN-WF-002.json").read_text())
original = run(case)
ablated = run(strip_evidence_labels(case))

print("\n1. Evidence-typed case")
print(json.dumps(summarize(original), indent=2))

print("\n2. Same case with evidence labels erased")
print(json.dumps(summarize(ablated), indent=2))

insuf = json.loads((ROOT / "cases" / "SYN-INSUF-001.json").read_text())
print("\n3. Insufficient-evidence case")
print(json.dumps(summarize(run(insuf)), indent=2))

outside = json.loads((ROOT / "cases" / "SYN-OUT-001.json").read_text())
print("\n4. Outside-current-ontology case")
print(json.dumps(summarize(run(outside)), indent=2))

print("\nInterpretation:")
print("- The demo is developmental, not a validity test.")
print("- It shows evidence typing, abstention, and ontology escape are executable and auditable.")
print("- Confirmatory claims require independently authored blinded holdouts.")
