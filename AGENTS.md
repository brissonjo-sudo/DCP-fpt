# Consignes de contribution — dépôt `dcp-fpt`

Ce dépôt porte un **skill d'aide à la décision**, pas une documentation. Ce qui
y est écrit est lu par un modèle et devient une réponse donnée à un acheteur
public. Une erreur peut faire annuler un marché, engager la responsabilité de
la collectivité ou exposer un agent ou un élu à une poursuite pénale. Les
contraintes ci-dessous ne sont pas des préférences de style.

## Contraintes non négociables

1. **Français** partout : contenu, commentaires de code, messages de commit.
2. **Aucune règle de droit, valeur ou délai de mémoire.** Seuils de procédure,
   délais de réception des offres, délai de suspension, délais de recours :
   ils se vérifient à la source ou ne s'écrivent pas. Les seuils changent
   périodiquement : ils ne vivent que dans le cache daté.
3. **Aucun identifiant officiel en dur** (`LEGIARTI`, `JORFTEXT`, `CETATEXT`,
   CELEX) dans les fichiers du skill (`SKILL.md`, `references/`, `objets/`)
   hors de `references/references-verifiees.md`, seul registre autorisé, et
   seulement pour des identifiants **réellement vérifiés**, datés. Les
   dossiers de vérification de `docs/socle/` en contiennent aussi : ce sont
   les pièces de travail d'où le registre est tiré, hors runtime.
4. **Applicabilité aux collectivités.** Une règle propre à l'État, aux
   autorités publiques centrales, aux entités adjudicatrices ou aux
   concessions ne se présente jamais comme applicable à une collectivité sans
   la source qui l'établit. La doctrine (guides et fiches de la direction des
   affaires juridiques de Bercy, Observatoire économique de la commande
   publique) n'est pas du droit positif.
5. **Les deux garde-fous sont intouchables.** Le garde-fou égalité de
   traitement et le garde-fou acte irréversible sous délai s'affichent
   **avant** tout contenu métier. Les affaiblir ou les rendre conditionnels
   est une régression bloquante.
6. **Les frontières sont opposables** : volet financier du marché →
   `dirfi-fpt` ; contenu technique d'un achat informatique → `dsi-fpt` ;
   clauses relatives aux données personnelles → `dpo-ct` ; déontologie et
   sanction d'un agent → `drh-fpt` ; concessions et délégations de service
   public : hors périmètre. Une frontière ne s'illustre pas.
7. **Aucune donnée nominative**, ni nom d'entreprise candidate, ni montant ou
   offre d'une consultation réelle identifiable, nulle part, y compris dans
   `JOURNAL.md`.
8. **Jamais d'aide à contourner la mise en concurrence** : pas de cahier des
   charges taillé pour un candidat, pas de découpage pour passer sous un
   seuil, pas d'information privilégiée, pas de rédaction destinée à
   justifier après coup un choix déjà fait.
9. **Pas de duplication** : les branches pointent les unes vers les autres, les
   objets pointent vers les branches. Le même contenu n'existe qu'à un endroit.
10. **Jurisprudence** : jamais citée par son seul nom d'usage ou son
    millésime. Juridiction, date et numéro, vérifiés, ou rien.

## Décisions structurantes

Toute décision d'architecture (ajout d'une couche, déplacement d'une frontière,
changement de gabarit) fait l'objet d'une ADR dans `docs/adr/`.
