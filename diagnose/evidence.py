from .models import EvidenceItem

def build_evidence_ledger(case):
    ledger = []
    i = 1
    for section, etype in [
        ("observations", "observation"),
        ("participant_claims", "participant_claim"),
        ("researcher_interpretations", "interpretation"),
        ("assumptions", "assumption"),
        ("missing_evidence", "missing_evidence"),
    ]:
        for item in case.get(section, []):
            ledger.append(EvidenceItem(
                id=f"E{i:03d}",
                text=item if isinstance(item, str) else item.get("text", ""),
                evidence_type=etype,
                source=section,
                reliability=(item.get("reliability", "unspecified")
                             if isinstance(item, dict) else "unspecified"),
            ))
            i += 1
    return ledger
