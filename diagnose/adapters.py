from abc import ABC, abstractmethod

class ModelAdapter(ABC):
    """Provider-neutral interface for Stage-2 LLM agents."""
    @abstractmethod
    def generate(self, system_prompt, user_prompt, metadata=None):
        raise NotImplementedError

class EchoAdapter(ModelAdapter):
    """Deterministic development adapter; does not call an external model."""
    def generate(self, system_prompt, user_prompt, metadata=None):
        return {
            "provider": "development",
            "model": "echo-adapter",
            "output": user_prompt,
            "metadata": metadata or {}
        }

class AdapterRegistry:
    def __init__(self):
        self._adapters = {}
    def register(self, name, adapter):
        self._adapters[name] = adapter
    def get(self, name):
        if name not in self._adapters:
            raise KeyError(f"Adapter not registered: {name}")
        return self._adapters[name]
    def names(self):
        return sorted(self._adapters)
