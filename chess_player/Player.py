from abc import ABC, abstractmethod
from BoardStateTreeNode import BoardStateTreeNode
import chess
import random
from statistics import mean


class Player(ABC):
    def __init__(self):
        self._root = None

    def play_move(self, board: chess.Board):
        self._enumerate_game_states(board)
        move = self._choose_move(board.turn)
        board.push(move)

    @abstractmethod
    def _enumerate_game_states(self, board: chess.Board):
        pass

    @abstractmethod
    def _choose_move(self, turn) -> chess.Move:
        pass


class RandomPlayer(Player):
    def _enumerate_game_states(self, board: chess.Board):
        self._root = BoardStateTreeNode(board, move=None)
        self._root.populate_tree(depth=1)

    def _choose_move(self, turn) -> chess.Move:
        moves = self._root.enumerate_moves()
        return random.choice(moves)


class SearchPlayer(Player):
    def __init__(self, search_depth, score_func, agg_func=mean, max_children=None):
        super().__init__()
        self._search_depth = search_depth
        self._score_func = score_func
        self._agg_func = agg_func
        self._max_children = max_children

    def _enumerate_game_states(self, board: chess.Board):
        self._root = BoardStateTreeNode(board, move=None, max_children=self._max_children)
        self._root.populate_tree(depth=self._search_depth)

    def _choose_move(self, turn) -> chess.Move:
        scored_moves = self._root.evaluate_moves(self._score_func, self._agg_func)
        best_move = None
        best_move_score = 0.0
        for score, move in scored_moves:
            if turn == chess.WHITE:
                if score > best_move_score:
                    best_move = move
            else:
                if score < best_move_score:
                    best_move = move
        return best_move
