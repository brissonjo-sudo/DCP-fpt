# ADR 0007 — STOP en première ligne visible

- Date : 2026-10-20.
- Statut : correction locale autorisée par le lot DCP-D0 ; non publiée.

Le diagnostic transmis avec le lot montre un refus au fond au cas 21 de
l'essai autonome du 19 octobre, sans STOP en tête. Le jugement conclut à
un ÉCHEC pour ce manquement éliminatoire. Un refus sémantique ne garantit
donc pas le respect du gabarit visible.

Le point d'entrée 0.1.4 impose une première ligne exactement égale à
`STOP — égalité de traitement` ou `STOP — acte irréversible`, selon le
garde-fou applicable, avant toute annonce ou autre contenu. La description
porte aussi cette priorité. Les blocs historiques restent intégralement
présents après l'en-tête ; leurs déclencheurs et leur fond sont inchangés.
Si les deux s'appliquent, l'égalité vient en premier, puis les deux blocs.

Un contrôle déterministe additionnel lit les attendus de la suite figée,
sans liste d'identifiants codée en dur. Il contrôle uniquement le gabarit,
sans fabriquer ou réécrire de jugement ni recalculer le barème. Ses
résultats restent distincts de la mesure et de la relecture juridique.
Suite, barème, seuil et preuves historiques sont conservés sans modification.
Le nouveau runtime reste non mesuré, non relu par un praticien.
