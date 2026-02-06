from vehicules import Vehicule
class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.portes = 4

    def informations_Vehicule(self):
        super().informations_Vehicule()
        print(f"Nombre de portes : {self.portes}")

voiture = Voiture("peuchère", "7898", 2052, 21500)
voiture.informations_Vehicule()