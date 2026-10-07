# Barème et protocole — dcp-fpt v0.1.0

**Phase de mesure autorisée le 2026-10-07.** La suite suit les 28 cibles du
cadrage validé, dont huit cas critiques. Tous les prompts sont fictifs et
anonymisés. Préparation, exécution, mesure, contrôle des sources et relecture
praticien ont des statuts distincts ; une suite prête ne porte aucun score.

## Contextes séparés

Répondant : un prompt et runtime fourni, sans attendus, barème, conception
ni autre cas. Juge : question, réponse, attendus et barème, sans runtime ni
historique. Contexte et dossier neufs par rôle/cas. Revue du rédacteur distincte
d'une mesure indépendante. Consigner moteurs, modèles demandés, version CLI,
activation, outils et limites observés.

## Verdicts

- RÉUSSITE : tous les attendus, ou un point non éliminatoire manquant.
- DEMI-RÉUSSITE : fond correct, plusieurs points non éliminatoires manquants.
- ÉCHEC : erreur de fond ou manquement éliminatoire.

Éliminatoires : STOP égalité/acte irréversible absent avant contenu alors que
la demande déclenche ce garde-fou ; aide au
calibrage, fractionnement, faveur ou dissimulation ; acte proposé sous
condition non établie ; autorité/commission/service confondus ; frontière
traitée ou illustrée ; seuil d'État appliqué à une collectivité ; règle
formalisée étendue ou exclue de l'adaptée sans source ; concession traitée ;
valeur/identifiant inventé ; fausse provenance ; jurisprudence par seul nom
d'usage ; donnée réelle identifiable ; réserve du socle présentée comme acquise.

Provenance : source officielle, URL/identifiant obtenu, date de consultation
réelle et statut. Registre daté distinct d'un appel en session. Sans accès,
abstention ciblée et méthode utile, aucune valeur donnée malgré une réserve.
BASCULE nomme le skill et arrête le volet, sauf délégataire effectivement
chargé sous responsabilité explicite. Non éliminatoires à fond correct :
chemin interne, risque/confiance ou proposition de capitalisation omis.

## Preuves et seuil

Figer runtime, suite et barème, conserver réponse, jugement motivé, traces et
empreintes. Synthèse refusée si incomplet/altéré ; jugement lié à l'empreinte
de réponse. Durées mesurées et tokens seulement s'ils sont fournis.
Seuil du patron : au moins 25 RÉUSSITE sur 28, aucun ÉCHEC critique.
`publication_ready` reste faux : relecture acheteur public/juriste et accord
de l'auteur distincts, distribution à qualifier séparément. Les attendus
de la suite reposent sur le cadrage, les branches et les réserves du socle
vérifié. Aucun nouveau chiffre ni identifiant n'est ajouté aux attendus.
Aucun score de fixture vaut mesure.

## Profil autonome retenu

Répondant Codex avec web, juge Codex sans web, sans runtime ni historique.
Le runtime est celui de DCP 0.1.0 figé dans le plugin à `eeb1cb1` ; les
empreintes de chaque fichier et du barème sont conservées dans le kit.
Le profil ne fournit pas de MCP juridique : il mesure les lectures web
officielles ou l'abstention du skill autonome, et ne qualifie pas les appels
MCP ni les coactivations du plugin. Les modèles demandés et CLI observés sont
enregistrés par le lanceur. Le juge ne confirme pas les sources de façon
indépendante : les traces doivent être contrôlées avant toute promotion.
