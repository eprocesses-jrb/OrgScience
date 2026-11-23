def classify_contingencies(case):
    c = case.get("contingencies", {})
    allowed = {
        "environmental_volatility": ["low","medium","high","unknown"],
        "organizational_maturity": ["low","medium","high","unknown"],
        "change_depth": ["local","cross-functional","systemic","unknown"],
        "system_coupling": ["loose","moderate","tight","unknown"],
        "evidence_quality": ["low","medium","high","unknown"],
        "authority_distribution": ["centralized","distributed","mixed","unknown"],
        "intervention_reversibility": ["low","medium","high","unknown"],
    }
    out = {}
    for key, values in allowed.items():
        value = c.get(key, "unknown")
        out[key] = value if value in values else "unknown"
    return out
