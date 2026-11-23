from .evidence import build_evidence_ledger
from .agents import generate_rival_diagnoses
from .contingencies import classify_contingencies
from .frameworks import assess_framework_fit
from .audit import adversarial_audit
from .measures import compute_measures
from .sufficiency import assess_evidence_sufficiency
from .models import serialise

def run(case):
    ledger = build_evidence_ledger(case)
    diagnoses = generate_rival_diagnoses(case, ledger)
    contingencies = classify_contingencies(case)
    fits = assess_framework_fit(diagnoses, contingencies)
    audit = adversarial_audit(case, ledger, diagnoses, fits)
    sufficiency = assess_evidence_sufficiency(ledger, diagnoses, case)
    measures = compute_measures(diagnoses, ledger, contingencies, fits, case)
    return {
        "case_id": case.get("case_id", "unknown"),
        "accepted_explanation": case.get("accepted_explanation"),
        "epistemic_rule": "Accepted explanations and formal representations are hypotheses until tested against operating evidence.",
        "ground_truth_mechanisms": case.get("ground_truth_mechanisms", []),
        "evidence_ledger": serialise(ledger),
        "rival_diagnoses": serialise(diagnoses),
        "evidence_sufficiency": sufficiency,
        "contingencies": contingencies,
        "framework_fit": fits,
        "adversarial_audit": serialise(audit),
        "epistemic_performance_measures": measures,
        "human_adjudication": {
            "status": "pending",
            "instructions": "Accept/reject/modify diagnoses; record confidence, reasoning, requested evidence, and whether evidence is sufficient to commit."
        }
    }
