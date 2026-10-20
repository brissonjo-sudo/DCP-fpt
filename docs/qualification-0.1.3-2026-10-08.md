# Qualification DCP 0.1.3 — 2026-10-08

Les 28 cas et leurs 56 rôles sont achevés : **27 RÉUSSITE, une DEMI-RÉUSSITE,
zéro ÉCHEC**. Les huit cas critiques réussissent. Le seuil automatique est
atteint ; la publication reste non qualifiée, sans avis praticien.

La demi-réussite concerne le cas-06 : le rôle et le mode d'exercice de la
centrale sont insuffisamment qualifiés et le renvoi budgétaire manque. Le
jugement et la première réponse sont conservés. Cas-01, cas-16 et cas-24
réussissent. Aucune reprise ne remplace une réponse ayant échoué.

Runtime source : `129f374e6ab8ea3b47bcfd9de9ddd52a2d3d9498`.
Codex CLI 0.160.0, modèle demandé gpt-6.1-sol pour les deux rôles. Répondant
avec web et MCP droit-francais disponibles ; juge sans web, MCP ou runtime.
Le MCP disponible n'est pas utilisé dans chaque cas : deux sources MCP sont
exportées. Les autres lectures sont principalement réalisées par le web.
La suite et le barème sont inchangés ; aucun attendu métier n'est fourni
au répondant. Le profil et le runtime ont changé depuis 0.1.2 : ce résultat
n'isole pas l'effet de la seule correction rédactionnelle.

Les preuves publiques sont dans `tests/runs/codex-mcp-v0.1.3-r5/`.
Leur export confronte les octets du runtime au commit source, vérifie chaque
rôle et conserve les réponses, jugements et empreintes. Flux bruts, pensées,
signatures et données d'authentification restent hors dépôt.

Deux liens personnels vers le runtime temporaire, dans cas-25 et cas-27,
sont remplacés par des chemins relatifs dans la copie publique. Les originaux
privés et les jugements restent inchangés ; `redaction.json` lie les deux
empreintes, et la validation rattache le jugement à l'original du répondant.
Seuls ces chemins sont transformés. Cet assainissement est vérifié à l'export ;
la CI contrôle les empreintes publiques et leurs liens, sans accéder aux originaux privés.

L'inventaire relève **quinze citations dans quatre cas** (01, 15, 16, 17)
sans correspondance explicite avec une récupération identifiée. Des actions
web sont classées « other » ; une alerte ne démontre pas une fausse lecture.
Treize articles distincts ont été relus après exécution via l'API officielle,
avec texte empreinté et métadonnées de version/applicabilité conservées. Cette
relecture ne prouve pas une lecture dans la session initiale, ne corrige
aucun jugement et ne certifie pas leur application au dossier.

Voir `docs/socle/audit-provenance-0.1.3-2026-10-08.json`. L'inventaire couvre
les URL officielles explicites ; il ne constitue pas un audit complet de
toutes les assertions juridiques. Notes d'application, jurisprudence,
CCAG et pièces locales restent à examiner dans la grille praticien.

L'essai web 0.1.2 est conservé séparément : quinze cas achevés, régression
source au cas-01, campagne interrompue et aucun score global. Le cas-24
y réussit après correction du circuit financier. Les scores antérieurs
restent liés à leurs propres runtimes, sans transfert de qualification.

Paquet déterministe : 30 fichiers, SHA-256
`70fed26db3441e89e9fe77539302f8e0d44f0abd9765e6f5f81d1376efcd5e46`.
Le point d'entrée garde l'avertissement antérieur à la mesure pour préserver
les octets testés. Le statut actuel est documenté hors paquet.

La [grille praticien](relecture-candidat-0.1.3-2026-10-08.md) reste vierge.
Contrôles locaux : 1673 contrôles statiques, 45 tests logiciels réussis.
La qualification du plugin et son smoke installé sont documentés séparément
dans la PR plugin #13. La distribution publique reste gelée sur v1.1.1.
