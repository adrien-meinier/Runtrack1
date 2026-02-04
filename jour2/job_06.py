class Commande:
    TVA = 0.20  

    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats = {}  
        self.__statut = "en cours"

    def ajouter_plat(self, nom_plat, prix):
        if self.__statut != "en cours":
            print("Impossible d'ajouter un plat : la commande n'est plus en cours.")
            return
        self.__plats[nom_plat] = prix

    def annuler_commande(self):
        self.__statut = "annulée"

    def __calculer_total(self):
        return sum(self.__plats.values())

    def calculer_tva(self):
        return self.__calculer_total() * Commande.TVA

    def afficher_commande(self):
        print(f"Commande n°{self.__numero_commande}")
        print(f"Statut : {self.__statut}")

        if not self.__plats:
            print("Aucun plat commandé.")
            return

        print("Plats commandés :")
        for plat, prix in self.__plats.items():
            print(f" - {plat} : {prix:.2f} €")

        total_ht = self.__calculer_total()
        tva = self.calculer_tva()
        total_ttc = total_ht + tva

        print(f"Total HT : {total_ht:.2f} €")
        print(f"TVA (20%) : {tva:.2f} €")
        print(f"Total TTC : {total_ttc:.2f} €")


commande1 = Commande(101)

commande1.ajouter_plat("Pizza", 12.50)
commande1.ajouter_plat("Pâtes", 9.00)
commande1.ajouter_plat("Dessert", 4.50)

commande1.afficher_commande()

#print("\n--- Annulation de la commande ---")
#commande1.annuler_commande()

commande1.ajouter_plat("filet mignon", 17.00)

commande1.afficher_commande()

