class Operation:
    def __init__(self, nombre1, nombre2):
        self.Nombre1 = nombre1
        self.Nombre2 = nombre2

    def addition(self):
        resultat = self.Nombre1 + self.Nombre2
        print(resultat)

operation1 = Operation(2, 3)
operation1.addition()
