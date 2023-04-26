import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur
        
    def __str__(self):
        return "{} de {}".format(self.valeur, self.couleur)

class Jeu:
    def __init__(self):
        valeurs = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi"]
        couleurs = ["Coeur", "Carreau", "Pique", "Trèfle"]
        self.paquet = []
        for couleur in couleurs:
            for valeur in valeurs:
                self.paquet.append(Carte(valeur, couleur))
                
    def melanger(self):
        random.shuffle(self.paquet)
        
    def tirer_carte(self):
        return self.paquet.pop(0)
        
class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.main = []
        self.score = 0
        
    def ajouter_carte(self, carte):
        self.main.append(carte)
        if carte.valeur == "As":
            if self.score + 11 <= 21:
                self.score += 11
            else:
                self.score += 1
        elif carte.valeur in ["Valet", "Dame", "Roi"]:
            self.score += 10
        else:
            self.score += int(carte.valeur)
            
    def afficher_main(self):
        print("Main de {}:".format(self.nom))
        for carte in self.main:
            print("-", carte)
        print("Score:", self.score)
        
class Blackjack:
    def __init__(self):
        self.jeu = Jeu()
        self.jeu.melanger()
        self.joueur = Joueur("Joueur")
        self.croupier = Joueur("Croupier")
        
    def jouer(self):
        # Distribuer les cartes initiales
        self.joueur.ajouter_carte(self.jeu.tirer_carte())
        self.croupier.ajouter_carte(self.jeu.tirer_carte())
        self.joueur.ajouter_carte(self.jeu.tirer_carte())
        self.croupier.ajouter_carte(self.jeu.tirer_carte())
        self.joueur.afficher_main()
        # Tour du joueur
        while self.joueur.score < 21:
            choix = input("Voulez-vous prendre une carte ? (o/n) ")
            if choix.lower() == "o":
                self.joueur.ajouter_carte(self.jeu.tirer_carte())
                self.joueur.afficher_main()
            else:
                break       
        # Tour du croupier
        self.croupier.afficher_main()
        while self.croupier.score < 17:
            self.croupier.ajouter_carte(self.jeu.tirer_carte())
            self.croupier.afficher_main() 
        # Résultat de la partie
        if self.joueur.score > 21:
            print("Vous avez dépassé 21, vous avez perdu.")
        elif self.croupier.score > 21:
            print("Le croupier a dépassé 21, vous avez gagné !")
        elif self.joueur.score > self.croupier.score:
            print("Vous avez un score supérieur au
