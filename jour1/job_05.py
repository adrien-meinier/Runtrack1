class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Coordonnées : ({self.x}, {self.y})")

    def afficherX(self):
        print(f"X = {self.x}")

    def afficherY(self):
        print(f"Y = {self.y}")

    def changerX(self, nouveauX):
        self.x = nouveauX

    def changerY(self, nouveauY):
        self.y = nouveauY


point = Point(3, 5)

point.afficherLesPoints()
point.afficherX()
point.afficherY()

point.changerX(15)
point.changerY(28)

point.afficherLesPoints()

point.afficherX()
point.afficherY()
