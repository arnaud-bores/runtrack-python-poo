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



import math

class Cercle(Forme):
    def __init__(self, radius):
        self.__radius = radius
        
    def aire(self):
        return math.pi * self.__radius ** 2

r = Rectangle(5, 3)
c = Cercle(2)

print("Aire du rectangle :", r.aire())  # affiche 15
print("Aire du cercle :", c.aire())  # affiche environ 12.57
