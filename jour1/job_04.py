class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    
    def se_presenter(self):
        return f"Je m'appelle {self.nom} {self.prenom}."
    
p1 = Personne("philippe", "meurisse")
p2 = Personne("ouioui", "nonon")
p3 = Personne("dark", "vador")

print(p3.se_presenter())
    
         