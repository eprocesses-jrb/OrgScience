# Stage-2 Experimental Protocol Skeleton

## Research question
When organizational evidence is incomplete and competing causal mechanisms are plausible, how do
human-only, AI-only, and structured human–AI diagnostic systems differ in explanatory search,
calibration, traceability, and susceptibility to premature closure?

## Conditions
1. Human only
2. Single-agent LLM
3. Multi-agent rivals without adversarial audit
4. Multi-agent rivals plus adversarial audit
5. Full DIAGNOSE with human adjudication

The three primary conditions for the paper can remain human-only, AI-only, and human-directed
DIAGNOSE; conditions 2–4 provide architecture ablations.

## Case sequence
Each case is revealed in waves:

- Wave 0: accepted organizational explanation
- Wave 1: initial observations and participant claims
- Wave 2: discriminating evidence
- Wave 3: disconfirming or contradictory evidence
- Wave 4: optional intervention outcome

At each wave, collect:
- preferred diagnosis;
- confidence (0–100);
- viable alternative diagnoses;
- evidence requested next;
- framework/intervention choice;
- willingness to reopen a prior conclusion.

## Primary dependent variables

### Mechanism accuracy
Top-1, top-k, and reciprocal rank where known causal structure exists.

### Search breadth
Number and diversity of plausible rival mechanisms retained at each wave.

### Premature closure
Commitment to a single diagnosis before the discriminating evidence wave.

### Reopening rate
Probability of revising a committed diagnosis after contradictory evidence.

### Calibration / ADC
Difference between expressed confidence and evidence-supported confidence, examined using
calibration curves and case-level evidentiary sufficiency.

### Traceability
Share of diagnostic claims linked to specific evidence items; expert assessment of whether linked
evidence actually supports the claim.

### Unsupported causality
Blinded expert count of causal claims not warranted by provided evidence.

### Ontology escape
Frequency and appropriateness of diagnoses not represented in the initial mechanism families.

## Key ablations
- Evidence labels visible versus hidden
- Open-class rival present versus absent
- Adversarial audit present versus absent
- Human adjudication required versus optional
- Confidence elicited before versus after AI exposure

## Planned case families
- clean single-mechanism cases
- interacting-mechanism cases
- misleading accepted-explanation cases
- observationally equivalent cases requiring new evidence
- cases with missing critical evidence
- out-of-ontology cases
- cases where the correct conclusion is "insufficient evidence"

## Validity protections
- Independent case authors
- Blinded holdout set
- Preregistered scoring
- Expert adjudicators blind to condition
- Multiple LLM families
- Frozen prompts for confirmatory runs
- Raw output archive
- No tuning on confirmatory holdouts

## Interpretation rule
The research claim will be architectural, not universal. DIAGNOSE is supported only if its added
structure improves pre-specified epistemic outcomes relative to simpler alternatives. Faster output
alone does not count as success.
