"""Vérifie la preuve réelle 0.1.7 et la séparation juge/avis humain, sans modèle."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import export_mesure_controlee as export

RUN = export.ROOT / "tests/runs/codex-web-v0.1.7-dcp-017-20261108-b"


class MesurePublique017(unittest.TestCase):
    def test_preuve_56_roles_et_reserves_sans_reecrire_le_juge(self):
        result = export.verify_public_run(RUN)
        self.assertEqual(result, {"totals": {"RÉUSSITE": 25, "DEMI-RÉUSSITE": 2, "ÉCHEC": 1},
                                  "sessions": 56, "input_tokens": 6_115_143, "stop_checks": 6})
        review = export.load(RUN / "avis-humain-jo-20261108.json")
        self.assertEqual(set(review["reserves"]), {"cas-06", "cas-08", "cas-18"})
        self.assertEqual(export.load(RUN / "cas-18/judgment.json")["verdict"], "ÉCHEC")
        self.assertEqual(review["verdicts"]["cas-18"], "en réserve")
        self.assertEqual(export.load(RUN / "controle-citations.json")["occurrence_count"], 0)
        self.assertFalse(export.load(RUN / "provenance.json")["publication_ready"])
