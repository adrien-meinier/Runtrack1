class Personnage:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def gauche(self):
        self.y -= 1

    def droite(self):
        self.y += 1

    def haut(self):
        self.x -= 1

    def bas(self):
        self.x += 1

    def position(self):
        return (self.x, self.y)    
    
p = Personnage(7, 8)
p.gauche()
p.haut()
print(p.position())