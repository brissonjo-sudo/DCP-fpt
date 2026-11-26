"""Vérifie la preuve réelle 0.2.2 et la séparation juge/avis humain, sans modèle."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import export_mesure_controlee as export

RUN = export.ROOT / "tests/runs/codex-web-v0.2.2-dcp-025-20261126-a"
RESERVES = {"cas-07", "cas-12", "cas-15"}


class MesurePublique022(unittest.TestCase):
    def test_preuve_56_roles_et_reserves_sans_reecrire_le_juge(self):
        result = export.verify_public_run(RUN)
        self.assertEqual(result, {"totals": {"RÉUSSITE": 27, "DEMI-RÉUSSITE": 1, "ÉCHEC": 0},
                                  "sessions": 56, "input_tokens": 6_165_580, "stop_checks": 6})
        review = export.load(RUN / "avis-humain-jo-20261126.json")
        self.assertEqual(set(review["reserves"]), RESERVES)
        # L'avis humain ne réécrit pas le juge : cas-15 reste DEMI-RÉUSSITE, 07 et 12 restent RÉUSSITE.
        self.assertEqual(export.load(RUN / "cas-15/judgment.json")["verdict"], "DEMI-RÉUSSITE")
        for case in ("cas-07", "cas-12"):
            self.assertEqual(export.load(RUN / case / "judgment.json")["verdict"], "RÉUSSITE")
        self.assertEqual(export.load(RUN / "controle-citations.json")["occurrence_count"], 0)
        self.assertFalse(export.load(RUN / "provenance.json")["publication_ready"])


if __name__ == "__main__":
    unittest.main()
