
class Menu:
    def __init__(self):
        self.ITEMS = [
            "[1] Créer un nouveau tournoi",
            "[2] Enregistrer un nouveau joueur",
            "[3] Rapports",
            "[4] Quitter"
        ]
        self.RAPPORTS = [
            "[1] Afficher la liste des joueurs",
            "[2] Afficher l'historique des tournois",
            "[3] Afficher le détail d'un tournoi",
            "[4] Retour"
        ]

    def items(self, value):
        """displays menu depending on given value"""
        menu_type = []
        if value == 1:
            menu_type = self.ITEMS
            print()
            print("MENU GENERAL")
        if value == 2:
            menu_type = self.RAPPORTS
            print()
            print("MENU RAPPORTS")
        for i in menu_type:
            print(i)
        while True:
            try:
                choice = input("Choix ? : ")
                if int(choice) not in range(1, len(menu_type) + 1):
                    print("Choisissez un chiffre entre 1 et", len(menu_type))
                else:
                    return choice
            except ValueError:
                print("Veuillez entrer un chiffre")
