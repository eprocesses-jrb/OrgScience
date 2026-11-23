# Developmental Failure and Perturbation Analysis — v0.3

The internal benchmark is intentionally favorable to the transparent baseline and therefore cannot
establish validity. v0.3 uses perturbations to test whether specific architectural choices change
known failure modes.

## Evidence typing now changes diagnostic behavior

In SYN-WF-002, the evidence-weighted baseline ranks **workflow/process** first. When evidence labels
are removed and participant claims, interpretations, and assumptions are treated as if they were
observations, the top diagnosis flips to **capacity/resources**. The developmental ADC proxy also
moves from -0.182 to +0.430.

In SYN-LEAD-002, the weighted baseline ranks **structure/coordination** first. Removing evidence labels
moves **decision rights/governance** to the top and increases the developmental ADC proxy from +0.078
to +0.184.

These are synthetic demonstrations, not statistical results. Their value is that they produce a
specific confirmatory prediction: epistemic typing should reduce anchoring on organizational claims
that contain salient causal vocabulary but weak evidentiary status.

## Evidence removal produces rational instability

Removing 25% of observations from SYN-WF-002 changes the top diagnosis from workflow/process to
decision rights/governance. Both are designed true mechanisms in that case. This is useful: DIAGNOSE
should not be invariant when discriminating evidence is removed. Robustness cannot mean refusing to
update.

## Accepted-explanation manipulation

Replacing the accepted explanation with a neutral statement did not change the top diagnosis in the
two tested mechanism cases. This is desirable for the transparent baseline because the accepted
explanation is stored separately and is not scored as ground truth. Stage 2 will test whether LLM
conditions are more susceptible to this narrative anchor.

## Insufficient-evidence cases

Three v0.3 cases are explicitly designed so that the supplied evidence does not justify commitment to
a single mechanism. The pipeline returns `insufficient_evidence` for all three. This is developmental
plumbing only: because the cases carry that hidden design label, confirmatory evidence-sufficiency
performance must be tested on independently authored blinded cases.

## Implication for Stage 2

The strongest evaluation is not "Does DIAGNOSE get a high benchmark score?" It is:

- Does evidence typing reduce unsupported narrative anchoring?
- Does the system appropriately change its view when discriminating evidence changes?
- Does an accepted explanation bias AI conditions even when evidence does not support it?
- Can the system abstain when evidence is non-discriminating?
- Does an open-class rival detect mechanisms outside the ontology?
- Does adversarial structure improve calibration without merely increasing verbosity?

A negative result remains scientifically informative. If a simpler system performs as well on these
preregistered outcomes, DIAGNOSE's added architecture is not justified.
