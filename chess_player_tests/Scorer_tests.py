import unittest
import chess
from chess_player.Scorer import SimplifiedEvaluationFunction, PeSTOEvaluationFunction


class TestSimplifiedEvaluationFunction(unittest.TestCase):
    def setUp(self, board: chess.Board = None):
        self._board = board if board is not None else chess.Board()
        self._scorer = SimplifiedEvaluationFunction()

    def test_default_board_is_not_endgame(self):
        expected = False
        actual = self._scorer.is_endgame(self._board)
        self.assertEqual(expected, actual)

    def test_no_queens_is_endgame(self):
        expected = True
        board = chess.Board(fen='rnb1kbnr/8/8/8/8/8/8/RNB1KBNR')
        actual = self._scorer.is_endgame(board)
        self.assertEqual(expected, actual)

    def test_one_queen_and_no_other_pieces_is_endgame(self):
        expected = True
        board = chess.Board(fen='7q/8/8/8/8/8/8/7K')
        actual = self._scorer.is_endgame(board)
        self.assertEqual(expected, actual)

    def test_one_queen_and_one_other_piece_is_endgame(self):
        expected = True
        board = chess.Board(fen='6rq/8/8/8/8/8/8/7K')
        actual = self._scorer.is_endgame(board)
        self.assertEqual(expected, actual)

    def test_one_queen_and_two_other_pieces_is_not_endgame(self):
        expected = False
        board = chess.Board(fen='5brq/8/8/8/8/8/8/7K')
        actual = self._scorer.is_endgame(board)
        self.assertEqual(expected, actual)

    def test_default_board_score(self):
        expected = 0
        actual = self._scorer.evaluate(self._board)
        self.assertEqual(expected, actual)