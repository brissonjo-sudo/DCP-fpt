# ADR 0009 — Export 0.1.5 aligné sur le barème

Date : 2026-10-23. Décision de Jo transmise textuellement dans le lot D2 :
« Aligner sur le barème ».

> L'export accepte tout résultat qui atteint le seuil du barème (≥ 25 RÉUSSITE,
> aucun ÉCHEC critique) et vos réserves, en les inscrivant visiblement dans la
> preuve. Tous les contrôles d'intégrité (empreintes, scellés, scanner) restent
> intacts. Nom de l'avis paramétré par date.

## Application bornée

Pour 0.1.5 uniquement, les 28 jugements restent inchangés. Le seuil est
recalculé depuis les jugements : au moins 25 RÉUSSITE et aucun ÉCHEC critique.
Les DEMI-RÉUSSITE sont conservées et affichées dans `relecture-reserves.md`.
Les contrôles de rattachement, scellés, empreintes, rôles, consommation, STOP
et confidentialité restent appliqués avant toute écriture de l'export.

L'avis humain contient les 28 identifiants dans `verdicts`, avec les valeurs
`conforme` ou `en réserve`. Le dictionnaire `reserves` associe exactement
chaque cas `en réserve` à son texte non vide. Aucun texte n'est reformulé ni
nettoyé ; une entrée vide, un cas inconnu ou un statut incohérent sont refusés.
Un dictionnaire vide signifie aucune réserve, avec les 28 statuts conformes.

Les réserves exactes figurent dans l'avis original, la provenance, la
progression par cas et le relevé lisible. Elles ne modifient pas le verdict
automatique et ne permettent pas de franchir un seuil non atteint.
Une réserve contenant un motif privé reste refusée par le scanner inchangé.

`--review-date YYYY-MM-DD` est obligatoire pour 0.1.5 : motif ASCII strict,
date calendaire valide et concordance avec la date UTC de l'avis lié.
Le nom exporté est `avis-humain-jo-YYYYMMDD.json`. La vérification publique
contrôle de nouveau la date, les liens, les réserves et leur affichage.

L'historique 0.1.4 conserve son nom d'avis, 28 RÉUSSITE et aucune réserve.
Ses fichiers, octets sources et tests existants sont préservés. Les essais
0.1.5 de D2 sont exclusivement simulés ; ils ne portent aucun score réel.
