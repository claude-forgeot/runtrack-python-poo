class Voiture:
    def __init__(self, marque, modele, annee, kilometrage, en_marche=False):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = en_marche
        self.__reservoir = 50
    
    def getMarque(self):
        print(f"La marque du véhicule est :{self.__marque}")
    
    def getModele(self):
        print(f"Le modele du véhicule est :{self.__modele}")
    
    def getAnnee(self):
        print(f"L'année du véhicule est :{self.__annee}")
        
    def getKilometrage(self):
        print(f"Le kilométrage du véhicule est :{self.__kilometrage}")    
    
    def getEn_marche(self):
        print(f"Le véhicule est :{self.__en_marche}")
        
    def getReservoir(self):
        print(f"Le véhicule à {self.__reservoir}L en réserve")   
    
    def setMarque(self, marque):
        self.__marque = marque
        
    def setModele(self, modele):
        self.__modele = modele
            
    def setAnnee(self, annee):
        self.__annee = annee
        
    def setKilometrage(self, kilometrage):
        self.__kilometrage = kilometrage
        
    def setEn_marche(self, en_marche):
        self.__en_marche = en_marche
    
    def demarrer(self):
        if self.__en_marche == False:
            if self.__verifier_plein() > 5:
                self.__en_marche = True
                print("La voiture run, bruh.")
        else:
            print("La voiture est déjà démarrée.")
    
    def arreter(self):
        if self.__en_marche == True:
            self.__en_marche = False
            print("La voiture ne run plus")
        else:
            print("La voiture est éteinte.")
            
    def __verifier_plein(self):
        return self.__reservoir
    
my_caisse = Voiture("Toyota", "Incognito",1995,100000,False)

my_caisse.arreter()
my_caisse.demarrer()
