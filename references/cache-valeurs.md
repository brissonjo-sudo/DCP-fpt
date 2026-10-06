# Cache des valeurs datées

> **Registre de maintenance, hors runtime distribué** (exclu du paquet du
> skill). Il réunit les valeurs volatiles — seuils de procédure, montants,
> délais, pourcentages, peines — lues à la source, avec leur date de lecture.
> Il sert à rédiger et à mettre à jour le skill ; le skill lui-même n'énonce
> **jamais** une de ces valeurs sans la revérifier à la source en session et
> sans dater sa provenance.
>
> **Règle** : une valeur de ce cache n'est jamais recopiée telle quelle dans
> une réponse. Elle indique **quoi vérifier**, et **où**.
>
> **Révision obligatoire** : les seuils européens sont révisés tous les deux
> ans par règlement délégué de la Commission, repris par un avis français.
> À chaque révision, relire les deux et mettre à jour ce fichier.
>
> Toutes les valeurs ci-dessous ont été lues le **2026-10-06** (sources et
> identifiants : `references-verifiees.md` et `docs/socle/`).

## Synthèse des seuils de procédure formalisée (applicables au 2026-01-01)

Confrontation faite le 2026-10-06 : les montants de l'avis français (lu par
WebFetch, résumé) **concordent** avec ceux du règlement délégué (UE)
2025/2152, lu en texte intégral sur CELLAR (lot 3).

| Catégorie | Fournitures et services | Travaux | Vise une collectivité ? |
|---|---|---|---|
| Autres pouvoirs adjudicateurs (« sous-centraux ») | 216 000 € HT | 5 404 000 € HT | **Oui** |
| Autorités publiques centrales | 140 000 € HT | 5 404 000 € HT | **Non** (l'annexe I de la directive ne liste aucune collectivité) |
| Entités adjudicatrices | 432 000 € HT | 5 404 000 € HT | Sous conditions (activité d'opérateur de réseaux) |

**Piège d'applicabilité** : le seuil de 140 000 € HT est celui de l'État. Le
présenter comme celui d'une commune est une erreur (cas de test critique).

## Valeurs du droit français (code de la commande publique, partie réglementaire)

Valeurs lues dans le texte des articles (champ `text` de `get_article`) ; aucune n'est reprise de la mémoire. Date de lecture : 2026-10-06. « Début d'application » = `version_start_date` de la version lue.

| Valeur | Source exacte | Date de lecture | Date de début d'application (version lue) |
|---|---|---|---|
| Besoin de faible montant, marchés de fournitures ou de services : valeur estimée inférieure à 60 000 euros HT (marché sans publicité ni mise en concurrence) | CCP, art. R. 2122-8 (LEGIARTI000053222294) | 2026-10-06 | 2026-04-01 |
| Besoin de faible montant, marchés de travaux : valeur estimée inférieure à 100 000 euros HT | CCP, art. R. 2122-8 (LEGIARTI000053222294) | 2026-10-06 | 2026-04-01 |
| Livraisons complémentaires du fournisseur initial, marché passé par un pouvoir adjudicateur : durée maximale de trois ans, périodes de reconduction comprises, « sauf cas dûment justifié » | CCP, art. R. 2122-4, 1° (LEGIARTI000037730877) | 2026-10-06 | 2019-04-01 |
| Prestations similaires (marché précédent mis en concurrence), marché passé par un pouvoir adjudicateur : les nouveaux marchés ne peuvent être conclus que pendant trois ans à compter de la notification du marché initial | CCP, art. R. 2122-7 (LEGIARTI000037730871) | 2026-10-06 | 2019-04-01 |
| Lot d'un marché alloti de valeur totale égale ou supérieure aux seuils formalisés, procédure adaptée possible : valeur estimée de chaque lot inférieure à 80 000 euros HT (fournitures ou services) ou à 1 million d'euros HT (travaux) | CCP, art. R. 2123-1, 2°, a (LEGIARTI000043316424) | 2026-10-06 | 2021-04-02 |
| Même mécanisme : montant cumulé de ces lots n'excédant pas 20 % de la valeur totale estimée de tous les lots | CCP, art. R. 2123-1, 2°, b (LEGIARTI000043316424) | 2026-10-06 | 2021-04-02 |
| Appel d'offres ouvert : délai minimal de réception des candidatures et des offres de trente-cinq jours à compter de la date d'envoi de l'avis de marché | CCP, art. R. 2161-2 (LEGIARTI000037730439) | 2026-10-06 | 2019-04-01 |
| Appel d'offres ouvert, délai ramené à quinze jours si avis de préinformation ou avis périodique indicatif non utilisé comme avis d'appel à la concurrence, envoyé pour publication trente-cinq jours au moins à douze mois au plus avant l'envoi de l'avis de marché, avec les mêmes renseignements | CCP, art. R. 2161-3, 1° (LEGIARTI000037730437) | 2026-10-06 | 2019-04-01 |
| Appel d'offres ouvert, délai ramené à trente jours si les candidatures et les offres sont ou peuvent être transmises par voie électronique | CCP, art. R. 2161-3, 2° (LEGIARTI000037730437) | 2026-10-06 | 2019-04-01 |
| Appel d'offres ouvert, délai ramené à quinze jours en cas de situation d'urgence dûment justifiée rendant le délai minimal impossible à respecter | CCP, art. R. 2161-3, 3° (LEGIARTI000037730437) | 2026-10-06 | 2019-04-01 |
| Appel d'offres restreint, pouvoirs adjudicateurs : délai minimal de réception des candidatures de trente jours à compter de l'envoi de l'avis de marché (ou de l'invitation à confirmer l'intérêt si l'appel à la concurrence passe par un avis de préinformation) | CCP, art. R. 2161-6, 1° (LEGIARTI000037730429) | 2026-10-06 | 2019-04-01 |
| Appel d'offres restreint, pouvoirs adjudicateurs, urgence dûment justifiée : délai de réception des candidatures non inférieur à quinze jours | CCP, art. R. 2161-6, 1° (LEGIARTI000037730429) | 2026-10-06 | 2019-04-01 |
| Appel d'offres restreint, entités adjudicatrices (non applicable à une collectivité agissant comme pouvoir adjudicateur) : quinze jours pour la réception des candidatures | CCP, art. R. 2161-6, 2° (LEGIARTI000037730429) | 2026-10-06 | 2019-04-01 |
| Appel d'offres restreint, pouvoirs adjudicateurs : délai minimal de réception des offres de trente jours à compter de l'envoi de l'invitation à soumissionner | CCP, art. R. 2161-7 (LEGIARTI000037730427) | 2026-10-06 | 2019-04-01 |
| Appel d'offres restreint, délai de réception des offres ramené à dix jours (avis de préinformation envoyé trente-cinq jours au moins à douze mois au plus avant l'avis de marché, mêmes renseignements) | CCP, art. R. 2161-8, 1° (LEGIARTI000037730425) | 2026-10-06 | 2019-04-01 |
| Appel d'offres restreint, délai de réception des offres ramené à vingt-cinq jours si les offres sont transmises par voie électronique | CCP, art. R. 2161-8, 2° (LEGIARTI000037730425) | 2026-10-06 | 2019-04-01 |
| Appel d'offres restreint, délai de réception des offres ramené à dix jours en cas de situation d'urgence dûment justifiée | CCP, art. R. 2161-8, 3° (LEGIARTI000037730425) | 2026-10-06 | 2019-04-01 |
| Appel d'offres restreint, pouvoir adjudicateur autre qu'autorité publique centrale, à défaut d'accord sur la date limite de réception des offres : délai non inférieur à dix jours à compter de l'envoi de l'invitation à soumissionner | CCP, art. R. 2161-9 (LEGIARTI000037730423) | 2026-10-06 | 2019-04-01 |
| Procédure avec négociation (pouvoirs adjudicateurs) : délai minimal de réception des candidatures de trente jours à compter de l'envoi de l'avis de marché (ou de l'invitation à confirmer l'intérêt) | CCP, art. R. 2161-12 (LEGIARTI000037730413) | 2026-10-06 | 2019-04-01 |
| Même procédure, urgence dûment justifiée : délai de réception des candidatures non inférieur à quinze jours | CCP, art. R. 2161-12 (LEGIARTI000037730413) | 2026-10-06 | 2019-04-01 |
| Procédure adaptée des collectivités : en dessous de 90 000 euros HT de valeur estimée du besoin, modalités de publicité librement adaptées ; à partir de 90 000 euros HT et en dessous des seuils de procédure formalisée, avis de marché au BOAMP ou dans un journal habilité à recevoir des annonces légales | CCP, art. R. 2131-12, 1° et 2° (LEGIARTI000037955801) | 2026-10-06 | 2022-01-01 |
| Mise à disposition des documents de la consultation sur un profil d'acheteur obligatoire dès que la valeur estimée du besoin est égale ou supérieure à 60 000 euros HT et que la procédure donne lieu à un avis d'appel à la concurrence | CCP, art. R. 2132-2 (LEGIARTI000053222317) | 2026-10-06 | 2026-04-01 |
| Délai minimal entre l'envoi de la notification de rejet et la signature du marché en procédure formalisée : onze jours | CCP, art. R. 2182-1, 1re phrase (LEGIARTI000037729989) | 2026-10-06 | 2019-04-01 |
| Même délai porté à seize jours lorsque la notification de rejet n'a pas été transmise par voie électronique | CCP, art. R. 2182-1, 2e phrase (LEGIARTI000037729989) | 2026-10-06 | 2019-04-01 |
| Avis d'attribution (besoin égal ou supérieur aux seuils européens) : envoi pour publication au plus tard trente jours à compter de la signature du marché | CCP, art. R. 2183-1 (LEGIARTI000037729971) | 2026-10-06 | 2019-04-01 |
| Données essentielles : publication pour les marchés de valeur égale ou supérieure à 40 000 euros HT, dans les deux mois suivant la notification du marché ou sa modification | CCP, art. R. 2196-1, 1er alinéa (LEGIARTI000045739606) | 2026-10-06 | 2024-01-01 |
| Données essentielles, marchés conclus en application de R. 2122-8 de valeur égale ou supérieure à 25 000 euros HT : même obligation, avec possibilité de publier à la place, au premier trimestre de chaque année, la liste des marchés de l'année précédente | CCP, art. R. 2196-1, derniers alinéas (LEGIARTI000045739606) | 2026-10-06 | 2024-01-01 |
| Modification de faible montant, marchés de services et de fournitures : montant de la modification inférieur à 10 % du montant du marché initial (et inférieur aux seuils européens de l'avis annexé, voir §7) | CCP, art. R. 2194-8 (LEGIARTI000037729541) | 2026-10-06 | 2019-04-01 |
| Modification de faible montant, marchés de travaux : montant de la modification inférieur à 15 % du montant du marché initial (et inférieur aux seuils européens de l'avis annexé) | CCP, art. R. 2194-8 (LEGIARTI000037729541) | 2026-10-06 | 2019-04-01 |
| Sous-traitance déclarée après la notification : le silence de l'acheteur pendant vingt-et-un jours à compter de la réception des documents de R. 2193-3 vaut acceptation du sous-traitant et agrément des conditions de paiement | CCP, art. R. 2193-4 (LEGIARTI000037729621) | 2026-10-06 | 2019-04-01 |
| Seuil de procédure formalisée, fournitures et services, « Autres pouvoirs adjudicateurs » (catégorie des collectivités) : 216 000 euros HT | Avis du 13 janvier 2026, JORFTEXT000053346567 (lu par WebFetch, repli) ; mêmes valeurs rapportées dans l'avis du 26 décembre 2025, JORFTEXT000053170349 | 2026-10-06 | 2026-01-01 |
| Seuil de procédure formalisée, fournitures et services, « Autorités publiques centrales sauf dans les cas du c) » (État et autorités listées, hors collectivités) : 140 000 euros HT | Avis du 13 janvier 2026, JORFTEXT000053346567 (lu par WebFetch, repli) ; même valeur rapportée dans l'avis du 26 décembre 2025 | 2026-10-06 | 2026-01-01 |
| Seuil de procédure formalisée, marchés de travaux (toutes catégories de pouvoirs adjudicateurs) : 5 404 000 euros HT | Avis du 13 janvier 2026, JORFTEXT000053346567 (lu par WebFetch, repli) ; même valeur rapportée dans l'avis du 26 décembre 2025 | 2026-10-06 | 2026-01-01 |
| Seuil de procédure formalisée, fournitures et services, entités adjudicatrices (non applicable à une collectivité pouvoir adjudicateur) : 432 000 euros HT | Avis du 13 janvier 2026, JORFTEXT000053346567 (lu par WebFetch, repli) | 2026-10-06 | 2026-01-01 |
| Seuil des contrats de concession (hors périmètre du socle) : 5 404 000 euros HT | Avis du 13 janvier 2026, JORFTEXT000053346567 (lu par WebFetch, repli) | 2026-10-06 | 2026-01-01 |

## Valeurs du droit de l'Union, du CJA, du CGCT et du code pénal

Valeurs lues dans le texte des articles ou des règlements (champ `text` de `get_article` ; texte intégral CELLAR) ; aucune n'est reprise de la mémoire. Date de lecture : 2026-10-06. « Date d'application » = `version_start_date` de la version lue, ou date d'application inscrite dans l'acte.

#### A. Seuils : droit de l'Union, confrontation au lot 2

Colonne « Concorde avec le lot 2 ? » : comparaison avec la ligne correspondante de la section « Valeurs relevées » du lot 2 (lue par WebFetch, résumé, avis du 13 janvier 2026, JORFTEXT000053346567).

| Valeur | Source exacte | Date de lecture | Date d'application | Concorde avec le lot 2 ? |
|---|---|---|---|---|
| Fournitures et services, pouvoirs adjudicateurs sous-centraux (catégorie des collectivités) : 216 000 euros HT | Directive 2014/24/UE, art. 4, c), montant tel que consolidé au 01.01.2026 (CELEX 02014L0024-20260101) ; règlement délégué (UE) 2025/2152, art. 1er, 1), c) : « «221 000 EUR» est remplacée par «216 000 EUR» » (CELEX 32025R2152) | 2026-10-06 | 2026-01-01 (« Il est applicable à partir du 1er janvier 2026 ») | **Oui** (216 000 euros HT « Autres pouvoirs adjudicateurs ») |
| Fournitures et services, autorités publiques centrales : 140 000 euros HT | Directive 2014/24/UE, art. 4, b), consolidé ; règlement 2025/2152, art. 1er, 1), b) : « «143 000 EUR» est remplacée par «140 000 EUR» » | 2026-10-06 | 2026-01-01 | **Oui** (140 000 euros HT) |
| Travaux : 5 404 000 euros HT | Directive 2014/24/UE, art. 4, a), consolidé ; règlement 2025/2152, art. 1er, 1), a) : « «5 538 000 EUR» est remplacée par «5 404 000 EUR» » | 2026-10-06 | 2026-01-01 | **Oui** (5 404 000 euros HT) |
| Services sociaux et autres services spécifiques (annexe XIV) : 750 000 euros HT, non modifié par le règlement | Directive 2014/24/UE, art. 4, d), consolidé | 2026-10-06 | texte initial (non modifié par M6) | Non comparé : le lot 2 n'avait pas relevé cette valeur (avis annexé non lu sur ce point, lot 2, « Non trouvé ») |
| Seuil de l'art. 13 (marchés subventionnés), travaux : 5 404 000 euros HT ; services : 216 000 euros HT | Règlement 2025/2152, art. 1er, 2), a) et b) | 2026-10-06 | 2026-01-01 | Non comparé (valeur absente du lot 2) |
| Entités adjudicatrices, fournitures et services : 432 000 euros HT (ancien : 443 000 euros) ; travaux : 5 404 000 euros HT (ancien : 5 538 000 euros) | Règlement délégué (UE) 2025/2150 : « «443 000 EUR» est remplacée par «432 000 EUR» » ; « «5 538 000 EUR» est remplacée par «5 404 000 EUR» » (CELEX 32025R2150) | 2026-10-06 | 2026-01-01 | **Oui** pour 432 000 (non applicable à une collectivité pouvoir adjudicateur) |
| Concessions : 5 404 000 euros HT (ancien : 5 538 000 euros) | Règlement délégué (UE) 2025/2151, art. 1er : « la mention «5 538 000 EUR» est remplacée par «5 404 000 EUR» » (CELEX 32025R2151) | 2026-10-06 | 2026-01-01 | **Oui** (hors périmètre v1) |
| Défense ou sécurité (directive 2009/81/CE, art. 8) : 432 000 euros (ancien : 443 000 euros) ; 5 404 000 euros (ancien : 5 538 000 euros) | Règlement délégué (UE) 2025/2487 : « «443 000 EUR» est remplacé par «432 000 EUR» » ; « «5 538 000 EUR» est remplacé par «5 404 000 EUR» » (CELEX 32025R2487) | 2026-10-06 | 2026-01-01 | **Divergence du lot 2 expliquée** : 443 000 et 5 538 000 sont les anciens montants ; 432 000 et 5 404 000 les nouveaux |
| Lots dispensés de la directive, valeur estimée du lot inférieure à : 80 000 euros HT (fournitures ou services), 1 000 000 euros HT (travaux) ; cumul des lots n'excédant pas 20 % de la valeur cumulée de tous les lots | Directive 2014/24/UE, art. 5, §10 | 2026-10-06 | texte consolidé 01.01.2026 | **Oui** (lot 2 : R. 2123-1, 2°, a et b : 80 000 euros HT, 1 million d'euros HT, 20 %) |
| Marchés de fournitures ou de services réguliers : base de calcul = valeur réelle des contrats successifs des douze mois précédents ou de l'exercice précédent, ou valeur estimée des douze mois suivants (ou de l'exercice si supérieur à douze mois) | Directive 2014/24/UE, art. 5, §11 | 2026-10-06 | texte consolidé 01.01.2026 | Non comparé (cf. lot 2 §1, calcul de la valeur) |
| Services sans prix total : durée déterminée de quarante-huit mois au plus : valeur totale pour la durée ; durée indéterminée ou supérieure : valeur mensuelle multipliée par 48 | Directive 2014/24/UE, art. 5, §14 | 2026-10-06 | texte consolidé 01.01.2026 | Non comparé |

**Résultat de la confrontation.** Les trois seuils utiles à une collectivité (216 000 / 140 000 / 5 404 000 euros HT) et ceux des entités adjudicatrices et des concessions **concordent** entre le lot 2 (avis du 13 janvier 2026, lu par WebFetch) et le droit de l'Union (texte intégral lu dans CELLAR). Ces montants sont donc **confirmés à la source de l'Union**. ⚠️ Le texte de l'avis français n'a pas été relu intégralement (annexe n° 2 du CCP) : la confirmation porte sur le montant d'origine, pas sur la reprise littérale par l'avis.

#### B. Délais, seuils et pourcentages du droit français lus dans ce lot

| Valeur | Source exacte | Date de lecture | Date d'application |
|---|---|---|---|
| Juge du référé précontractuel : statue dans un délai de vingt jours ; ne peut statuer avant le seizième jour à compter de l'envoi de la décision d'attribution, ramené au onzième jour si communication électronique à l'ensemble des opérateurs ; pour les contrats de L. 551-15, al. 1, pas avant le onzième jour à compter de la publication de l'intention de conclure | CJA, art. R. 551-5 (LEGIARTI000021357742) | 2026-10-06 | 2009-12-01 |
| Juge du référé contractuel : statue dans un délai d'un mois | CJA, art. R. 551-9 (LEGIARTI000021357773) | 2026-10-06 | 2009-12-01 |
| Saisine du juge du référé contractuel : au plus tard le trente et unième jour suivant la publication au JOUE de l'avis d'attribution (ou, pour accord-cadre / SAD, suivant la notification de la conclusion du contrat, qui doit mentionner le nom du titulaire et les motifs du choix) ; à défaut de publication ou notification : jusqu'à six mois à compter du lendemain du jour de la conclusion du contrat | CJA, art. R. 551-7 (LEGIARTI000032308765) | 2026-10-06 | 2016-04-01 |
| Référé contractuel fermé : contrat sans publicité préalable si l'intention de conclure a été rendue publique et un délai de onze jours observé après la publication | CJA, art. L. 551-15, al. 1 (LEGIARTI000020602072) | 2026-10-06 | 2009-05-09 |
| Référé contractuel fermé : contrats sur accord-cadre ou SAD, délai de seize jours entre l'envoi de la décision d'attribution et la conclusion, réduit à onze jours si la décision a été communiquée à tous les titulaires par voie électronique | CJA, art. L. 551-15, al. 2 (LEGIARTI000020602072) | 2026-10-06 | 2009-05-09 |
| Interdiction de signer le contrat : à compter de la saisine du tribunal administratif jusqu'à la notification au pouvoir adjudicateur de la décision juridictionnelle (pas de durée chiffrée) | CJA, art. L. 551-4 (LEGIARTI000020602109) | 2026-10-06 | 2009-05-09 |
| Délai de suspension avant signature (rappel du lot 2, R. 2182-1) : onze jours, seize si notification non électronique. Concorde avec les onze et seize jours de R. 551-5 / L. 551-15 lus ici (même ordre de grandeur, textes distincts) | CCP, art. R. 2182-1 (lot 2, non relu ici) ; CJA, art. R. 551-5 et L. 551-15 | lot 2 : 2026-10-06 | 2019-04-01 (R. 2182-1) |
| Commission d'appel d'offres (région, collectivité de Corse, département, commune de 3 500 habitants et plus, établissement public) : autorité habilitée ou son représentant, président, et cinq membres de l'assemblée délibérante élus en son sein à la représentation proportionnelle au plus fort reste | CGCT, art. L. 1411-5, II, a (LEGIARTI000041411540), par renvoi de L. 1414-2 | 2026-10-06 | 2019-12-29 |
| CAO, commune de moins de 3 500 habitants : maire ou son représentant, président, et trois membres du conseil municipal élus à la représentation proportionnelle au plus fort reste ; suppléants en nombre égal | CGCT, art. L. 1411-5, II, b (LEGIARTI000041411540) | 2026-10-06 | 2019-12-29 |
| Quorum de la CAO : plus de la moitié des membres ayant voix délibérative présents ; à défaut, nouvelle convocation, la commission se réunit alors valablement sans condition de quorum | CGCT, art. L. 1411-5, II (LEGIARTI000041411540) | 2026-10-06 | 2019-12-29 |
| Avenant soumis pour avis à la CAO : augmentation du montant global supérieure à 5 % | CGCT, art. L. 1414-4 (LEGIARTI000030927820) | 2026-10-06 | 2016-04-01 |
| CAO compétente pour attribuer : procédure formalisée dont la valeur estimée HT prise individuellement est égale ou supérieure aux « seuils européens qui figurent en annexe du code de la commande publique » (pas de montant dans l'article) | CGCT, art. L. 1414-2 (LEGIARTI000037739193) | 2026-10-06 | 2019-04-01 |
| Seuil de transmission des marchés au représentant de l'État : « celui qui s'applique aux marchés publics de fournitures et de services passés par les pouvoirs adjudicateurs autres que les autorités publiques centrales selon l'une des procédures formalisées » ; pas de montant dans l'article. Valeur correspondante lue ailleurs (UE, ligne « sous-centraux », section A) : 216 000 euros HT, applicable à partir du 2026-01-01. ⚠️ Pas de lecture du texte de L. 2124-1 CCP ni de l'avis pour confirmer que 216 000 euros HT est bien la valeur visée par D. 2131-5-1 (inférence) | CGCT, art. D. 2131-5-1 (LEGIARTI000039633616) ; L. 2131-2, 4° ; L. 3131-2, 4° ; L. 4141-2, 3° | 2026-10-06 | 2020-01-01 |
| Transmission des décisions individuelles dans un délai de quinze jours à compter de leur signature (décisions individuelles, pas les marchés) | CGCT, art. L. 2131-2, II (LEGIARTI000044190560) | 2026-10-06 | 2022-07-01 |
| Régime dérogatoire des petites communes (prise illégale d'intérêts) : communes comptant 3 500 habitants au plus ; maires, adjoints ou conseillers délégués peuvent traiter avec leur commune pour le transfert de biens ou la fourniture de services dans la limite d'un montant annuel fixé à 16 000 euros | CP, art. 432-12 (LEGIARTI000053152943) | 2026-10-06 | 2025-12-24 |

#### C. Peines (code pénal), lues à titre de valeurs, jamais à reproduire hors de ce tableau

| Valeur | Source exacte | Date de lecture | Date d'application |
|---|---|---|---|
| Atteinte à la liberté d'accès et à l'égalité des candidats (favoritisme) : deux ans d'emprisonnement et amende de 200 000 euros, ce montant pouvant être porté au double du produit tiré de l'infraction | CP, art. 432-14 (LEGIARTI000033611461) | 2026-10-06 | 2016-12-11 |
| Prise illégale d'intérêts : cinq ans d'emprisonnement et amende de 500 000 euros, ce montant pouvant être porté au double du produit tiré de l'infraction | CP, art. 432-12 (LEGIARTI000053152943) | 2026-10-06 | 2025-12-24 |
