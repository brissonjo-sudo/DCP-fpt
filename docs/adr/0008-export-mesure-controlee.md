# ADR 0008 — Export public de la mesure contrôlée 0.1.4

Date : 2026-10-20. Lot DCP-D2, versionnement local sans poussée.

Le contrôleur D1 conserve les preuves par rôle et un résumé final ; il ne
produit pas le fichier `execution.json` qu'attend l'exporteur historique.
Les originaux privés ne sont pas complétés ou réécrits pour le satisfaire.
Un exporteur distinct vérifie plan et autorisation scellés, runtime au
commit source, 56 rôles, bilans de consommation, contrôles STOP et avis Jo.
Il reprend les traces assainies et le rattachement réponse/jugement du dépôt.
L'exporteur historique, les validateurs, le barème et les cas restent intacts.

Les seules projections nouvelles concernent la gouvernance : chemin personnel
de CLI et identifiants de thread omis, chemins de résultats relatifs.
Chaque source originale reste liée par SHA-256. Réponses et jugements de
cette mesure sont copiés sans transformation. Homes, credentials et flux
bruts restent hors dépôt ; un inventaire public et des contre-épreuves
contrôlent l'intégrité de l'export et l'absence de motifs privés.

La convention de `ff35b7a` est maintenue : statut actuel du skill hors
runtime, afin de préserver les octets mesurés. Le score 28/28 et la revue
de Jo, non praticien, n'emportent ni relecture praticien ni qualification
du plugin. Les campagnes historiques gardent leurs propres résultats.
