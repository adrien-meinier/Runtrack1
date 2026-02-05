from personne import Personne
class Professeur(Personne):
    def __init__(self, matiere, age=14):
        super().__init__(age)  
        self.__matiereEnseignee = matiere  

    def enseigner(self):
        print("Le cours va commencer")  

    def afficherAge(self):
        print(f"Le professeur a {self.age} ans")

    def get_matiere(self):
        return self.__matiereEnseignee
    
    def afficher_matiere(self):
        print(f"Il enseigne {self.__matiereEnseignee}")
        
