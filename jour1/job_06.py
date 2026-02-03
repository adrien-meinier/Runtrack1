class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, prenom):
        self.prenom = prenom


animal = Animal()

print(f"L'age de l'animal est de {animal.age}")

animal.vieillir()

print(f"L'age de l'animal est de {animal.age}")

animal.nommer("Philippe")

print(f"L'animal se nomme {animal.prenom}")
