# Benchmark Documentation — v0.3

## Developmental set
19 synthetic cases:
- 16 cases with designed organizational or out-of-ontology mechanisms
- 3 cases where the intended conclusion is insufficient evidence

The set exists to test execution, failure modes, and measurement plumbing. It is not a confirmatory benchmark.

## Internal developmental results
Using the evidence-weighted transparent baseline:
- top-1 mechanism accuracy on the 16 mechanism cases: 1.00
- top-3 accuracy: 1.00
- mean reciprocal rank: 1.00
- insufficient-evidence abstention on the 3 designed cases: 1.00

These values should **not** be interpreted as evidence of scientific validity. The cases and baseline
remain developmentally coupled. Indeed, the perfect internal score is a reason to prioritize
independent holdouts rather than tune further on this set.

## Perturbation signal
Evidence-label ablation changes the leading diagnosis in two deliberately selected cases. This
demonstrates that evidence typing is behaviorally consequential in the baseline and provides a
preregisterable Stage-2 hypothesis.

## Confirmatory benchmark
Use `independent_case_authoring_protocol.md`, `case_author_template.json`, and
`ground_truth_template_HIDDEN.json`. Ground-truth files must never be provided to model conditions.
