# ADR-0001 — Adopter le patron d'architecture de `dirfi-fpt`

**Statut** : accepté (cadrage validé par l'auteur le 2026-10-06)
**Date** : 2026-10-06

## Contexte

Cinq skills métier territoriaux existent ou sont en cours : `dpm-fpt`,
`drh-fpt`, `dpo-ct`, `dirfi-fpt` et `dsi-fpt`. Ils sont distribués par le
plugin `collectivite-territoriale` avec `recherche-juridique`. Tous excluent
la **passation des marchés publics** : `dirfi-fpt` n'en traite que l'aval
financier, `dsi-fpt` que l'exécution technique des contrats informatiques.
Aucun skill ne couvre donc le cœur de la fonction achat d'une collectivité.

La commande publique combine deux dimensions : des étapes de procédure (besoin,
publicité, analyse, attribution, exécution, contentieux) et des situations
récurrentes qui les traversent (un marché de travaux, un accord-cadre, un
candidat évincé qui conteste, un titulaire défaillant).

## Décision

Reprendre l'architecture de `dirfi-fpt`, elle-même issue de `dpm-fpt`, et
déjà adaptée par `dsi-fpt` : routeur, branches thématiques, objets métier,
gabarits d'écrit ; scripts de validation, de packaging et d'évaluation ; CI ;
`docs/adr/` ; `vault/`.

Écarts assumés par rapport à `dirfi-fpt`, repris de `dsi-fpt` :

1. **Pas d'adaptateur `.claude-plugin/` ni de dossier `skills/`.** Le plugin
   agrégateur est le canal de distribution.
2. **Colonne d'applicabilité dans le socle.** Une partie du droit de la
   commande publique distingue l'État et les autres acheteurs (seuils
   européens), les pouvoirs adjudicateurs et les entités adjudicatrices, les
   marchés et les concessions. Chaque référence porte la mention
   « applicable aux collectivités : oui, non, sous conditions ».
3. **Fiches de cadrage par branche avant rédaction**, pour que plusieurs
   agents rédigent sans doublon ni contradiction.

Écart propre à ce skill :

4. **Seuils et délais exclusivement au cache daté.** Les seuils de procédure
   sont révisés périodiquement. Aucun seuil n'entre dans le runtime ; le skill
   nomme le seuil pertinent et renvoie à sa vérification.

## Conséquences

- Coût de maintenance élevé : 12 branches, 6 objets, 5 gabarits, 3 scripts,
  28 cas de test.
- Revue obligatoire du cache à chaque révision des seuils.
- La justesse pratique ne peut pas être validée par la seule campagne de
  mesure : relecture par un acheteur public ou un juriste de la commande
  publique avant la v1.0.0.

## Alternatives écartées

- **Étendre `dirfi-fpt`** à la passation : sa description et ses garde-fous
  (gestion de fait, contrôle budgétaire) ne couvrent ni l'égalité de
  traitement ni le contentieux de la passation ; le skill dépasserait déjà la
  taille recommandée.
- **Inclure les concessions dès la v1** : régime juridique distinct, qui
  doublerait le socle. Reporté, signalé comme hors périmètre.
