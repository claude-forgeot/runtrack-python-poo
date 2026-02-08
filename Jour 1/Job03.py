class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
    
    def addition(self):
        return self.nombre1 + self.nombre2

objet_test = Operation(12, 3)

print(f"Le nombre1 est {objet_test.nombre1}")
print(f"Le nombre2 est {objet_test.nombre2}")
print(f"La somme est {objet_test.addition()}")


# class Operation:
#     def __init__(self, nombre1, nombre2):
#         self.nombre1 = nombre1
#         self.nombre2 = nombre2
    
#     def addition(self):
#         print(self.nombre1 + self.nombre2)

# objet_test = Operation(12, 3)

# print(f"Le nombre1 est {objet_test.nombre1}")
# print(f"Le nombre2 est {objet_test.nombre2}")
# print(f"La somme est {objet_test.addition()}")