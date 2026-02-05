class Equipe:
    def __init__(self, nom):
        self.__nom = nom
        self.__joueurs = []

    def getNom(self):
        return self.__nom

    def getJoueurs(self):
        return self.__joueurs

    def ajouterJoueur(self, joueur):
        self.__joueurs.append(joueur)

    def AfficherStatistiquesJoueurs(self):
        print(f"Équipe : {self.__nom}")
        print("=" * 30)
        for joueur in self.__joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, joueur, action):
        if joueur in self.__joueurs:
            if action == "but":
                joueur.marquerUnBut()
            elif action == "passe":
                joueur.effectuerUnePasseDecisive()
            elif action == "jaune":
                joueur.recevoirUnCartonJaune()
            elif action == "rouge":
                joueur.recevoirUnCartonRouge()
