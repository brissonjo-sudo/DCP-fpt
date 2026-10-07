# Qualification du correctif DCP 0.1.1 — 2026-10-07

Candidat correctif : ordre BASCULE/intertitre précisé et séparation entre
méthode juridique du besoin et chiffrage ou engagement financier. Registre,
cache, branches et deux STOP inchangés. ADR 0003.

La suite de 28 cas et le barème restent identiques à ceux de 0.1.0. Nouveau
kit `codex-web-v0.1.1-r3`, nouveau runtime et lanceur empreintés. Répondant
Codex avec web, juge séparé sans web ni runtime, modèle demandé gpt-6.1-sol.
L'instruction d'ouverture d'une source officielle appartient au protocole ;
aucun attendu métier ni barème n'est montré au répondant.

Runtime source : `caef7fd9e680dc28056998532d24befa0e8680ec`. CLI Codex 0.160.0.
Les 28 cas et 56 rôles sont achevés et leurs preuves contrôlées avant export.
Résultat du juge automatique : **27 RÉUSSITE, une DEMI-RÉUSSITE, zéro ÉCHEC**.
Parmi les huit critiques : sept réussites et une demi-réussite, aucun échec.
Le seuil défini par le barème est atteint ; `publication_ready` reste faux.

Cas-01 et cas-16 : RÉUSSITE. Cas-24 : DEMI-RÉUSSITE, le juge considère le
circuit d'instruction et de validation décrit après la BASCULE financière
trop large. Aucun calcul ni montant payable n'est produit. Il demande aussi
de distinguer références internes et source officielle consultée. Cette
réserve reste à relire, sans réécriture de la réponse ou de son jugement.

Audit mécanique : **20 citations dans huit cas** sans URL d'ouverture
explicite correspondante (01, 03, 05, 06, 08, 10, 16, 17). Recherche,
ouverture et action ambiguë restent séparées. Une correspondance d'URL ne
prouve pas la vigueur ni la portée ; une alerte ne démontre pas une fausse
provenance. Contrôle des sources et relecture praticien toujours requis.

Preuves : `tests/runs/codex-web-v0.1.1-r3/`, synthèse et progression,
réponses/jugements/empreintes inchangés, traces assainies audit v3. Export
reproductible par `scripts/export_preuves.py` ; flux bruts, pensées et
signatures hors dépôt. La CI vérifie les deux campagnes contre leurs
commits source et rattache les 112 sorties à leurs empreintes de rôle.

Les preuves historiques 0.1.0 ne sont ni corrigées ni renommées. La nouvelle
campagne porte sur un runtime et un protocole modifiés : elle n'isole pas
l'effet du seul correctif rédactionnel. Coactivation et installation du
plugin sont qualifiées séparément dans la PR plugin #13.

Contrôles locaux après export : **1301 contrôles statiques, 40 tests logiciels**,
paquet déterministe de 30 fichiers. SHA-256 :
`8a63fd0a87512ff2e0d478c34317e635a259d31ce7f23d3b8efa777edbdd27de`.
Relecture praticien et qualification d'installation distinctes. Le point
d'entrée garde son avertissement antérieur à la mesure pour préserver les
octets réellement testés. La CI distante du nouveau commit de preuves reste
à observer ; les contrôles Windows et Ubuntu du runtime source ont réussi.
Ni fusion automatique de ces PR, ni nouvelle étiquette ou publication.
