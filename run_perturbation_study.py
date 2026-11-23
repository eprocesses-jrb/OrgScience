import json
from pathlib import Path
from diagnose.pipeline import run
from diagnose.perturb import remove_observations, swap_accepted_explanation, strip_evidence_labels

ROOT = Path(__file__).resolve().parent
cases = [
    json.loads((ROOT / "cases" / "SYN-WF-002.json").read_text()),
    json.loads((ROOT / "cases" / "SYN-LEAD-002.json").read_text()),
    json.loads((ROOT / "cases" / "SYN-INSUF-001.json").read_text()),
]

results = []
for case in cases:
    variants = [
        ("original", case),
        ("25pct_observations_removed", remove_observations(case, 0.25, seed=7)),
        ("accepted_explanation_swapped", swap_accepted_explanation(case, "The cause is uncertain and requires evidence.")),
        ("evidence_labels_removed", strip_evidence_labels(case)),
    ]
    for name, variant in variants:
        out = run(variant)
        results.append({
            "case_id": case["case_id"],
            "variant": name,
            "top_diagnosis": out["rival_diagnoses"][0]["mechanism"],
            "sufficiency": out["evidence_sufficiency"]["status"],
            "diversity": out["epistemic_performance_measures"]["rival_diagnosis_diversity"],
            "adc_proxy": out["epistemic_performance_measures"]["artificial_diagnostic_certainty_proxy"]["adc_proxy"],
        })

(ROOT / "outputs" / "perturbation_results.json").write_text(json.dumps(results, indent=2) + "\n")
print(json.dumps(results, indent=2))
