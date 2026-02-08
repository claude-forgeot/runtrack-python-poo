import random

class Carte:
    def __init__(self, valeur, couleur):
        self.__valeur = valeur
        self.__couleur = couleur

    def getPoints(self):
        if self.__valeur in ["Valet", "Dame", "Roi"]:
            return 10
        elif self.__valeur == "As":
            return 11
        else:
            return int(self.__valeur)

    def afficher(self):
        print(f"{self.__valeur} de {self.__couleur}")


class Jeu:
    def __init__(self):
        self.__paquet = []
        self.__main_joueur = []
        self.__main_croupier = []
        self.__creerPaquet()
        self.__melangerPaquet()

    def __creerPaquet(self):
        couleurs = ["Coeur", "Carreau", "Trefle", "Pique"]
        valeurs = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi"]
        for couleur in couleurs:
            for valeur in valeurs:
                self.__paquet.append(Carte(valeur, couleur))

    def __melangerPaquet(self):
        random.shuffle(self.__paquet)

    def __piocherCarte(self):
        return self.__paquet.pop()

    def __calculerPoints(self, main):
        total = 0
        nb_as = 0
        for carte in main:
            total += carte.getPoints()
            if carte.getPoints() == 11:
                nb_as += 1
        while total > 21 and nb_as > 0:
            total -= 10
            nb_as -= 1
        return total

    def __afficherMain(self, nom, main):
        print(f"\nMain de {nom} :")
        for carte in main:
            carte.afficher()
        print(f"Total : {self.__calculerPoints(main)}")

    def distribuer(self):
        for i in range(2):
            self.__main_joueur.append(self.__piocherCarte())
            self.__main_croupier.append(self.__piocherCarte())

    def tourJoueur(self):
        while True:
            self.__afficherMain("Joueur", self.__main_joueur)
            if self.__calculerPoints(self.__main_joueur) > 21:
                print("Perdu ! Vous depassez 21.")
                return False
            choix = input("Prendre (p) ou Passer (s) ? ")
            if choix == "p":
                self.__main_joueur.append(self.__piocherCarte())
            else:
                return True

    def tourCroupier(self):
        while self.__calculerPoints(self.__main_croupier) < 17:
            self.__main_croupier.append(self.__piocherCarte())
        self.__afficherMain("Croupier", self.__main_croupier)

    def verifierGagnant(self):
        points_joueur = self.__calculerPoints(self.__main_joueur)
        points_croupier = self.__calculerPoints(self.__main_croupier)
        if points_croupier > 21:
            print("Le croupier depasse 21. Vous gagnez !")
        elif points_joueur > points_croupier:
            print("Vous gagnez !")
        elif points_joueur == points_croupier:
            print("Egalite !")
        else:
            print("Le croupier gagne.")

    def lancerPartie(self):
        self.distribuer()
        if self.tourJoueur():
            self.tourCroupier()
            self.verifierGagnant()



jeu = Jeu()
jeu.lancerPartie()
