"""Barrière 0.1.5 autorisée par Jo : contre-épreuves sans aucun appel modèle."""
from copy import deepcopy
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import export_mesure_controlee as export
from support_export_controle import diagnostic, save


class ExportControle015(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="diagnostic-015-", dir=export.ROOT / "tests/runs")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)

    def check_export(self, fixture):
        result = export.export(**fixture)
        public = export.verify_public_run(fixture["output"])
        self.assertEqual(public["sessions"], 56)
        self.assertEqual(result["sessions"], 56)
        self.assertFalse(export.load(fixture["output"] / "summary.json")["publication_ready"])
        return public

    def test_accepte_25_sur_28_et_conserve_les_trois_demi_reussites(self):
        fixture = diagnostic(self.root, {f"cas-{i:02d}": "DEMI-RÉUSSITE" for i in (1, 2, 3)})
        public = self.check_export(fixture)
        self.assertEqual(public["totals"], {"RÉUSSITE": 25, "DEMI-RÉUSSITE": 3, "ÉCHEC": 0})
        human = export.load(fixture["output"] / "provenance.json")["human_review"]
        self.assertEqual(human["demi_reussites"], ["cas-01", "cas-02", "cas-03"])
        self.assertEqual(human["reserves"], {})

    def test_accepte_27_sur_28_et_reserve_exacte_visible(self):
        text = "SIMULATION : réserve de forme.\nTexte exact ; `citation` et ``` conservés."
        fixture = diagnostic(self.root, {"cas-06": "DEMI-RÉUSSITE"}, {"cas-06": text})
        before = {p: export.digest(p.read_bytes()) for p in fixture["attempt"].rglob("*") if p.is_file()}
        public = self.check_export(fixture)
        self.assertEqual(public["totals"]["RÉUSSITE"], 27)
        target = fixture["output"]
        self.assertTrue((target / "avis-humain-jo-20261023.json").is_file())
        self.assertEqual((target / "avis-humain-jo-20261023.json").read_bytes(), fixture["review_path"].read_bytes())
        self.assertIn(text, (target / "relecture-reserves.md").read_text(encoding="utf-8"))
        self.assertEqual(export.load(target / "provenance.json")["human_review"]["reserves"], {"cas-06": text})
        case = export.load(target / "progression.json")["cases"][5]
        self.assertEqual((case["verdict"], case["human_verdict"], case["reserve"]), ("DEMI-RÉUSSITE", "en réserve", text))
        self.assertEqual(before, {p: export.digest(p.read_bytes()) for p in before})

    def test_echec_standard_autorise_si_seuil_atteint_sans_echec_critique(self):
        fixture = diagnostic(self.root, {"cas-01": "ÉCHEC", "cas-02": "DEMI-RÉUSSITE", "cas-03": "DEMI-RÉUSSITE"},
                             {"cas-01": "SIMULATION : réserve explicitement maintenue."})
        self.assertEqual(self.check_export(fixture)["totals"]["RÉUSSITE"], 25)

    def test_refuse_seuil_non_atteint(self):
        fixture = diagnostic(self.root, {f"cas-{i:02d}": "DEMI-RÉUSSITE" for i in (1, 2, 3, 4)})
        with self.assertRaisesRegex(ValueError, "seuil non atteint"):
            export.export(**fixture)
        self.assertFalse(fixture["output"].exists())

    def test_refuse_echec_critique_meme_avec_27_reussites(self):
        fixture = diagnostic(self.root, {"cas-21": "ÉCHEC"})
        with self.assertRaisesRegex(ValueError, "ÉCHEC critique"):
            export.export(**fixture)
        summary_path = fixture["attempt"] / "kit/resultats/summary.json"
        summary = export.load(summary_path)
        summary.update(threshold_passed=True, critical_failures=[])
        save(summary_path, summary)
        with self.assertRaisesRegex(ValueError, "ÉCHEC critique"):
            export.export(**fixture)

    def test_refuse_reserve_vide_inconnue_ou_statut_incoherent(self):
        fixture = diagnostic(self.root, reserves={"cas-06": "SIMULATION : texte de réserve."})
        original = export.load(fixture["review_path"])
        invalid = []
        for text in ("", " \n\t", None, {}, []):
            review = deepcopy(original)
            review["reserves"]["cas-06"] = text
            invalid.append(review)
        for reserves in ({"inconnu": "texte"}, {}, [], None):
            review = deepcopy(original)
            review["reserves"] = reserves
            invalid.append(review)
        review = deepcopy(original)
        review["verdicts"]["cas-06"] = "conforme"
        invalid.append(review)
        for review in invalid:
            with self.subTest(review=review["reserves"]):
                save(fixture["review_path"], review)
                with self.assertRaisesRegex(ValueError, "[Rr]éserve"):
                    export.export(**fixture)
                self.assertFalse(fixture["output"].exists())

    def test_refuse_avis_incomplet_et_non_lie(self):
        fixture = diagnostic(self.root)
        original = export.load(fixture["review_path"])
        for field, value in (("tete", "0" * 40), ("tentative", "autre"),
                             ("resume_final_sha256", "0" * 64), ("fiche_relecture_sha256", "0" * 64),
                             ("decideur", "autre"), ("verdicts", {})):
            with self.subTest(field=field):
                save(fixture["review_path"], {**original, field: value})
                with self.assertRaises(ValueError):
                    export.export(**fixture)
                self.assertFalse(fixture["output"].exists())

    def test_refuse_dates_invalides_traversee_unicode_et_date_non_liee(self):
        fixture = diagnostic(self.root)
        for value in (None, "20261023", "2026-10-24", "2026-02-30", "2026-13-01",
                      "../../2026-10-23", "２０２６-10-23", "2026-10-23\n", "2026-1-23"):
            with self.subTest(date=value), self.assertRaisesRegex(ValueError, "Date d'avis"):
                export.export(**{**fixture, "review_date": value})
        review = export.load(fixture["review_path"])
        review["date_utc"] = "2026-10-23T12:00:00"
        save(fixture["review_path"], review)
        with self.assertRaisesRegex(ValueError, "Date d'avis"):
            export.export(**fixture)

    def test_refuse_toute_derive_des_octets_scelles_et_des_roles(self):
        fixture = diagnostic(self.root)
        attempt = fixture["attempt"]
        paths = [attempt.parent / "MANIFESTE-LANCEUR-D1.json", attempt.parent / "PLAN-D1.json",
                 attempt.parent / "autorisation-jo.json", self.root / "PLAN-MESURE-D0.md",
                 self.root / "preuves/SCELLEMENT-D0.json", attempt / "kit/scripts/eval_suite.py",
                 attempt / "kit/runtime/SKILL.md", attempt / "kit/resultats/suite.json",
                 attempt / "kit/resultats/bareme.md", attempt / "kit/resultats/cas-01/prompt.md",
                 attempt / "kit/resultats/cas-01/response.md", attempt / "kit/resultats/cas-01/judgment.json",
                 attempt / "kit/resultats/cas-01/juge-execution.json", attempt / "kit/resultats/cas-01/juge-stdout.txt",
                 attempt / "kit/resultats/cas-01/juge-stderr.txt", attempt / "kit/resultats/cas-21/controle-stop.json"]
        for path in paths:
            original = path.read_bytes()
            try:
                path.write_bytes(original + b"\nCANARI\n")
                with self.subTest(file=path.name), self.assertRaises((ValueError, OSError)):
                    export.export(**fixture)
                self.assertFalse(fixture["output"].exists())
            finally:
                path.write_bytes(original)

    def test_scanner_refuse_une_reserve_contenant_un_secret(self):
        fixture = diagnostic(self.root, reserves={"cas-06": "SIMULATION : Bearer " + "factice_" * 5})
        with self.assertRaisesRegex(ValueError, "motifs privés"):
            export.export(**fixture)
        self.assertFalse(fixture["output"].exists())

    def test_refuse_controleur_roles_usage_et_budget_incoherents(self):
        fixture = diagnostic(self.root)
        controller_path = fixture["attempt"] / "resume-final.json"
        original = export.load(controller_path)
        review = export.load(fixture["review_path"])
        changes = []
        for key, value in (("status", "stopped"), ("failure", "SIMULATION erreur"),
                           ("input_tokens_complete", False), ("sessions_started", 55),
                           ("input_tokens_limit", 10_000_001), ("input_tokens_total_known", 561)):
            changes.append({**deepcopy(original), key: value})
        for key, value in (("status", "failed"), ("process_exit", 1), ("usage_complete", False),
                           ("usage", {"input_tokens": 11, "cached_input_tokens": 3, "output_tokens": 2})):
            modified = deepcopy(original)
            modified["roles"][0][key] = value
            changes.append(modified)
        modified = deepcopy(original)
        modified["roles"][1]["thread_id"] = modified["roles"][0]["thread_id"]
        changes.append(modified)
        modified = deepcopy(original)
        modified["stop_header_checks"][0]["sha256"] = "0" * 64
        changes.append(modified)
        modified = deepcopy(original)
        modified["roles"][0], modified["roles"][1] = modified["roles"][1], modified["roles"][0]
        changes.append(modified)
        for index, controller in enumerate(changes):
            save(controller_path, controller)
            save(fixture["review_path"], {**review, "resume_final_sha256": export.digest(controller_path.read_bytes())})
            with self.subTest(index=index), self.assertRaises(ValueError):
                export.export(**fixture)
            self.assertFalse(fixture["output"].exists())

    def test_refuse_budget_depasse_meme_avec_liens_reempreintes(self):
        fixture = diagnostic(self.root)
        plan_dir = fixture["attempt"].parent
        auth_path = plan_dir / "autorisation-jo.json"
        auth_original = export.load(auth_path)
        controller_path = fixture["attempt"] / "resume-final.json"
        controller = export.load(controller_path)
        review = export.load(fixture["review_path"])
        for key, value in (("max_input_tokens", 10), ("max_sessions", 55)):
            save(auth_path, {**auth_original, key: value})
            launcher_path = plan_dir / "MANIFESTE-LANCEUR-D1.json"
            launcher = export.load(launcher_path)
            launcher["files"][auth_path.name] = {"sha256": export.digest(auth_path.read_bytes()), "octets": auth_path.stat().st_size}
            save(launcher_path, launcher)
            save(controller_path, {**controller, "launcher_manifest_sha256": export.digest(launcher_path.read_bytes())})
            save(fixture["review_path"], {**review, "resume_final_sha256": export.digest(controller_path.read_bytes())})
            with self.subTest(key=key), self.assertRaisesRegex(ValueError, "plafond"):
                export.export(**fixture)
            self.assertFalse(fixture["output"].exists())

    def test_refuse_destination_existante_et_chemins_de_preuve_traversants(self):
        fixture = diagnostic(self.root)
        fixture["output"].mkdir()
        with self.assertRaisesRegex(ValueError, "Destination neuve"):
            export.export(**fixture)
        for name in ("../avis.json", "/avis.json", "Z:/avis.json", "a\\avis.json"):
            with self.subTest(name=name), self.assertRaisesRegex(ValueError, "Chemin"):
                export.safe_relative(self.root, name)

    def test_reempreinter_ne_suffit_pas_pour_masquer_une_reserve_publique(self):
        fixture = diagnostic(self.root, {"cas-06": "DEMI-RÉUSSITE"}, {"cas-06": "SIMULATION : réserve exacte."})
        self.check_export(fixture)
        target = fixture["output"]
        report = target / "relecture-reserves.md"
        report.write_bytes(b"Aucune reserve.\n")
        inventory = export.load(target / "empreintes.json")
        inventory["files"][report.name] = export.digest(report.read_bytes())
        save(target / "empreintes.json", inventory)
        with self.assertRaisesRegex(ValueError, "Réserves publiques"):
            export.verify_public_run(target)

    def test_historique_reste_strict_sans_reserve_et_nom_inchange(self):
        run = export.ROOT / "tests/runs/codex-web-v0.1.4-dcp-stop-20261020-a"
        result = export.verify_public_run(run)
        self.assertEqual(result["totals"]["RÉUSSITE"], 28)
        review = export.load(run / "avis-humain-jo-20261020.json")
        cases = export.eval_suite.load_cases(run / "suite.json")
        self.assertEqual(export.review_filename(review, "0.1.4"), "avis-humain-jo-20261020.json")
        review["reserves"] = {"cas-06": "SIMULATION, refus en historique."}
        with self.assertRaisesRegex(ValueError, "historique"):
            export.validate_review(review, cases, "0.1.4")


if __name__ == "__main__":
    unittest.main()
