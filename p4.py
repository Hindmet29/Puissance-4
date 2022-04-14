class Game:
    
    def __init__(self) :# Création de la grille de jeu
        self.grille = [[0] * 7 for i in range (6)]  
        self.joueur1 = input("J1, entrez votre prénom :")
        self.joueur2 = input("J2, entrez votre prénom :")

        
    def poser_jeton(self, joueur, colonne):
        for ligne in range(7):
            if "0" in self.grille[colone]:
                if self.grille[colone][ligne] == "0":
                    self.grille[colone][ligne] = joueur
                    break
        
    def est_gagnant (self)->int:
        trouve=0
        
    def est_gagnant_horiz(self)-> int :
        for ligne in self.grille:
            joueur = 0
            repetition = 0
            for colonne in range (7):
                if ligne[colonne] == joueur and ligne[colonne] != 0 :
                    repetition += 1
                else :
                    joueur = ligne[colonne]
                    repetition =  0
                if repetition == 3:
                    return joueur
    
    def est_gagnant_vert(self)-> int :
        for colonne in self.grille :
            joueur = 0
            repetition = 0
            for ligne in range(6):
                if colonne[ligne] == joueur and colonne[ligne] != 0 :
                    repetition += 1
                    if joueur1 >= 4:
                        trouve = 1
                        return trouve
                elif self.grille [ligne][colonne] == 2:
                    joueur1 = 0
                    Joueur2 += 1
                    if joueur2 >= 4:
                        trouve = 2
                        return trouve
                else:
                    joueur1=0
                    Joueur2=0
     
    def est_gagnant_diag(self)-> int :
        return None

jeu= Game()
print(jeu.grille)
jeu.grille[5] = [1,1,2,2,2,2,1]
print(jeu.grille)
print(jeu.est_gagnant_horiz())
jeu= Game()
print(jeu.grille)
jeu.grille[6] = [[0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,1],
                 [0,0,0,0,0,0,1],
                 [0,0,0,0,0,0,1],
                 [1,1,2,2,2,0,1],]
                 

print(jeu.grille)
print(jeu.est_gagnant_vert())
