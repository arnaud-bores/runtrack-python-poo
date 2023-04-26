class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
    
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

# Création d'un livre
livre1 = Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien", 1178)

# Affichage des attributs
livre1.afficher_livre()  # Titre : Le Seigneur des Anneaux ; Auteur : J.R.R. Tolkien ; Nombre de pages : 1178

# Modification du titre
livre1.set_titre("Le Hobbit")

# Affichage du nouveau titre
print(livre1.get_titre())  # Le Hobbit

# Tentative de modification du nombre de pages avec une valeur invalide
livre1.set_nb_pages(-100)  # Le nombre de pages doit être un entier positif.

# Modification du nombre de pages avec une valeur valide
livre1.set_nb_pages(310)

# Affichage des attributs mis à jour
livre1.afficher_livre()  # Titre : Le Hobbit ; Auteur : J.R.R. Tolkien ; Nombre de pages : 310
