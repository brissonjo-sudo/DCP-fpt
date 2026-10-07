"""Contre-épreuves d'assainissement et de conservation des preuves."""
import json
import hashlib
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import export_preuves as export
import eval_suite


class ExportPreuvesTests(unittest.TestCase):
    def test_domaine_trompeur_refuse_et_selecteur_documentaire_conserve(self):
        self.assertFalse(export.official("https://fauxlegifrance.gouv.fr/article"))
        self.assertFalse(export.official("https://legifrance.gouv.fr.example.org/article"))
        url = "https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX%3AX&access_token=CANARI#signature"
        self.assertEqual(export.clean_url(url), "https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX%3AX")

    def test_pensee_et_resultat_recherche_ne_deviennent_pas_ouverture(self):
        source = {"url": "https://www.legifrance.gouv.fr/article?token=CANARI", "title": "Article"}
        events = [{"type": "item.completed", "item": {"type": "reasoning", "text": "CANARI"}},
                  {"type": "item.completed", "item": {"type": "web_search", "action": {"type": "search"}, "results": [source]}}]
        result = export.role_trace(events)
        self.assertEqual(result["official_open_results"], [])
        self.assertEqual(len(result["official_search_results"]), 1)
        self.assertNotIn("CANARI", json.dumps(result))
        events[1]["item"]["action"]["type"] = "other"
        self.assertEqual(export.role_trace(events)["official_open_results"], [])

    def test_preuve_differente_non_ecrasable(self):
        with tempfile.TemporaryDirectory() as directory:
            source, target = Path(directory) / "source", Path(directory) / "cible"
            source.write_bytes(b"preuve originale\n")
            export.copy_checked(source, target)
            source.write_bytes(b"preuve modifiee\n")
            with self.assertRaises(ValueError):
                export.copy_checked(source, target)
            self.assertEqual(target.read_bytes(), b"preuve originale\n")

    def test_recuperation_mcp_explicitement_verifiee_sans_flux_brut(self):
        node = {"id": "identifiant-factice", "url": "https://www.legifrance.gouv.fr/article?token=CANARI",
                "text": "CANARI", "metadata": {"verified": True, "applicable_at_as_of_date": False}}
        item = {"type": "mcp_tool_call", "server": "droit-francais", "tool": "get_article",
                "status": "completed", "result": {"structuredContent": node}}
        result = export.role_trace([{"type": "item.completed", "item": item}])
        self.assertEqual(len(result["mcp_calls"][0]["sources"]), 1)
        self.assertFalse(result["mcp_calls"][0]["sources"][0]["metadata"]["applicable_at_as_of_date"])
        self.assertNotIn("CANARI", json.dumps(result))
        item["result"]["isError"] = True
        self.assertEqual(export.role_trace([{"type": "item.completed", "item": item}])["mcp_calls"][0]["sources"], [])
        item["result"]["isError"] = False
        item["server"] = "serveur-etranger"
        self.assertEqual(export.role_trace([{"type": "item.completed", "item": item}])["mcp_calls"][0]["sources"], [])

    def test_campagnes_publiques_liees_a_leurs_runtime_et_sorties(self):
        """La CI refuse une synthèse complète dont une preuve publique a dérivé."""
        for profile in ("codex-web-v0.1.0-r2", "codex-web-v0.1.1-r3"):
            with self.subTest(profil=profile):
                folder = export.ROOT / "tests/runs" / profile
                manifest = json.loads((folder / "manifest.json").read_text(encoding="utf-8"))
                summary = json.loads((folder / "summary.json").read_text(encoding="utf-8"))
                self.assertEqual(eval_suite.validate_run(folder), summary["totals"])
                self.assertEqual(summary["case_count"], 28)
                self.assertEqual(summary["runtime_sha256"], manifest["runtime_sha256"])
                self.assertFalse(summary["publication_ready"])
                for name, digest in manifest["runtime_sha256"].items():
                    blob = subprocess.run(["git", "show", f'{manifest["source_runtime_commit"]}:{name}'],
                        cwd=export.ROOT, check=True, capture_output=True).stdout
                    self.assertEqual(hashlib.sha256(blob).hexdigest(), digest)
                for case in eval_suite.load_cases(folder / "suite.json"):
                    for role, output in (("respondant", "response.md"), ("juge", "judgment.json")):
                        path = folder / case["id"]
                        evidence = json.loads((path / f"{role}-execution.json").read_text(encoding="utf-8"))
                        self.assertEqual(evidence["output_sha256"], hashlib.sha256((path / output).read_bytes()).hexdigest())
                        self.assertTrue(evidence["fresh_process"] and evidence["fresh_workspace"])
                        self.assertEqual(evidence["web_requested"], role == "respondant")
                        self.assertEqual(evidence["native_skill_present"], role == "respondant")
