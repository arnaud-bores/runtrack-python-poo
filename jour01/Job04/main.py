class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    
    def SePresenter(self):
        return "Je m'appelle {} {}".format(self.nom, self.prenom)

personne1 = Personne("Dupont", "Jean")
print(personne1.SePresenter())

personne2 = Personne("Martin", "Marie")
print(personne2.SePresenter())

personne3 = Personne("Dubois", "Paul")
print(personne3.SePresenter())
