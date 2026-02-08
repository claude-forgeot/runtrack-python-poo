class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print(f"Age :{self.age}")

    def bonjour(self):
        print("Hello")

    def modifierAge(self, age):
        self.age = age

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print(f"J'ai {self.age} ans")

class Professeur(Personne):
    def __init__(self, age, matiereEnseignee):
        super().__init__(age)
        self.__matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")


e = Eleve()
e.bonjour()
e.allerEnCours()
e.modifierAge(15)
e.afficherAge()
prof = Professeur(40, "Maths")
prof.bonjour()
prof.enseigner()
