def assess_evidence_sufficiency(ledger, diagnoses, case):
    """Transparent *developmental* abstention heuristic. Not validated.

    This uses only input evidence quantity/quality, not benchmark answer keys.
    It deliberately errs toward abstention when evidence is weak and missing
    critical observations, but does not prove causal discriminability.
    """
    observations = [e for e in ledger if e.evidence_type == "observation"]
    missing = [e for e in ledger if e.evidence_type == "missing_evidence"]
    top_ids = set(diagnoses[0].support_evidence_ids) if diagnoses else set()
    direct_support = sum(e.id in top_ids for e in observations)
    quality = case.get("contingencies", {}).get("evidence_quality", "unknown")

    if len(observations) < 2 or direct_support == 0:
        status = "insufficient_evidence"
        reason = "Direct observational support is too sparse for provisional commitment."
    elif quality == "low" and len(missing) >= 3:
        status = "insufficient_evidence"
        reason = "Low declared evidence quality and multiple missing discriminatory observations."
    else:
        status = "provisional_diagnosis_possible"
        reason = "Some direct evidence is present; causal diagnosis remains provisional pending rival tests."

    return {
        "status": status,
        "reason": reason,
        "direct_observations": len(observations),
        "missing_evidence_items": len(missing),
        "validation_status": "developmental_not_validated",
    }
