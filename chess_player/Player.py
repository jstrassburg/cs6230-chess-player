from abc import ABC, abstractmethod
from BoardStateTreeNode import BoardStateTreeNode
import chess


class Player(ABC):
    def __init__(self):
        self._moves = list[chess.Move]

    @abstractmethod
    def _enumerate_game_states(self, board: chess.Board):
        pass

    @abstractmethod
    def _score_moves(self):
        pass

    @abstractmethod
    def _choose_move(self):
        pass

    @abstractmethod
    def play_move(self, board: chess.Board):
        pass


class RandomPlayer(Player):
    def _enumerate_game_states(self, board: chess.Board):
        pass

    def _score_moves(self):
        pass

    def _choose_move(self):
        pass

    def play_move(self, board: chess.Board):
        pass


class SearchPlayer(Player):
    def __init__(self, search_depth, score_func, agg_func, max_children=None):
        super().__init__()
        self._search_depth = search_depth
        self._score_func = score_func
        self._agg_func = agg_func
        self._max_children = max_children
        self._root = BoardStateTreeNode()

    def _enumerate_game_states(self, board: chess.Board):
        pass

    def _score_moves(self):
        pass

    def _choose_move(self):
        pass

    def play_move(self, board: chess.Board):
        pass
