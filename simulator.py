from game_elements.Game import *
from DisplayModule import *

game = Game()
dm = DisplayModule()
game.dm = dm
dm.start_display(game)
