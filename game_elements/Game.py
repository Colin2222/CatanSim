from game_classes import *
from board_setup import *
from DisplayModule import *


class Game:
    board: CatanBoard
    dm: DisplayModule

    def __init__(self):
        self.board = CatanBoard()
        load_board(self.board, "game_data/board_basic", 550, 220)
        print(self.board.resource_tiles)

    def HighlightSomething(self):
        print("POOP")
        for edge in self.board.resource_tiles[0][8].edges:
            edge.ownIcons[0].image_location = "images/placeholder_2.png"
        self.dm.refresh_display()
