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
    def test_assainissement_ne_change_que_lien_runtime_et_refuse_derivation(self):
        original=b"Un texte. [Skill](C:/Users/CANARI/Temp/session/.agents/skills/dcp-fpt/SKILL.md).\n"
        public,metadata=eval_suite.redact_response(original)
        self.assertEqual(public,b"Un texte. [Skill](.agents/skills/dcp-fpt/SKILL.md).\n")
        self.assertEqual(metadata['original_response_sha256'],hashlib.sha256(original).hexdigest())
        self.assertNotIn('CANARI',json.dumps(metadata))
        with tempfile.TemporaryDirectory() as directory:
            folder=Path(directory);response=folder/'response.md';response.write_bytes(public)
            (folder/'redaction.json').write_text(json.dumps(metadata),encoding='utf-8')
            (folder/'respondant-execution.json').write_text(json.dumps({'output_sha256':metadata['original_response_sha256']}),encoding='utf-8')
            self.assertEqual(eval_suite.canonical_response_digest(response),hashlib.sha256(original).hexdigest())
            response.write_bytes(public+b'Autre contenu.\n')
            with self.assertRaises(ValueError):eval_suite.canonical_response_digest(response)
            response.write_bytes(public)
            (folder/'respondant-execution.json').write_text(json.dumps({'output_sha256':'0'*64}),encoding='utf-8')
            with self.assertRaises(ValueError):eval_suite.canonical_response_digest(response)

    def test_relecture_retrospective_ne_prouve_pas_lecture_initiale(self):
        folder=export.ROOT/'tests/runs/codex-mcp-v0.1.3-r5'
        audit=json.loads((export.ROOT/'docs/socle/audit-provenance-0.1.3-2026-10-08.json').read_text(encoding='utf-8'))
        self.assertEqual(audit['completed_count'],28)
        self.assertEqual(len(audit['records']),28)
        self.assertFalse(audit['human_legal_validation'])
        self.assertFalse(audit['publication_ready'])
        self.assertFalse(audit['matching_url_proves_legal_applicability'])
        for record in audit['records']:
            response=folder/record['case_id']/'response.md'
            self.assertEqual(record['response_sha256'],eval_suite.canonical_response_digest(response))
            for check in record['retrospective_primary_checks']:
                self.assertFalse(check['original_session_read_proven'])
                self.assertFalse(check['legal_applicability_to_case_validated'])
                self.assertTrue(check['metadata']['verified'])
                self.assertRegex(check['text_sha256'],r'^[a-f0-9]{64}$')

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
        item["result"] = {"structured_content": node}
        self.assertEqual(len(export.role_trace([{"type": "item.completed", "item": item}])["mcp_calls"][0]["sources"]), 1)
        item["result"]["isError"] = True
        self.assertEqual(export.role_trace([{"type": "item.completed", "item": item}])["mcp_calls"][0]["sources"], [])
        item["result"]["isError"] = False
        node["metadata"]["content_complete"] = False
        self.assertEqual(export.role_trace([{"type": "item.completed", "item": item}])["mcp_calls"][0]["sources"], [])
        node["metadata"]["content_complete"] = True
        item["server"] = "serveur-etranger"
        self.assertEqual(export.role_trace([{"type": "item.completed", "item": item}])["mcp_calls"][0]["sources"], [])

    def test_campagnes_publiques_liees_a_leurs_runtime_et_sorties(self):
        """La CI refuse une synthèse complète dont une preuve publique a dérivé."""
        for profile in ("codex-web-v0.1.0-r2", "codex-web-v0.1.1-r3", "codex-mcp-v0.1.3-r5"):
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
                        expected = eval_suite.canonical_response_digest(path / output) if role == "respondant" else hashlib.sha256((path / output).read_bytes()).hexdigest()
                        self.assertEqual(evidence["output_sha256"], expected)
                        self.assertTrue(evidence["fresh_process"] and evidence["fresh_workspace"])
                        self.assertEqual(evidence["web_requested"], role == "respondant")
                        self.assertEqual(evidence["native_skill_present"], role == "respondant")
                        if profile == "codex-mcp-v0.1.3-r5":
                            self.assertEqual(evidence["mcp_requested"], role == "respondant")
                    if profile == "codex-mcp-v0.1.3-r5":
                        trace = json.loads((folder / case["id"] / "trace-assainie.json").read_text(encoding="utf-8"))
                        self.assertEqual(trace["roles"]["juge"]["mcp_calls"], [])
                        self.assertEqual(trace["roles"]["juge"]["official_open_results"], [])

    def test_campagne_interrompue_ne_devient_pas_score_global(self):
        folder = export.ROOT / "tests/runs/codex-web-v0.1.2-r4-partiel"
        stop = json.loads((folder / "arret.json").read_text(encoding="utf-8"))
        progress = json.loads((folder / "progression.json").read_text(encoding="utf-8"))
        self.assertEqual(stop["completed_count"], progress["completed_count"])
        self.assertLess(progress["completed_count"], progress["case_count"])
        self.assertFalse((folder / "summary.json").exists())
        self.assertFalse(progress["publication_ready"])
        for case in progress["cases"]:
            response = folder / case["case_id"] / "response.md"
            self.assertEqual(case["response_sha256"], hashlib.sha256(response.read_bytes()).hexdigest())
