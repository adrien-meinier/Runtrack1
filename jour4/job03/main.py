from parallepipede import Parallepipede
from rectangle import Rectangle

r = Rectangle(5, 3)
print("Surface du rectangle :", r.surface())  
print("Perimetre:", r.perimetre())
print("-"*30)


p = Parallepipede(5, 3, 2)
print("Perimetre:", p.perimetre())
print("Surface du parallepipede :", p.surface())    
print("Volume du parallepipede :", p.volume())  
