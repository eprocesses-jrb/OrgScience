import copy
import random

def remove_observations(case, proportion=0.25, seed=1):
    rng = random.Random(seed)
    out = copy.deepcopy(case)
    obs = list(out.get("observations", []))
    if not obs:
        return out
    n = max(1, round(len(obs) * proportion))
    drop = set(rng.sample(range(len(obs)), min(n, len(obs))))
    out["observations"] = [x for i, x in enumerate(obs) if i not in drop]
    out["perturbation"] = {"type": "remove_observations", "proportion": proportion, "seed": seed}
    return out

def contradict_leading_evidence(case):
    out = copy.deepcopy(case)
    obs = list(out.get("observations", []))
    obs.append("A later independent audit reports evidence inconsistent with the currently favored causal explanation.")
    out["observations"] = obs
    out["perturbation"] = {"type": "contradictory_evidence"}
    return out

def swap_accepted_explanation(case, new_text):
    out = copy.deepcopy(case)
    out["accepted_explanation"] = new_text
    out["perturbation"] = {"type": "accepted_explanation_swap"}
    return out

def strip_evidence_labels(case):
    out = copy.deepcopy(case)
    merged = []
    for key in ["observations","participant_claims","researcher_interpretations","assumptions"]:
        merged.extend(out.get(key, []))
    out["observations"] = merged
    out["participant_claims"] = []
    out["researcher_interpretations"] = []
    out["assumptions"] = []
    out["perturbation"] = {"type": "evidence_label_ablation"}
    return out
