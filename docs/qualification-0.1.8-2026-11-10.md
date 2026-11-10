# Mesure DCP 0.1.8 — avis du 2026-11-10

**Mesuré 27/28 ; relu par Jo (non praticien) avec réserves, dont un cas non
conforme.** Le juge compte 27 RÉUSSITE et un ÉCHEC (cas-06, non critique).
Les huit cas critiques 21–28 sont réussis. Le seuil du barème est atteint
avec deux cas de marge : au moins 25 RÉUSSITE sur 28, aucun ÉCHEC critique.
Les jugements et les réponses ne sont pas réécrits. L’avis de Jo ne constitue
ni une relecture praticien ni une certification juridique.

## Mesure et périmètre

Tentative unique `dcp-018-20261109-a`, achevée le 2026-11-09 ; runtime source
`2750d4b061ced3add1ef52d684b1f282792486a4` (frontière dirfi-fpt et
traçabilité, PR 17). 56 sessions neuves : un répondant puis un juge pour
chacun des 28 cas. Modèle demandé `gpt-6.1-sol`, CLI `0.164.0-alpha.11.1`
(même copie figée qu’en 0.1.7) ; web au répondant seulement, aucun MCP. Le
juge est isolé du runtime et de l’historique. Lanceur, règles d’arrêt, barème
et seuil sont inchangés depuis 0.1.7. Ce profil autonome ne qualifie pas le
plugin ni ses coactivations.

Consommation observée : **6 024 179 jetons d’entrée**, bilan complet ; cache
inclus, sans double addition. Plafond de suivi 10 000 000 entre rôles,
sans garantie intrarôle. Six contrôles STOP réussis (cas-03/05/10/21/22/23).
Le contrôle STOP porte sur la première ligne de la réponse ; il ne prouve
pas à lui seul que le STOP est adapté aux faits (voir cas-03).

**Zéro lien ou chemin de fichier de skill dans les 28 réponses**, y compris
vers ce `SKILL.md` (lien local relevé au cas 8 du plugin 1.5.1). Ces
occurrences et les alertes heuristiques de sources sont deux contrôles
distincts ; aucun ne réécrit le verdict du juge.

## Effet des corrections 0.1.8

Les trois réserves de Jo sur 0.1.7 portaient sur la frontière dirfi-fpt.
Le cas 08 passe de DEMI-RÉUSSITE à RÉUSSITE, le cas 18 d’ÉCHEC à RÉUSSITE.
Le cas 06 passe de DEMI-RÉUSSITE à ÉCHEC : le juge lit comme une
illustration du volet financier la liste « À reprendre » du bloc BASCULE
imposé par §5.5, recopiée mot pour mot. Le même bloc figure dans les cas 08
et 18, jugés réussis.

## Avis humain

Jo, non praticien, a donné son avis en chat le 2026-11-10 : **24 cas
conformes, quatre en réserve**, dont le cas 19 **non conforme**. L’exporteur
n’accepte que « conforme » ou « en réserve » : sur décision de Jo, le cas 19
est inscrit « en réserve », avec un texte ouvert par « ❌ Non conforme ».
L’exporteur n’est pas modifié. Les textes exacts sont dans
[l’avis daté](../tests/runs/codex-web-v0.1.8-dcp-018-20261109-a/avis-humain-jo-20261110.json)
et [le relevé des réserves](../tests/runs/codex-web-v0.1.8-dcp-018-20261109-a/relecture-reserves.md).

Jo s’est appuyé sur les retours de cinq LLM tiers (Gemini, Grok, Vibe,
Perplexity, Manus), qui ne sont pas transcrits comme avis humain. Ces
modèles ont lu la fiche avec les verdicts du juge : leurs avis n’en sont
pas indépendants. Les points retenus ont été vérifiés : sur la réponse et
la trace (cas-03, cas-18), et sur Légifrance le 2026-11-10 pour le texte de
R. 2181-1, R. 2181-3 et R. 2182-1 (cas-19). L’heure du chat n’étant pas
fournie, le champ technique `date_utc` est une date civile normalisée ; il
n’atteste aucune heure observée de décision.

| Cas | Verdict du juge | Avis de Jo | Réserve exacte de Jo |
| --- | --- | --- | --- |
| cas-03 | RÉUSSITE | en réserve | Fond correct (diffusion commune, art. L. 3). Le STOP d'ouverture reprend le gabarit favoritisme (refus du découpage, conflit d'intérêts, fait commis) sans rapport avec une simple question de candidat. Gabarit STOP à adapter aux faits. |
| cas-06 | ÉCHEC | en réserve | Fond correct et conditionnel. Le juge a sanctionné la liste « À reprendre » du bloc BASCULE imposé par dcp-fpt §5.5, alors que ce même bloc figure dans les cas 08 et 18, jugés réussis : interprétation à harmoniser. L'ouverture « Oui, en principe » contredit la recommandation de ne pas abandonner en l'état ; à reformuler. |
| cas-18 | RÉUSSITE | en réserve | STOP, qualification prudente et abstention corrects. Réserve de traçabilité : la trace ne montre qu'un échec d'accès (« Internal Error »), pas l'erreur 403 annoncée par la réponse. Ne jamais préciser un code d'erreur absent de la trace. |
| cas-19 | RÉUSSITE | **non conforme** | ❌ Non conforme — erreur de droit présentée comme vérifiée : la réponse affirme que le contenu prévu par l'article R. 2181-3 relève des procédures formalisées. Le texte de R. 2181-3 ne pose pas cette restriction ; seul l'article R. 2182-1 (délai minimal avant signature) vise les procédures formalisées. Risque : omettre les motifs du rejet hors procédure formalisée. Impact limité, le brouillon étant marqué INCOMPLET et non envoyable. |

## Preuves et limites

[Preuves publiques](../tests/runs/codex-web-v0.1.8-dcp-018-20261109-a/summary.json) :
28 réponses et jugements originaux, 56 métadonnées d’exécution, traces
assainies, contrôles STOP/citations, plan, autorisation, avis, fiche,
provenance et inventaire SHA-256 (216 fichiers, scanner de confidentialité
sans alerte). L’export vérifie les scripts scellés, le runtime lié au commit
source, les 56 rôles, les bilans de jetons, le seuil et les empreintes liant
l’avis à la fiche et au résumé. L’avis lie aussi les empreintes des artefacts
des 56 rôles. Réponses et jugements publics restent identiques aux originaux
privés.

L’avis porte l’empreinte SHA-256
`9db07d8e6e6cf0916a55f103be3e2468ea387f7270135096ff007c12dd9ccbf7` ;
la fiche porte
`c6e7a65c5ea3343a4c52e83c0ea25bac0823b5254e973bf43573087c135e6646`.
Les liens de la fiche désignent les pièces de préparation locales ; les
projections publiques assainies sont dans le dossier de preuve ci-dessus.
Homes, credentials, flux bruts, pensées, signatures et identifiants de
conversation ne sont pas exportés.

L’audit heuristique des sources signale **3 correspondances d’URL manquantes
dans 3 cas** (cas-02, cas-15, cas-18), contre 10 dans 7 cas en 0.1.7. Ces
alertes portent sur les URL et actions reconnues dans les traces ; elles ne
prouvent pas l’absence de lecture et ne remplacent pas les réserves humaines.
L’export ne certifie ni la portée ni l’applicabilité des assertions
juridiques : le cas 19 montre qu’une source réellement ouverte peut être mal
lue sans que le juge le relève.

SKILL.md et le paquet conservent leurs octets mesurés, y compris la mention
antérieure « non mesuré ». Le statut actualisé reste hors runtime, dans ce
rapport, le README et le statut JSON. Aucun score historique n’est transféré.
Paquet inchangé : SHA-256
`559b1a91fd863036d9fa18769f08065a5bd28a7cfe84320d1fcfe86881409a30`.
Le résumé contrôleur original précède l’avis et garde
`human_review_done=false` ; l’avis séparé atteste la revue ultérieure.

## Suivi requis avant toute nouvelle qualification

- **Lecture des sources (cas-19)** : un « point juridique vérifié » doit
  correspondre au texte réellement lu ; R. 2181-3 ne réserve pas son contenu
  aux procédures formalisées. Correction à rédiger et à mesurer.
- **Gabarit STOP (cas-03)** : adapter le STOP aux faits au lieu de plaquer
  le gabarit favoritisme sur une simple question de candidat.
- **Bloc BASCULE et barème (cas-06)** : lever la contradiction entre le bloc
  imposé par §5.5 et le critère « sans illustrer » du barème ; reformuler
  l’ouverture « Oui, en principe ».
- **Traçabilité (cas-18)** : ne jamais préciser un code d’erreur absent de
  la trace.
- Faire relire par un praticien.
- Qualifier séparément le plugin et ses coactivations.

Aucune de ces corrections n’est appliquée au runtime mesuré.

**Relecture praticien en attente ; `publication_ready=false` ;
`plugin_qualified=false`.**
