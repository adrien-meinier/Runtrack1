class Operation:
    def __init__(self, nombre1=12, nombre2=3):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

# Instanciation de la classe
mon_operation = Operation()

print(f"Le nombre1 est {mon_operation.nombre1}")
print(f"Le nombre2 est {mon_operation.nombre2}")