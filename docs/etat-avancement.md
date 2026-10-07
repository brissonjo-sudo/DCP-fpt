# État d'avancement — dcp-fpt v0.1.0

## Actualisation du 2026-10-07

Rédaction fusionnée par la PR #4 ; intégration candidate du plugin fusionnée
par les PR #10 puis #9. Distribution toujours gelée sur v1.1.1, sans DCP.
Suite métier rédigée : 28 cas, huit critiques. CI passée en validation complète.
Profil autonome Codex web et profil plugin MCP séparés (ADR 0002).
Mesure autonome en cours ; relecture praticien non réalisée. Les 36 tests
logiciels passent, dont le correctif du backend sandbox Windows.
Le relevé ci-dessous conserve le périmètre historique de la rédaction.
Preuves de la nouvelle phase : `docs/qualification-2026-10-07.md`.

## État historique de la passation du 2026-10-06

Date : 2026-10-06. Périmètre : docs/passation-redaction.md.
Statut produit : **non mesuré, non relu par un praticien**.

| Livrable | État |
|---|---|
| Point d'entrée, neuf sections, STOP/frontières | Rédigé avant branches |
| Routeur et deux gabarits | Rédigés avant branches |
| Douze branches | Rédigées, lacunes réservées |
| Six objets | Rédigés, parcours par pointeurs |
| Cinq écrits | Brouillons anonymisés et [INCOMPLET] si manque |
| Quatre scripts, tests, CI, index | Adaptés, contrôles locaux et CI distante réussis |
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

Exécutable utilisé : Python embarqué du runtime Codex, **3.12.14**.
Environnement `PYTHONUTF8=1` pour les sorties françaises.

- Validation : **625 contrôles**, zéro erreur ; seul avertissement : suite
  métier absente, conformément au périmètre.
- Tests logiciels initiaux : **33 réussis**, CLI simulées et fixtures temporaires.
- Validateur skill-creator : **Skill is valid!**, avec Python 3.13 existant
  (le runtime embarqué ne contient pas PyYAML ; aucune dépendance installée).
- Paquet : **30 fichiers**, cache et conception exclus. Le test initial ne
  prouvait que le déterminisme sur une même machine ; métadonnées ZIP
  désormais normalisées après relecture pour retirer la dépendance à l'OS.
- Empreinte initiale Windows retirée : elle n'était pas reproductible sous Linux.
- SHA-256 du paquet corrigé : `a74ed0222561d3836c7d80c0a4aa3af05cfec953d28d9971df730867a70af9b3`.
- Registre, cache, méthode de sources et docs/socle : aucun diff Git.
- Suite métier et tests/runs absents ; aucun modèle réellement appelé.

PR vers main : [#4](https://github.com/brissonjo-sudo/DCP-fpt/pull/4), ouverte,
sans fusion, branche codex/redaction-outillage-dcp.

CI distante sur le commit de rédaction `78ba1a846384b49ff6dbeb021e0d1d3821b1cd1a`,
observée le 2026-10-06 :

- [Push](https://github.com/brissonjo-sudo/DCP-fpt/actions/runs/37516401449) : réussi.
- [Pull request](https://github.com/brissonjo-sudo/DCP-fpt/actions/runs/37516412441) : réussi.
- Les trois étapes (validation sans campagne, tests, paquet) sont vertes sur
  Ubuntu/Python 3.12, en plus des contrôles Windows locaux.

Tests/CI distincts de mesure et de relecture ; aucun score métier ni permission
de fusion. Ce relevé porte sur le commit de rédaction ; l'ajout de ce relevé
est un commit documentaire distinct soumis à la même CI.

## Prise en compte de la relecture de la PR #4

Le chemin utilisateur a été retiré. Le paquet fixe désormais le système
créateur, les versions ZIP et les permissions ; deux tests supplémentaires
contrôlent les métadonnées de chaque entrée et l'empreinte publiée ci-dessus.
La CI exécute les mêmes contrôles sur Windows et Ubuntu, avec Python 3.12.
Les deux systèmes ont réussi sur le commit corrigé `2b168fe`, avec la même
empreinte publiée : [CI PR](https://github.com/brissonjo-sudo/DCP-fpt/actions/runs/37518012410)
et [CI push](https://github.com/brissonjo-sudo/DCP-fpt/actions/runs/37518005873).
L'ajout de ce relevé est un commit documentaire soumis à la même CI.
Revalidation locale du 2026-10-06 : **625 contrôles statiques sans erreur**
et **35 tests logiciels réussis**, avec le seul avertissement attendu
concernant la suite métier absente. L'empreinte du paquet corrigé est
contrôlée par ces tests.

La branche contentieux attribue au juge le contrôle de l'intérêt à agir et
de la lésion ; le conseil en apprécie le risque. Les prérequis MCP et CLI
avant mesure sont consignés dans docs/campagne-locale.md et restent ouverts.
Aucune campagne ni fusion n'est réalisée au titre de ces corrections.
