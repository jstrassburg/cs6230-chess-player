import chess
from random import sample

from chess_player.Scorer import Scorer
from statistics import mean


class BoardStateTreeNode:
    def __init__(self, board: chess.Board, move: chess.Move = None, max_children: int = None):
        self._board = board.copy(stack=False)
        self.move = move
        self._max_children = max_children
        self._turn_color = chess.WHITE
        self._is_end_game = board.is_game_over()
        self._children = list()

    def populate_tree(self, depth: int):
        if depth == 0:
            return

        all_legal_moves = self._board.legal_moves
        moves = all_legal_moves if self._max_children is None else sample(list(all_legal_moves), self._max_children)
        self._children = [BoardStateTreeNode(self._board, move, self._max_children) for move in moves]

        for child in self._children:
            child.populate_tree(depth - 1)

    def enumerate_moves(self) -> list[chess.Move]:
        return [child.move for child in self._children]

    def evaluate_moves(self, score_func: Scorer, agg_func=mean) -> list[(float, chess.Move)]:
        pass