class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print(f"Marque = {self.marque}")
        print(f"Model = {self.modele}")
        print(f"Annee = {self.annee}")
        print(f"Prix = {self.prix}")

    def demarrer(self):
        print("Attention, je roule")

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.portes = 4

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de porte = {self.portes}")

    def demarrer(self):
        print("La voiture demarre")

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__( marque, modele, annee, prix)
        self.roue = 2

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roue = {self.roue}")

    def demarrer(self):
        print("La moto demarre")


v = Voiture("Mercedes", "Classe A", 2020, 18500)
v.informationsVehicule()
v.demarrer()
m = Moto("Yamaha", "1200 Vmax", 1987, 4500)
m.informationsVehicule()
m.demarrer()
