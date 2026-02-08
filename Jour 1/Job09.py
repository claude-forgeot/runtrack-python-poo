# class Cercle:
#     def __init__(self, rayon):
#         self.rayon = rayon
        
#     def changerRayon(self, rayon):
#         self.rayon = rayon
    
#     def afficherInfos(self):
#         print(f"{self.rayon}, {self.circonference()}, {self.aire()}, {self.diametre()}")
        
#     def circonference(self):
#         return 2 * pi * self.rayon
        
#     def aire(self):
#         return self.rayon ** 2 * pi
        
#     def diametre(self):
#         return 2 * self.rayon
        
# my_circle = Cercle(4)
# my_circle_2 = Cercle(7)

# my_circle.changerRayon(10)
# my_circle.afficherInfos()
# my_circle_2.afficherInfos()

class Produit:
    def __init__(self, nom, prix, TVA):
        self.nom = nom
        self.prix = prix
        self.TVA = TVA
        
    def calculerPrixTTC(self):
        return self.prix + (self.prix * self.TVA/100) 
    
    def afficher(self):
        print(self.nom, self.prix, self.TVA)

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom
        return nouveau_nom
    
    def modifierPrix(self, nouveau_prix):
        self.prix = nouveau_prix
        return nouveau_prix
    
    def getNom(self):
        return self.nom
    
    def getPrix(self):
        return self.prix
    
    def getTVA(self):
        return self.TVA

my_laptop = Produit("Laptop", 1000, 20)
my_laptop2 = Produit("Desktop", 5000, 20)
my_laptop3 = Produit("Serveur", 15000, 20)

my_laptop.afficher()
my_laptop2.afficher()
my_laptop3.afficher()
my_laptop.modifierNom("Rasp")
my_laptop.modifierPrix(40)
print(my_laptop.calculerPrixTTC())
my_laptop.afficher()



