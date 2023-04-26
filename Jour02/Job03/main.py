class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)
    
    def surface(self):
        return self.__longueur * self.__largeur
    
    def getLongueur(self):
        return self.__longueur
    
    def getLargeur(self):
        return self.__largeur
    
    def setLongueur(self, longueur):
        self.__longueur = longueur
    
    def setLargeur(self, largeur):
        self.__largeur = largeur

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur
    
    def volume(self):
        return self.surface() * self.__hauteur

r = Rectangle(5, 3)
print(r.perimetre())  # affiche 16
print(r.surface())  # affiche 15
r.setLongueur(10)
print(r.getLongueur())  # affiche 10

p = Parallelepipede(5, 3, 2)
print(p.volume())  # affiche 30
