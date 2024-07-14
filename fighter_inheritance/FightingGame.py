from Arena import *
from Fighter import *

fighter1 = Fighter("Garry the Invincible", 100, 15)
fighter2 = DualWieldingFighter("Legolas", 85, 25)

theArena = Arena()

theArena.Fight(fighter1, fighter2)
