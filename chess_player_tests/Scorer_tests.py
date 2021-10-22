import unittest
import chess
from chess_player.Scorer import SimplifiedEvaluationFunction, PeSTOEvaluationFunction


class TestSimplifiedEvaluationFunction(unittest.TestCase):
    def test_default_board_has_zero_score(self):
        scorer = SimplifiedEvaluationFunction()
        expected = 0
        board = chess.Board()
        actual = scorer.evaluate()
