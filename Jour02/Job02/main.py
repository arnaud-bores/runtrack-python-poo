class Personne:
    def __init__(self, age=14):
        self.age = age
    
    def afficherAge(self):
        print(f"J'ai {self.age} ans")
    
    def bonjour(self):
        print("Hello")
    
    def modifierAge(self, new_age):
        self.age = new_age

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")
    
    def affichageAge(self):
        print(f"J'ai {self.age} ans")

class Professeur(Personne):
    def __init__(self, age=30, matiereEnseignee=""):
        super().__init__(age)
        self.matiereEnseignee = matiereEnseignee
    
    def enseigner(self):
        print("Le cours va commencer")

p = Personne()
e = Eleve()
print(e.age)  # affiche 14, l'âge par défaut de la classe Personne

e = Eleve()
e.bonjour()  # affiche "Hello"
e.allerEnCours()  # affiche "Je vais en cours"
e.modifierAge(15)  # redéfinit l'âge de l'élève à 15 ans

prof = Professeur(age=40, matiereEnseignee="maths")
prof.bonjour()  # affiche "Hello"
prof.enseigner()  # affiche "Le cours va commencer"
