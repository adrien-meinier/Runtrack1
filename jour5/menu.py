from ship import Ship
from part import Part
def menu(ship):
    while True:
        print("\n--- MENU ---")
        print("1. Afficher l'état du bateau")
        print("2. Modifier le matériau d'une pièce")
        print("3. Remplacer une pièce")
        print("4. Afficher l'historique")
        print("5. Quitter")

        choice = input("Choix : ")

        if choice == "1":
            ship.display_state()

        elif choice == "2":
            name = input("Nom de la pièce : ")
            material = input("Nouveau matériau : ")
            ship.change_part(name, material)

        elif choice == "3":
            name = input("Nom de la pièce à remplacer : ")
            new_name = input("Nom de la nouvelle pièce : ")
            new_material = input("Matériau : ")
            ship.replace_part(name, Part(new_name, new_material))

        elif choice == "4":
            print("\nHistorique des modifications :")
            for event in ship.history:
                print("-", event)

        elif choice == "5":
            print("Fin du programme.")
            break

        else:
            print("Choix invalide.")
