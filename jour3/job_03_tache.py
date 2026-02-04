class Tache:
    def __init__(self, titre, description, statut="à faire"):
        self.__titre = titre
        self.__description = description
        self.__statut = statut  

    def get_titre(self):
        return self.__titre

    def get_description(self):
        return self.__description

    def get_statut(self):
        return self.__statut

    def set_statut(self, nouveau_statut):
        if nouveau_statut in ["à faire", "terminée"]:
            self.__statut = nouveau_statut
        else:
            print("Erreur : le statut doit être 'à faire' ou 'terminée'")