# DIAGNOSE v0.4A — Stage-1 Submission Manifest

## Required Stage-1 components

### 1. Proposal
Separately submitted as `01_DIAGNOSE_Stage1_Proposal_Anonymous.docx`

Purpose: 1,500–2,000-word statement of the scientific contribution, completed work, proposed work,
execution risks, and how the project could change organizational and social science.

### 2. Technical appendix
`docs/technical_appendix.md`

Purpose: architecture, evidence typing, rival mechanisms, abstention, perturbation tests,
provider-neutral model interface, reproducibility, and Stage-2 evaluation design.

### 3. Research artifact / prototype
Executable Python repository requiring Python 3.10+ and no third-party packages for the baseline.

Reviewer entry points:
```bash
python reviewer_demo.py
python run_benchmark.py
python run_perturbation_study.py
python -m unittest discover -s tests -v
```

## What reviewers can verify immediately
- Evidence ledger separates observation, participant claim, interpretation, assumption, and missing evidence.
- Rival mechanisms remain simultaneously available.
- An open-class explanation prevents a closed ontology.
- The system can return `insufficient_evidence`.
- Erasing evidence labels can change the leading diagnosis in developmental cases.
- Every diagnostic object can be traced to evidence IDs.
- Human adjudication remains a distinct layer.
- All baseline tests run without an external API.

## What is *not* claimed at Stage 1
- Validated organizational diagnostic accuracy.
- General superiority over human researchers or single-agent LLMs.
- A validated Artificial Diagnostic Certainty scale.
- Independence of the internal synthetic benchmark.
- Clinical, legal, personnel, or other high-stakes decision authority.

## Stage-2 confirmatory commitments
- Independently authored cases.
- Blinded holdouts.
- Preregistered outcomes and scoring.
- Multiple accessible model families.
- Human-only, single-agent AI, and human-directed DIAGNOSE conditions.
- Explicit insufficient-evidence and out-of-ontology cases.
- Raw-output and prompt archiving.
