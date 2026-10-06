# dcp-fpt — Direction de la commande publique en collectivité territoriale

> **Statut : en construction (v0.1.0, non mesuré).** Le skill n'est pas encore
> utilisable. Le cadrage sera dans `docs/cadrage.md`.

Système expert d'aide à la décision pour la fonction **commande publique**
d'une collectivité territoriale française : définition du besoin, choix et
conduite des procédures de passation, analyse des offres, attribution, puis
exécution juridique des marchés (modifications, résiliation, contentieux).

Il rejoint la famille de skills `collectivite-territoriale`, aux côtés de
`dpm-fpt` (police municipale), `drh-fpt` (ressources humaines), `dpo-ct`
(protection des données), `dirfi-fpt` (finances) et `dsi-fpt` (systèmes
d'information), avec `recherche-juridique` comme validateur de fond.

## Ce que le skill ne fait pas

- Il ne traite pas le volet financier d'un marché (avances, acomptes, révision
  des prix, pénalités, paiement) : c'est `dirfi-fpt`.
- Il ne traite pas les concessions ni les délégations de service public dans
  sa première version.
- Il n'aide jamais à orienter une procédure vers un candidat choisi d'avance.

## Feuille de route

1. Cadrage et décisions d'architecture.
2. Socle de sources vérifiées, avec applicabilité aux collectivités.
3. Rédaction : `SKILL.md`, puis branches, objets et gabarits.
4. Outillage de validation et de mesure.
5. Campagne de mesure de 28 cas, relecture par un praticien ; v1.0.0 au
   premier passage du seuil.
6. Intégration au plugin `collectivite-territoriale`.

## Licence

CC-BY-SA-4.0, comme le plugin `collectivite-territoriale` et les skills qu'il
embarque. Voir `LICENSE`.
