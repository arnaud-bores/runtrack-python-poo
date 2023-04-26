class Student:
    def __init__(self, nom, prenom, num_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__num_etudiant = num_etudiant
        self.__credits = 0
        self.__level = self.__studentEval()

    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits

    def __studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien."
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def studentInfo(self):
        print("Nom : ", self.__nom)
        print("Prénom : ", self.__prenom)
        print("Numéro d'étudiant : ", self.__num_etudiant)
        print("Niveau : ", self.__level)

# Créer l'objet représentant l'étudiant John Doe
john_doe = Student("Doe", "John", 145)

# Ajouter des crédits à trois reprises
john_doe.add_credits(30)
john_doe.add_credits(35)
john_doe.add_credits(25)

# Imprimer son total de crédits
print("Total de crédits : ", john_doe._Student__credits)

# Imprimer ses informations
john_doe.studentInfo()
