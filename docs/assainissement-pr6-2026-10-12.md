# Préparation locale de PR6 — 12 octobre 2026

PR conservée en brouillon. Aucun push, aucune fusion GitHub, aucun appel de modèle dans cette préparation.

## Références

- Tête de PR6 : `ff35b7af38f2e03bf39a1244ebdae292b53daccd`.
- Main intégré localement : `b90c7f4370df8ef42060d25994998f0a502693a4`.
- Base commune : `fe9cb3db8b008a4abd5783c211d4df9d91eff8dc`.
- Graphe : huit commits propres à PR6, trois propres à main.
- Les trois commits de main ajoutent et corrigent la suite initiale, sa documentation et son contrôle CI. Aucun diff de runtime dans ces commits.

## Choix des cinq conflits

| Fichier | Choix et raison |
|---|---|
| CHANGELOG.md | Conserver les évolutions 0.1.1 à 0.1.3 et les campagnes de la PR ; ajouter la préparation initiale de main comme événement historique daté. |
| README.md | Conserver le statut du candidat 0.1.3 et les liens vers ses preuves ; ne pas rétablir le statut initial non mesuré. |
| docs/campagne-locale.md | Conserver le protocole de la PR et ses limites ; le statut sans campagne de main décrit l’étape initiale. |
| tests/bareme-cas-de-test.md | Conserver strictement les octets de la PR, rattachés aux mesures déjà réalisées. |
| tests/cas-de-test.json | Conserver strictement la suite ultérieure de la PR. La suite initiale de main reste récupérable au SHA b90c7f4 et dans le bundle local vérifié. |

Les deux versions de chaque conflit sont copiées hors candidat avec manifeste SHA-256. Les preuves tests/runs, le socle, les deux STOP, les frontières et le runtime ne sont pas modifiés.

## Contrôles et critères restant ouverts

Validation statique, tests logiciels sans réseau et paquet déterministe sont recontrôlés sur la copie locale. Ils ne remplacent pas une relecture juridique ou praticien.
La grille praticien du 8 octobre est vierge. Le cas-06, la provenance des citations et les réserves du socle restent à examiner. Aucune nouvelle conclusion de qualification ni autorisation de publication.
Le runtime mesuré reste celui du commit `129f374e6ab8ea3b47bcfd9de9ddd52a2d3d9498`. Une comparaison d’octets et du paquet établit seulement la conservation de ce runtime.
Le candidat local doit faire l’objet d’une validation ciblée de Jo avant toute poussée normale. La CI distante devra alors être relue sur ce SHA.
Si main devient rouge après une éventuelle fusion autorisée : arrêt de la chaîne, proposition d’une PR de revert, aucune fusion suivante avant le retour au vert.
