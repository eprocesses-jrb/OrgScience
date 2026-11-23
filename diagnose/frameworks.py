FRAMEWORKS = {
    "process_mapping_lean": {
        "targets": {"workflow_process", "capacity_resources"},
        "strength": "Makes end-to-end flow, waiting, rework, and bottlenecks visible.",
        "blind_spot": "May under-address authority, institutional legitimacy, or deep cultural mechanisms."
    },
    "congruence_diagnosis": {
        "targets": {"structure_coordination", "measurement_incentives", "leadership_behavior", "culture_norms"},
        "strength": "Assesses fit among organizational components.",
        "blind_spot": "Depends on the accuracy of the representation of components and relationships."
    },
    "governance_redesign": {
        "targets": {"decision_rights_governance", "structure_coordination"},
        "strength": "Clarifies authority, accountability, interfaces, and escalation.",
        "blind_spot": "Can formalize the wrong causal story if process evidence is weak."
    },
    "capacity_queue_intervention": {
        "targets": {"capacity_resources", "workflow_process"},
        "strength": "Addresses demand-capacity imbalance and accumulation.",
        "blind_spot": "Adding capacity can mask process, incentive, or decision-rights problems."
    },
    "leadership_change": {
        "targets": {"leadership_behavior", "culture_norms"},
        "strength": "Addresses leadership signals, role modeling, communication, and behavioral reinforcement.",
        "blind_spot": "Risks attributing system-produced behavior to individuals."
    },
    "strategy_realignment": {
        "targets": {"environment_strategy", "measurement_incentives", "structure_coordination"},
        "strength": "Reconnects organizational systems to strategic and external requirements.",
        "blind_spot": "May be too high-level for local operating mechanisms."
    },
}

def assess_framework_fit(diagnoses, contingencies):
    results = []
    for name, f in FRAMEWORKS.items():
        diagnostic_support = sum(d.score for d in diagnoses if d.mechanism in f["targets"])
        score = diagnostic_support / max(1, len(f["targets"]))
        # Evidence-quality penalty makes uncertainty explicit.
        evidence_quality = contingencies.get("evidence_quality", "unknown")
        multiplier = {"high": 1.0, "medium": 0.85, "low": 0.65, "unknown": 0.70}[evidence_quality]
        fit = round(min(1.0, score * multiplier), 2)
        results.append({
            "framework": name,
            "conditional_fit": fit,
            "strength": f["strength"],
            "blind_spot": f["blind_spot"],
            "targets": sorted(f["targets"]),
            "status": "candidate_not_prescription"
        })
    return sorted(results, key=lambda x: x["conditional_fit"], reverse=True)
