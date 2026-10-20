# Mesure DCP 0.1.4 — 2026-10-20

**Mesuré : 28 RÉUSSITE sur 28, aucun ÉCHEC critique, protocole autonome
Codex ; relu par Jo (non praticien)**. Les six contrôles STOP attendus
réussissent. Jo a déclaré les 28 cas conformes, sans réserve ; l'avis daté
est lié par empreinte au résumé original et à la fiche de relecture.
Cet avis ne vaut ni relecture praticien, ni certification juridique,
ni qualification du plugin.

Source runtime : `071737280debb275549647ffc8c1340cab544a18`, version 0.1.4.
Tentative unique `dcp-stop-014-20261020-a` : 56 rôles neufs, répondant puis
juge pour chacun des 28 cas. Modèle demandé `gpt-6.1-sol` pour les deux rôles,
CLI `0.163.0-alpha.10.2`, web au répondant seulement ; aucun MCP. Le juge
ne reçoit ni runtime ni historique. Ce profil autonome reste distinct
des coactivations et outils du plugin.

Consommation constatée : **5 829 642 jetons d'entrée**, cache inclus et non
additionné une seconde fois ; bilan complet des 56 rôles. Le plafond de
suivi autorisé était de 10 000 000 entre rôles, sans garantie intrarôle.
La règle d'arrêt est celle du barème inchangé : au moins 25 RÉUSSITE sur
28 et aucun ÉCHEC critique. Une DEMI-RÉUSSITE isolée n'arrête pas la mesure.
Aucune nouvelle campagne ni aucun appel modèle dans le lot D2.

Les preuves publiques sont dans `tests/runs/codex-web-v0.1.4-dcp-stop-20261020-a/` : réponses originales,
jugements, métadonnées d'exécution, six contrôles STOP, synthèses, plan,
autorisation, avis de Jo, fiche de relecture et inventaire d'empreintes.
L'export vérifie les scripts scellés, le rattachement du runtime au commit
source, chaque rôle et son bilan, les contrôles STOP et les liens de l'avis.
Les 28 réponses publiques sont identiques aux réponses privées ; les
jugements ne sont pas réécrits. Les projections du plan et du contrôleur
retirent chemin personnel de CLI et identifiants de thread ; leurs
empreintes originales sont conservées dans `provenance.json`.

Homes, credentials, flux bruts, pensées et signatures restent hors dépôt.
Le scanner refuse les motifs de secrets, chemins personnels, courriels,
téléphones et identifiants personnels structurés ; les prompts sont les
28 cas fictifs et anonymisés de la suite inchangée. Cela reste un contrôle
d'export, pas une preuve indépendante de véracité du fond.

L'audit reprend la convention de traces assainies : **18 correspondances
d'URL manquantes dans 11 cas** (cas-01, cas-07, cas-08, cas-09, cas-10, cas-12, cas-13, cas-15, cas-18, cas-19, cas-26).
Ces alertes heuristiques ne sont pas des réserves formulées par Jo et
ne démontrent pas l'absence de lecture : elles portent sur les URL et
actions reconnues dans les traces. Aucune consultation officielle nouvelle
n'est effectuée par D2 ; la portée et l'applicabilité des assertions ne
sont pas certifiées par cet export. Le contrôle STOP porte sur la première
ligne de `response.md` ; l'ordre des messages de progression n'est pas
prouvé par ce seul contrôle.

Comme dans `ff35b7a`, SKILL.md et le paquet restent aux octets effectivement
mesurés, avec leur avertissement antérieur « non mesuré, non relu par un
praticien ». Le statut actuel du skill est porté hors runtime par
`docs/statut-0.1.4.json`, le README et l'index. Aucun score antérieur transféré.
Paquet inchangé : 30 fichiers, SHA-256
`9446c8355d3232ebdf7cd62b7bd1d75855c5fb4f5475d64c495bc2ea4ae7c369`.

Le résumé contrôleur historique précède la relecture et garde
`human_review_done=false` ; l'avis ultérieur séparé fait foi pour le statut
de la revue. `publication_ready=false` est conservé. Jo autorise la poussée
et une PR brouillon, confiées à Claude ; D2 ne réalise aucune poussée,
création de PR, publication de release, installation ou qualification plugin.
