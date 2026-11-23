# Stage-2 Preregistration Draft

## Primary research question
Does a structured human–AI diagnostic workflow improve the epistemic quality of organizational
diagnosis relative to human-only and simpler AI conditions?

## Primary confirmatory conditions
1. Human only
2. Single-agent AI
3. Human-directed DIAGNOSE

Architecture ablations are secondary but preregistered.

## Primary outcomes
1. Top-k mechanism accuracy on cases with adjudicated ground truth
2. Premature closure rate
3. Reopening rate after disconfirming evidence
4. Confidence calibration / artificial diagnostic certainty
5. Evidence-to-inference traceability
6. Unsupported causal-claim rate
7. Correct use of "insufficient evidence"
8. Appropriate ontology escape

## Primary hypotheses
### H1 Search breadth
DIAGNOSE will retain a greater number and diversity of viable rival explanations before the
discriminating-evidence wave than single-agent AI.

### H2 Premature closure
DIAGNOSE will have a lower premature-closure rate than single-agent AI.

### H3 Calibration
DIAGNOSE will show lower positive artificial diagnostic certainty than single-agent AI.

### H4 Traceability
DIAGNOSE will produce a higher proportion of diagnostic claims linked to specific supporting evidence.

### H5 Evidence sufficiency
DIAGNOSE will more often select "insufficient evidence" on cases where independent experts judge
that the available evidence cannot discriminate among leading mechanisms.

### H6 Ontology escape
DIAGNOSE with an open-class rival will identify out-of-ontology cases more often than the same
architecture with the open-class rival removed.

## Case reveal structure
Wave 0: accepted explanation
Wave 1: initial evidence
Wave 2: discriminating evidence
Wave 3: disconfirming evidence
Wave 4: optional intervention outcome

At each wave collect diagnosis, confidence, viable rivals, evidence requested next, and willingness to commit.

## Exclusion rules
Exclude a case from accuracy analysis if adjudicators cannot agree that a defensible mechanism ground
truth exists, essential evidence was accidentally omitted, or the case was exposed during development.
Retain such cases for sufficiency analysis when appropriate.

## Scoring rules
- Top-1 accuracy: first ranked diagnosis matches any adjudicated true mechanism.
- Top-3 accuracy: any of first three matches.
- Premature closure: participant commits before the preregistered discriminating-evidence wave.
- Reopening: a committed diagnosis is revised after contradictory evidence.
- Traceability: proportion of causal claims with valid evidence references plus blinded expert support rating.
- Unsupported causality: blinded expert count of causal claims not warranted by available evidence.
- Insufficient-evidence accuracy: correct abstention on non-discriminating cases.
- Ontology escape: appropriate use of an explanation outside the initial ontology.

## ADC analysis
The v0.3 development proxy will not be the confirmatory estimator. Confirmatory ADC will be frozen
before holdout evaluation using confidence calibration, evidence sufficiency, synthetic truth where
available, and response to disconfirming evidence.

## Interpretation principle
The added complexity of DIAGNOSE is justified only if it improves preregistered epistemic outcomes.
Speed or output volume alone does not count as superiority.
