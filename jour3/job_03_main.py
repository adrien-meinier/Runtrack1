from job_03_tache import Tache
from job_03_liste_tache import ListeDeTaches

t1 = Tache("Faire les courses", "Acheter du lait et des œufs")
t2 = Tache("Réviser le cours", "Réviser les chapitres 1 à 3")
t3 = Tache("Appeler maman", "Demander comment elle va")

# Création de la liste de tâches
ma_liste = ListeDeTaches()

# Ajout des tâches
ma_liste.ajouterTache(t1)
ma_liste.ajouterTache(t2)
ma_liste.ajouterTache(t3)

# Afficher toutes les tâches
print("\nToutes les tâches :")
ma_liste.afficherListe()

# Supprimer une tâche
ma_liste.supprimerTache("Appeler maman")

# Marquer une tâche comme terminée
ma_liste.marquerCommeFinie("Réviser le cours")

# Afficher toutes les tâches après modifications
print("\nToutes les tâches après modifications :")
ma_liste.afficherListe()

# Afficher uniquement les tâches à faire
print("\nTâches à faire :")
taches_a_faire = ma_liste.filterListe("à faire")
for tache in taches_a_faire:
    print("Titre:", tache.get_titre())

# Afficher uniquement les tâches terminées
print("\nTâches terminées :")
taches_terminees = ma_liste.filterListe("terminée")
for tache in taches_terminees:
    print("Titre:", tache.get_titre())