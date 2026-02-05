from rectangle import Rectangle
class Parallepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.hauteur = hauteur

    def volume(self):
       return self.surface() * self.hauteur