from ship import Ship
from part import Part
from racing_ship import RacingShip
import menu


ship = Ship("Black Pearl")

mast = Part("Mât", "Bois")
ship.add_part(mast)

ship.change_part("Mât", "Acier")

print(mast)

racing_ship = RacingShip("Speedster", 80)

racing_ship.add_part(Part("Coque", "Fibre de carbone"))
racing_ship.add_part(Part("Voile", "Kevlar"))

racing_ship.display_speed()
menu.menu(racing_ship)

