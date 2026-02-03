class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def calculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA)

    def afficher(self):
        return {
            "nom": self.nom,
            "prixHT": self.prixHT,
            "TVA": self.TVA,
            "prixTTC": self.calculerPrixTTC()
        }

    def modifierNom(self, nouveauNom):
        self.nom = nouveauNom

    def modifierPrixHT(self, nouveauPrix):
        self.prixHT = nouveauPrix

    def getNom(self):
        return self.nom

    def getPrixHT(self):
        return self.prixHT

    def getTVA(self):
        return self.TVA