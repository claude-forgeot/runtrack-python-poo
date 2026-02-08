from math import pi

# class Personnage:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
        
#     def gauche(self):
#         self.x -=1
#         return self.x
    
#     def droite(self):
#         self.x +=1
#         return self.x
        
#     def bas(self):
#         self.y +=1
#         return self.y
    
#     def haut(self):
#         self.y -=1
#         return self.y

#     def position(self):
#         return (self.x, self.y)
    
# my_char = Personnage(0,0)

# print(f"La position de mon character est {my_char.position()}")
# my_char.droite()
# my_char.haut()
# print(f"La position de mon character est {my_char.position()}")


class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon
        
    def changerRayon(self, rayon):
        self.rayon = rayon
    
    def afficherInfos(self):
        print(f"{self.rayon}, {self.circonference()}, {self.aire()}, {self.diametre()}")
        
    def circonference(self):
        return 2 * pi * self.rayon
        
    def aire(self):
        return self.rayon ** 2 * pi
        
    def diametre(self):
        return 2 * self.rayon
        
my_circle = Cercle(4)
my_circle_2 = Cercle(7)

my_circle.changerRayon(10)
my_circle.afficherInfos()
my_circle_2.afficherInfos()