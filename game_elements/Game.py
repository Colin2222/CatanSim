from game_classes import *
from board_setup import *


class Game:
    board: CatanBoard

    def __init__(self):
        self.board = CatanBoard()
        load_board(self.board, "game_data/board_basic", 550, 220)
