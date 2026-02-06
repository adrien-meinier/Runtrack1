from joueur import Joueur
class Croupier(Joueur):
    def __init__(self):
        super().__init__("croupier")

    def doit_tirer(self):
        return self.calcul_score() < 17
