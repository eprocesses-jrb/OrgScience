from .models import Diagnosis

MECHANISMS = {
    "workflow_process": {
        "terms": ["handoff","queue","backlog","cycle time","workflow","rework","waiting","sequence","bottleneck","routing"],
        "tests": ["Directly observe end-to-end work flow and measure waiting versus touch time.",
                  "Test whether removing or resequencing handoffs changes throughput."]
    },
    "structure_coordination": {
        "terms": ["silo","boundary","cross-functional","coordination","unit","department","fragmented","interface"],
        "tests": ["Map dependencies across formal units and compare them with actual coordination paths.",
                  "Test whether failures cluster at organizational boundaries."]
    },
    "decision_rights_governance": {
        "terms": ["approval","authority","decision","escalation","permission","governance","sign-off","veto"],
        "tests": ["Trace who has formal and de facto authority at each decision point.",
                  "Test whether delays persist after decision rights are clarified."]
    },
    "measurement_incentives": {
        "terms": ["metric","target","quota","incentive","performance","utilization","productivity","bonus","scorecard"],
        "tests": ["Compare local performance measures with system-level outcomes.",
                  "Test whether behavior changes when the contested measure is removed or redesigned."]
    },
    "capacity_resources": {
        "terms": ["capacity","staff","staffing","resource","volume","demand","load","workload","shortage","vacancy"],
        "tests": ["Estimate demand, effective capacity, variability, and queue accumulation.",
                  "Test whether additional capacity reduces the focal failure after process constraints are held constant."]
    },
    "leadership_behavior": {
        "terms": ["leader","manager","supervisor","leadership","communication","priority","accountability","sponsor"],
        "tests": ["Compare espoused leadership priorities with observed allocation and escalation decisions.",
                  "Test whether behavior changes when leadership signals are held constant but system constraints change."]
    },
    "culture_norms": {
        "terms": ["culture","norm","trust","fear","identity","values","psychological","informal","taboo"],
        "tests": ["Seek repeated behavioral evidence of the proposed norm across settings and actors.",
                  "Test rival structural explanations for behavior attributed to culture."]
    },
    "environment_strategy": {
        "terms": ["customer","market","regulation","supplier","strategy","competitive","external","policy","mandate"],
        "tests": ["Separate externally imposed constraints from internally generated constraints.",
                  "Test whether similar units facing the same external conditions show different outcomes."]
    },
}

EVIDENCE_WEIGHTS = {
    "observation": 1.00,
    "participant_claim": 0.45,
    "interpretation": 0.35,
    "assumption": 0.15,
    "missing_evidence": 0.00,
}

def _evidence_hits(ledger, terms):
    evidence_ids, hits, weighted_signal = [], [], 0.0
    for e in ledger:
        low = e.text.lower()
        matched = [t for t in terms if t in low]
        if matched:
            evidence_ids.append(e.id)
            hits.extend(matched)
            weighted_signal += EVIDENCE_WEIGHTS.get(e.evidence_type, 0.25) * len(matched)
    return list(dict.fromkeys(evidence_ids)), list(dict.fromkeys(hits)), weighted_signal

def generate_rival_diagnoses(case, ledger):
    diagnoses = []
    for mechanism, spec in MECHANISMS.items():
        evidence_ids, hits, weighted_signal = _evidence_hits(ledger, spec["terms"])
        score = 0.08 + min(0.78, 0.095 * weighted_signal + 0.015 * len(evidence_ids))
        rationale = ([f"Weighted evidence signals: {', '.join(hits[:6])}."]
                     if hits else ["No direct coded signal; retained as a rival explanation."])
        diagnoses.append(Diagnosis(
            mechanism=mechanism,
            score=round(score, 3),
            rationale=rationale,
            support_evidence_ids=evidence_ids,
            disconfirming_evidence_needed=spec["tests"],
            ontology_status="in_ontology",
        ))

    open_ids = []
    for e in ledger:
        if any(term in e.text.lower() for term in case.get("unclassified_signals", [])):
            open_ids.append(e.id)
    max_known = max(d.score for d in diagnoses) if diagnoses else 0
    sparse_known_support = sum(bool(d.support_evidence_ids) for d in diagnoses) <= 2
    open_score = 0.10
    if open_ids:
        open_score = 0.62
    elif sparse_known_support or max_known < 0.26:
        open_score = 0.38

    diagnoses.append(Diagnosis(
        mechanism="outside_current_ontology",
        score=round(open_score, 3),
        rationale=["Open-class rival retained to prevent the ontology from becoming a closed explanatory world."],
        support_evidence_ids=open_ids,
        disconfirming_evidence_needed=[
            "Ask independent experts for mechanisms not represented in the current taxonomy.",
            "Run an unconstrained diagnosis and compare emergent mechanisms with the fixed ontology."
        ],
        ontology_status="open_class",
    ))
    diagnoses.sort(key=lambda d: d.score, reverse=True)
    return diagnoses
