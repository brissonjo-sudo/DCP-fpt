# État d'avancement — dcp-fpt v0.1.0

Date : 2026-10-06. Périmètre : docs/passation-redaction.md.
Statut produit : **non mesuré, non relu par un praticien**.

| Livrable | État |
|---|---|
| Point d'entrée, neuf sections, STOP/frontières | Rédigé avant branches |
| Routeur et deux gabarits | Rédigés avant branches |
| Douze branches | Rédigées, lacunes réservées |
| Six objets | Rédigés, parcours par pointeurs |
| Cinq écrits | Brouillons anonymisés et [INCOMPLET] si manque |
| Quatre scripts, tests, CI, index | Adaptés, contrôles locaux réussis ; CI distante à suivre |
| Registre/cache/docs-socle | Conservés sans nouvelle attestation |
| Suite métier/campagne/relecture | Non réalisées, hors périmètre |
| Plugin/autres skills/fusion | Hors périmètre, aucun changement |

## Provenance de l'outillage

Patron brissonjo-sudo/DSI-fpt, branche codex/achever-redaction-outillage-dsi,
commit `e4a2439f59b61d44befa3a4f473791a38aa86f7b`. Aucun résultat DSI copié.
Adaptations : inventaires DCP, frontières, garde-fous, pourcentages,
docs/socle autorisés à porter les identifiants hors runtime,
`--sans-campagne` limité à la suite absente et fixtures temporaires.
Preuves en UTF-8/LF pour la reprise Windows.

## Points ouverts

Lacunes de passation signalées dans branches et grille de relecture. Aucune
doctrine non ouverte citée, aucune citation littérale jurisprudentielle
reprise, aucune portée récente déclarée acquise. Toute nouvelle vérification
ira au lot puis au registre. Rédaction sans attestation de lecture juridique
nouvelle en session.

## Preuves de livraison

Contrôles Windows/PowerShell du 2026-10-06, Python embarqué **3.12.14** :

```powershell
python scripts/validate_repo.py --sans-campagne
python -m unittest discover -s tests -p 'test_*.py'
python scripts/package_skill.py
```

Exécutable utilisé :
`C:\Users\Krn\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe`.
Environnement `PYTHONUTF8=1` pour les sorties françaises.

- Validation : **625 contrôles**, zéro erreur ; seul avertissement : suite
  métier absente, conformément au périmètre.
- Tests logiciels : **33 réussis**, CLI simulées et fixtures temporaires.
- Validateur skill-creator : **Skill is valid!**, avec Python 3.13 existant
  (le runtime embarqué ne contient pas PyYAML ; aucune dépendance installée).
- Paquet : **30 fichiers**, cache et conception exclus, déterminisme testé.
- SHA-256 : `a976a02d9973acd6c029174a4f9618b84e20906402a4976f62fff6302f2acd6d`.
- Registre, cache, méthode de sources et docs/socle : aucun diff Git.
- Suite métier et tests/runs absents ; aucun modèle réellement appelé.

CI distante et PR : à constater après envoi de la branche. Tests/CI distincts
de mesure et de relecture ; aucun score métier ni permission de fusion.
