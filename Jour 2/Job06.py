class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__liste_plats = {}
        self.__statut_commande = "En cours"
        
    def ajouterPlat(self, nom, prix):
        self.__liste_plats[nom] = prix
        
    def annuler(self):
        if self.__statut_commande == "En cours":
            self.__statut_commande = "Annulé"
        else:
            pass
        
    def __calculerTotal(self):
        return sum(self.__liste_plats.values())
        
    def afficherCommandeTotal(self):
        print(f" Le total est : {self.__calculerTotal()}")
        print(f"Plats : {self.__liste_plats}")
        print(f"Statut : {self.__statut_commande}")
        
    def calculerTVA(self):
        print(f"TTC : {self.__calculerTotal() * 1.2}")
        
    
commande_une = Commande(1)

commande_une.ajouterPlat("Pizza :",12.00)
commande_une.ajouterPlat("Sauce Tomate :",24.00)
commande_une.afficherCommandeTotal()
commande_une.calculerTVA()
commande_une.annuler()
