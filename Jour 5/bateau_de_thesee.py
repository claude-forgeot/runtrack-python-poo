class Part:
    def __init__(self, name, material):
        self.__name = name
        self.__material = material

    def change_material(self, new_material):
        self.__material = new_material

    def get_name(self):
        return self.__name

    def get_material(self):
        return self.__material

    def __str__(self):
        return f"{self.__name} en {self.__material}"


class Ship:
    def __init__(self, name, parts):
        self.__name = name
        self.__parts = parts
        self.__historique = []

    def display_state(self):
        print(f"\nEtat du navire '{self.__name}' :")
        for nom, part in self.__parts.items():
            print(f"  - {part}")

    def replace_part(self, part_name, new_part):
        if part_name in self.__parts:
            self.__historique.append(f"Remplacement : {self.__parts[part_name]} -> {new_part}")
            self.__parts[part_name] = new_part
        else:
            print(f"Piece '{part_name}' introuvable.")

    def change_part(self, part_name, new_material):
        if part_name in self.__parts:
            old = self.__parts[part_name].get_material()
            self.__parts[part_name].change_material(new_material)
            self.__historique.append(f"Modification : {part_name} {old} -> {new_material}")
        else:
            print(f"Piece '{part_name}' introuvable.")

    def afficher_historique(self):
        print(f"\nHistorique du navire '{self.__name}' :")
        for entry in self.__historique:
            print(f"  {entry}")

    def get_name(self):
        return self.__name



class RacingShip(Ship):
    def __init__(self, name, parts, max_speed):
        super().__init__(name, parts)
        self.__max_speed = max_speed

    def display_speed(self):
        print(f"Vitesse max : {self.__max_speed} noeuds. Ouais, frère.")


def menu(ship):
    while True:
        print("Menu")
        print("1 Afficher l'etat du navire")
        print("2 Remplacer une piece")
        print("3 Modifier le materiau d'une piece")
        print("4 bAfficher l'historique")
        print("5 Quitter")
        choix = input("Choix : ?")

        if choix == "1":
            ship.display_state()
        elif choix == "2":
            nom = input("Nom de la piece a remplacer : ")
            new_name = input("Nom de la nouvelle piece : ")
            new_mat = input("Materiau de la nouvelle piece : ")
            ship.replace_part(nom, Part(new_name, new_mat))
        elif choix == "3":
            nom = input("Nom de la piece : ")
            mat = input("Nouveau materiau : ")
            ship.change_part(nom, mat)
        elif choix == "4":
            ship.afficher_historique()
        elif choix == "5":
            break



pieces = {
    "Mat": Part("Mat", "Bois"),
    "Coque": Part("Coque", "Bois"),
    "Voile": Part("Voile", "Tissu"),
    "Gouvernail": Part("Gouvernail", "Bois"),
    "Ancre": Part("Ancre", "Fer")
}

navire = Ship("Navire de Thesee", pieces)
navire.display_state()


print("\n-- Modification du mat du Mat --")
navire.change_part("Mat", "Carbone")
navire.display_state()


print("\n-- Remplacemnt de la Voile --")
navire.replace_part("Voile", Part("Voile", "Nylon"))
navire.display_state()


navire.afficher_historique()


print("\n-- Racing Ship --")
pieces_racing = {
    "Mat": Part("Mat", "Carbone"),
    "Coque": Part("Coque", "Fibre de verre"),
    "Voile": Part("Voile", "Kevlar")
}
racing = RacingShip("Thunderbolt", pieces_racing, 45)
racing.display_state()
racing.display_speed()


