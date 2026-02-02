class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    
    def se_presenter(self):
        return f"Je m'appelle {self.prenom} {self.nom}."
    
p1 = Personne("philippe", "meurisse")
p2 = Personne("ouioui", "nonon")
p3 = Personne("dark", "vador")

print(p1.se_presenter())
    
         