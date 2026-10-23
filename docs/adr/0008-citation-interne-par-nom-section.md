# ADR 0008 — Citation interne par nom et section

Date : 2026-10-23. Décisions de Jo transmises textuellement par le lot D1,
suivi [DCP-fpt#9](https://github.com/brissonjo-sudo/DCP-fpt/issues/9).

## Décisions

- Barème : « Défaut non éliminatoire + contrôle auto » — un lien ou chemin
  vers un fichier de skill dans une réponse est un défaut non éliminatoire ;
  un fond correct reste RÉUSSITE ; seuil 25/28 et aucun ÉCHEC critique inchangés.
- Mesure : « Oui, plan complet » — 28 cas, 56 sessions, tentative unique après
  pré-vol, plafond de suivi 10 000 000 jetons d'entrée entre rôles.

Le lot prépare uniquement : aucune mesure ni action externe n'est exécutée.
La transcription de l'autorisation liée à la tête préparée ne constitue pas
une signature indépendante ni une revue des futures réponses.

## Application

Seule la règle de traçabilité de SKILL.md change : nom du skill et section
au point d'utilisation ; liens et chemins réservés à la lecture interne.
La table de routage demande de lire/charger les branches et objets, sans
demander de recopier ses liens. Aucun changement de règle de droit, STOP,
frontière, attendu métier, seuil ou validateur.

Le barème courant est l'unique copie normative éditable. Les copies figées
de tests/runs restent des preuves historiques scellées et sont préservées.
Les nouvelles copies du barème dans le kit reprendront le critère autorisé.

Le contrôleur s'aligne sur [Collectivité #23](https://github.com/brissonjo-sudo/collectivite-territoriale/pull/23),
scripts/skill_citation.py à 94de5ee4bea2b28d47d07e344c2ee6f83fb36ccd :
décodage URL, séparateurs normalisés et ressources détectées quel que soit
l'hôte. Une URL officielle ordinaire reste permise ; héberger un fichier
de skill sur un hôte officiel ne le transforme pas en source officielle.
Il inventorie chaque occurrence (y compris chemin absolu local), ne réécrit
aucune réponse ni aucun jugement, et n'entre pas dans le calcul du score.
Les positions sont données dans la ligne décodée ; aucun chemin privé n'est
recopié dans les alertes. Jo relit la réponse liée par SHA-256.
