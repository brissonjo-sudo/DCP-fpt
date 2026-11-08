# Mesure DCP 0.1.7 — avis du 2026-11-08

**Mesuré 25/28 ; relu par Jo (non praticien) avec réserves.** Le juge compte
25 RÉUSSITE, deux DEMI-RÉUSSITE (cas-06, cas-08), un ÉCHEC (cas-18, non
critique). Les huit cas critiques 21–28 sont réussis. Le seuil du barème
est atteint, sans marge : au moins 25 RÉUSSITE sur 28, aucun ÉCHEC critique.
Les jugements et les réponses ne sont pas réécrits. L’avis de Jo ne constitue
ni une relecture praticien ni une certification juridique.

## Mesure et périmètre

Tentative `dcp-017-20261108-b`, achevée le 2026-11-08 ; runtime source
`5debffd54a6d76e86c79ab261446f9123e564494` (correction R6, PR 15). 56 sessions
neuves : un répondant puis un juge pour chacun des 28 cas. Modèle demandé
`gpt-6.1-sol`, CLI `0.164.0-alpha.11.1` (copie figée, la même que la campagne
du plugin 1.5.0) ; web au répondant seulement, aucun MCP. La CLI de la mesure
0.1.5 n’existant plus sur le poste, l’environnement d’exécution diffère de
0.1.5. Le juge est isolé du runtime et de l’historique. Ce profil autonome ne
qualifie pas le plugin ni ses coactivations.

Une première tentative, `dcp-017-20261108-a`, s’est arrêtée au précontrôle
natif du cas 02 (aucun modèle) après deux sessions : un second lancement de la
commande avait reconfiguré le sandbox du home principal en pleine mesure. Elle
n’est pas retenue ; la tentative b porte deux gardes supplémentaires hors
lanceur (verrou de commande, reconfiguration refusée pendant une mesure).
Lanceur, règles d’arrêt, barème et seuil sont inchangés.

Consommation observée : **6 115 143 jetons d’entrée**, bilan complet ; cache
inclus, sans double addition. Plafond de suivi 10 000 000 entre rôles,
sans garantie intrarôle. Six contrôles STOP réussis (cas-03/05/10/21/22/23).
Le contrôle STOP porte sur la première ligne de la réponse ; il ne prouve
pas à lui seul l’ordre des messages de progression.

**Zéro lien ou chemin de fichier de skill dans les 28 réponses**, comme en
0.1.5, avec le même contrôle informatif. Ces occurrences et les alertes
heuristiques de sources sont deux contrôles distincts ; aucun ne réécrit le
verdict du juge.

## Avis humain

Jo, non praticien, a donné son avis en chat le 2026-11-08 : **25 cas
conformes, trois en réserve**. Il a suivi le précédent de l’avis 0.1.5
(un ÉCHEC non critique noté « en réserve », score du juge inchangé). Les
textes exacts sont dans
[l’avis daté](../tests/runs/codex-web-v0.1.7-dcp-017-20261108-b/avis-humain-jo-20261108.json)
et [le relevé des réserves](../tests/runs/codex-web-v0.1.7-dcp-017-20261108-b/relecture-reserves.md).

Jo s’est appuyé sur les retours de quatre LLM tiers (Grok, Vibe, Gemini,
Manus), qui ne sont pas transcrits comme avis humain. Aucun ne relève d’erreur
de droit dans les cas 06, 08 et 18 ; trois sur quatre confirment les verdicts
du juge. L’heure du chat n’étant pas fournie, le champ technique `date_utc`
est une date civile normalisée ; il n’atteste aucune heure observée de décision.

| Cas | Verdict du juge | Réserve exacte de Jo |
| --- | --- | --- |
| cas-06 | DEMI-RÉUSSITE | rôle exact de la centrale non qualifié ; renvoi du volet budgétaire à dirfi-fpt absent |
| cas-08 | DEMI-RÉUSSITE | fondements possibles de la modification non examinés ; chiffrage non renvoyé à dirfi-fpt |
| cas-18 | ÉCHEC | après BASCULE dirfi-fpt, imputation financière encore traitée (« excédents de dépenses » / « toutes les dépenses ») : frontière déléguée franchie ; droit énoncé non contesté |

## Preuves et limites

[Preuves publiques](../tests/runs/codex-web-v0.1.7-dcp-017-20261108-b/summary.json) :
28 réponses et jugements originaux, 56 métadonnées d’exécution, traces
assainies, contrôles STOP/citations, plan, autorisation, avis, fiche,
provenance et inventaire SHA-256. L’export vérifie les scripts scellés,
le runtime lié au commit source, les 56 rôles, les bilans de jetons,
le seuil et les empreintes liant l’avis à la fiche et au résumé. L’avis
lie aussi les empreintes des artefacts des 56 rôles. Réponses et jugements
publics restent identiques aux originaux privés.

L’avis porte l’empreinte SHA-256
`2507a1f444fa0a73b54f249609187e06d3479cd5f7fee5ee29f5e327da94f1f8` ;
la fiche porte
`150a4adbe77f4e31b87d2616e5a2ad57bd0031cf30fae5acb8eed1e20e665dab`.
Les liens de la fiche désignent les pièces de préparation locales ; les
projections publiques assainies sont dans le dossier de preuve ci-dessus.
Homes, credentials, flux bruts, pensées, signatures et identifiants de
conversation ne sont pas exportés. Le scanner de confidentialité demeure
intact.

L’audit heuristique des sources signale **10 correspondances d’URL manquantes
dans 7 cas** (cas-01, cas-04, cas-12, cas-13, cas-15, cas-16, cas-26). Ces
alertes portent sur les URL et actions reconnues dans les traces ; elles ne
prouvent pas l’absence de lecture et ne remplacent pas les réserves humaines.
L’export ne certifie ni la portée ni l’applicabilité des assertions juridiques.

SKILL.md et le paquet conservent leurs octets mesurés, y compris la mention
antérieure « non mesuré ». Le statut actualisé reste hors runtime, dans ce
rapport, le README et le statut JSON. Aucun score historique n’est transféré.
Paquet inchangé : SHA-256
`dbe4ba9b7cd9472ce502933beebbbddb33a80e197fcc3dfd36571323338e6023`.
Le résumé contrôleur original précède l’avis et garde
`human_review_done=false` ; l’avis séparé atteste la revue ultérieure.

## Suivi requis avant toute nouvelle qualification

- **Frontière dirfi-fpt** : le renvoi du volet budgétaire manque aux cas 06
  et 08, déjà en réserve en 0.1.5 pour le même motif ; au cas 18, le volet
  financier est encore traité après la BASCULE. Correction à rédiger et à
  mesurer dans une version ultérieure ; elle n’est pas appliquée au runtime
  mesuré.
- Faire relire par un praticien.
- Qualifier séparément le plugin et ses coactivations.

**Relecture praticien en attente ; `publication_ready=false` ;
`plugin_qualified=false`.**
