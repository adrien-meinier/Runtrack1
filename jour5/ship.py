class Ship:
    def __init__(self, name):
        self.name = name
        self.__parts = {}  
        self.history = []  

    def add_part(self, part):
        self.__parts[part.name] = part
        self.history.append(f"Ajout de la pièce {part.name}")

    def display_state(self):
        print(f"\nÉtat du bateau : {self.name}")
        for part in self.__parts.values():
            print(part)

    def replace_part(self, part_name, new_part):
        if part_name in self.__parts:
            self.__parts[part_name] = new_part
            self.history.append(
                f"Remplacement de {part_name} par {new_part.name}"
            )
        else:
            print("Pièce introuvable.")

    def change_part(self, part_name, new_material):
        if part_name in self.__parts:
            self.__parts[part_name].change_material(new_material)
            self.history.append(
                f"Changement du matériau de {part_name} en {new_material}"
            )
        else:
            print("Pièce introuvable.")

    def get_part(self, part_name):
        return self.__parts.get(part_name)
