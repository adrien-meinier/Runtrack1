from job_04_equipe import Equipe
from job_04_joueur import Joueur

j1 = Joueur("Poutou", 10, "Défenseur")
j2 = Joueur("Messi", 30, "Attaquant")
j3 = Joueur("Menon", 3, "Défenseur" )

equipe1 = Equipe("PSG")

equipe1.ajouterJoueur(j1)
equipe1.ajouterJoueur(j2)
equipe1.ajouterJoueur(j3)

equipe1.AfficherStatistiquesJoueurs()

equipe1.mettreAJourStatistiquesJoueur(j2, "but")
equipe1.mettreAJourStatistiquesJoueur(j1, "jaune")
equipe1.mettreAJourStatistiquesJoueur(j3, "rouge")

equipe1.AfficherStatistiquesJoueurs()
