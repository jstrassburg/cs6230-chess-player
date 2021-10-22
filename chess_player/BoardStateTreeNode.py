import chess
from enum import Enum
from Scorer import Scorer


class Turn(Enum):
    WHITE = 0
    BLACK = 1


class BoardStateTreeNode:
    def __init__(self, board: chess.Board, move: chess.Move = None, max_children: int = None):
        self._board = board
        self._move = move
        self._max_children = max_children
        self._turn_color = Turn.WHITE
        self._is_end_game = False
        self._children = list[BoardStateTreeNode]

    def populate_tree(self, depth: int):
        pass

    def enumerate_moves(self) -> list[chess.Move]:
        pass

    def evaluate_moves(self, score_func: Scorer, agg_func) -> list[(float, chess.Move)]:
        pass
