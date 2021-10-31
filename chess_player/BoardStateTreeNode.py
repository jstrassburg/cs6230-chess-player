import chess
from random import sample
from chess_player.Scorer import Scorer
from itertools import chain
from statistics import mean


class BoardStateTreeNode:
    def __init__(self, board: chess.Board, move: chess.Move = None, max_children: int = None):
        self._board = board.copy(stack=False)
        if move is not None:
            self._board.push(move)
        self.move = move
        self._max_children = max_children
        self._turn_color = chess.WHITE
        self._is_end_game = board.is_game_over()
        self._children = list()

    def populate_tree(self, depth: int):
        if depth == 0:
            return

        all_legal_moves = list(self._board.legal_moves)
        moves = all_legal_moves if self._max_children is None or len(all_legal_moves) <= self._max_children \
            else sample(all_legal_moves, self._max_children)
        self._children = [BoardStateTreeNode(self._board, move, self._max_children) for move in moves]

        for child in self._children:
            child.populate_tree(depth - 1)

    def enumerate_moves(self) -> list[chess.Move]:
        return [child.move for child in self._children]

    def evaluate_moves(self, scorer: Scorer, agg_func=mean) -> list[(float, chess.Move)]:
        # There are three cases here:
        #   1. A leaf node should return it's board's score
        #   2. A root node should return the list of all of its children's score's and moves
        #   3. An internal node should return the aggregate (agg_func) of its children's scores
        if not self._children:   # I am a leaf on the wind...~`
            my_score = scorer.evaluate(self._board)
            return [(my_score, self.move)]
        elif self.move is None:  # I am [G]root.
            return list(chain(*[child.evaluate_moves(scorer, agg_func) for child in self._children]))
        else:                    # It just takes some time. Little girl, you're in the middle of the ride(tree)
            child_scores_and_moves = list(chain(*[child.evaluate_moves(scorer, agg_func) for child in self._children]))
            child_scores = list(zip(*child_scores_and_moves))[0]
            child_scores_agg = agg_func(child_scores)
            return [(child_scores_agg, self.move)]
