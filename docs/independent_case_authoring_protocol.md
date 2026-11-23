# Independent Case Authoring Protocol

## Purpose
The v0.3 internal benchmark is developmental. A confirmatory benchmark must be authored independently
of the DIAGNOSE ontology, prompts, and baseline code.

## Eligible authors
Independent organizational researchers, experienced practitioners with documented case knowledge,
doctoral researchers supervised by domain experts, or methods researchers assigned to construct
factorial synthetic cases. Authors should not have participated in the DIAGNOSE ontology or scoring design.

## Materials given to case authors
Authors receive only:
1. the case template;
2. a generic definition of diagnostic mechanism as a causal process capable of generating the focal outcome;
3. instructions to include evidence sufficient to discriminate among some, but not necessarily all, explanations;
4. instructions to include an accepted organizational explanation that may be correct, incomplete, or wrong.

Authors do **not** receive the eight DIAGNOSE mechanism families.

## Required case fields
- focal organizational outcome
- accepted explanation
- direct observations
- participant claims
- relevant documents or metrics
- known missing evidence
- most defensible mechanism(s), if ground truth is intended
- plausible rival mechanisms
- discriminating evidence
- whether the correct conclusion is "insufficient evidence"
- author confidence in ground truth
- provenance: synthetic, public documentary, or de-identified practitioner case

## Independent adjudication
Two experts who did not author the case independently rate:
- causal specificity of the mechanism label;
- evidentiary support;
- presence of meaningful rivals;
- whether the case is overdetermined;
- whether "insufficient evidence" is the correct conclusion.

Disagreement is retained. A third adjudicator may resolve only the confirmatory label.

## Blinding
Confirmatory cases receive opaque IDs. Ground-truth metadata is stored separately from case text.
Prompt authors and model evaluators do not see the hidden fields.

## Holdout rule
No confirmatory holdout may be used to alter prompts, ontology, scoring weights, model choice, or thresholds.

## Recommended minimum confirmatory composition
- 10 clean single-mechanism cases
- 10 interacting-mechanism cases
- 10 misleading accepted-explanation cases
- 10 insufficient-evidence cases
- 10 out-of-ontology or ontology-challenging cases

A stronger target is 75–100 total cases across multiple authors and sectors.

## Rationale
The strongest threat to DIAGNOSE is circularity. Independent authorship makes ontology escape,
causal discrimination, and evidence sufficiency genuine tests rather than self-confirmation.
