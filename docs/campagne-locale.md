# Outillage de campagne future — dcp-fpt v0.1.0

**Arrêt avant campagne.** Aucun cas métier, run, kit de mesure ou score livré.
Fixtures logicielles temporaires uniquement. Statut : **non mesuré, non relu
par un praticien**.

## Validation de rédaction

Python 3.11 ou ultérieur, bibliothèque standard uniquement :

```powershell
python scripts/validate_repo.py --sans-campagne
python -m unittest discover -s tests -p 'test_*.py'
python scripts/package_skill.py
```

`--sans-campagne` tolère uniquement tests/cas-de-test.json absent. Inventaires,
liens, versions, garde-fous et outillage restent requis. Une suite présente
reste entièrement contrôlée. Sans option, son absence est bloquante.
`--partiel` reste un mode historique de rédaction du patron ; il n'est utilisé
ni pour la livraison ni dans la CI.

## Phase de mesure distincte

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
