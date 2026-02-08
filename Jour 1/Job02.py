# class Rectangle:
#     def __init__(self, longueur, largeur):
#         self.__longueur = longueur
#         self.__largeur = largeur
        
#     def getLongueur(self):
#         print(self.__longueur)
    
#     def getLargeur(self):
#         print(self.__largeur)
    
#     def setLongueur(self, longueur):
#         self.__longueur = longueur
#         print(f"La longueur est {longueur}")
        
#     def setLargeur(self, largeur):
#         self.__largeur = largeur
#         print(f"La largeur est {largeur}")
    
# mon_rectangle = Rectangle(10, 5) 

# mon_rectangle.setLongueur(15)
# mon_rectangle.setLargeur(20)
# mon_rectangle.getLongueur()
# mon_rectangle.getLargeur()

class Livre:
    def __init__(self,titre, auteur, pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages
    
    def getTitre(self):
        print(f"Le titre est :{self.__titre}")
        
    def getAuteur(self):
        print(f"L'auteur est:{self.__auteur}")
    
    def getPages(self):
        print(f"Le livre contient {self.__pages} pages.")
        
    def setTitre(self, titre):
        # print(input(f"Entrer le titre :{self.__titre}"))
        self.__titre = titre
        
        
    def setAuteur(self, auteur):
        # print(input(f"Entrer l'auteur: {self.__auteur}"))
        self.__auteur = auteur
        
        
    def setPages(self, pages):
        if pages.isdigit():
            pages = int(pages)
            if pages > 0:
                # print(input(f"Entrer le nombre de pages: {self.__auteur}"))
                self.__pages = pages
            else:
                print("Doit être supérieur à zéro")
        else:
            print("N'est pas positif ou un chiffre")


my_book = Livre("?","?",15)


my_book.getTitre()
my_book.getAuteur()
my_book.getPages()
my_book.setTitre(input("Entrer le titre : "))
my_book.setAuteur(input("Entrer l'auteur : "))
my_book.setPages(input("Entrer le nombre de pages : "))
my_book.getTitre()
my_book.getAuteur()
my_book.getPages()