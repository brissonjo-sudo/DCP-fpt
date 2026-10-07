# dcp-fpt — Direction de la commande publique en collectivité territoriale v0.1.2

> **Candidat 0.1.2 : renvoi financier borné, nouvelle mesure requise.**

> **Historique 0.1.1 mesuré sur Codex : 27 réussites, une demi-réussite, aucun
> échec selon le juge automatique. Non relu par un praticien.**
> Réserve cas-24 et 20 alertes de correspondance de sources dans huit cas.
> Seuil automatique atteint ; qualification juridique et plugin ouvertes.

Les campagnes 0.1.0 et 0.1.1 conservent leurs propres réponses et jugements.
Le runtime figé avant mesure garde la mention « non mesuré, non relu par un praticien » ;
son statut actualisé est consigné hors paquet dans le
[rapport 0.1.1](docs/qualification-0.1.1-2026-10-07.md), sans changer ses octets.

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
- Contenu informatique → `dsi-fpt` ; clauses de données personnelles →
  `dpo-ct` ; déontologie/sanction d'agent → `drh-fpt` ; besoin opérationnel
  PM → `dpm-fpt`. Vigueur/portée → `recherche-juridique`.
- Contrats de l'État et droit étranger : hors périmètre. Une frontière ne
  s'illustre pas.
- Il n'aide jamais à orienter une procédure vers un candidat choisi d'avance.

## Contenu et usage

Lire [SKILL.md](SKILL.md), puis le [routeur](references/analyse-situation.md).
Douze branches, six objets et cinq gabarits orientent conditions, autorités
et écrits. Deux STOP avant contenu : égalité de traitement et acte irréversible
sous condition non établie. Mode intégré, mutualisé, groupement, centrale ou
assistance externe à lever en ouverture. Aucune donnée réelle identifiable.

Registre daté distinct d'une vérification en session. Le cache des valeurs
est **exclu du runtime** : source officielle en session pour seuil, délai ou
pourcentage. Réserves dans les branches et [grille de relecture](docs/relecture-praticien.md).

## Contrôles et paquet

Python 3.11 ou ultérieur, sans bibliothèque tierce, depuis le dépôt :

```powershell
python scripts/validate_repo.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/package_skill.py
```

`--sans-campagne` tolère uniquement la suite métier absente. Si elle est
présente, elle reste contrôlée ; sans option, l'absence échoue. Aucun mode
partiel général dans la CI. Tests avec fixtures temporaires et CLI simulées,
sans appel modèle ni score du skill.

Archive déterministe : dist/dcp-fpt-0.1.2.zip. Contenu : SKILL.md,
agents/openai.yaml, references/ sauf cache, objets/. Conception, scripts,
tests, preuves, journal et index hors paquet. Distribution via plugin après
phase de qualification autorisée, aucune installation dans cette passation.

## Feuille de route

1. Cadrage et décisions d'architecture : validés.
2. Socle daté et applicabilité : conservés, avec réserves.
3. Point d'entrée, branches, objets et gabarits : rédigés.
4. Outillage de validation, mesure et export de preuves : livré.
5. Suite de 28 cas mesurée sur les runtimes 0.1.0 puis 0.1.1 ; seuil
   automatique atteint pour chaque campagne, résultats séparés.
   Relecture praticien et contrôle des sources à réaliser. Promotion en
   v1.0.0 et mesure du runtime promu à établir.
6. Intégration candidate au plugin `collectivite-territoriale` 1.2.0 réalisée ;
   distribution maintenue sur v1.1.1, sans DCP, avant qualification.

[État et preuves](docs/etat-avancement.md) · [Passation](docs/passation-redaction.md) ·
[Cadrage](docs/cadrage.md) · [Protocole de mesure](docs/campagne-locale.md).
Aucun seuil de publication déclaré atteint. Patron DSI : provenance dans l'état.

## Licence

CC-BY-SA-4.0, comme le plugin `collectivite-territoriale` et les skills qu'il
embarque. Voir `LICENSE`.
