class MenuView:
    """Affiche le menu.
    Demande à l'uitilisateur de choisir une option du menu affiché
    """

    def __init__(self, menu):
        """
        Permet à MenuView de recevoir un menu instancié dans le controller d'application
        Arguments:
            menu (instance de Menu())
        """
        self.menu = menu

    def display_menu(self):
        """Affichage des entrées du menu
        """
        for key, entry in self.menu.items():
            print("{}: {}".format(key, entry))
        print()

    def get_user_choice(self):
        """Demande à l'uitilisateur son choix et le retourne au controller

        Returns:
            instance d'objet MenuEntry -- entrée du menu désignée par choice
        """
        while True:
            self.display_menu()
            choice = input(">> ")
            if choice in self.menu:
                return self.menu[choice]
