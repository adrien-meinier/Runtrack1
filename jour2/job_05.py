class Voiture:
    def __init__(self, marque, modele, annee, kilometres, reservoir=0):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometres = kilometres
        self.__en_marche = False
        self.__reservoir = reservoir

    # getters
    def get_marque(self):
        return self.__marque

    def get_modele(self):
        return self.__modele

    def get_annee(self):
        return self.__annee

    def get_kilometres(self):
        return self.__kilometres

    def get_en_marche(self):
        return self.__en_marche

    def get_reservoir(self):
        return self.__reservoir

    # setters
    def set_marque(self, marque):
        self.__marque = marque

    def set_modele(self, modele):
        self.__modele = modele

    def set_annee(self, annee):
        self.__annee = annee

    def set_kilometres(self, kilometres):
        self.__kilometres = kilometres

    def set_reservoir(self, reservoir):
        self.__reservoir = reservoir

    def __verifier_plein(self):
        return self.__reservoir > 5

    def demarrer(self):
        if self.__verifier_plein():
            self.__en_marche = True
            print("La voiture démarre.")
        else:
            print("Impossible de démarrer : réservoir insuffisant.")

    def arreter(self):
        self.__en_marche = False
        print("La voiture est arrêtée.")

    def voiture_info(self):
        print(f"Marque : {self.__marque}")
        print(f"Modèle : {self.__modele}")
        print(f"Année : {self.__annee}")
        print(f"Kilomètres : {self.__kilometres}")
        print(f"Réservoir : {self.__reservoir} L")


voiture1 = Voiture("Audi", "AudiQ7", 2005, 45000, 50)

voiture1.voiture_info()
voiture1.demarrer()