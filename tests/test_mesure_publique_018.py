"""Vérifie la preuve réelle 0.1.8 et la séparation juge/avis humain, sans modèle."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import export_mesure_controlee as export

RUN = export.ROOT / "tests/runs/codex-web-v0.1.8-dcp-018-20261109-a"


class MesurePublique018(unittest.TestCase):
    def test_preuve_56_roles_et_reserves_sans_reecrire_le_juge(self):
        result = export.verify_public_run(RUN)
        self.assertEqual(result, {"totals": {"RÉUSSITE": 27, "DEMI-RÉUSSITE": 0, "ÉCHEC": 1},
                                  "sessions": 56, "input_tokens": 6_024_179, "stop_checks": 6})
        review = export.load(RUN / "avis-humain-jo-20261110.json")
        self.assertEqual(set(review["reserves"]), {"cas-03", "cas-06", "cas-18", "cas-19"})
        self.assertEqual(export.load(RUN / "cas-06/judgment.json")["verdict"], "ÉCHEC")
        self.assertEqual(export.load(RUN / "cas-19/judgment.json")["verdict"], "RÉUSSITE")
        self.assertTrue(review["reserves"]["cas-19"].startswith("❌ Non conforme"))
        self.assertEqual(export.load(RUN / "controle-citations.json")["occurrence_count"], 0)
        self.assertFalse(export.load(RUN / "provenance.json")["publication_ready"])
