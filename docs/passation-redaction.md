# Dossier de passation — rédaction et outillage de `dcp-fpt`

> **Destinataire** : la session (ChatGPT / Codex) qui rédige le skill.
> **Date** : 2026-10-06. **Décision de l'auteur** : la rédaction et
> l'outillage sont confiés à cette session ; **arrêt avant la campagne de
> mesure**.
> **À lire en premier** : `AGENTS.md` (contraintes non négociables), puis ce
> dossier, puis `docs/cadrage.md`.

---

## 1. État du dépôt au départ

| Élément | Où | Statut |
|---|---|---|
| Cadrage (persona, périmètre, garde-fous, frontières, 12 fiches de branche, objets, gabarits, plan des 28 cas) | `docs/cadrage.md` | **Validé par l'auteur** : source d'autorité |
| Décision d'architecture | `docs/adr/0001-adoption-patron-dirfi-fpt.md` | Acceptée |
| Partage avec `dsi-fpt` | `docs/frontiere-dsi-fpt.md` | Adopté |
| Registre des identifiants vérifiés | `references/references-verifiees.md` | Seul fichier du skill autorisé à porter des identifiants |
| Valeurs datées (seuils, délais, pourcentages, peines) | `references/cache-valeurs.md` | Hors runtime : **exclu du paquet** |
| Méthode de vérification | `references/socle-sources-verification.md` | À conserver, à compléter si besoin |
| Pièces de travail du socle | `docs/socle/lot-1` à `lot-4` | Ne pas modifier sans nouvelle vérification datée |

## 2. Modèle à reproduire

Le skill `dsi-fpt`, achevé par une session ChatGPT/Codex sur la branche
`codex/achever-redaction-outillage-dsi` du dépôt
`brissonjo-sudo/DSI-fpt`, est le modèle le plus récent de la famille. Il
reprend le patron de `dirfi-fpt` (ADR 0001). Reprendre **sa structure et son
outillage**, adapter les constantes et le fond :

| Modèle `dsi-fpt` | Équivalent `dcp-fpt` |
|---|---|
| `SKILL.md` en 9 sections (déclenchement, posture, routeur, branches, dispositifs transverses, écrits, auto-vérification, limites, maintenance) | Même plan ; §5 adapté (voir §4 ci-dessous) |
| `references/analyse-situation.md` (séquence imposée, signaux → branche, frontières, objets, écrits, pièges) | Même structure, signaux de la commande publique |
| `references/_gabarit-branche.md` (12 sections), `objets/_gabarit-objet.md` (6 sections) | Repris, adaptés (« obligation / bonne pratique », « procédure adaptée / formalisée », « collectivité / État ») |
| 12 branches, 6 objets, 5 gabarits d'écrit | Ceux de `docs/cadrage.md` §5 à §8 |
| `scripts/validate_repo.py`, `package_skill.py`, `eval_suite.py`, `mesure_locale.py` | Repris, constantes adaptées (§5) |
| `tests/test_outillage.py`, `tests/test_mesure_locale.py` | Repris |
| `.github/workflows/validation.yml`, `agents/openai.yaml`, `vault/index-dsi-fpt.md` | Repris en `dcp-fpt` |
| `docs/etat-avancement.md`, `docs/relecture-praticien.md` | Repris : suivi et grille du relecteur (acheteur public ou juriste) |

Taille indicative d'une branche dans le modèle : une douzaine de kilo-octets.
Viser la décision, pas l'exhaustivité.

## 3. Ordre de rédaction imposé

1. **`SKILL.md`** d'abord, figé avant toute branche : il porte le routeur,
   les garde-fous et les frontières, que les branches ne font qu'appliquer.
2. **`references/analyse-situation.md`** et les **deux gabarits**.
3. **Les 12 branches**, chacune à partir de **sa fiche** (`docs/cadrage.md`
   §6) : couvre, renvoie, questions types, références candidates. Une
   référence candidate ne s'écrit dans une branche que si elle figure au
   registre.
4. **Les 6 objets** (`docs/cadrage.md` §7) : ils agrègent et pointent vers
   les branches, sans dupliquer.
5. **Les 5 gabarits d'écrit** (`docs/cadrage.md` §8), dans
   `references/templates/`.
6. **Outillage, tests, CI, `vault/`, `README.md`, `CHANGELOG.md`,
   `JOURNAL.md`.**

Si plusieurs rédacteurs travaillent en parallèle, chacun reçoit le `SKILL.md`
figé et **sa seule fiche**, sur des fichiers disjoints.

## 4. `SKILL.md` — points propres à `dcp-fpt`

**Frontmatter** : `name` et `description` seuls ; description de moins de
1 024 caractères, qui **nomme ce qu'elle exclut** : volet financier
(`dirfi-fpt`), contenu technique d'un achat informatique (`dsi-fpt`),
clauses de données personnelles (`dpo-ct`), déontologie et sanction des
agents (`drh-fpt`), besoin opérationnel de police municipale (`dpm-fpt`),
concessions et délégations de service public.

**Mode d'exercice** à lever en ouverture : intégré, mutualisé, groupement de
commandes, centrale d'achat, assistance externe (`docs/cadrage.md` §1).

**Garde-fous** (`docs/cadrage.md` §3), en blocs `STOP` affichés **avant tout
contenu métier**, texte verbatim repris dans `validate_repo.py` :

- **§5.2 Égalité de traitement** : besoin taillé pour un candidat, découpage
  pour passer sous un seuil, information privilégiée, conflit d'intérêts,
  justification après coup. Refus du « comment », risque nommé sans chiffre,
  voie régulière proposée, déport et `BASCULE drh-fpt` pour un agent, aucune
  aide à dissimuler un fait commis.
- **§5.3 Acte irréversible sous délai** : signature ou notification avant la
  fin du délai de suspension ou pendant un référé, exécution sans contrat,
  urgence invoquée sans que ses conditions soient établies. Ne pas signer, ne
  pas notifier, ne pas faire exécuter ; nommer la condition, jamais un délai
  de mémoire ; dire qui décide.

**Frontières** (`docs/cadrage.md` §4) en blocs `BASCULE <skill>` ; règle
commune : « Une frontière ne s'illustre pas. » Concessions : signaler et
s'arrêter.

**Limites** (§8) : mention explicite **« non mesuré, non relu par un
praticien »** tant que la campagne et la relecture n'ont pas eu lieu.

## 5. Adaptations de l'outillage

Dans `scripts/validate_repo.py` :

- `SKILL_NAME = "dcp-fpt"` ;
- `REQUIRED_GUARDRAIL_SNIPPETS` : les phrases d'ouverture verbatim des deux
  blocs `STOP` de `dcp-fpt`, la formule « Une frontière ne s'illustre pas » et
  un bloc `BASCULE dirfi-fpt` ;
- `BRANCH_FILES`, `EXPECTED_OBJETS`, `EXPECTED_TEMPLATES` : les noms du
  cadrage §5, §7 et §8 ;
- contrôle de la description : les frontières `dirfi-fpt`, `dsi-fpt`,
  `dpo-ct`, `drh-fpt`, `dpm-fpt` doivent y figurer ;
- `VALUE_PATTERNS` : garder montants, délais, dates ; **ajouter les
  pourcentages** (modifications de faible montant) ; retirer ce qui ne sert
  qu'au numérique (versions de référentiels) ;
- `SIBLING_REPO_NAMES` : ajouter `dcp-fpt` et `dsi-fpt` ;
- `VALUE_EXEMPT` : registre, cache, gabarits de conception.

Dans `scripts/package_skill.py` : exclure `references/cache-valeurs.md` du
paquet, comme dans le modèle.

## 6. Règles de fond à ne pas perdre

1. **Aucune valeur, aucun identifiant** hors du registre et du cache. Une
   branche nomme le seuil ou le délai pertinent et renvoie à sa vérification.
2. **Seuil de l'État ou seuil d'une collectivité.** Les seuils de procédure
   formalisée des fournitures et services diffèrent entre les autorités
   publiques centrales et les autres pouvoirs adjudicateurs. Le confondre est
   l'erreur que vise un cas de test critique (`cache-valeurs.md`, synthèse).
3. **Procédure adaptée ou formalisée.** Délai de suspension, motivation
   détaillée du rejet, compétence de la commission d'appel d'offres : textes
   écrits pour les procédures formalisées ; ne pas les étendre ni les exclure
   sans la source (`socle-sources-verification.md`, réflexe 4).
4. **Qualité de la collectivité** : pouvoir adjudicateur par inférence des
   définitions générales ; le dire comme tel.
5. **Versions récentes** de plusieurs articles (offre économiquement la plus
   avantageuse, besoin de faible montant, profil d'acheteur, sous-traitance,
   référé précontractuel) : renvoyer à la vérification de la version
   applicable à la date de lancement de la consultation.
6. **Jurisprudence** : juridiction, date, numéro, depuis le registre (§14) ;
   jamais le seul nom d'usage.
7. **Doctrine** : non normative, le dire.
8. **Volet financier** : toujours renvoyé à `dirfi-fpt`.

## 7. Points ouverts du socle — à traiter ou à signaler

| Point | Où | Traitement attendu |
|---|---|---|
| Citations des 13 décisions du Conseil d'État lues par WebFetch (extraction) | Registre §14, lot 4 | Relire sur Légifrance avant de reprendre une citation dans une branche ; sinon citer la décision sans citation littérale |
| Décision très récente sur la résiliation pour motif d'intérêt général | Registre §14 | Portée à confirmer avant usage |
| Doctrine de la direction des affaires juridiques et de l'Observatoire : non ouverte | Registre §15, lot 4 | Ouvrir si possible et dater ; sinon ne rien en citer |
| Vigueur des CCAG sans modification depuis leur approbation : non consolidée | Registre §9 | Vérifier ou maintenir la réserve |
| Lacunes : paiement direct du sous-traitant, comités consultatifs de règlement amiable, livre IV (marchés globaux), R. 2194-2, -3 et -6, exceptions à la voie électronique | Sections « Non trouvé » des lots | Vérifier avant de rédiger le point, ou le signaler « à vérifier » dans la branche |

Toute nouvelle vérification s'ajoute **au lot concerné puis au registre**,
avec sa date ; jamais directement dans une branche.

## 8. Définition de « terminé »

- `python3 scripts/validate_repo.py` : **zéro erreur**. Seule l'absence de
  `tests/cas-de-test.json` est tolérée, la campagne étant hors périmètre (ou
  reprendre l'option `--partiel` du modèle et le documenter).
- Tests unitaires verts ; CI verte.
- Version **0.1.0** alignée dans `SKILL.md` (titre et métadonnées),
  `README.md`, `CHANGELOG.md`, `vault/index-dcp-fpt.md`.
- Mention « non mesuré, non relu par un praticien » dans `README.md` et
  `SKILL.md`.
- `docs/socle/` et le registre inchangés, sauf ajout vérifié et daté.
- Une PR vers `main` ; pas de fusion sans l'accord de l'auteur.

## 9. Hors périmètre de cette passation

- Rédaction des 28 cas de test et campagne de mesure.
- Intégration au plugin `collectivite-territoriale`.
- Mise à jour des frontières dans les autres skills (`dirfi-fpt`, `dsi-fpt`) :
  elle n'interviendra qu'une fois `dcp-fpt` distribué, pour ne pas créer de
  renvoi vers un skill inexistant.
