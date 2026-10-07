# Outillage de campagne future — dcp-fpt v0.1.0

**Arrêt avant campagne.** La suite de 28 cas (`tests/cas-de-test.json`) est
écrite, contrôlée statiquement et **non lancée** : aucun run, kit de mesure ni
score livré. Les fixtures logicielles restent temporaires. Statut : **non mesuré, non relu
par un praticien**.

## Validation de rédaction

Python 3.11 ou ultérieur, bibliothèque standard uniquement :

```powershell
python scripts/validate_repo.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/package_skill.py
```

La suite étant présente, la validation s'exécute sans option : son absence
serait bloquante. `--sans-campagne` ne tolère que tests/cas-de-test.json absent
et ne sert plus qu'aux fixtures. Une suite présente reste entièrement contrôlée
(schéma, 28 cas, couverture, classification).
`--partiel` reste un mode historique de rédaction du patron ; il n'est utilisé
ni pour la livraison ni dans la CI.

## Phase de mesure distincte

Après autorisation : la rédaction des cas/attendus depuis le socle est faite
(2026-10-07) et contrôlée sans `--sans-campagne` ; reste à figer
suite/runtime/barème avec eval_suite.py.
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
