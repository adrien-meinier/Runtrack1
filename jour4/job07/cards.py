class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def points(self):
        if self.valeur in ["Valet", "Dame", "Roi"]:
            return 10
        elif self.valeur == "As":
            return 11
        else:
            return int(self.valeur)

    def __str__(self):
        return f"{self.valeur} de {self.couleur}"
