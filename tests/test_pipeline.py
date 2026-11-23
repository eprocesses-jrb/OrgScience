import json, unittest
from pathlib import Path
from diagnose.pipeline import run
from diagnose.benchmark import run_benchmark, aggregate
from diagnose.perturb import remove_observations, strip_evidence_labels
from diagnose.adapters import EchoAdapter, AdapterRegistry

ROOT = Path(__file__).resolve().parents[1]

class TestPipeline(unittest.TestCase):
    def test_pipeline_is_auditable(self):
        case = json.loads((ROOT / "cases" / "SYN-WF-001.json").read_text())
        result = run(case)
        self.assertTrue(result["evidence_ledger"])
        self.assertEqual(len(result["rival_diagnoses"]), 9)
        self.assertIn("evidence_sufficiency", result)
        self.assertEqual(result["human_adjudication"]["status"], "pending")

    def test_outside_ontology_escape_route(self):
        case = json.loads((ROOT / "cases" / "SYN-OUT-001.json").read_text())
        result = run(case)
        self.assertEqual(result["rival_diagnoses"][0]["mechanism"], "outside_current_ontology")

    def test_insufficient_evidence_case_abstains(self):
        case = json.loads((ROOT / "cases" / "SYN-INSUF-001.json").read_text())
        result = run(case)
        self.assertEqual(result["evidence_sufficiency"]["status"], "insufficient_evidence")

    def test_insufficient_evidence_does_not_read_answer_key(self):
        case = json.loads((ROOT / "cases" / "SYN-INSUF-001.json").read_text())
        case.pop("ground_truth_mechanisms", None)
        result = run(case)
        self.assertEqual(result["evidence_sufficiency"]["status"], "insufficient_evidence")

    def test_perturbation_removes_observations(self):
        case = json.loads((ROOT / "cases" / "SYN-WF-002.json").read_text())
        perturbed = remove_observations(case, proportion=0.5, seed=2)
        self.assertLess(len(perturbed["observations"]), len(case["observations"]))

    def test_evidence_label_ablation(self):
        case = json.loads((ROOT / "cases" / "SYN-WF-002.json").read_text())
        perturbed = strip_evidence_labels(case)
        self.assertEqual(perturbed["participant_claims"], [])
        self.assertGreater(len(perturbed["observations"]), len(case["observations"]))

    def test_model_adapter_registry(self):
        reg = AdapterRegistry()
        reg.register("echo", EchoAdapter())
        out = reg.get("echo").generate("system", "user")
        self.assertEqual(out["model"], "echo-adapter")

    def test_all_benchmark_cases_run(self):
        rows = run_benchmark(ROOT / "cases")
        self.assertEqual(len(rows), 19)
        summary = aggregate(rows)
        self.assertEqual(summary["n_cases"], 19)
        self.assertEqual(summary["n_insufficient_evidence_cases"], 3)

if __name__ == "__main__":
    unittest.main()
