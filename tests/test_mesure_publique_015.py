"""Vérifie la preuve réelle 0.1.5 et la séparation juge/avis humain, sans modèle."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import export_mesure_controlee as export

RUN = export.ROOT / "tests/runs/codex-web-v0.1.5-dcp-015-20261023-a"


class MesurePublique015(unittest.TestCase):
    def test_preuve_56_roles_et_reserves_sans_reecrire_le_juge(self):
        result = export.verify_public_run(RUN)
        self.assertEqual(result, {"totals": {"RÉUSSITE": 25, "DEMI-RÉUSSITE": 2, "ÉCHEC": 1},
                                  "sessions": 56, "input_tokens": 5_463_220, "stop_checks": 6})
        review = export.load(RUN / "avis-humain-jo-20261024.json")
        self.assertEqual(set(review["reserves"]),
                         {"cas-06", "cas-08", "cas-09", "cas-15", "cas-17", "cas-26"})
        self.assertEqual(export.load(RUN / "cas-17/judgment.json")["verdict"], "ÉCHEC")
        self.assertEqual(review["verdicts"]["cas-17"], "en réserve")
        self.assertEqual(export.load(RUN / "controle-citations.json")["occurrence_count"], 0)
        self.assertFalse(export.load(RUN / "provenance.json")["publication_ready"])
