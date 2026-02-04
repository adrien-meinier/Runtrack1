class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)
        print(f"Tâche '{tache.get_titre()}' ajoutée.")

    def supprimerTache(self, titre):
        for tache in self.taches:
            if tache.get_titre() == titre:
                self.taches.remove(tache)
                print(f"Tâche '{titre}' supprimée.")
                return
        print(f"Tâche '{titre}' non trouvée.")

    def marquerCommeFinie(self, titre):
        for tache in self.taches:
            if tache.get_titre() == titre:
                tache.set_statut("terminée")
                print(f"Tâche '{titre}' marquée comme terminée.")
                return
        print(f"Tâche '{titre}' non trouvée.")

    def afficherListe(self):
        if not self.taches:
            print("La liste de tâches est vide.")
        for tache in self.taches:
            print("Titre:", tache.get_titre())
            print("Description:", tache.get_description())
            print("Statut:", tache.get_statut())
            print("---")

    def filterListe(self, statut):
        return [tache for tache in self.taches if tache.get_statut() == statut]
