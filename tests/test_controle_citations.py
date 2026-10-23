"""Contre-exemples de citation ; aucune inférence, aucun verdict réécrit."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import controle_citations as control
import eval_suite
import mesure_locale

ROOT = Path(__file__).resolve().parents[1]
HISTORICAL = ROOT / "tests/runs/codex-web-v0.1.4-dcp-stop-20261020-a"


class CitationTests(unittest.TestCase):
    def test_chemins_liens_hotes_encodages_et_absolus(self):
        fixtures = [
            'SKILL.md', '`references/`', 'objets/accord-cadre.md',
            '.agents/skills/dcp-fpt/SKILL.md', r'references\procedures.md',
            '[skill](references/procedures.md)', '[skill](<X:/a b/SKILL.md>)',
            '[skill](https://example.invalid/SKILL.md)',
            'https://example.invalid/references/a.md',
            '<https://www.legifrance.gouv.fr/objets/accord-cadre.md>',
            'https://example.invalid/%53KILL%2Emd',
            '[skill][ref]\n[ref]: references/a.md',
            'file:///opt/local/skill.txt', '/tmp/a.txt', '/opt/skill/fichier.txt',
            r'Z:\dossier\fichier.txt', r'\\serveur\partage\fichier.txt',
        ]
        for fixture in fixtures:
            with self.subTest(fixture=fixture):
                self.assertEqual(len(control.occurrences(fixture)), 1)

    def test_sources_officielles_et_reference_par_nom_permises(self):
        for text in (
            'dcp-fpt, objet accord-cadre, §3',
            '[Source](https://www.legifrance.gouv.fr/codes/article_lc/EXEMPLE)',
            '<https://www.economie.gouv.fr/daj/commande-publique>',
            'https://www.collectivites-locales.gouv.fr/commande-publique',
            'https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=EXEMPLE',
            'La section et les références officielles restent à lire.',
        ):
            with self.subTest(text=text):
                self.assertEqual(control.occurrences(text), [])

    def test_toutes_occurrences_sans_double_compte_et_sans_fuite(self):
        text = '[x](Z:/factice/SKILL.md) puis objets/a.md et SKILL.md\nreferences/b.md'
        check = control.check_response('cas-01', text.encode())
        self.assertEqual(check['occurrence_count'], 4)
        self.assertEqual([a['line'] for a in check['occurrences']], [1, 1, 1, 2])
        self.assertNotIn('factice', json.dumps(check))
        self.assertFalse(check['verdict_modified'])

    def test_28_reponses_historiques_lecture_seule_et_cli_informative(self):
        before = {p: hashlib.sha256(p.read_bytes()).hexdigest() for p in HISTORICAL.rglob('*') if p.is_file()}
        audit = control.audit_run(HISTORICAL)
        self.assertEqual(len(audit['checks']), 28)
        self.assertTrue(all(not c['verdict_modified'] for c in audit['checks']))
        process = subprocess.run([sys.executable, str(Path(control.__file__)), '--run-dir', str(HISTORICAL)],
                                 capture_output=True, check=False)
        self.assertEqual(process.returncode, 0, process.stderr)
        self.assertEqual(json.loads(process.stdout), audit)
        self.assertEqual(before, {p: hashlib.sha256(p.read_bytes()).hexdigest() for p in before})
        with self.assertRaisesRegex(ValueError, 'inconnu'):
            control.audit_run(HISTORICAL, ['inconnu'])

    def test_kit_scelle_copie_barreme_et_controle_sans_jugement(self):
        with tempfile.TemporaryDirectory() as temporary:
            folder = Path(temporary)
            run, kit = folder / 'run', folder / 'kit'
            eval_suite.prepare_run(run, 'factice', 'factice')
            mesure_locale.export_kit(kit, run)
            self.assertEqual((kit / 'resultats/bareme.md').read_bytes(), (ROOT / 'tests/bareme-cas-de-test.md').read_bytes())
            frozen = json.loads((kit / 'kit.json').read_bytes())
            self.assertIn('controle_citations.py', frozen['scripts_sha256'])
            for case in eval_suite.load_cases():
                (kit / 'resultats' / case['id'] / 'response.md').write_text('SKILL.md\n', encoding='utf-8')
            self.assertEqual(control.audit_run(kit / 'resultats')['occurrence_count'], 28)
            self.assertFalse(list((kit / 'resultats').glob('cas-*/judgment.json')))
            (kit / 'scripts/controle_citations.py').write_text('altéré', encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'altéré'):
                mesure_locale.verify_kit(kit)

    def test_refus_preuves_absentes_ou_alterees(self):
        with tempfile.TemporaryDirectory() as temporary:
            run = Path(temporary) / 'run'
            eval_suite.prepare_run(run, 'factice', 'factice')
            with self.assertRaises(FileNotFoundError):
                control.audit_run(run)
            (run / 'suite.json').write_text('[]', encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'altéré'):
                control.audit_run(run)


if __name__ == '__main__':
    unittest.main()
