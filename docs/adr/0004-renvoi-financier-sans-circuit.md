# ADR 0004 — Borner le renvoi sans délégataire chargé

- Date : 2026-10-07.
- Statut : accepté pour le candidat 0.1.2, non publié.

La réponse du cas autonome 24 en 0.1.1 arrête les calculs mais propose encore
un circuit d'instruction et de validation financière. Le point d'entrée
borne désormais la poursuite aux pièces manquantes et au point juridique
du marché. Aucun circuit financier ni acteur du paiement n'est prescrit
sans chargement du délégataire.

Les deux STOP, les branches, le registre et le barème restent inchangés.
Aucune règle de droit ni valeur n'est ajoutée. Les preuves 0.1.1 restent
conservées ; leurs scores ne qualifient pas les octets de 0.1.2. Un nouveau
kit mesure le candidat, puis l'intégration plugin exige de nouveaux essais.
