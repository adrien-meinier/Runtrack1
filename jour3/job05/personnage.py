class Personnage:
    def __init__(self, nom, vie):
        self.__nom = nom
        self.__vie = vie

    def getNom(self):
        return self.__nom

    def getVie(self):
        return self.__vie

    def attaquer(self, adversaire):
        degats = 10
        adversaire.recevoirDegats(degats)
        print(f"{self.__nom} attaque {adversaire.getNom()} et inflige {degats} dégâts.")

    def recevoirDegats(self, degats):
        self.__vie -= degats
        if self.__vie < 0:
            self.__vie = 0

    def estVivant(self):
        return self.__vie > 0
