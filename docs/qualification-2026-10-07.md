# Qualification autonome DCP — 2026-10-07

## Périmètre

Phase autorisée après intégration candidate dans le plugin 1.2.0. La suite
comprend les 28 cibles du cadrage, dont huit critiques, avec uniquement des
situations fictives. Runtime mesuré : DCP 0.1.0, identique au commit amont
`eeb1cb1` épinglé dans le plugin ; registre, cache et branches inchangés.
Le paquet reste celui de la rédaction, sans cache ni conception.

## Protocole retenu

Kit `codex-web-v0.1.0-r2`, CLI Codex 0.160.0, modèles demandés
`gpt-6.1-sol` pour répondant et juge. Processus et dossier neufs pour chaque
rôle, contexte de réponse sans attendus ni barème, juge sans runtime ni web.
Le répondant a le web et le runtime natif ; aucune configuration MCP
personnelle n'est importée. Exécution séquentielle et reprise avec contrôle
des empreintes de réponse, jugement, entrées et sorties.

Sous Windows, le backend sandbox est rétabli explicitement malgré
`--ignore-user-config`, avec lecture seule. L'essai `r1` du cas-23 est
conservé hors dépôt comme contrôle d'environnement ; ses lectures de branches
ont été bloquées et il n'est pas compté. `r2` confirme ces lectures.

## Preuves

Les réponses, jugements, métadonnées et traces assainies sont dans
`tests/runs/codex-web-v0.1.0-r2/`. `progression.json` indique les cas achevés ;
`summary.json` n'apparaît qu'après les 28 jugements et le contrôle complet.
Les flux bruts restent dans le kit local hors dépôt. Raisonnements,
signatures et débogage ne sont pas publiés. Les empreintes des bruts sont
conservées dans les métadonnées d'exécution.

La correspondance des citations avec les URL effectivement ouvertes est
contrôlée dans les traces. Une différence d'URL est un signal de relecture,
pas une preuve automatique d'erreur : les variantes datées demandent examen.
Le juge ne confirme pas indépendamment les sources. Aucun seuil n'est
déclaré sur un sous-ensemble ni à partir des fixtures unitaires.

## Point de relecture identifié

Le cas-01 est jugé ÉCHEC : absence de BASCULE financière. La relecture doit
examiner la séparation entre méthode juridique d'estimation pour choisir la
procédure et calcul financier effectivement délégué à dirfi-fpt. La réponse
et le jugement sont conservés ; ni attendu ni verdict ne sont réécrits pour
faire passer cet essai. Le cas-24 éprouve explicitement révision et pénalités.

## Qualification distincte du plugin

La campagne plugin porte sur neuf cas et impose ses propres coactivations
et outils MCP. Le processus Claude charge les six skills du candidat, mais
son MCP indique `needs-auth` et le compte une limite de session. La recherche
MCP réussie dans la session Codex principale ne qualifie pas ce processus.
Une mesure autonome web ne remplace pas cette campagne.

Le smoke local Codex du 2026-10-07 vérifie les six copies natives, leurs
versions, le manifeste, les deux STOP DCP et le contrat DRH, en lecture seule.
Il ne teste ni une installation marketplace ni le MCP. La relecture par
un acheteur public ou juriste reste à réaliser avec la grille dédiée.
Distribution gelée sur v1.1.1 ; aucune promotion, étiquette ni publication.
