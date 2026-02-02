class Operation:
    def __init__(self, nombre1=12, nombre2=3):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        return self.nombre1 + self.nombre2
        

# Instanciation de la classe
mon_operation = Operation()
print(mon_operation.addition())