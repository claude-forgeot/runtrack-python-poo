# class Animal:
#     def __init__(self):
#         self.age =0
#         self.prenom = ""
        
#     def nommer(self, prenom):
#         self.prenom = prenom
#         print(f"Le monstre s'appelle {self.prenom}")
#         return prenom
        
#     def vieillir(self):
#         print(f"L'age du monstre est {self.age} an.")
#         self.age +=1
#         print(f"L'age de l'ouragan est {self.age} an.")
#         return
        

    
# my_pet = Animal()


# # print(f"Elle s'appelle {my_pet.nommer()}. Le plus mignon des petits","chats actuellement sur mon bureau.")
# my_pet.vieillir()
# my_pet.nommer("Cali")


class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def gauche(self):
        self.x -=1
        return self.x
    
    def droite(self):
        self.x +=1
        return self.x
        
    def bas(self):
        self.y +=1
        return self.y
    
    def haut(self):
        self.y -=1
        return self.y

    def position(self):
        return (self.x, self.y)
    
my_char = Personnage(0,0)

print(f"La position de mon character est {my_char.position()}")
my_char.droite()
my_char.haut()
print(f"La position de mon character est {my_char.position()}")
