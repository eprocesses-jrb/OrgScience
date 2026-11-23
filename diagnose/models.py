from dataclasses import dataclass, asdict, field
from typing import List, Any

@dataclass
class EvidenceItem:
    id: str
    text: str
    evidence_type: str
    source: str = "case"
    reliability: str = "unspecified"

@dataclass
class Diagnosis:
    mechanism: str
    score: float
    rationale: List[str] = field(default_factory=list)
    support_evidence_ids: List[str] = field(default_factory=list)
    disconfirming_evidence_needed: List[str] = field(default_factory=list)
    ontology_status: str = "in_ontology"

@dataclass
class AuditFinding:
    issue: str
    severity: str
    explanation: str

def serialise(obj: Any):
    if hasattr(obj, "__dataclass_fields__"):
        return asdict(obj)
    if isinstance(obj, list):
        return [serialise(x) for x in obj]
    if isinstance(obj, dict):
        return {k: serialise(v) for k, v in obj.items()}
    return obj
