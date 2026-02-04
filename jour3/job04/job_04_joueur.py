class Joueur:
    def __init__(self, nom, numero, position):
        self.__nom = nom
        self.__numero = numero
        self.__position = position
        self.__cartons_rouge = 0
        self.__cartons_jaune = 0
        self.__buts = 0
        self.__passes = 0

    def But(self):
        self.__buts += 1
        print(f"{self.__nom} a marqué un but ! Total buts : {self.__buts}")

    
    def Passe(self):
        self.__passes += 1
        print(f"{self.__nom} a réalisé une passe décisive ! Total passes : {self.__passes}")


    def CartonJaune(self):
        self.__cartons_jaune += 1
        print(f"{self.__nom} a reçu un carton jaune ! Total cartons jaunes : {self.__cartons_jaune}")

    def CartonRouge(self):
        self.cartons_rouge += 1
        print(f"{self.__nom} a reçu un carton rouge ! Total cartons rouges : {self.__cartons_rouge}")

    def Statistiques(self):
        print(f"Statistiques de {self.__nom} :")
        print(f"Numéro : {self.__numero}")
        print(f"Position : {self.__position}")
        print(f"Buts : {self.__buts}")
        print(f"Passes décisives : {self.__passes}")
        print(f"Cartons jaunes : {self.__cartons_jaune}")
        print(f"Cartons rouges : {self.__cartons_rouge}")


joueur1 = Joueur("Poutou", 10, "defenseur")
joueur1.But()
joueur1.Passe()
joueur1.CartonJaune()
joueur1.Statistiques()
joueur1.But()
joueur1.Passe()
joueur1.CartonJaune()
joueur1.Statistiques()