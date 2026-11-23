# Reviewer Guide — DIAGNOSE v0.4A

## Fastest path
Run:
```bash
python reviewer_demo.py
```

The demo shows four properties in one run:
1. evidence typing affects the diagnostic ranking;
2. the same case changes when epistemic labels are erased;
3. the pipeline can abstain when evidence is insufficient;
4. the pipeline can rank an outside-current-ontology explanation.

## Full reproducibility
```bash
python run_benchmark.py
python run_perturbation_study.py
python -m unittest discover -s tests -v
```

## Scientific question
DIAGNOSE asks whether AI can improve organizational science by preserving rival explanations,
making evidence-to-inference links explicit, and delaying convergence until evidence discriminates
among mechanisms.

## Important interpretation boundary
The synthetic benchmark is developmental and partially coupled to the baseline. High internal
accuracy is not a validity claim. The intended Stage-2 test uses independently authored, blinded
holdouts and compares human-only, single-agent AI, and human-directed DIAGNOSE conditions.

## Where to look
- Scientific contribution: see the separately submitted anonymous Stage-1 proposal
- Architecture: `docs/technical_appendix.md`
- Failure modes: `docs/developmental_failure_analysis.md`
- Independent validation: `docs/independent_case_authoring_protocol.md`
- Preregistration: `docs/preregistration_stage2.md`
- Public-case seeds: `docs/public_validation_seed.md`
