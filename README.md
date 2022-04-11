# Puissance4
Le jeu que je vais essayer de programmer avec une interface graphique se nomme Puissances 4 , ce jeu ce joue à 2 , un joueur possède des jetons de couleur rouge et l'autre joueur de couleur jaune.

Le jeu se joue sur une grille de 7 colonnes et 6 rangées.


L'objectif du jeu est d'aligner 4 jetons de la même couleur, verticalement, horizontalement ou en diagonale.


Si la grille se remplit et que personne n'a réussi à aligner 4 jetons alors il y a un match nul.


Je vais utiliser un tableau (liste de liste) pour modéliser ma grille.



-SDD : 0 = colonne vide  1= joueur 1 2= joueur 2
## Decomposition en sous-problèmes
- Tour d’abord, on demande aux joueurs à tour de rôle dans quelles colonnes, ils veulent jouer (Demande_colonne () )

- On va faire une fonction qui détecte une colonne pleine et la grille pleine afin de déposer le jeton (Poser_jetons () )

- Une fonction qui renvoie une grille ( Grille () ) et une fonction qui affiche la grille du jeu par interface graphique (Affiche_grille () )

- des fonction qui cherche 4 pions alignés verticalement, cherche 4 pions alignés horizontalement, cherche 4 pions alignés en diagonale : vérifie_horizontalemen() ,vérifie_verticalement(),vérifie_diagonalement():

- une fonction afin de déterminer le gagnant (Est_gagndant () )

## MVP

- En premier temps je vais faire un programme afin qu'il fonctionne dans la console  

- En deuxième réaliser une interface graphique 


