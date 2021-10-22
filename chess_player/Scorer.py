from abc import ABC, abstractmethod
import chess


class Scorer(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def evaluate(self, board: chess.Board) -> float:
        pass


# https://www.chessprogramming.org/Simplified_Evaluation_Function
class SimplifiedEvaluationFunction(Scorer):
    def __init__(self):
        super().__init__()
        self._black_pawn_scores = \
            [0, 0, 0, 0, 0, 0, 0, 0,
             50, 50, 50, 50, 50, 50, 50, 50,
             10, 10, 20, 30, 30, 20, 10, 10,
             5, 5, 10, 25, 25, 10, 5, 5,
             0, 0, 0, 20, 20, 0, 0, 0,
             5, -5, -10, 0, 0, -10, -5, 5,
             5, 10, 10, -20, -20, 10, 10, 5,
             0, 0, 0, 0, 0, 0, 0, 0]
        self._white_pawn_scores = self._black_pawn_scores[::-1]
        self._black_knight_scores = \
            [-50, -40, -30, -30, -30, -30, -40, -50,
             -40, -20, 0, 0, 0, 0, -20, -40,
             -30, 0, 10, 15, 15, 10, 0, -30,
             -30, 5, 15, 20, 20, 15, 5, -30,
             -30, 0, 15, 20, 20, 15, 0, -30,
             -30, 5, 10, 15, 15, 10, 5, -30,
             -40, -20, 0, 5, 5, 0, -20, -40,
             -50, -40, -30, -30, -30, -30, -40, -50]
        self._white_knight_scores = self._black_knight_scores[::-1]
        self._black_bishop_scores = \
            [-20, -10, -10, -10, -10, -10, -10, -20,
             -10, 0, 0, 0, 0, 0, 0, -10,
             -10, 0, 5, 10, 10, 5, 0, -10,
             -10, 5, 5, 10, 10, 5, 5, -10,
             -10, 0, 10, 10, 10, 10, 0, -10,
             -10, 10, 10, 10, 10, 10, 10, -10,
             -10, 5, 0, 0, 0, 0, 5, -10,
             -20, -10, -10, -10, -10, -10, -10, -20]
        self._white_bishop_scores = self._black_bishop_scores[::-1]
        self._black_rook_scores = \
            [0, 0, 0, 0, 0, 0, 0, 0,
             5, 10, 10, 10, 10, 10, 10, 5,
             -5, 0, 0, 0, 0, 0, 0, -5,
             -5, 0, 0, 0, 0, 0, 0, -5,
             -5, 0, 0, 0, 0, 0, 0, -5,
             -5, 0, 0, 0, 0, 0, 0, -5,
             -5, 0, 0, 0, 0, 0, 0, -5,
             0, 0, 0, 5, 5, 0, 0, 0]
        self._white_rook_scores = self._black_rook_scores[::-1]
        self._black_queen_scores = \
            [-20, -10, -10, -5, -5, -10, -10, -20,
             -10, 0, 0, 0, 0, 0, 0, -10,
             -10, 0, 5, 5, 5, 5, 0, -10,
             -5, 0, 5, 5, 5, 5, 0, -5,
             0, 0, 5, 5, 5, 5, 0, -5,
             -10, 5, 5, 5, 5, 5, 0, -10,
             -10, 0, 5, 0, 0, 0, 0, -10,
             -20, -10, -10, -5, -5, -10, -10, -20]
        self._black_king_middle_game_scores = \
            [-30, -40, -40, -50, -50, -40, -40, -30,
             -30, -40, -40, -50, -50, -40, -40, -30,
             -30, -40, -40, -50, -50, -40, -40, -30,
             -30, -40, -40, -50, -50, -40, -40, -30,
             -20, -30, -30, -40, -40, -30, -30, -20,
             -10, -20, -20, -20, -20, -20, -20, -10,
             20, 20, 0, 0, 0, 0, 20, 20,
             20, 30, 10, 0, 0, 10, 30, 20]
        self._white_king_middle_game_scores = self._black_king_middle_game_scores[::-1]
        self._black_king_end_game_scores = \
            [-50, -40, -30, -20, -20, -30, -40, -50,
             -30, -20, -10, 0, 0, -10, -20, -30,
             -30, -10, 20, 30, 30, 20, -10, -30,
             -30, -10, 30, 40, 40, 30, -10, -30,
             -30, -10, 30, 40, 40, 30, -10, -30,
             -30, -10, 20, 30, 30, 20, -10, -30,
             -30, -30, 0, 0, 0, 0, -30, -30,
             -50, -30, -30, -30, -30, -30, -30, -50]
        self._white_king_end_game_scores = self._black_king_end_game_scores[::-1]

    def evaluate(self, board: chess.Board) -> float:
        piece_map = board.piece_map()
        for index, piece in piece_map.items():
            pass

    @staticmethod
    def is_endgame(board: chess.Board) -> bool:
        piece_map = board.piece_map()
        if 'q' not in piece_map.values() and 'Q' not in piece_map.values():
            return True
        if 'q' in piece_map.values() and 'Q' in piece_map.values():
            return False
        # TODO:  Every side which has a queen has additionally no other pieces or one minor piece maximum.

# https://www.chessprogramming.org/PeSTO%27s_Evaluation_Function
class PeSTOEvaluationFunction(Scorer):
    def evaluate(self, board: chess.Board) -> float:
        pass
