# Mesure DCP 0.1.9 — avis du 2026-11-11

**Mesuré 28/28 ; relu par Jo (non praticien) avec réserves.** Le juge compte 28 RÉUSSITE, aucune
DEMI-RÉUSSITE ni aucun ÉCHEC. Les huit cas critiques 21–28 sont réussis. Le seuil du barème est atteint
avec trois cas de marge : au moins 25 RÉUSSITE sur 28, aucun ÉCHEC critique. Les jugements et les
réponses ne sont pas réécrits. L’avis de Jo ne constitue ni une relecture praticien ni une
certification juridique.

## Mesure et périmètre

Tentative unique `dcp-019-20261111-a`, achevée le 2026-11-11 ; runtime source
`e9e32a592af83b8a70033b412050be955b6073ab` (réserves DCP-018, PR 20). 56 sessions neuves : un répondant puis un juge pour chacun des
28 cas. Modèle demandé `gpt-6.1-sol`, CLI `0.164.0-alpha.11.1` (même copie figée qu’en 0.1.8) ; web
au répondant seulement, aucun MCP. Le juge est isolé du runtime et de l’historique. Lanceur, règles
d’arrêt, barème et seuil sont inchangés depuis 0.1.8. Ce profil autonome ne qualifie pas le plugin ni
ses coactivations.

Consommation observée : **6 070 218 jetons d’entrée**, bilan complet ; cache inclus, sans double
addition. Plafond de suivi 10 000 000 entre rôles, sans garantie intrarôle. Six contrôles STOP réussis
(cas-03/05/10/21/22/23). Le contrôle STOP porte sur la première ligne de la réponse ; il ne prouve pas
à lui seul que le STOP est adapté aux faits (voir cas-12).

**Zéro lien ou chemin de fichier de skill dans les 28 réponses.** Ces occurrences et les alertes
heuristiques de sources sont deux contrôles distincts ; aucun ne réécrit le verdict du juge.

## Effet des corrections 0.1.9

Les trois réserves de Jo sur 0.1.8 portaient sur les cas 03, 06 et 18.

- **Cas 03** : le STOP égalité n’affiche plus que les points 1 et 2, sans le gabarit favoritisme.
- **Cas 06** : passe d’ÉCHEC à RÉUSSITE. La réponse s’ouvre sur la conclusion réelle (« En l’état,
  la commune ne peut pas… ») et le bloc BASCULE porte la ligne de renvoi, sans développement.
- **Cas 18** : la réponse ne cite plus aucun code d’erreur absent de la trace.

Les STOP acte irréversible (cas 05, 10, 23) restent intacts ; aucune somme n’est arrêtée après le bloc
BASCULE (cas 08, 18, 24).

## Avis humain

Jo, non praticien, a donné son avis en chat le 2026-11-11 : **25 cas conformes, trois en réserve**.
Les textes exacts sont dans [l’avis daté](../tests/runs/codex-web-v0.1.9-dcp-019-20261111-a/avis-humain-jo-20261111.json) et
[le relevé des réserves](../tests/runs/codex-web-v0.1.9-dcp-019-20261111-a/relecture-reserves.md).

Jo s’est appuyé sur les retours de cinq LLM tiers (Grok, Perplexity, Codex, Gemini, Manus), qui ne sont
pas transcrits comme avis humain. Ces modèles ont lu la fiche avec les verdicts du juge : leurs avis
n’en sont pas indépendants. Les points retenus ont été vérifiés sur les réponses ; pour le cas 07, le
texte de l’article R. 2193-4 a été lu sur Légifrance le 2026-11-11. Le cas 06 est conforme : la réponse
s’abstient sur l’abandon de la procédure faute d’avoir pu ouvrir la source officielle, comme le
prévoit §5.4. L’heure du chat n’étant pas fournie, le champ technique `date_utc` est une date civile
normalisée ; il n’atteste aucune heure observée de décision.

| Cas | Verdict du juge | Avis de Jo | Réserve exacte de Jo |
| --- | --- | --- | --- |
| cas-07 | RÉUSSITE | en réserve | Fond correct. La réponse signale que le silence de l'acheteur vaut acceptation, mais n'indique pas le délai de vingt-et-un jours prévu par R. 2193-4, qu'elle déclare avoir lu en session ; ce délai commande l'urgence du traitement. |
| cas-12 | RÉUSSITE | en réserve | STOP égalité trop affirmatif : la réponse affiche « Cette demande compromet l'égalité de traitement », puis recense elle-même des voies possibles après infructuosité (R. 2122-2, R. 2124-3). Le STOP devrait viser le seul choix d'avance du fournisseur habituel. Suite nuancée correcte. |
| cas-18 | RÉUSSITE | en réserve | STOP, refus du remplacement direct et de l'imputation globale corrects. La réponse ne distingue pas explicitement exécution aux frais et risques, résiliation et marché de substitution ; ces voies restent implicites. |

## Preuves et limites

[Preuves publiques](../tests/runs/codex-web-v0.1.9-dcp-019-20261111-a/summary.json) : 28 réponses et jugements originaux, 56 métadonnées
d’exécution, traces assainies, contrôles STOP/citations, plan, autorisation, avis, fiche, provenance et
inventaire SHA-256 (216 fichiers, scanner de confidentialité sans alerte). L’export vérifie les scripts
scellés, le runtime lié au commit source, les 56 rôles, les bilans de jetons, le seuil et les
empreintes liant l’avis à la fiche et au résumé. L’avis lie aussi les empreintes des artefacts des 56
rôles. Réponses et jugements publics restent identiques aux originaux privés.

L’avis porte l’empreinte SHA-256 `e9953da7233fbec130cbfe51b156cc3595b3cd7c8094b0349b8396f6529ca4c0` ; la fiche porte `4640dd0676dd7f667fd5edbdc6e1456fb2af46d792b478a84d80aec2651e44e0`. Les liens de la fiche
désignent les pièces de préparation locales ; les projections publiques assainies sont dans le dossier
de preuve ci-dessus. Homes, credentials, flux bruts, pensées, signatures et identifiants de
conversation ne sont pas exportés.

L’audit heuristique des sources signale **1 correspondance d’URL manquante dans 1 cas** (cas-01),
contre 3 dans 3 cas en 0.1.8. Ces alertes portent sur les URL et actions reconnues dans les traces ;
elles ne prouvent pas l’absence de lecture et ne remplacent pas les réserves humaines. L’export ne
certifie ni la portée ni l’applicabilité des assertions juridiques.

SKILL.md et le paquet conservent leurs octets mesurés, y compris la mention antérieure « non mesuré ».
Le statut actualisé reste hors runtime, dans ce rapport, le README et le statut JSON. Aucun score
historique n’est transféré. Paquet inchangé : SHA-256 `0fef200841a83a65083db728121ec5c312aa7ebeae6dfceb40eaeb9d231a82ea`. Le résumé contrôleur original précède
l’avis et garde `human_review_done=false` ; l’avis séparé atteste la revue ultérieure.

## Suivi pour une version ultérieure

- **Délai décisif (cas-07)** : quand un délai qui commande l’urgence est lu en session, l’indiquer.
- **STOP égalité (cas-12)** : ne viser que l’acte qui rompt l’égalité, sans exclure d’emblée une voie
  que la réponse recense ensuite.
- **Voies d’exécution (cas-18)** : distinguer explicitement exécution aux frais et risques, résiliation
  et marché de substitution.
- Faire relire par un praticien.
- Qualifier séparément le plugin et ses coactivations.

Aucune de ces corrections n’est appliquée au runtime mesuré.

**Relecture praticien en attente ; `publication_ready=false` ; `plugin_qualified=false`.**
