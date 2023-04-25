class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

animal1 = Animal()
animal1.vieillir()
print(animal1.age)





