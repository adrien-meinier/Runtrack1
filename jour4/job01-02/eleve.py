from personne import Personne
class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours") 

    def afficherAge(self):
        print(f"J'ai {self.age} ans") 