# ADR 0006 — Liens personnels dans les preuves publiques

Date : 2026-10-08.

Deux réponses contiennent un lien vers le dossier temporaire personnel du
répondant. Les originaux du kit privé et les jugements ne sont pas modifiés.
L'export remplace uniquement le chemin absolu personnel vers `.agents/skills/`
par son chemin relatif. Aucun autre contenu n'est transformé.

Chaque copie assainie porte un `redaction.json` avec empreintes originale et
publique. Le juge reste rattaché à l'empreinte de l'original, également portée
par la preuve d'exécution. L'export vérifie la transformation depuis les octets
privés ; la CI vérifie la copie publique et les liens d'empreinte, sans disposer
de l'original privé. Une dérivation de la copie publique ou un rattachement
incohérent est refusé. Ces contrôles ne certifient pas une preuve de façon
indépendante ni sa qualification juridique.

Les scores restent ceux des réponses originales. Les anciennes campagnes
sans assainissement gardent leur contrôle direct de réponse/jugement.
