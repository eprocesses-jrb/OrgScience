# DIAGNOSE Technical Appendix — v0.4

## 1. Epistemic design rule
Accepted explanations and formal representations are represented as hypotheses, not ground truth.

## 2. Pipeline
Input -> Evidence Ledger -> Weighted Rival Diagnoses -> Open-Class Rival -> Evidence-Sufficiency Gate
-> Contingency Classification -> Conditional Framework Fit -> Adversarial Audit ->
Epistemic Performance Measures -> Human Adjudication -> Versioned Audit Record.

## 3. Evidence weighting
The transparent baseline now weights direct observations more heavily than participant claims,
researcher interpretations, and assumptions. Missing-evidence statements receive no diagnostic
support weight. The unweighted condition remains conceptually important as an ablation.

This is not asserted to be the correct universal weighting. The purpose is to make the epistemic
status of evidence experimentally manipulable rather than silently collapsing all text into one pool.

## 4. Rival explanations and ontology escape
Eight initial mechanism families are retained plus `outside_current_ontology`. The open-class rival
is always available and becomes a confirmatory outcome in out-of-ontology cases.

## 5. Evidence sufficiency
v0.4 adds a separate sufficiency decision. A research system can therefore return:
- provisional diagnosis possible; or
- insufficient evidence.

The Stage-2 task will require blinded sufficiency judgments rather than access to a hidden benchmark label.

## 6. Perturbation engine
The repository can:
- remove a proportion of direct observations;
- replace the accepted explanation;
- add contradictory evidence;
- erase evidence-type labels.

These manipulations support causal tests of the architecture itself.

## 7. Provider-neutral model adapters
`diagnose/adapters.py` defines a provider-neutral interface so Stage-2 models can be swapped without
altering the audit schema. v0.4 includes only a deterministic development adapter and makes no
external model calls.

## 8. Independent benchmark protocol
External authors do not receive the DIAGNOSE mechanism ontology. Ground truth is stored separately
from visible case text. Independent adjudicators review mechanism specificity, evidence sufficiency,
and rival plausibility. Confirmatory holdouts cannot be used for development.

## 9. Confirmatory outcomes
- mechanism accuracy where ground truth is defensible
- search breadth and rival diversity
- premature closure
- reopening after disconfirming evidence
- confidence calibration / artificial diagnostic certainty
- evidence-to-inference traceability
- unsupported causal claims
- correct abstention for insufficient evidence
- appropriate ontology escape

## 10. Reproducibility
The core baseline uses only Python's standard library. The package includes cases, prompts, tests,
benchmark and perturbation runners, version metadata, a license, citation metadata, an independent
case-authoring protocol, hidden-ground-truth template, and preregistration draft.

## 11. Stage-1 proof claim
v0.4 demonstrates that the proposed epistemic architecture is executable, perturbable, and auditable.
It does not establish diagnostic validity. That claim is reserved for independent Stage-2 evaluation.
