# Outillage de campagne — dcp-fpt v0.1.0

**Phase de préparation autorisée le 2026-10-07.** Les 28 cas métier sont
désormais rédigés, fictifs et anonymisés. Un kit prêt et un dry-run ne sont
pas une mesure. Statut : **non mesuré, non relu par un praticien** tant que
la campagne retenue n'est pas complète et ses traces contrôlées.

## Validation de rédaction

Python 3.11 ou ultérieur, bibliothèque standard uniquement :

```powershell
python scripts/validate_repo.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/package_skill.py
```

`--sans-campagne` tolère uniquement tests/cas-de-test.json absent. Inventaires,
liens, versions, garde-fous et outillage restent requis. Une suite présente
reste entièrement contrôlée. Sans option, son absence est bloquante.
`--partiel` reste un mode historique de rédaction du patron ; il n'est utilisé
ni pour la livraison ni dans la CI.

## Phase de mesure distincte — état historique de la passation

Après autorisation : rédiger les cas/attendus depuis le socle, contrôler sans
`--sans-campagne`, figer suite/runtime/barème avec eval_suite.py.
mesure_locale.py export fournit un kit sans appels ; run --dry-run contrôle
sans CLI ni appel. Aucune de ces opérations n'est exécutée avec une suite
métier dans cette passation.

Le lanceur repris du patron DSI sépare répondant/juge, processus/dossiers neufs,
empreintes et reprise contrôlée. UTF-8/LF explicites préservent les octets sous
Windows. Aucun résultat modifié manuellement ; une correction impose un nouveau
runtime et une nouvelle campagne.

## Limites à qualifier avant lancement

Les tests simulent les CLI : aucun appel réel, authentification ou accès
juridique en direct validé. Vérifier les options avec claude --help et codex
exec --help à la date de lancement. Une option inconnue arrête le rôle sans
verdict fabriqué. Modèles explicitement renseignés, web demandé au répondant
seulement ; sans web, mode dégradé du skill.

Dossiers neufs et sandbox ne constituent pas une isolation complète du
système ; politiques du poste, outils et configuration imposée peuvent
influencer les résultats. Contrôler traces et sources réellement consultées.
Les empreintes ne sont pas une signature d'archive. Appels réels consommateurs
de ressources du compte, réservés à une phase autorisée.

Seuil atteint distinct de relecture et publication. Le juge sans web ne
vérifie pas indépendamment les sources : revue des traces indispensable.
`publication_ready` demeure faux dans l'outillage.

## Points à trancher avant la mesure — relecture PR #4

Le répondant Claude reçoit actuellement une configuration MCP vide : il
n'a pas accès à `droit-francais`. L'accès web éventuel permet une lecture
officielle, mais ne reproduit pas les outils `mcp__droit-francais__*` requis
par le harnais du plugin collectivite-territoriale. Ces environnements ne
doivent pas être présentés comme comparables.

Avant campagne, définir et documenter le profil d'outils autorisé : accès
MCP Légifrance qualifié et reproductible, ou campagne web/mode dégradé
explicitement distincte de la qualification du plugin. Ne pas charger une
configuration MCP personnelle implicitement pour combler cet écart.
Cette décision reste ouverte ; aucune modification du lanceur ni campagne
dans cette correction de rédaction.

Les options CLI, dont `--restricted`, restent testées par simulation.
Prévoir une vérification sur CLI réelle dans la phase autorisée, puis
consigner versions, options acceptées et traces avant de retenir une mesure.

## Profil et contrôles du 2026-10-07

Voir l'ADR 0002 : suite autonome Codex avec web pour le répondant, sans web
pour le juge, aucun MCP implicite. La qualification plugin reste un autre
profil, avec coactivation et appels MCP du plugin obligatoires.

CLI vérifiées par leur aide réelle : Claude Code 2.1.288 et Codex 0.160.0.
Claude charge les six skills du candidat, mais indique une limite de session
et `needs-auth` pour le MCP. Une recherche MCP dans la session principale
Codex réussit ; cette connexion n'est pas transférée au processus Claude.

Le premier essai autonome `r1`, cas-23, est conservé comme contrôle de
l'environnement : le jugement est favorable, mais les lectures des branches
ont été bloquées. Il ne compte pas dans la mesure retenue. Le lanceur rétablit
explicitement `windows.sandbox="elevated"` sous Windows malgré
`--ignore-user-config`, tout en maintenant `--sandbox read-only`.
Un nouveau kit `r2` fige ce correctif. Aucune protection n'est désactivée.

Les kits et flux bruts restent hors dépôt. Le rapport publie seulement les
réponses, jugements et métadonnées utiles après contrôle ; raisonnements,
signatures et sorties de débogage ne sont pas promus en preuve publique.
