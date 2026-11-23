# Anonymous review artifact — DIAGNOSE v0.4A

This repository contains a self-contained Python proof of concept and synthetic developmental
benchmark for the Organization Science *AI-Enabled Frontiers* special issue submission.

- Run `python reviewer_demo.py` for the short demonstration.
- Run `python run_benchmark.py` to regenerate developmental scores.
- Run `python run_perturbation_study.py` to reproduce perturbations.
- Run `python -m unittest discover -s tests -v` to execute tests.

All procedures use only the Python standard library. No API keys or external datasets are needed.

### Limitations

The current executable diagnosis baseline is **rule-based**, not a functioning LLM multi-agent
system; LLM adapters are at the interface stage. Internal case performance is illustrative,
not independently validated. The evidence-sufficiency gate has been corrected for review so
it does **not** read hidden benchmark answer labels. The Stage-2 proposal specifies independent
case authorship and blinded evaluation as future work.

This is intentionally an anonymous review release; identifying author metadata has been omitted.
