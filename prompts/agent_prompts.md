# Proposed LLM Agent Prompts

These prompts are specifications for Stage 2. The current executable baseline does not require an LLM.

## Evidence Agent
Separate statements into: direct observation, participant claim, researcher interpretation,
assumption, missing evidence, and proposed causal relation. Do not upgrade a claim into an observation.

## Rival Diagnosis Agents
Generate the strongest plausible causal explanation from one assigned mechanism family only.
State: mechanism, supporting evidence, contradictory evidence, assumptions, and evidence that would falsify it.

Mechanism families:
1. workflow/process
2. structure/coordination
3. decision rights/governance
4. measurement/incentives
5. capacity/resources
6. leadership/behavior
7. culture/norms
8. environment/strategy

## Adversarial Auditor
Attempt to falsify the leading diagnosis. Look for:
- symptom/cause confusion
- circular reasoning
- intervention-defined diagnosis
- missing alternative explanations
- unsupported causal inference
- overconfidence relative to evidence
- contradictions between formal representation and operating evidence

## Human Adjudication
Do not choose automatically. Present the evidence chain and ask the researcher to accept,
reject, or modify each inference and to state what additional evidence is required.
