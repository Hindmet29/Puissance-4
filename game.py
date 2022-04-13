class game:
    
    
    def création_joueur ():
        joueur1=input("J1, entrez votre prénom :")
        joueur2=input("J2, entrez votre prénom :")
    return joueur1,joueur2
    
    def __init__(self) :# Création de la grille de jeu
        self.grille [["0"] * 7 for i in range (6)]
    
    def methode1 (self):
        self.grille[i][j]=2
        
    def poser_jeton(self, joueur, colone):
        for ligne in range(7):
            if "0" in self.grille[colone]:
                if self.grille[colone][ligne] == "0":
                    self.grille[colone][ligne] = joueur
                    break
 

        
    def est_gagnant (self)->int:
        trouve=0
        
    def est_gagnant_vert(self)-> int :
        for ligne in self.grille:
            joueur =0
            repetition=0
            for i in range (6):
                if ligne[i] == joueur :
                    repetition += 1
                else :
                    joueur =ligne (1)
                    repetition =  0 
    
    def est_gagnant_horiz(self)-> int :
     
    def est_gagnant_diag(self)-> int :



        
