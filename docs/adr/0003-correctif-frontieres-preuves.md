# ADR 0003 — Corriger les frontières et renforcer la preuve de lecture

- Date : 2026-10-07.
- Statut : accepté pour le candidat correctif, non publié.
- Autorisation : poursuite demandée après les résultats et réserves de mesure.

Le cas plugin finance/données place les BASCULE après leurs intertitres.
Le point d'entrée précise désormais l'ordre attendu : bloc de transfert,
intertitre du délégataire, analyse de celui-ci. Les deux STOP sont inchangés.
Le cadrage juridique de l'estimation reste DCP ; chiffrage, crédits et
engagement relèvent de dirfi. Une note incomplète doit nommer ce relais.

Le candidat prend la version 0.1.1. Aucune nouvelle règle de droit, valeur ou
référence n'est ajoutée. Le socle et le registre restent inchangés. Les
preuves de 0.1.0 sont conservées sans retouche et sans transfert de score.

Le protocole du répondant exige une ouverture officielle avant toute
déclaration de lecture. Une recherche ou une action sérialisée de manière
ambiguë ne suffit pas à attester cette lecture. Les attendus et le barème
restent hors contexte du répondant. Nouveau kit, suite et barème inchangés.

L'intégration du nouveau runtime dans le plugin doit être épinglée à son
commit, puis faire l'objet de nouveaux essais. La distribution v1.1.1 et
la relecture praticien restent distinctes de ces opérations.
