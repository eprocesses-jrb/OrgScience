# DIAGNOSE v0.4A
## Preserving Competing Explanations in AI-Assisted Organizational Science

DIAGNOSE is an executable research infrastructure for studying how humans and AI move from
organizational evidence to causal explanation.

Its governing epistemic rule is:

> Accepted explanations and formal representations are hypotheses until they survive comparison
> with rival explanations and operating evidence.

This v0.4A anonymous review artifact strengthens the project around **independent validation, evidence sufficiency, and perturbation
testing** rather than simply adding more internally designed cases.

## What is new in v0.4A
- Evidence-type weighting in the transparent baseline
- Three cases where the correct result is **insufficient evidence**
- Explicit evidence-sufficiency output
- Evidence-perturbation engine
- Accepted-explanation perturbation
- Evidence-label ablation
- Provider-neutral model-adapter interface
- Independent case-authoring protocol
- Stage-2 preregistration draft
- Updated benchmark runner for abstention accuracy
- Expanded test suite

## Run the benchmark
```bash
python run_benchmark.py
```

## Run perturbation study
```bash
python run_perturbation_study.py
```

## Run tests
```bash
python -m unittest discover -s tests -v
```

## Interpretation boundary
The internal benchmark remains developmental. Accuracy on these cases is **not** evidence that
DIAGNOSE is validated. Confirmatory evaluation requires independently authored, blinded holdout cases.

The key Stage-2 question is architectural:

> Does preserving rival explanations, evidence typing, adversarial testing, ontology escape, and
> human adjudication improve epistemic outcomes relative to simpler human or AI workflows?

See:
- `docs/independent_case_authoring_protocol.md`
- `docs/preregistration_stage2.md`
- `docs/stage2_experimental_protocol.md`
- `docs/developmental_failure_analysis.md`

## Reviewer entry point
Run `python reviewer_demo.py` for the shortest executable demonstration.


## Review artifact note — November 2026

This is a **preliminary** reproducible research artifact, not a trained LLM-based multi-agent
system. The executable current baseline is transparent and rule-based; the provider-neutral
LLM interface is only scaffolding for proposed Stage-2 work. Synthetic internal cases must
not be represented as independent validation.

The developmental evidence-sufficiency gate uses only input evidence quantity/quality and
missing-evidence counts. It does **not** read the benchmark ground-truth label. The reported
abstention-rate for the self-authored cases remains a development check, not a validation claim.

Reproduce the preliminary findings without any credentials:

```bash
python reviewer_demo.py
python run_benchmark.py
python run_perturbation_study.py
python -m unittest discover -s tests -v
```

All 19 benchmark examples are synthetic, and all code and materials needed for these
**developmental** outputs are included. No human-participant or confidential data are present.
