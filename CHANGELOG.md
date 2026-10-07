# Historique — dcp-fpt

## [Non publié] — 2026-10-07

### Ajouté (hors runtime)
- `tests/cas-de-test.json` : suite de 28 cas du cadrage §9 (12 branches,
  6 objets, 2 gabarits, 8 cas critiques), attendus limités au socle vérifié,
  sans valeur ni identifiant.
- Relecture contradictoire en lecture seule (second modèle) : deux
  contradictions avec le skill et neuf imprécisions corrigées avant dépôt.
- Validation complète en CI (sans `--sans-campagne`) : schéma, 28 cas,
  couverture et classification sont contrôlés.

### Inchangé
Runtime (`SKILL.md`, `references/`, `objets/`), registre, cache : version
0.1.0 conservée, empreinte du paquet identique. **Suite écrite, jamais
lancée : aucun score.** Statut : non mesuré, non relu par un praticien.

## [0.1.0] — 2026-10-06

Point d'entrée, routeur, douze branches, six objets, cinq gabarits,
quatre scripts et contrôles CI. STOP égalité/acte irréversible et frontières
explicites. Registre/socle conservés, cache exclu du runtime, lacunes réservées.
Gabarits [INCOMPLET] tant que faits, source ou compétence manquent.

**Non mesuré, non relu par un praticien** : aucune suite métier/campagne,
intégration plugin ou modification des autres skills. Tests logiciels avec
entrées factices temporaires uniquement.

Relecture PR #4 : retrait du chemin utilisateur, normalisation des
métadonnées ZIP avec contrôle de l'empreinte sur Windows et Ubuntu,
clarification du rôle du juge en contentieux et prérequis MCP/CLI avant mesure.
