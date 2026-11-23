from .models import AuditFinding

def adversarial_audit(case, ledger, diagnoses, framework_fit):
    findings = []
    accepted = case.get("accepted_explanation", "").strip()
    if accepted:
        findings.append(AuditFinding(
            issue="accepted_explanation_present",
            severity="medium",
            explanation="The case arrives with an accepted explanation; DIAGNOSE treats it as a hypothesis, not ground truth."
        ))

    n_obs = sum(e.evidence_type == "observation" for e in ledger)
    n_assumptions = sum(e.evidence_type == "assumption" for e in ledger)
    if n_obs == 0:
        findings.append(AuditFinding(
            issue="no_direct_observations",
            severity="high",
            explanation="No direct observations are represented; causal diagnosis should remain provisional."
        ))
    if n_assumptions > n_obs:
        findings.append(AuditFinding(
            issue="assumption_heavy_case",
            severity="high",
            explanation="Assumptions outnumber observations, increasing the risk of narrative closure."
        ))

    if diagnoses:
        lead = diagnoses[0]
        second = diagnoses[1] if len(diagnoses) > 1 else None
        if second and abs(lead.score - second.score) <= 0.12:
            findings.append(AuditFinding(
                issue="diagnostic_ambiguity",
                severity="medium",
                explanation=f"Leading diagnoses are close ({lead.mechanism}={lead.score}, {second.mechanism}={second.score}); do not collapse the search space."
            ))

    if framework_fit and framework_fit[0]["conditional_fit"] >= 0.8:
        findings.append(AuditFinding(
            issue="possible_artificial_certainty",
            severity="medium",
            explanation="A high framework-fit score should not be interpreted as causal proof; it is a conditional prioritization for further testing."
        ))
    return findings
