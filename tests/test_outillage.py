"""Régressions : mesure incomplète, preuve altérée et exclusion du cache."""

import hashlib
import json
import re
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import eval_suite
import package_skill
import validate_repo
from support_outillage import fixture_cases


class PreuvesMesure(unittest.TestCase):
    """Exerce des échecs qui pourraient attribuer un score trompeur."""

    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.run = Path(self.temporary.name) / "mesure"
        eval_suite.prepare_run(self.run, "modèle de test", "juge de test", fixture_cases(Path(self.temporary.name)))

    def complete(self, critical_failure=False):
        for case in eval_suite.load_cases(self.run / "suite.json"):
            directory = self.run / eval_suite.case_dir_name(case)
            response = directory / "response.md"
            response.write_text("Réponse factice de test logiciel, aucune mesure du skill.\n", encoding="utf-8", newline="\n")
            judgment = {"verdict": "ÉCHEC" if critical_failure and case["id"] == "cas-21" else "RÉUSSITE",
                        "notes": "Artefact factice de test logiciel.",
                        "response_sha256": eval_suite.suite_digest(response)}
            (directory / "judgment.json").write_text(json.dumps(judgment), encoding="utf-8", newline="\n")

    def test_campagne_preparee_ne_produit_pas_de_score(self):
        with self.assertRaisesRegex(ValueError, "Artefacts manquants"):
            eval_suite.validate_run(self.run)
        self.assertFalse((self.run / "summary.json").exists())

    def test_preparation_non_ecrasable(self):
        with self.assertRaises(ValueError):
            eval_suite.prepare_run(self.run, "autre", "autre")

    def test_suite_alteree_refusee(self):
        (self.run / "suite.json").write_text("[]")
        with self.assertRaisesRegex(ValueError, "empreinte"):
            eval_suite.validate_run(self.run)

    def test_bareme_altere_refuse(self):
        (self.run / "bareme.md").write_text("barème différent")
        with self.assertRaisesRegex(ValueError, "Barème"):
            eval_suite.validate_run(self.run)

    def test_prompt_altere_refuse(self):
        (self.run / "cas-01" / "prompt.md").write_text("autre prompt")
        with self.assertRaisesRegex(ValueError, "prompt altéré"):
            eval_suite.validate_run(self.run)

    def test_jugement_non_lie_refuse(self):
        self.complete()
        (self.run / "cas-01" / "response.md").write_text("réponse modifiée")
        with self.assertRaisesRegex(ValueError, "jugement non rattaché"):
            eval_suite.validate_run(self.run)

    def test_echec_critique_bloque_malgre_score_global(self):
        self.complete(critical_failure=True)
        totals = eval_suite.validate_run(self.run)
        summary = json.loads(eval_suite.write_summary(self.run, totals).read_text())
        self.assertEqual(summary["totals"]["RÉUSSITE"], 27)
        self.assertFalse(summary["threshold_passed"])
        self.assertEqual(summary["critical_failures"], ["cas-21"])

    def test_seuil_ne_remplace_pas_relecture_praticien(self):
        self.complete()
        summary = json.loads(eval_suite.write_summary(self.run, eval_suite.validate_run(self.run)).read_text())
        self.assertTrue(summary["threshold_passed"])
        self.assertFalse(summary["publication_ready"])


class Packaging(unittest.TestCase):
    def test_cache_et_conception_exclus(self):
        paths = {p.relative_to(package_skill.ROOT).as_posix() for p in package_skill.runtime_files()}
        self.assertIn("references/references-verifiees.md", paths)
        self.assertNotIn("references/cache-valeurs.md", paths)
        self.assertFalse(any(p.startswith(("tests/", "docs/", "vault/")) for p in paths))

    def test_destination_hors_depot_refusee(self):
        with self.assertRaises(ValueError):
            package_skill.checked_output("/tmp/dcp-fpt.zip", "0.1.0")

    def test_source_non_ecrasable(self):
        with self.assertRaises(ValueError):
            package_skill.checked_output("SKILL.md", "0.1.0")

    def test_determinisme_archive(self):
        with tempfile.TemporaryDirectory() as temporary:
            first, second = (Path(temporary) / name for name in ("a.zip", "b.zip"))
            package_skill.write_package(first)
            package_skill.write_package(second)
            self.assertEqual(hashlib.sha256(first.read_bytes()).digest(),
                             hashlib.sha256(second.read_bytes()).digest())

    def test_metadonnees_archive_independantes_de_os(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "paquet.zip"
            package_skill.write_package(output)
            with zipfile.ZipFile(output) as archive:
                for info in archive.infolist():
                    with self.subTest(fichier=info.filename):
                        self.assertEqual(info.create_system, 3)
                        self.assertEqual(info.create_version, 20)
                        self.assertEqual(info.extract_version, 20)
                        self.assertEqual(info.date_time, package_skill.FIXED_TIMESTAMP)
                        self.assertEqual(info.external_attr, 0o100644 << 16)

    def test_empreinte_publiee_correspond_au_paquet(self):
        """La CI Windows/Linux doit retrouver la même empreinte publiée."""
        report = (package_skill.ROOT / "docs" / "etat-avancement.md").read_text(encoding="utf-8")
        match = re.search(r"^- SHA-256 du paquet corrigé : `([0-9a-f]{64})`\.$", report, re.M)
        self.assertIsNotNone(match, "Empreinte du paquet corrigé absente du relevé")
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "paquet.zip"
            package_skill.write_package(output)
            self.assertEqual(hashlib.sha256(output.read_bytes()).hexdigest(), match.group(1))


class InvariantsRedaction(unittest.TestCase):
    """Bloque les régressions de périmètre et les valeurs embarquées."""

    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.patcher = patch.object(validate_repo, "ROOT", self.root)
        self.patcher.start()
        self.addCleanup(self.patcher.stop)

    def write(self, relative, content):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8", newline="\n")

    def test_absence_suite_toleree_uniquement_sur_demande(self):
        strict = validate_repo.Validation()
        validate_repo.validate_cases(strict)
        self.assertTrue(strict.errors)
        scoped = validate_repo.Validation(sans_campagne=True)
        validate_repo.validate_cases(scoped)
        self.assertFalse(scoped.errors)
        self.assertEqual(len(scoped.warnings), 1)

    def test_mode_sans_campagne_ne_masque_pas_suite_invalide(self):
        self.write("tests/cas-de-test.json", "[]")
        validation = validate_repo.Validation(sans_campagne=True)
        validate_repo.validate_cases(validation)
        self.assertTrue(validation.errors)

    def test_mode_sans_campagne_ne_tolere_pas_branche_absente(self):
        validation = validate_repo.Validation(sans_campagne=True)
        validate_repo.check_inventory(validation, self.root / "references",
                                      validate_repo.BRANCH_FILES, "references/")
        self.assertTrue(validation.errors)

    def test_pourcentage_bloque_dans_branche_et_point_entree(self):
        for path in ("references/modifications.md", "SKILL.md"):
            with self.subTest(path=path):
                self.write(path, "Limite non sourcée : 12,5 %")
                validation = validate_repo.Validation()
                validate_repo.validate_forbidden_content(validation)
                self.assertTrue(any("pourcentage" in e for e in validation.errors))

    def test_identifiant_hors_registre_bloque_socle_hors_runtime_autorise(self):
        identifier = "LEGIARTI" + "000000000001"
        self.write("docs/socle/lot-factice.md", identifier)
        self.write("references/references-verifiees.md", identifier)
        validation = validate_repo.Validation()
        validate_repo.validate_forbidden_content(validation)
        self.assertFalse(validation.errors)
        self.write("references/modifications.md", identifier)
        validation = validate_repo.Validation()
        validate_repo.validate_forbidden_content(validation)
        self.assertTrue(any("identifiant" in e for e in validation.errors))

    def test_frontiere_dsi_requise_dans_description(self):
        description = "dpo-ct drh-fpt dpm-fpt dirfi-fpt"
        self.write("SKILL.md", f"---\nname: dcp-fpt\ndescription: {description}\n---\n")
        validation = validate_repo.Validation()
        validate_repo.validate_frontmatter(validation)
        self.assertTrue(any("dsi-fpt" in e for e in validation.errors))

    def test_retrait_stop_bloque(self):
        snippets = validate_repo.REQUIRED_GUARDRAIL_SNIPPETS
        for removed in snippets[:1] + snippets[3:4]:
            with self.subTest(removed=removed):
                self.write("SKILL.md", "\n".join(s for s in snippets if s != removed))
                validation = validate_repo.Validation()
                validate_repo.validate_guardrail_invariants(validation)
                self.assertTrue(validation.errors)


if __name__ == "__main__":
    unittest.main()
