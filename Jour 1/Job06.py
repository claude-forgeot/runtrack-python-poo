# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def afficherLesPoints(self):
#         return str(self.x) + "," + str(self.y)
    
#     def afficherX(self):
#         return self.x
    
#     def afficherY(self):
#         return self.y
    
#     def changeX(self, x):
#         self.x = x
#         return x
    
#     def changeY(self, y ):
#         self.y = y
#         return y
    
# coordo_v = Point(1,2)
# coordo_h = Point(3,4)

# print(f" Coordonnées verticales {coordo_v.afficherLesPoints()}")
# print(f" Coordonnées horizontales {coordo_h.afficherLesPoints()}")
# print(f" Nouvelles coordonnées verticales de X = {coordo_v.changeX(99)}")

class Animal:
    def __init__(self):
        self.age =0
        self.prenom = ""
        
    def nommer(self, prenom):
        self.prenom = prenom
        print(f"Le monstre s'appelle {self.prenom}")
        return prenom
        
    def vieillir(self):
        print(f"L'age du monstre est {self.age} an.")
        self.age +=1
        print(f"L'age de l'ouragan est {self.age} an.")
        return
        

    
my_pet = Animal()


# print(f"Elle s'appelle {my_pet.nommer()}. Le plus mignon des petits","chats actuellement sur mon bureau.")
my_pet.vieillir()
my_pet.nommer("Cali")
