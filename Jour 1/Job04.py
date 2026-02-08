# class Livre:
#     def __init__(self,titre, auteur, pages, disponible=True):
#         self.__titre = titre
#         self.__auteur = auteur
#         self.__pages = pages
#         self.__disponible = disponible
    
#     def getTitre(self):
#         print(f"Le titre est :{self.__titre}")
        
#     def getAuteur(self):
#         print(f"L'auteur est:{self.__auteur}")
    
#     def getPages(self):
#         print(f"Le livre contient {self.__pages} pages.")
        
#     def setTitre(self, titre):
#         # print(input(f"Entrer le titre :{self.__titre}"))
#         self.__titre = titre
        
#     def setAuteur(self, auteur):
#         # print(input(f"Entrer l'auteur: {self.__auteur}"))
#         self.__auteur = auteur
        
#     def setPages(self, pages):
#         if pages.isdigit():
#             pages = int(pages)
#             if pages > 0:
#                 # print(input(f"Entrer le nombre de pages: {self.__auteur}"))
#                 self.__pages = pages
#             else:
#                 print("Doit être supérieur à zéro")
#         else:
#             print("N'est pas positif ou un chiffre")

#     def verification(self):
#         if self.__disponible == True:
#             return True
#         else:
#             return False

#     def emprunter(self):
#         if self.verification() == True:
#             self.__disponible = False
#         else:
#             print("Non disponible")
            
#     def rendre(self): 
#         if self.verification() == False:
#             self.__disponible = True
#             print("Rendre le livre")
#         else:
#             print("Disponible")
    
# my_book = Livre("?","?",15)


# my_book.getTitre()
# my_book.getAuteur()
# my_book.getPages()
# my_book.setTitre(input("Entrer le titre : "))
# my_book.setAuteur(input("Entrer l'auteur : "))
# my_book.setPages(input("Entrer le nombre de pages : "))
# my_book.getTitre()
# my_book.getAuteur()
# my_book.getPages()
# my_book.emprunter()
# my_book.verification()
# my_book.emprunter()
# my_book.rendre()
# my_book.verification()


class Student:
    def __init__(self, nom, prenom, id):
        self.__nom = nom
        self.__prenom = prenom
        self.__id = id
        self.__credits = 0
        self.__level = self.__studentEval()
        
    def addCredit(self, credits):
        if credits > 0:
            self.__credits = credits + self.__credits
            self.__level = self.__studentEval()
            print(f"Les crédits de {self.__nom} {self.__prenom} sont de {self.__credits} crédits.")
        else:
            print("Les crédits doivent être positifs")
            
    def __studentEval(self):
        if self.__credits > 89:
            return "Excellent"
        elif self.__credits > 79:
            return "Très bien"
        elif self.__credits > 69:
            return "Bien"
        elif self.__credits > 59:
            return "Passable"
        else:
            return "Insuffisant"
        
    def studentInfo(self):
        print(f"Nom = {self.__nom}")
        print(f"Prenom = {self.__prenom}")
        print(f"Id = {self.__id}")
        print(f"Niveau = {self.__level}")
        print(f"Credits = {self.__credits}")
    
student_1 = Student("John","Doe",145)

student_1.studentInfo()
student_1.addCredit(10)
student_1.addCredit(10)
student_1.addCredit(10)
student_1.studentInfo()
student_1.addCredit(50)
student_1.studentInfo()


