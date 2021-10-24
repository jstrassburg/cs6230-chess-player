from abc import ABC, abstractmethod
import chess


class Scorer(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def evaluate(self, board: chess.Board) -> int:
        pass


# https://www.chessprogramming.org/Simplified_Evaluation_Function
class SimplifiedEvaluationFunction(Scorer):
    def __init__(self):
        super().__init__()
        # We must mirror the array for white/black scoring since these boards aren't symmetrical
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
        self._white_queen_scores = self._black_queen_scores[::-1]
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
        white_score = 0
        black_score = 0
        is_endgame = self.is_endgame(board)
        for index, piece in piece_map.items():
            if piece == chess.Piece.from_symbol('p'):
                black_score += self._black_pawn_scores[index]
            if piece == chess.Piece.from_symbol('r'):
                black_score += self._black_rook_scores[index]
            if piece == chess.Piece.from_symbol('n'):
                black_score += self._black_knight_scores[index]
            if piece == chess.Piece.from_symbol('b'):
                black_score += self._black_bishop_scores[index]
            if piece == chess.Piece.from_symbol('q'):
                black_score += self._black_queen_scores[index]
            if piece == chess.Piece.from_symbol('k'):
                if is_endgame:
                    black_score += self._black_king_end_game_scores[index]
                else:
                    black_score += self._black_king_middle_game_scores[index]
            if piece == chess.Piece.from_symbol('P'):
                white_score += self._white_pawn_scores[index]
            if piece == chess.Piece.from_symbol('R'):
                white_score += self._white_rook_scores[index]
            if piece == chess.Piece.from_symbol('N'):
                white_score += self._white_knight_scores[index]
            if piece == chess.Piece.from_symbol('B'):
                white_score += self._white_bishop_scores[index]
            if piece == chess.Piece.from_symbol('Q'):
                white_score += self._white_queen_scores[index]
            if piece == chess.Piece.from_symbol('K'):
                if is_endgame:
                    white_score += self._white_king_end_game_scores[index]
                else:
                    white_score += self._white_king_middle_game_scores[index]

        return white_score - black_score

    @staticmethod
    def is_endgame(board: chess.Board) -> bool:
        # Using an endgame definition from : https://www.chessprogramming.org/Simplified_Evaluation_Function
        pieces = board.piece_map().values()
        white_queen = chess.Piece.from_symbol('Q')
        black_queen = chess.Piece.from_symbol('q')
        # we're in the endgame if neither side has a queen
        if black_queen not in pieces and white_queen not in pieces:
            return True
        # we're not in the endgame if both sides have their queen
        if black_queen in pieces and white_queen in pieces:
            return False
        # we're in the endgame if either side with a queen has, at most, one minor piece
        if black_queen in pieces:
            black_minor_pieces_count = len(
                [piece for piece in pieces if SimplifiedEvaluationFunction.is_black_minor_piece(piece)])
            return black_minor_pieces_count <= 1
        if white_queen in pieces:
            white_minor_pieces_count = len(
                [piece for piece in pieces if SimplifiedEvaluationFunction.is_white_minor_piece(piece)])
            return white_minor_pieces_count <= 1

    @staticmethod
    def is_black_minor_piece(piece: chess.Piece):
        if piece == chess.Piece.from_symbol('r') or \
                piece == chess.Piece.from_symbol('b') or \
                piece == chess.Piece.from_symbol('n'):
            return True
        return False

    @staticmethod
    def is_white_minor_piece(piece: chess.Piece):
        if piece == chess.Piece.from_symbol('R') or \
                piece == chess.Piece.from_symbol('B') or \
                piece == chess.Piece.from_symbol('N'):
            return True
        return False


# https://www.chessprogramming.org/PeSTO%27s_Evaluation_Function
class PeSTOEvaluationFunction(Scorer):
    def evaluate(self, board: chess.Board) -> float:
        pass
