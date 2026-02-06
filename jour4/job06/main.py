from voitures import Voiture
from moto import Moto

voiture = Voiture("peuchère", "7898", 2052, 21500)
moto = Moto("Terminator", "turfu15", 2072, 75000)

print("Informations de la moto :")
moto.informations_Vehicule()

print("\nDémarrage de la moto :")
moto.demarrer()

print("Informations de la voiture :")
voiture.informations_Vehicule()

print("\nDémarrage de la voiture :")
voiture.demarrer()