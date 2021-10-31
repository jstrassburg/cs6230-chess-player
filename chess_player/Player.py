from abc import ABC, abstractmethod
from chess_player.BoardStateTreeNode import BoardStateTreeNode
from chess_player.Scorer import Scorer
import chess
import random
from statistics import mean


class Player(ABC):
    def __init__(self):
        self._root = None

    def play_move(self, board: chess.Board):
        self._enumerate_game_states(board)
        move = self._choose_move(board.turn)
        #  print(f"{'White' if board.turn == chess.WHITE else 'Black'} plays move {move.uci()}")
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
    def __init__(self, search_depth, scorer: Scorer, agg_func=mean, max_children=None):
        super().__init__()
        self._search_depth = search_depth
        self._scorer = scorer
        self._agg_func = agg_func
        self._max_children = max_children

    def _enumerate_game_states(self, board: chess.Board):
        self._root = BoardStateTreeNode(board, move=None, max_children=self._max_children)
        self._root.populate_tree(depth=self._search_depth)

    def _choose_move(self, turn) -> chess.Move:
        scored_moves = self._root.evaluate_moves(self._scorer, self._agg_func)
        best_move = None
        best_move_score = float('-inf') if turn == chess.WHITE else float('inf')
        for score, move in scored_moves:
            if turn == chess.WHITE:
                if score > best_move_score:
                    best_move = move
                    best_move_score = score
            else:
                if score < best_move_score:
                    best_move = move
                    best_move_score = score
        return best_move
