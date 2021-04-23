class MenuEntry:
    """Modélise les entrées des menus
    """
    def __init__(self, option, handler):
        """Une entrée du menu contient:
            Une description textuelle de cette entrée afin que l'utilisateur puisse identifier
            clairement à quelle séquence permet d'accéder cette entrée
            Et un des controlleur de séquence d'application contenu dans applicationcontroller.py

        Arguments:
            option (string) -- décrit textuellement l'option du menu
            handler (objet d'une classe de applicationcontroller.py) --
        """
        self.option = option
        self.handler = handler

    def __str__(self):
        """Pour affichage de la description textuelle seule lors de l'affichage d'une entrée de menu

        Returns:
            (string)
        """
        return str(self.option)


class Menu:
    """Permet de construire un menu avec plusieurs entrées.
    Lie une entrée de menu à une clé (chiffre ou lettre) permettant à l'utilisateur de choisir cette entrée
    self.entries : dictionnaire d'instances de MenuEntry {key: MenuEntry(option, handler)}
    self.autokey : clé d'autonumérotation des entrées
    """

    def __init__(self, title):
        self.entries = {}
        self.autokey = 1
        self.title = title
        
    def __str__(self):
        """Affiche le titre du menu
        """
        return str(self.title)

    def add(self, key, option, handler):
        """Permet d'ajouter une entrée au menu

        Arguments:
            key (str) ou (int) -- converti en string lors de l'ajout dans self.entries
            option (string) -- décrit textuellement l'option du menu
            handler (objet controlleur de séquence d'application) -- correspond à l'option décrite
        """
        if key == "auto":
            key = str(self.autokey)
            self.autokey += 1
        self.entries[str(key)] = MenuEntry(option, handler)

    def items(self):
        """Permet un itération sur le contenu de self.entries

        Returns:
            (objet dict_items)
        """
        return self.entries.items()

    def __contains__(self, choice):
        """Permet de vérifier si choice se trouve dans le menu

        Arguments:
            choice (string) -- choix saisi par l'utilisateur

        Returns:
            (bool) -- renvoie True si choice est dans self.entries
        """
        return str(choice) in self.entries

    def __getitem__(self, choice):
        """Permet d'obtenir menu[choice] pour obtenir l'entrée correspondant au choix

        Arguments:
            choice (string) -- choix saisi par l'utilisateur

        Returns:
            (instance d'objet MenuEntry) -- entrée du menu désignée par choice
        """
        return self.entries[choice]
