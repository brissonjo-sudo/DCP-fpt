# Mesure DCP 0.1.5 — avis du 2026-10-24

**Mesuré 25/28 ; relu par Jo (non praticien) avec réserves.** Le juge compte
25 RÉUSSITE, deux DEMI-RÉUSSITE (cas-08, cas-15), un ÉCHEC (cas-17, non
critique). Les huit cas critiques 21–28 sont réussis. Le seuil du barème
est atteint : au moins 25 RÉUSSITE sur 28, aucun ÉCHEC critique. Les
jugements et les réponses ne sont pas réécrits. L’avis de Jo ne constitue
ni une relecture praticien ni une certification juridique.

## Mesure et périmètre

Tentative unique `dcp-015-20261023-a`, achevée le 2026-10-23 ; runtime source
`f5c9095f3183dff8e5a1fe56c54bde953a9b91c0`. 56 sessions neuves : un répondant
puis un juge pour chacun des 28 cas. Modèle demandé `gpt-6.1-sol`, CLI
`0.163.0-alpha.10.2` ; web au répondant seulement, aucun MCP. Le juge est
isolé du runtime et de l’historique. Ce profil autonome ne qualifie pas
le plugin ni ses coactivations.

Consommation observée : **5 463 220 jetons d’entrée**, bilan complet ; cache
inclus, sans double addition. Plafond de suivi 10 000 000 entre rôles,
sans garantie intrarôle. Six contrôles STOP réussis (cas-03/05/10/21/22/23).
Le contrôle STOP porte sur la première ligne de la réponse ; il ne prouve
pas à lui seul l’ordre des messages de progression.

**Zéro lien ou chemin de fichier de skill dans les 28 réponses**, contre
116 occurrences sur les 28 réponses de 0.1.4 avec le même contrôle informatif.
Ces occurrences et les alertes heuristiques de sources sont deux contrôles
distincts ; aucun ne réécrit le verdict du juge.

## Avis humain et arbitrage

Jo, non praticien, a donné son avis en chat le 2026-10-24 : **22 cas
conformes, six en réserve**. Les textes exacts sont dans
[l’avis daté](../tests/runs/codex-web-v0.1.5-dcp-015-20261023-a/avis-humain-jo-20261024.json)
et [le relevé des réserves](../tests/runs/codex-web-v0.1.5-dcp-015-20261023-a/relecture-reserves.md).
Aucun avis de LLM tiers n’est transcrit comme avis humain. L’heure du chat
n’étant pas fournie, le champ technique `date_utc` est explicitement une
date civile normalisée ; il n’atteste aucune heure observée de décision.

| Cas | Verdict du juge | Réserve exacte de Jo |
| --- | --- | --- |
| cas-06 | RÉUSSITE | renvoi du volet budgétaire à dirfi-fpt absent |
| cas-08 | DEMI-RÉUSSITE | fondements alternatifs non examinés, chiffrage non renvoyé à dirfi-fpt |
| cas-09 | RÉUSSITE | renvoi financier à dirfi-fpt absent ; identifiant du registre cité sans lecture |
| cas-15 | DEMI-RÉUSSITE | fractionnement non refusé, principes en cas de dispense non rappelés |
| cas-17 | ÉCHEC | identifiant du registre cité sans lecture, à limiter au titre de la source |
| cas-26 | RÉUSSITE | identifiant du registre cité sans lecture, à limiter au titre de la source |

Jo arbitre l’incohérence de traitement du juge entre cas-09, cas-17 et
cas-26 par « Souple, avec réserve » : il ne considère pas ces références
comme une « valeur donnée malgré une réserve ». Le score automatique reste
25 ; cas-17 reste ÉCHEC au juge et en réserve dans l’avis humain. Cet
arbitrage autorise l’export au seuil décidé, sans modifier les attendus,
le barème ni les contrôles d’intégrité.

## Preuves et limites

[Preuves publiques](../tests/runs/codex-web-v0.1.5-dcp-015-20261023-a/summary.json) :
28 réponses et jugements originaux, 56 métadonnées d’exécution, traces
assainies, contrôles STOP/citations, plan, autorisation, avis, fiche,
provenance et inventaire SHA-256. L’export vérifie les scripts scellés,
le runtime lié au commit source, les 56 rôles, les bilans de jetons,
le seuil et les empreintes liant l’avis à la fiche et au résumé. L’avis
lie aussi les empreintes des artefacts des 56 rôles. Réponses et jugements
publics restent identiques aux originaux privés.

L’avis porte l’empreinte SHA-256
`b33259548e308c9b3ad04302a787a1685a88fb3b1c5845491e3831f6894f55ed` ;
la fiche porte
`71b2f8c253427d94e8b4fcc96239281a5f6d0ffd1d7ec3e56f31bbbf651d152c`.
Les liens de la fiche désignent les pièces de préparation locales ; les
projections publiques assainies sont dans le dossier de preuve ci-dessus.
Homes, credentials, flux bruts, pensées, signatures et identifiants de
conversation ne sont pas exportés. Le scanner de confidentialité demeure
intact. Aucune nouvelle consultation juridique ni aucun modèle dans D4.

L’audit heuristique des sources signale **7 correspondances d’URL manquantes
dans 6 cas** (cas-03, cas-08, cas-13, cas-16, cas-20, cas-26). Ces alertes portent sur les URL et
actions reconnues dans les traces ; elles ne prouvent pas l’absence de
lecture et ne remplacent pas les réserves humaines. L’export ne certifie
ni la portée ni l’applicabilité des assertions juridiques.

SKILL.md et le paquet conservent leurs octets mesurés, y compris la mention
antérieure « non mesuré, non relu par un praticien ». Le statut actualisé
reste hors runtime, dans ce rapport, le README et le statut JSON. Aucun
score historique n’est transféré. Paquet inchangé : 30 fichiers, SHA-256
`6cccf0970a9fe6c5708f70c953b8cb3fd2c3d64b4e8153f55e60fdeb15e417da`.
Le résumé contrôleur original précède l’avis et garde
`human_review_done=false` ; l’avis séparé atteste la revue ultérieure.

## Suivi requis avant toute nouvelle qualification

- Préciser dans une version ultérieure du skill la règle d’abstention
  décidée par Jo : « identifiant du registre cité sans lecture, à limiter
  au titre de la source ». Cas concernés par l’arbitrage : 09/17/26.
  Cette précision reste à rédiger et à vérifier ; elle n’est pas appliquée
  au runtime déjà mesuré. Suivi du chantier : dépôt DCP-fpt, issue #9.
- Traiter les autres réserves (frontières financières, fondements
  alternatifs, fractionnement et principes), puis faire relire par un praticien.
- Qualifier séparément le plugin et ses coactivations.

**Relecture praticien en attente ; `publication_ready=false` ;
`plugin_qualified=false`.** D4 réalise l’export et la documentation locaux.
Aucune poussée, PR distante, publication ou nouvelle campagne n’est effectuée.
