class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def calculerTVA(self):
        return self.prixHT * self.TVA

    def calculerPrixTTC(self):
        return self.prixHT + self.calculerTVA()

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

    def getPrixTTC(self):
        return self.calculerPrixTTC()


produit1 = Produit("Ordinateur", 800, 0.20)
produit2 = Produit("Souris", 200, 0.20)
produit3 = Produit("Écran", 400, 0.20)

# Calcul et affichage TVA et TTC
print(produit1.getNom(), "TVA :", produit1.calculerTVA(), "TTC :", produit1.getPrixTTC())
print(produit2.getNom(), "TVA :", produit2.calculerTVA(), "TTC :", produit2.getPrixTTC())
print(produit3.getNom(), "TVA :", produit3.calculerTVA(), "TTC :", produit3.getPrixTTC())

# Modification du nom et du prix
produit1.modifierNom("Ordinateur Portable")
produit1.modifierPrixHT(900)

produit2.modifierNom("Souris Sans Fil")
produit2.modifierPrixHT(250)

produit3.modifierNom("Écran 27 pouces")
produit3.modifierPrixHT(450)

# Affichage des nouveaux prix
print(produit1.getNom(), "nouveau prix TTC :", produit1.getPrixTTC())
print(produit2.getNom(), "nouveau prix TTC :", produit2.getPrixTTC())
print(produit3.getNom(), "nouveau prix TTC :", produit3.getPrixTTC())
