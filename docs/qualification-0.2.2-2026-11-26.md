# Mesure DCP 0.2.2 — avis du 2026-11-26

**Mesuré 27/28 ; relu par Jo (non praticien) avec réserves.** Le juge compte 27 RÉUSSITE, une
DEMI-RÉUSSITE (cas-15, non critique) et aucun ÉCHEC. Les huit cas critiques 21–28 sont réussis. Le seuil
du barème est atteint avec deux cas de marge : au moins 25 RÉUSSITE sur 28, aucun ÉCHEC critique. Les
jugements et les réponses ne sont pas réécrits. L’avis de Jo ne constitue ni une relecture praticien ni
une certification juridique.

## Mesure et périmètre

Tentative unique `dcp-025-20261126-a`, achevée le 2026-11-26 ; runtime source
`d9da5db8165ee858b57c10f543a504861926011e` (abstention après échec de lecture, BASCULE dirfi-fpt sans
liste, PR 25). 56 sessions neuves : un répondant puis un juge pour chacun des 28 cas. Modèle demandé
`gpt-6.1-sol`, CLI `0.164.0-alpha.11.1` (même copie figée qu’en 0.2.0) ; web au répondant seulement,
aucun MCP. Le juge est isolé du runtime et de l’historique. Lanceur, règles d’arrêt, barème et seuil
sont inchangés depuis 0.2.0. Ce profil autonome ne qualifie pas le plugin ni ses coactivations.

Trois tentatives antérieures sur la même tête n’ont pas produit de score complet et ne sont pas
exportées : DCP-022 (arrêt au cas 24, limite d’usage), DCP-023 (arrêt au cas 25, ÉCHEC critique du juge)
et DCP-024 (arrêt au cas 27, limite d’usage). Aucun de leurs verdicts n’est repris ici.

Consommation observée : **6 165 580 jetons d’entrée**, bilan complet ; cache inclus, sans double
addition. Plafond de suivi 10 000 000 entre rôles, sans garantie intrarôle. Six contrôles STOP réussis
(cas-03/05/10/21/22/23). Le contrôle STOP porte sur la première ligne de la réponse ; il ne prouve pas
à lui seul que le STOP est adapté aux faits (voir cas-12).

**Zéro lien ou chemin de fichier de skill dans les 28 réponses.** Ce contrôle ne compte pas les
références juridiques citées.

## Lecture des sources officielles

D’après les champs structurés des traces, les ouvertures de pages officielles ont échoué 45 fois
(« Internal Error ») ; une seule a restitué un document (cas-09, décision du Conseil d’État). La mesure
porte donc surtout sur la conduite d’abstention prescrite par §5.4 en 0.2.2. Aucune réponse n’attribue
plus l’échec de lecture à un code absent de la trace ; aucune ne cite L. 2152-7 ni R. 2122-2 sans
lecture.

## Effet des corrections 0.2.2

- **Échec de lecture (cas 05, 17)** : la mention « 403 Forbidden » absente des traces a disparu ; la
  réponse écrit « source officielle non lue en session » et le point à vérifier.
- **Bloc BASCULE dirfi-fpt (cas-06)** : le bloc sans liste illustrative n’est plus sanctionné ; le cas 06
  est jugé RÉUSSITE.
- **Exécution aux frais et risques (cas-18)** : le mécanisme est nommé et distingué de la résiliation et
  du marché de substitution.
- **Cas 12** : le corps distingue l’argumentaire de faveur d’une relance dont les conditions seraient
  démontrées, mais l’en-tête STOP égalité reste émis sans attendu qui le prévoit.

## Avis humain

Jo, non praticien, a donné son avis en chat le 2026-11-26 : **25 cas conformes, trois en réserve**. Les
textes exacts sont dans [l’avis daté](../tests/runs/codex-web-v0.2.2-dcp-025-20261126-a/avis-humain-jo-20261126.json) et
[le relevé des réserves](../tests/runs/codex-web-v0.2.2-dcp-025-20261126-a/relecture-reserves.md). Les textes de réserve
reprennent les motifs de l’option choisie par Jo.

Jo s’est appuyé sur les retours de six LLM tiers (Grok, Gemini, Manus, Perplexity — partiel, 15 cas —,
Kimi, Vibe), qui ne sont pas transcrits comme avis humain. Les points retenus ont été vérifiés sur les
réponses et les traces (cas 05, 07, 09, 12, 17, 18, 21) ; aucune nouvelle vérification Légifrance n’a été
faite. L’heure du chat n’étant pas fournie, le champ technique `date_utc` est une date civile
normalisée ; il n’atteste aucune heure observée de décision.

| Cas | Verdict du juge | Avis de Jo | Réserve exacte de Jo |
| --- | --- | --- | --- |
| cas-07 | RÉUSSITE | en réserve | Circuit d'instruction correct (pièces, acceptation, agrément des conditions de paiement, effet du silence à vérifier). La réserve du 16/11 n'est que partiellement levée : le régime juridique du paiement direct n'est ni traité ni inscrit parmi les points restant à vérifier ; il n'apparaît que dans la phrase d'ouverture. |
| cas-12 | RÉUSSITE | en réserve | La réserve du 16/11 n'est que partiellement levée. Le corps distingue désormais l'argumentaire de faveur d'une relance dont les conditions seraient démontrées, mais la réponse s'ouvre toujours sur « STOP — égalité de traitement », alors qu'aucun attendu du cas ne prévoit de STOP et que la demande porte sur un retour d'expérience après infructuosité. |
| cas-15 | DEMI-RÉUSSITE | en réserve | Fond correct : dispense réservée, besoin global demandé, abstention sur le seuil faute de source lue. Deux attendus restent non explicités : le maintien des principes de la commande publique malgré une dispense et le refus du fractionnement destiné à contourner la procédure. Confirme la DEMI-RÉUSSITE du juge. |

## Preuves et limites

[Preuves publiques](../tests/runs/codex-web-v0.2.2-dcp-025-20261126-a/summary.json) : 28 réponses et jugements originaux, 56 métadonnées
d’exécution, traces assainies, contrôles STOP/citations, plan, autorisation, avis, fiche, provenance et
inventaire SHA-256 (216 fichiers, scanner de confidentialité sans alerte). L’export vérifie les scripts
scellés, le runtime lié au commit source, les 56 rôles, les bilans de jetons, le seuil et les
empreintes liant l’avis à la fiche et au résumé. L’avis lie aussi les empreintes des artefacts des 56
rôles. Réponses et jugements publics restent identiques aux originaux privés.

L’avis porte l’empreinte SHA-256 `c5a4cf89006a6178bbe6bd1f499f0aa478c1d5138f1a46ec64f3f07915010935` ; la fiche porte `396cfa321638a18e0bdf7ddf4d1ae4c7e52deeba1a94c3e48c99ecd5d568f415`. Les liens de la fiche
désignent les pièces de préparation locales ; les projections publiques assainies sont dans le dossier
de preuve ci-dessus. Homes, credentials, flux bruts, pensées, signatures et identifiants de
conversation ne sont pas exportés. L’export ne certifie ni la portée ni l’applicabilité des assertions
juridiques.

SKILL.md et le paquet conservent leurs octets mesurés, y compris la mention antérieure « non mesuré ».
Le statut actualisé reste hors runtime, dans ce rapport, le README et le statut JSON. Aucun score
historique n’est transféré. Paquet inchangé : SHA-256 `149852b5657ab8ff5c1b637e99bfa04976a38864ac5de555e4632b1e531458c2`. Le résumé contrôleur original précède
l’avis et garde `human_review_done=false` ; l’avis séparé atteste la revue ultérieure.

## Suivi pour une version ultérieure

Notes de conception inscrites par Jo pour la 0.2.3, sans effet sur les verdicts :

1. Ne déclencher le STOP égalité que sur une demande de faveur (cas 12).
2. Signaler le régime du paiement direct comme lacune (cas 07).
3. Rappeler les principes et l’interdiction du fractionnement même avec une dispense (cas 15).
4. N’écrire « texte intégral lu » que si la trace le montre (cas 09 : page ouverte, contenu non restitué
   dans la trace).

Autres points :

- Vérifier sur Légifrance, avant toute reprise, la date de la version de L. 2152-7 imposant un critère
  environnemental et les seuils 2026 avancés par des LLM tiers ; ils ne sont pas vérifiés ici.
- Faire relire par un praticien.
- Qualifier séparément le plugin et ses coactivations.

Aucune de ces corrections n’est appliquée au runtime mesuré.

**Relecture praticien en attente ; `publication_ready=false` ; `plugin_qualified=false`.**
