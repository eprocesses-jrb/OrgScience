import math

QUALITY = {"high": 1.0, "medium": 0.78, "low": 0.52, "unknown": 0.60}

def _norm_scores(diagnoses):
    vals = [max(0.0, float(d.score)) for d in diagnoses]
    total = sum(vals)
    return [v / total for v in vals] if total else [0.0 for _ in vals]

def rival_diagnosis_diversity(diagnoses):
    """Normalized Shannon entropy, 0=concentrated, 1=distributed search."""
    p = [x for x in _norm_scores(diagnoses) if x > 0]
    if len(p) <= 1:
        return 0.0
    h = -sum(x * math.log(x) for x in p)
    return round(h / math.log(len(p)), 3)

def diagnostic_concentration(diagnoses):
    p = _norm_scores(diagnoses)
    return round(max(p) if p else 0.0, 3)

def premature_closure_risk(diagnoses):
    """Prototype structural risk indicator, not a validated psychological measure."""
    if len(diagnoses) < 2:
        return {"risk": "high", "top_margin": 1.0}
    top = diagnoses[0].score
    second = diagnoses[1].score
    margin = round(top - second, 3)
    diversity = rival_diagnosis_diversity(diagnoses)
    # Very concentrated output is treated as closure risk because alternatives have collapsed.
    risk = "high" if diversity < 0.55 else ("medium" if diversity < 0.72 else "low")
    return {"risk": risk, "top_margin": margin, "diversity": diversity}

def evidence_traceability(diagnoses, ledger):
    valid = {e.id for e in ledger}
    referenced = []
    invalid = []
    for d in diagnoses:
        for eid in d.support_evidence_ids:
            (referenced if eid in valid else invalid).append(eid)
    diagnosable = [d for d in diagnoses if d.mechanism != "outside_current_ontology"]
    with_refs = sum(bool(d.support_evidence_ids) for d in diagnosable)
    coverage = with_refs / max(1, len(diagnosable))
    return {
        "diagnosis_reference_coverage": round(coverage, 3),
        "valid_reference_count": len(referenced),
        "invalid_reference_count": len(invalid),
    }

def ground_truth_metrics(diagnoses, case):
    truth = case.get("ground_truth_mechanisms", [])
    ranked = [d.mechanism for d in diagnoses]
    hit1 = bool(truth and ranked and ranked[0] in truth)
    hit3 = bool(truth and any(x in truth for x in ranked[:3]))
    rr = 0.0
    if truth:
        for i, m in enumerate(ranked, start=1):
            if m in truth:
                rr = 1 / i
                break
    return {
        "top1_ground_truth_hit": hit1 if truth else None,
        "top3_ground_truth_hit": hit3 if truth else None,
        "reciprocal_rank_first_true_mechanism": round(rr, 3) if truth else None,
    }

def framework_appropriateness(framework_fit, case):
    truth = set(case.get("ground_truth_mechanisms", []))
    if not truth or not framework_fit:
        return None
    top = framework_fit[0]
    return bool(truth.intersection(set(top.get("targets", []))))

def artificial_diagnostic_certainty_proxy(diagnoses, ledger, contingencies):
    """Exploratory proxy for development only; not yet a validated ADC measure."""
    if not diagnoses:
        return None
    top = diagnoses[0]
    expressed = min(1.0, max(0.0, top.score))
    direct_obs = [e for e in ledger if e.evidence_type == "observation"]
    supported_obs = [e for e in direct_obs if e.id in set(top.support_evidence_ids)]
    support_density = len(supported_obs) / max(1, len(direct_obs))
    warranted_proxy = support_density * QUALITY.get(contingencies.get("evidence_quality", "unknown"), 0.60)
    return {
        "expressed_confidence_proxy": round(expressed, 3),
        "evidence_supported_confidence_proxy": round(warranted_proxy, 3),
        "adc_proxy": round(expressed - warranted_proxy, 3),
        "validation_status": "developmental_not_validated"
    }

def compute_measures(diagnoses, ledger, contingencies, framework_fit, case):
    out = {
        "rival_diagnosis_diversity": rival_diagnosis_diversity(diagnoses),
        "diagnostic_concentration": diagnostic_concentration(diagnoses),
        "premature_closure_risk": premature_closure_risk(diagnoses),
        "evidence_traceability": evidence_traceability(diagnoses, ledger),
        "framework_appropriateness_top1": framework_appropriateness(framework_fit, case),
        "artificial_diagnostic_certainty_proxy": artificial_diagnostic_certainty_proxy(
            diagnoses, ledger, contingencies
        ),
    }
    out.update(ground_truth_metrics(diagnoses, case))
    return out
