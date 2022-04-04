# Puissance4
Le jeu que je vais essayer de programmer avec une interface graphique se nomme Puissances 4 , ce jeu ce joue à 2 , un joueur possède des jetons de couleurs rouge et l'autre joueur de couleur jaune.

Le jeux ce joue sur une grille de 7 colonnes et 6 rangées.

L'objectif du jeu est d'aligner 4 jetons de la même couleur, verticalement, horizontalement ou en diagonale.

Si la grille se remplit et que personne n'a réussi à aligner 4 jetons alors il ya un match nul.

- SDD : 
   0 = colonne vide 
   1= joueur 1 
   2= joueur 2

-Tour d’abord on demande aux joueurs à tour de rôle dans quelles colonnes ils veulent  jouer ( demande_colonne () )

-On va faire une fonction qui détecte une colonne pleine et la grille pleine afin de deposer le jetons ( poser_pièce () )

-Une fonction qui renvoie une grille ( grille () ) et une fonction qui affiche la grille du jeu par interface graphique ( affiche_grille () )

-une fonction qui cherche 4 pions alignés verticalement, cherche 4 pions  alignés horizontalement, cherche 4 pions  alignés en diagonale afin de detérminer le gagant  ( est_gagant() )

