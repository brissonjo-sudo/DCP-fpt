"""Vérifie la preuve réelle 0.2.0 et la séparation juge/avis humain, sans modèle."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import export_mesure_controlee as export

RUN = export.ROOT / "tests/runs/codex-web-v0.2.0-dcp-020-20261116-a"
RESERVES = {"cas-05", "cas-06", "cas-07", "cas-12", "cas-17", "cas-18", "cas-21"}


class MesurePublique020(unittest.TestCase):
    def test_preuve_56_roles_et_reserves_sans_reecrire_le_juge(self):
        result = export.verify_public_run(RUN)
        self.assertEqual(result, {"totals": {"RÉUSSITE": 27, "DEMI-RÉUSSITE": 0, "ÉCHEC": 1},
                                  "sessions": 56, "input_tokens": 7_453_854, "stop_checks": 6})
        review = export.load(RUN / "avis-humain-jo-20261116.json")
        self.assertEqual(set(review["reserves"]), RESERVES)
        # L'avis humain ne réécrit pas le juge : cas-06 reste ÉCHEC, les autres réservés restent RÉUSSITE.
        self.assertEqual(export.load(RUN / "cas-06/judgment.json")["verdict"], "ÉCHEC")
        for case in sorted(RESERVES - {"cas-06"}):
            self.assertEqual(export.load(RUN / case / "judgment.json")["verdict"], "RÉUSSITE")
        self.assertEqual(review["verdicts"]["cas-06"], "en réserve")
        self.assertEqual(export.load(RUN / "controle-citations.json")["occurrence_count"], 0)
        self.assertFalse(export.load(RUN / "provenance.json")["publication_ready"])


if __name__ == "__main__":
    unittest.main()
