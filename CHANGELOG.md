# Historique — dcp-fpt

## [0.1.8] — 2026-11-09 — Frontière dirfi-fpt et traçabilité, non mesuré

Trois réserves de Jo sur DCP-017 (cas-06, cas-08, cas-18) et réserve du cas
`plugin-dcp-frontiere-dsi-externe` du plugin collectivite-territoriale 1.4.0,
1.5.0 et 1.5.1. `SKILL.md` §5.5 : la BASCULE dirfi-fpt s'affiche dès que la
décision d'achat a une incidence financière (estimation ou montage, centrale
d'achat, modification ou avenant, exécution aux frais et risques), et non plus
seulement dans une note d'estimation ou de montage ; après elle, DCP ne dit
plus quelles sommes sont imputables, récupérables ou dues. §4 : la règle de
traçabilité vise aussi ce `SKILL.md` et ses sections, sans lien ni chemin.
Auto-vérification 10 et 12 alignées. Aucune règle de droit, valeur, garde-fou
ni STOP modifié. Runtime différent de 0.1.7 : aucun score transféré, mesure à
refaire.

## [0.1.7] — 2026-11-08 — Réserve R6, mesuré 25/28 avec réserves

Mesure `dcp-017-20261108-b` sur `5debffd` : 25 RÉUSSITE, deux DEMI-RÉUSSITE
(cas-06, cas-08), un ÉCHEC non critique (cas-18) ; huit critiques et six
contrôles STOP réussis ; 56 sessions, 6 115 143 jetons d'entrée. Avis de Jo
(non praticien) du 2026-11-08 : 25 conformes, trois en réserve sur la frontière
dirfi-fpt. Jugements inchangés ; tentative a arrêtée au cas 02 (incident de
sandbox), non retenue. Preuves : `tests/runs/codex-web-v0.1.7-dcp-017-20261108-b` ;
rapport : `docs/qualification-0.1.7-2026-11-08.md`. Relecture praticien en
attente, `publication_ready=false`.

Correction (avant mesure) :

Réserve R6 de la relecture humaine du plugin collectivite-territoriale 1.5.0
(campagne j) : le contrôle de légalité était placé après la notification.
`attribution-signature.md` : pour un marché soumis à transmission, la
transmission prouvée précède la notification ; mention de la transmission sur
le contrat notifié, puis information du représentant de l'État de la date de
notification (CGCT L. 2131-13 et L. 1411-9 pour les communes et leurs
établissements publics) ; prise d'effet sous réserve du contrôle de légalité
(CCP R. 2182-5). Équivalents départemental, régional et intercommunal non lus,
laissés à vérifier. Registre : trois articles ajoutés, lus par l'API Légifrance
le 2026-11-08 ; cache : délais de L. 1411-9. Aucun garde-fou ni STOP modifié.
Runtime différent de 0.1.6 : aucun score transféré, mesure à refaire.

## [0.1.6] — 2026-11-03 — Veille juridique, non mesuré

Veille du 2026-11-03 : textes relus par l'API Légifrance, aucune valeur
modifiée. Deux décisions du Conseil d'État intégrées (19/10/2026, n° 513188 :
seuils de dispense confirmés, L. 3 maintenu ; n° 508690 : paiements partiels
imputés d'abord sur le principal), dans `procedures.md`, `execution-juridique.md`
et le registre. Registre : cinq articles ajoutés (R. 2122-9-1, R. 2191-3,
R. 2191-7, R. 2191-33, R. 2192-31) ; cache : règle des intérêts moratoires
sans taux chiffré, avances, retenue de garantie, dispense innovation. Décision
inédite non intégrée. Intègre le passage à l'EUPL 1.2 (entrée suivante).
Aucun garde-fou ni STOP modifié. Runtime différent de 0.1.5 : aucun score
transféré, mesure à refaire avant toute revendication.

## [Non publié] - 2026-11-01 - Licence EUPL 1.2

Passage du dépôt à la licence publique de l'Union européenne (EUPL) 1.2, à
compter de cette version. Textes officiels de la Commission européenne :
anglais dans `LICENSE`, français dans `LICENCE.fr.txt`. Les versions
antérieures restent sous leur licence d'origine (CC-BY-SA-4.0), sans
réécriture de l'historique. Le kit de mesure locale embarque aussi
`LICENCE.fr.txt`. Aucun changement de comportement du skill.

## [0.1.5] — 2026-10-24 — mesuré avec réserves

Préparé le 2026-10-23 : références internes par nom du skill et section,
sans lien ni chemin dans la réponse. Liens officiels permis ; fond et STOP inchangés.
Décision de Jo : défaut de citation non éliminatoire à fond correct, avec
contrôle automatique informatif exporté pour relecture. Seuil 25/28 et
absence d’ÉCHEC critique inchangés. Aucun score historique transféré.
**Mesuré le 2026-10-23 : 25/28 ; relu par Jo (non praticien) avec réserves le 2026-10-24.**
Deux DEMI-RÉUSSITE (cas-08, cas-15), un ÉCHEC non critique (cas-17) ;
huit critiques réussis. 56 sessions, 5 463 220 jetons d’entrée, six STOP réussis.
Zéro lien ou chemin de skill sur 28 réponses (116 occurrences en 0.1.4).
Avis humain : 22 conformes, six réserves exactes exportées ; jugement inchangé.
Incohérence du juge sur cas-09/17/26 arbitrée par Jo ; règle d’abstention
à préciser pour la suite. Runtime mesuré préservé. Relecture praticien en
attente ; `publication_ready=false`, plugin non qualifié.
[Rapport et suivi](docs/qualification-0.1.5-2026-10-24.md).

## [0.1.4] — 2026-10-20 — STOP en première ligne visible

Gabarit explicite et priorité dans la description pour les deux garde-fous.
Les déclencheurs et le fond des blocs restent inchangés ; aucune règle de droit
nouvelle. Initialement non mesuré au lot D0 ; aucun ancien score transféré.
**Mesuré le 2026-10-20 : 28/28, protocole autonome Codex ; relu par Jo (non praticien).**
56 sessions, 5 829 642 jetons d'entrée, six contrôles STOP réussis. Jo déclare
les 28 cas conformes, sans réserve. Preuves publiques assainies versionnées ;
runtime mesuré préservé. Relecture praticien et qualification du plugin distinctes.
Contrôle automatique additionnel de la première ligne depuis les attendus
figés, exporté dans le kit, sans réécriture des jugements ni changement de barème.

## [0.1.3] — 2026-10-07 — Abstention ciblée et profil MCP

Une réserve finale ne permet pas d’affirmer une règle non vérifiée.
Nouveau profil de mesure autonome Codex/MCP : outils réservés au répondant,
trace des textes et versions récupérés, juge isolé. Suite et barème inchangés.
Les essais antérieurs sont conservés, sans transfert de score.

## [0.1.2] — 2026-10-07 — Renvoi financier borné

DCP ne prescrit plus de circuit financier sans délégataire chargé.
Aucune modification du socle, des STOP ou du barème. Nouvelle campagne
sur les octets de 0.1.2 ; les résultats de 0.1.1 restent historiques.

## [0.1.1] — 2026-10-07 — Candidat correctif

Ordre explicite BASCULE puis intertitre du délégataire, y compris en
coactivation. Séparation entre méthode juridique d'estimation et chiffrage,
crédits ou engagement financier, avec relais nommé dans une note incomplète.
Protocole de mesure : ouverture officielle distincte d'un résultat de
recherche. Aucun nouveau droit, identifiant ni valeur dans le runtime.
Nouvelle mesure : 27 réussites, une demi-réussite (cas-24), aucun échec selon
le juge automatique. Seuil atteint, sans avis praticien ; 20 alertes de
correspondance de sources dans huit cas. Exporteur vérifié et contrôles CI
des preuves contre leurs commits source. Preuves 0.1.0 conservées séparément.

## Mesure autonome — 2026-10-07

Campagne Codex web v0.1.0-r2 complète, 56 rôles avec preuves empreintées.
26 réussites, une demi-réussite et un échec ; huit critiques réussis selon
le juge automatique. Réponses et jugements conservés sans réécriture.
Audit des URL à relire et grille praticien toujours ouverte. Runtime et
version inchangés, aucune publication ni qualification complète du plugin.

## Préparation de mesure — 2026-10-07

Suite de 28 cas fictifs, huit critiques, conforme au cadrage ; barème adapté
à la phase autorisée. CI en mode complet. Profils autonome web et plugin MCP
séparés dans l'ADR 0002. Correction du backend sandbox Windows du lanceur
Codex, couvert par un test logiciel. Runtime, registre et cache inchangés.
La préparation et le contrôle initial ne prouvent aucun seuil atteint.

## Préparation initiale sur main — 2026-10-07 (historique)

Les commits `9bc348ee033ea7c09c4311ef3a01af8f946a4cae` et
`ddafe45216787ca6066d2cebbd7c2b1ff43a4c03`, intégrés par #7,
ont ajouté une première suite de 28 cas et sa relecture contradictoire.
Elle était non lancée à cette étape. La suite du candidat #6 et les
campagnes datées sont ultérieures ; leurs octets restent inchangés.
La fusion locale de préparation est décrite dans
[la note du 12 octobre](docs/assainissement-pr6-2026-10-12.md).

## [0.1.0] — 2026-10-06

Point d'entrée, routeur, douze branches, six objets, cinq gabarits,
quatre scripts et contrôles CI. STOP égalité/acte irréversible et frontières
explicites. Registre/socle conservés, cache exclu du runtime, lacunes réservées.
Gabarits [INCOMPLET] tant que faits, source ou compétence manquent.

**Non mesuré, non relu par un praticien** : aucune suite métier/campagne,
intégration plugin ou modification des autres skills. Tests logiciels avec
entrées factices temporaires uniquement.

Relecture PR #4 : retrait du chemin utilisateur, normalisation des
métadonnées ZIP avec contrôle de l'empreinte sur Windows et Ubuntu,
clarification du rôle du juge en contentieux et prérequis MCP/CLI avant mesure.
