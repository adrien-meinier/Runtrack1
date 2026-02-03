class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        if isinstance(nb_pages, int) and nb_pages > 0:
            self.__nb_pages = nb_pages
        else:
            self.__nb_pages = 0
            print("Erreur : le nombre de pages doit être un entier positif.")

    # getters
    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nb_pages(self):
        return self.__nb_pages

    # setters
    def set_titre(self, titre):
        self.__titre = titre

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def set_nb_pages(self, nb_pages):
        if isinstance(nb_pages, int) and nb_pages > 0:
            self.__nb_pages = nb_pages
        else:
            print("Erreur : le nombre de pages doit être un entier positif.")

    def afficher_info(self):
        print(f"Titre : {self.__titre}")
        print(f"Auteur : {self.__auteur}")
        print(f"Nombre de pages : {self.__nb_pages}")

livre1 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 96)
livre1.afficher_info()

# exemples avec une erreur
livre1.set_nb_pages(-50)  
livre1.set_auteur("Dark vador sa vie son oeuvre")
livre1.set_nb_pages(120)
livre1.afficher_info()
