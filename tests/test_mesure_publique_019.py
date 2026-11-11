"""Vérifie la preuve réelle 0.1.9 et la séparation juge/avis humain, sans modèle."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import export_mesure_controlee as export

RUN = export.ROOT / "tests/runs/codex-web-v0.1.9-dcp-019-20261111-a"


class MesurePublique019(unittest.TestCase):
    def test_preuve_56_roles_et_reserves_sans_reecrire_le_juge(self):
        result = export.verify_public_run(RUN)
        self.assertEqual(result, {"totals": {"RÉUSSITE": 28, "DEMI-RÉUSSITE": 0, "ÉCHEC": 0},
                                  "sessions": 56, "input_tokens": 6_070_218, "stop_checks": 6})
        review = export.load(RUN / "avis-humain-jo-20261111.json")
        self.assertEqual(set(review["reserves"]), {"cas-07", "cas-12", "cas-18"})
        for case in ("cas-07", "cas-12", "cas-18"):
            self.assertEqual(export.load(RUN / case / "judgment.json")["verdict"], "RÉUSSITE")
        self.assertEqual(review["verdicts"]["cas-06"], "conforme")
        self.assertEqual(export.load(RUN / "controle-citations.json")["occurrence_count"], 0)
        self.assertFalse(export.load(RUN / "provenance.json")["publication_ready"])
