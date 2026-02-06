class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.main = []

    def ajouter_carte(self, carte):
        self.main.append(carte)

    def calcul_score(self):
        score = 0
        nb_as = 0

        for carte in self.main:
            score += carte.points()
            if carte.valeur == "As":
                nb_as += 1

        while score > 21 and nb_as > 0:
            score -= 10
            nb_as -= 1

        return score

    def afficher_main(self):
        print(f"\nMain de {self.nom} :")
        for carte in self.main:
            print(carte)
        print("Score :", self.calcul_score())
