import json
from pathlib import Path
from .pipeline import run

def run_benchmark(cases_dir):
    rows = []
    for p in sorted(Path(cases_dir).glob("*.json")):
        case = json.loads(p.read_text())
        result = run(case)
        m = result["epistemic_performance_measures"]
        truth = case.get("ground_truth_mechanisms", [])
        is_insufficient = "insufficient_evidence" in truth
        rows.append({
            "case_id": result["case_id"],
            "top_diagnosis": result["rival_diagnoses"][0]["mechanism"],
            "sufficiency_status": result["evidence_sufficiency"]["status"],
            "insufficient_truth": is_insufficient,
            "insufficient_correct": (result["evidence_sufficiency"]["status"] == "insufficient_evidence") if is_insufficient else None,
            "top1_hit": None if is_insufficient else m["top1_ground_truth_hit"],
            "top3_hit": None if is_insufficient else m["top3_ground_truth_hit"],
            "rr": None if is_insufficient else m["reciprocal_rank_first_true_mechanism"],
            "diversity": m["rival_diagnosis_diversity"],
            "traceability": m["evidence_traceability"]["diagnosis_reference_coverage"],
            "adc_proxy": m["artificial_diagnostic_certainty_proxy"]["adc_proxy"],
            "framework_top1_appropriate": None if is_insufficient else m["framework_appropriateness_top1"],
        })
    return rows

def aggregate(rows):
    def mean_bool(key):
        vals = [1.0 if r[key] else 0.0 for r in rows if r[key] is not None]
        return round(sum(vals)/len(vals), 3) if vals else None
    def mean_num(key):
        vals = [float(r[key]) for r in rows if r[key] is not None]
        return round(sum(vals)/len(vals), 3) if vals else None
    return {
        "n_cases": len(rows),
        "n_accuracy_cases": sum(r["top1_hit"] is not None for r in rows),
        "n_insufficient_evidence_cases": sum(r["insufficient_truth"] for r in rows),
        "top1_accuracy": mean_bool("top1_hit"),
        "top3_accuracy": mean_bool("top3_hit"),
        "mean_reciprocal_rank": mean_num("rr"),
        "mean_rival_diversity": mean_num("diversity"),
        "mean_traceability_coverage": mean_num("traceability"),
        "mean_adc_proxy": mean_num("adc_proxy"),
        "top_framework_appropriateness": mean_bool("framework_top1_appropriate"),
        "insufficient_evidence_accuracy": mean_bool("insufficient_correct"),
    }
