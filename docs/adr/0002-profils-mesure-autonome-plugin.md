# ADR 0002 — Séparer mesure autonome et qualification du plugin

- Date : 2026-10-07.
- Statut : accepté pour la préparation et les contrôles autorisés.
- Autorisation : poursuite demandée après intégration du candidat plugin.

## Décision

La suite autonome comporte les 28 cas du cadrage, dont huit critiques. Les
attendus éprouvent le contenu du runtime et ses réserves ; aucun nouveau
identifiant officiel ni valeur juridique n'y est créé. La CI valide désormais
la suite avec le mode complet, sans tolérance de suite absente.

La mesure autonome retient Codex, runtime natif dans un dossier neuf,
répondant avec web et juge sans web. Modèle demandé : `gpt-6.1-sol` pour les
deux rôles. Chaque rôle s'exécute dans un processus distinct. La suite,
le runtime, le barème et les sorties sont empreintés. Aucun MCP personnel
n'est chargé pour remplacer silencieusement le profil défini.

Le runtime demeure celui de 0.1.0 épinglé dans le plugin à `eeb1cb1`. Les
changements de suite et de conception ne changent pas le paquet. Une
promotion future en 1.0.0 demandera un nouveau commit et une mesure attachée
au runtime promu ; les preuves de 0.1.0 ne sont pas renommées.

La campagne plugin reste distincte : six skills, neuf cas, Claude et appels
`mcp__droit-francais__*` pour les cas nominaux. Le contrôle du 2026-10-07 a
détecté `needs-auth` dans ce processus et la limite de session Claude. La
réussite d'une recherche MCP dans la session Codex principale ne qualifie
pas l'authentification du processus répondant Claude.

## Conséquences

Un seuil autonome atteint ne vaut ni qualification MCP, ni coactivation,
ni smoke du plugin, ni relecture par un acheteur ou juriste. Les résultats
partiels, erreurs de CLI et limites de quota sont conservés sans verdict
fabriqué. Les limites de l'isolation sur un même poste sont explicites.
La distribution reste `v1.1.1` ; `release_ready` et `publication_ready`
demeurent faux tant que les preuves requises ne sont pas réunies.
