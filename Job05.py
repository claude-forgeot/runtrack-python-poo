# class Personne:
#     def __init__(self, nom, prenom):
#         self.nom = nom
#         self.prenom = prenom
        
#     def SePresenter(self):
#         return self.nom + " " + self.prenom

# objet_un = Personne("John","Doe")
# objet_deux = Personne("Jean","Dupond")

# print(f" Je suis {objet_un.SePresenter()}")
# print(f" Je suis {objet_deux.SePresenter()}")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def afficherLesPoints(self):
        return str(self.x) + "," + str(self.y)
    
    def afficherX(self):
        return self.x
    
    def afficherY(self):
        return self.y
    
    def changeX(self, x):
        self.x = x
        return x
    
    def changeY(self, y ):
        self.y = y
        return y
    
coordo_v = Point(1,2)
coordo_h = Point(3,4)

print(f" Coordonnées verticales {coordo_v.afficherLesPoints()}")
print(f" Coordonnées horizontales {coordo_h.afficherLesPoints()}")
print(f" Nouvelles coordonnées verticales de X = {coordo_v.changeX(99)}")