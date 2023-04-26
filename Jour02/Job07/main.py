class Vehicule:
    def __init__(self, marque, model, annee, prix):
        self.marque = marque
        self.model = model
        self.annee = annee
        self.prix = prix
    
    def informationsVehicule(self):
        print(f"Marque : {self.marque}, model :{self.model}, année {self.annee}, prix : {self.prix}")
        
class Voiture(Vehicule):
    def __init__(self, marque, model, annee, prix):
        super().__init__(marque, model, annee, prix)
        self.roue = 2
        
    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues : {self.roue}")
        
ma_voiture = Voiture("Yamaha" ,"1200 Vmax", 1987, 4500)
ma_voiture.informationsVehicule()

class Vehicule:
    def demarrer(self):
        print("Attention, je roule.")

class Moto(Vehicule):
    def demarrer(self):
        print("Je démarre ma moto, vrrrooom !")

class Voiture(Vehicule):
    def demarrer(self):
        print("Je démarre ma voiture, vroum vroum !")

# Instanciation d'un objet moto et d'un objet voiture
ma_moto = Moto()
ma_voiture = Voiture()

# Appel de la méthode demarrer pour la moto et la voiture
ma_moto.demarrer()
ma_voiture.demarrer()

