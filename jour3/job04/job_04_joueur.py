class Joueur:
    def __init__(self, nom, numero, position, buts=0, passes=0, cartons_jaunes=0, cartons_rouges=0):
        self.__nom = nom
        self.__numero = numero
        self.__position = position
        self.__buts = buts
        self.__passes = passes
        self.__cartons_jaunes = cartons_jaunes
        self.__cartons_rouges = cartons_rouges

    def getNom(self):
        return self.__nom

    def getNumero(self):
        return self.__numero

    def getPosition(self):
        return self.__position

    def getButs(self):
        return self.__buts

    def getPasses(self):
        return self.__passes

    def getCartonsJaunes(self):
        return self.__cartons_jaunes

    def getCartonsRouges(self):
        return self.__cartons_rouges

    def marquerUnBut(self):
        self.__buts += 1

    def effectuerUnePasseDecisive(self):
        self.__passes += 1

    def recevoirUnCartonJaune(self):
        self.__cartons_jaunes += 1

    def recevoirUnCartonRouge(self):
        self.__cartons_rouges += 1

    def afficherStatistiques(self):
        print(f"{self.__nom} (#{self.__numero} - {self.__position})")
        print(f"Buts : {self.__buts}")
        print(f"Passes décisives : {self.__passes}")
        print(f"Cartons jaunes : {self.__cartons_jaunes}")
        print(f"Cartons rouges : {self.__cartons_rouges}")
        print("-" * 30)
