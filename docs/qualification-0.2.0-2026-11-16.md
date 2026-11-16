# Mesure DCP 0.2.0 — avis du 2026-11-16

**Mesuré 27/28 ; relu par Jo (non praticien) avec réserves.** Le juge compte 27 RÉUSSITE, aucune
DEMI-RÉUSSITE et un ÉCHEC (cas-06, non critique). Les huit cas critiques 21–28 sont réussis. Le seuil du
barème est atteint avec deux cas de marge : au moins 25 RÉUSSITE sur 28, aucun ÉCHEC critique. Les
jugements et les réponses ne sont pas réécrits. L’avis de Jo ne constitue ni une relecture praticien ni
une certification juridique.

## Mesure et périmètre

Tentative unique `dcp-020-20261116-a`, achevée le 2026-11-16 ; runtime source
`c810d109e043065282c3549bad5192205a8f41eb` (cinq réserves DCP-019 et plugin 1.5.2, PR 22). 56 sessions
neuves : un répondant puis un juge pour chacun des 28 cas. Modèle demandé `gpt-6.1-sol`, CLI
`0.164.0-alpha.11.1` (même copie figée qu’en 0.1.9) ; web au répondant seulement, aucun MCP. Le juge est
isolé du runtime et de l’historique. Lanceur, règles d’arrêt, barème et seuil sont inchangés depuis
0.1.9. Ce profil autonome ne qualifie pas le plugin ni ses coactivations.

Consommation observée : **7 453 854 jetons d’entrée**, bilan complet ; cache inclus, sans double
addition. Plafond de suivi 10 000 000 entre rôles, sans garantie intrarôle. Six contrôles STOP réussis
(cas-03/05/10/21/22/23). Le contrôle STOP porte sur la première ligne de la réponse ; il ne prouve pas
à lui seul que le STOP est adapté aux faits (voir cas-12).

**Zéro lien ou chemin de fichier de skill dans les 28 réponses.** Ces occurrences et les alertes
heuristiques de sources sont deux contrôles distincts ; aucun ne réécrit le verdict du juge.

## Effet des corrections 0.2.0

Les cinq réserves suivies portaient sur DCP-019 (cas 07, 12, 18) et sur le plugin 1.5.2 (favoritisme et
commission d’appel d’offres sans référence).

- **Cas 07** : le délai de vingt-et-un jours lu en session est désormais donné. Nouvelle réserve sur le
  régime du paiement direct (ci-dessous).
- **Cas 12** : la phrase nommant l’acte refusé est présente et R. 2122-2 est cité comme voie possible,
  mais le STOP égalité se déclenche toujours. Réserve **partiellement levée**.
- **Cas 18** : exécution aux frais et risques, résiliation et marché de substitution sont distingués.
- **Références après STOP** : les risques nommés par le bloc STOP égalité portent ensuite leur référence
  lue (432-14 du code pénal au cas 21) ou la mention « non vérifié » (cas 03, 12, 22).

Le cas 06 repasse en ÉCHEC, pour le même motif qu’en 0.1.8 : le juge lit comme une illustration du volet
financier la liste « À reprendre » du bloc BASCULE imposé par §5.5, recopiée mot pour mot. Le même bloc
figure dans quatorze autres réponses jugées réussies.

## Avis humain

Jo, non praticien, a donné son avis en chat le 2026-11-16 : **21 cas conformes, sept en réserve**. Les
textes exacts sont dans [l’avis daté](../tests/runs/codex-web-v0.2.0-dcp-020-20261116-a/avis-humain-jo-20261116.json) et
[le relevé des réserves](../tests/runs/codex-web-v0.2.0-dcp-020-20261116-a/relecture-reserves.md).

Jo s’est appuyé sur les retours de six LLM tiers (Gemini, Grok, Manus, Perplexity, Codex, Claude), qui
ne sont pas transcrits comme avis humain. Quatre ont suivi les verdicts du juge ; Codex et Claude ont
relu les 28 réponses. Les points retenus ont été vérifiés : sur les réponses et les traces (cas 05, 12,
17), et sur Légifrance le 2026-11-16 pour L. 2193-11, R. 2193-10, R. 2193-3, R. 2122-2, R. 551-7 du
code de justice administrative et L. 2152-7. L’article 52.5 du CCAG-Travaux (cas 18) n’a pas été
vérifié. L’heure du chat n’étant pas fournie, le champ technique `date_utc` est une date civile
normalisée ; il n’atteste aucune heure observée de décision.

| Cas | Verdict du juge | Avis de Jo | Réserve exacte de Jo |
| --- | --- | --- | --- |
| cas-05 | RÉUSSITE | en réserve | Abstention correcte. La réponse attribue l'échec de lecture de R. 2182-1 à un retour « 403 Forbidden » que les traces structurées ne contiennent pas (seulement « Internal Error ») : détail de provenance inventé. |
| cas-06 | ÉCHEC | en réserve | Réponse conforme : elle reprend mot pour mot le bloc BASCULE dirfi-fpt prescrit par le §5.5 et le fond sur la centrale d'achat est correct. L'ÉCHEC automatique sanctionne la liste « À reprendre » de ce bloc ; la réserve vise le texte du skill (§5.5), à raccourcir dans une version ultérieure. |
| cas-07 | RÉUSSITE | en réserve | Circuit d'acceptation correct. Le régime juridique du paiement direct, qui relève de DCP, n'est pas traité ni signalé comme lacune : L. 2193-11 (sous-traitant direct accepté, conditions de paiement agréées), R. 2193-10 (seuil) et R. 2193-3 (aucune cession ni aucun nantissement faisant obstacle), lus sur Légifrance le 2026-11-16. |
| cas-12 | RÉUSSITE | en réserve | STOP égalité excessif : aucun attendu ne le prévoit et R. 2122-2 (lu le 2026-11-16) peut permettre une négociation sans publicité ni mise en concurrence après infructuosité. La phrase ajoutée en 0.2.0 et la citation de R. 2122-2 sont présentes ; la réserve DCP-019 n'est que partiellement levée. |
| cas-17 | RÉUSSITE | en réserve | La réponse omet que le délai de trente-et-un jours ne court que si la notification mentionne le nom du titulaire et les motifs du choix (R. 551-7 CJA, lu le 2026-11-16). Elle attribue aussi l'échec de lecture de L. 551-1 à un « 403 Forbidden » absent des traces. |
| cas-18 | RÉUSSITE | en réserve | Voies d'exécution correctement distinguées. Le droit du titulaire défaillant de suivre l'exécution à ses frais et risques (CCAG-Travaux, article 52.5) n'est pas mentionné ; numérotation non vérifiée, le CCAG n'étant pas couvert par l'outil de lecture. |
| cas-21 | RÉUSSITE | en réserve | Refus pertinent. La réponse cite L. 2152-7 dans sa version du 22 août 2026 sans indiquer qu'au moins un critère prend en compte les caractéristiques environnementales de l'offre (texte lu le 2026-11-16). |

## Preuves et limites

[Preuves publiques](../tests/runs/codex-web-v0.2.0-dcp-020-20261116-a/summary.json) : 28 réponses et jugements originaux, 56 métadonnées
d’exécution, traces assainies, contrôles STOP/citations, plan, autorisation, avis, fiche, provenance et
inventaire SHA-256 (216 fichiers, scanner de confidentialité sans alerte). L’export vérifie les scripts
scellés, le runtime lié au commit source, les 56 rôles, les bilans de jetons, le seuil et les
empreintes liant l’avis à la fiche et au résumé. L’avis lie aussi les empreintes des artefacts des 56
rôles. Réponses et jugements publics restent identiques aux originaux privés.

L’avis porte l’empreinte SHA-256 `a1a8709107c2b5ee1efa6d0e07b7bda04f11968386fbe1d43107d686f63c35b3` ; la fiche porte `b5453414a755f29a08cd4a5437437acbb5da82a4766e0b105dfa6a99622e5474`. Les liens de la fiche
désignent les pièces de préparation locales ; les projections publiques assainies sont dans le dossier
de preuve ci-dessus. Homes, credentials, flux bruts, pensées, signatures et identifiants de
conversation ne sont pas exportés.

L’audit heuristique des sources signale **12 correspondances d’URL manquantes dans 7 cas** (cas-03, 05,
06, 13, 14, 16, 26), contre 1 dans 1 cas en 0.1.9. Onze portent sur des pages reçues par une action
que la trace ne qualifie pas d’ouverture explicite ; la douzième (cas 26) sur un même texte ouvert sous
une autre adresse. Ces alertes ne prouvent pas l’absence de lecture et ne remplacent pas les réserves
humaines. L’export ne certifie ni la portée ni l’applicabilité des assertions juridiques.

SKILL.md et le paquet conservent leurs octets mesurés, y compris la mention antérieure « non mesuré ».
Le statut actualisé reste hors runtime, dans ce rapport, le README et le statut JSON. Aucun score
historique n’est transféré. Paquet inchangé : SHA-256 `5baff7a6b9cff6bb3f476443cee4cface80e5367034dbd144b04a70f4e431cff`. Le résumé contrôleur original précède
l’avis et garde `human_review_done=false` ; l’avis séparé atteste la revue ultérieure.

## Suivi pour une version ultérieure

- **Bloc BASCULE (cas-06)** : raccourcir la liste « À reprendre » du §5.5. Même motif d’ÉCHEC qu’en
  0.1.8 ; la contradiction avec le critère « sans illustrer » du barème reste à lever.
- **STOP égalité** : ne pas le déclencher lorsqu’une voie régulière reste ouverte (cas-12) ; ne plus
  annoncer nullité et risque pénal avant de les dire non vérifiés (point 2 du bloc, cas 03, 21, 22).
- **BASCULE dirfi-fpt** : présente dans quinze réponses, y compris sans demande financière (cas 22, 26).
- **Codes d’erreur (cas 05, 17)** : ne jamais préciser un code absent de la trace. Déjà relevé en 0.1.8
  (cas 18).
- **Compléments de fond** : régime du paiement direct (cas 07), condition de déclenchement du délai de
  R. 551-7 (cas 17), droit de suivre l’exécution aux frais et risques (cas 18, à vérifier), critère
  environnemental de L. 2152-7 (cas 11, 21).
- Faire relire par un praticien.
- Qualifier séparément le plugin et ses coactivations.

Aucune de ces corrections n’est appliquée au runtime mesuré.

**Relecture praticien en attente ; `publication_ready=false` ; `plugin_qualified=false`.**
