from ville_job1 import Ville
from personne_job01 import Personne

# villes
paris = Ville("Paris", 1_000_000)
print("Population de Paris :", paris.get_nombre_habitants())

marseille = Ville("Marseille", 861_635)
print("Population de Marseille :", marseille.get_nombre_habitants())

# creation de personnages
john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

# Ajout de population
john.ajouter_population()
myrtille.ajouter_population()
chloe.ajouter_population()

# Affichage après ajout
print("Population de Paris après ajout :", paris.get_nombre_habitants())
print("Population de Marseille après ajout :", marseille.get_nombre_habitants())
