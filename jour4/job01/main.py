from personne import Personne
from eleve import Eleve
from proffesseur import Professeur

#eleve
eleve1 = Eleve()
eleve1.allerEnCours()     
eleve1.afficherAge()      
eleve1.modifierAge(16)
eleve1.afficherAge()      

# Prof
prof1 = Professeur("Physique", age=40)
prof1.bonjour()       
prof1.afficherAge()
prof1.afficher_matiere()
prof1.enseigner()     
