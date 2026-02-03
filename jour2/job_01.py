class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    def set_longueur(self, nouvelle_longueur):
        self.__longueur = nouvelle_longueur

    def set_largeur(self, nouvelle_largeur):
        self.__largeur = nouvelle_largeur

    def afficher(self):
        print(f"Longueur: {self.__longueur}, Largeur: {self.__largeur}")



mon_rectangle = Rectangle(10, 5)
mon_rectangle.afficher()  
mon_rectangle.set_longueur(15)
mon_rectangle.set_largeur(8)
mon_rectangle.afficher()  
