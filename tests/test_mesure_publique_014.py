"""Intégrité des preuves 0.1.4 ; aucun appel modèle ou accès privé en CI."""
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import export_mesure_controlee as export

RUN = export.ROOT / "tests/runs/codex-web-v0.1.4-dcp-stop-20261020-a"


class MesurePublique014(unittest.TestCase):
    def test_mesure_liee_runtime_56_roles_stop_et_avis(self):
        result = export.verify_public_run(RUN)
        self.assertEqual(result["totals"], {"RÉUSSITE": 28, "DEMI-RÉUSSITE": 0, "ÉCHEC": 0})
        self.assertEqual(result["sessions"], 56)
        self.assertEqual(result["input_tokens"], 5_829_642)
        self.assertEqual(result["stop_checks"], 6)

    def test_scanner_refuse_secrets_et_donnees_personnelles(self):
        fixtures = ["Bearer " + "factice_" * 4, "C:/Users/CANARI/dossier", "personne@example.invalid",
                    "06 00 00 00 00", "1 99 01 99 123 456 78", "192.0.2.1",
                    "API_KEY=" + "factice", "https://exemple.invalid/?access_token=CANARI"]
        for fixture in fixtures:
            with self.subTest(categorie=fixture.split()[0]):
                self.assertTrue(export.scan_public(fixture.encode()))
        self.assertFalse(export.scan_public(json.dumps({"sha256": "a199019912345678b" * 4}).encode()))

    def test_derivation_ou_ajout_de_flux_prive_refuse(self):
        with tempfile.TemporaryDirectory() as temporary:
            folder = Path(temporary) / "run"
            shutil.copytree(RUN, folder)
            response = folder / "cas-21/response.md"
            response.write_bytes(response.read_bytes() + b"\nCANARI\n")
            with self.assertRaisesRegex(ValueError, "Inventaire"):
                export.verify_public_run(folder)
            response.write_bytes((RUN / "cas-21/response.md").read_bytes())
            (folder / "cas-01/respondant-stdout.txt").write_bytes(b"CANARI")
            with self.assertRaisesRegex(ValueError, "Inventaire"):
                export.verify_public_run(folder)

    def test_reempreinter_un_jugement_altere_ne_suffit_pas(self):
        with tempfile.TemporaryDirectory() as temporary:
            folder = Path(temporary) / "run"
            shutil.copytree(RUN, folder)
            judgment = folder / "cas-01/judgment.json"
            value = export.load(judgment)
            value["verdict"] = "DEMI-RÉUSSITE"
            judgment.write_bytes(export.encoded(value))
            inventory = export.load(folder / "empreintes.json")
            inventory["files"]["cas-01/judgment.json"] = export.digest(judgment.read_bytes())
            (folder / "empreintes.json").write_bytes(export.encoded(inventory))
            with self.assertRaisesRegex(ValueError, "Synthèse"):
                export.verify_public_run(folder)
