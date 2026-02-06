import random
from cards import Carte
from joueur import Joueur
from croupier import Croupier
class Jeu:
    def __init__(self):
        self.paquet = []
        self.joueur = Joueur("joueur")
        self.croupier = Croupier()
        self.creer_paquet()
        self.melanger()

    def creer_paquet(self):
        valeurs = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
                   "Valet", "Dame", "Roi", "As"]
        couleurs = ["Pique", "Cœur", "Carreau", "Trèfle"]

        for couleur in couleurs:
            for valeur in valeurs:
                self.paquet.append(Carte(valeur, couleur))

    def melanger(self):
        random.shuffle(self.paquet)

    def tirer_carte(self):
        return self.paquet.pop()

    def distribuer(self):
        for _ in range(2):
            self.joueur.ajouter_carte(self.tirer_carte())
            self.croupier.ajouter_carte(self.tirer_carte())

    def tour_joueur(self):
        while True:
            self.joueur.afficher_main()

            if self.joueur.calcul_score() > 21:
                print("Vous avez dépassé 21. Vous perdez.")
                return False

            choix = input("Prendre une carte (p) ou passer (s) ? ").lower()
            if choix == "p":
                self.joueur.ajouter_carte(self.tirer_carte())
            elif choix == "s":
                return True

    def tour_croupier(self):
        while self.croupier.doit_tirer():
            self.croupier.ajouter_carte(self.tirer_carte())

    def resultat(self):
        self.croupier.afficher_main()

        score_joueur = self.joueur.calcul_score()
        score_croupier = self.croupier.calcul_score()

        if score_croupier > 21:
            print("Le croupier dépasse 21. Vous gagnez.")
        elif score_joueur > score_croupier:
            print("Vous gagnez.")
        else:
            print("Le croupier gagne.")

    def jouer(self):
        self.distribuer()
        if self.tour_joueur():
            self.tour_croupier()
            self.resultat()

