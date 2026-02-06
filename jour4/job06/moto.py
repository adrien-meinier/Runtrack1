from vehicules import Vehicule
class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.roue = 2

    def informations_Vehicule(self):
        super().informations_Vehicule()
        print(f"Nombre de roues : {self.roue}")

    def demarrer(self):
        print("La moto démarre, wweeeeeeeeeeeee !")