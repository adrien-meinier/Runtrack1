from personnage import Personnage
class Jeu:
    def __init__(self):
        self.__niveau = None
        self.__joueur = None
        self.__ennemi = None

    def choisirNiveau(self):
        print("Choisissez un niveau :")
        print("1 - Facile")
        print("2 - Moyen")
        print("3 - Difficile")

        self.__niveau = int(input("Votre choix : "))

    def lancerJeu(self):
        if self.__niveau == 1:
            self.__joueur = Personnage("Héros", 100)
            self.__ennemi = Personnage("Gobelin", 50)
        elif self.__niveau == 2:
            self.__joueur = Personnage("Héros", 80)
            self.__ennemi = Personnage("Orc", 80)
        else:
            self.__joueur = Personnage("Héros", 60)
            self.__ennemi = Personnage("Dragon", 120)

        self.deroulementCombat()

    def verifierSante(self):
        print(f"{self.__joueur.getNom()} : {self.__joueur.getVie()} PV")
        print(f"{self.__ennemi.getNom()} : {self.__ennemi.getVie()} PV")
        print("-" * 30)

    def verifierGagnant(self):
        if not self.__ennemi.estVivant():
            print(" Vous avez gagné !")
            return True
        if not self.__joueur.estVivant():
            print(" Vous avez perdu...")
            return True
        return False

    def deroulementCombat(self):
        print(" Le combat commence !")
        print("-" * 30)

        while True:
            input("Appuyez sur Entrée pour attaquer...")
            self.__joueur.attaquer(self.__ennemi)
            self.verifierSante()

            if self.verifierGagnant():
                break

            self.__ennemi.attaquer(self.__joueur)
            self.verifierSante()

            if self.verifierGagnant():
                break

        