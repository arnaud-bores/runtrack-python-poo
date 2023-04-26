class Forme:
    def aire(self):
        return 0


class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.__largeur = largeur
        self.__hauteur = hauteur
        
    def aire(self):
        return self.__largeur * self.__hauteur

r = Rectangle(5, 3)
print(r.aire())  # affiche 15
