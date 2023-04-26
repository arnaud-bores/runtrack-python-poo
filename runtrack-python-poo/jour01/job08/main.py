class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
        self.__disponible = True
    
    def get_titre(self):
        return self.__titre
    
    def set_titre(self, nouveau_titre):
        self.__titre = nouveau_titre
    
    def get_auteur(self):
        return self.__auteur
    
    def set_auteur(self, nouvel_auteur):
        self.__auteur = nouvel_auteur
    
    def get_nb_pages(self):
        return self.__nb_pages
    
    def set_nb_pages(self, nouveau_nb_pages):
        if isinstance(nouveau_nb_pages, int) and nouveau_nb_pages > 0:
            self.__nb_pages = nouveau_nb_pages
        else:
            print("Le nombre de pages doit être un entier positif.")
    
    def afficher_livre(self):
        print("Titre :", self.__titre)
        print("Auteur :", self.__auteur)
        print("Nombre de pages :", self.__nb_pages)
    
    def verification(self):
        return self.__disponible
    
    def emprunter(self):
        if self.verification():
            self.__disponible = False
            print("Le livre a été emprunté.")
        else:
            print("Le livre n'est pas disponible.")
    
    def rendre(self):
        if not self.verification():
            self.__disponible = True
            print("Le livre a été rendu.")
        else:
            print("Le livre n'a pas été emprunté.")

# Création d'un livre
livre1 = Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien", 1178)

# Vérification que le livre est disponible
print(livre1.verification())  # True

# Emprunt du livre
livre1.emprunter()  # Le livre a été emprunté.

# Vérification que le livre n'est plus disponible
print(livre1.verification())  # False

