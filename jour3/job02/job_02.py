class CompteBancaire:
    def __init__(self, n_compte, nom, prenom, solde, decouvert=False):
        self.__n_compte = n_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert
    
    def afficher(self):
        print("----- Détails du compte -----")
        print("Numéro de compte :", self.__n_compte)
        print("Nom :", self.__nom)
        print("Prénom :", self.__prenom)
        print("Solde :", self.__solde, "€")
        print("Découvert autorisé :", self.__decouvert)

    def afficherSolde(self):
        print("Solde actuel :", self.__solde, "€")

    def versement(self, montant):
        if montant > 0:
            self.__solde += montant
            print("Versement effectué. Nouveau solde :", self.__solde, "€")
        else:
            print("Montant de versement invalide.")

    def agios(self):
        if self.__solde < 0:
            agios = abs(self.__solde) * 0.05  
            self.__solde -= agios
            print("Agios appliqués :", agios, "€")
            print("Nouveau solde :", self.__solde, "€")
            

    def retrait(self, montant):
        if montant <= 0:
            print("Montant de retrait invalide.")
        elif self.__solde - montant < 0 and not self.__decouvert:
            print("Erreur : découvert non autorisé.")
        else:
            self.__solde -= montant
            print("Retrait effectué. Nouveau solde :", self.__solde, "€")

    def virement(self, reference, compte_destinataire, montant):
        print("Virement :", reference)
        if montant <= 0:
           print("Erreur : montant invalide.")
        elif self.__solde - montant < 0 and not self.__decouvert:
           print("Erreur : solde insuffisant pour le virement.")
        else:
           self.__solde -= montant
           compte_destinataire.versement(montant)
           print(f"Virement de {montant} € effectué vers {compte_destinataire.__nom} {compte_destinataire.__prenom}")


compte1 = CompteBancaire("123456", "jhon", "jhon", 10000, False)
compte2 = CompteBancaire("654321", "MonSaigneur", "Dracula", 5000, True)

compte1.afficher()
compte1.versement(500)
compte1.retrait(300)
compte1.retrait(1500)
compte1.afficherSolde()

compte2.afficher()
compte2.versement(500)
compte2.retrait(4000)
compte2.retrait(3000)
compte2.agios()
compte2.afficherSolde()

compte1.virement("VIR001", compte2, 2000)

compte1.afficherSolde()
compte2.afficherSolde()

