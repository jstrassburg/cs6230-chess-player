import unittest
import chess
from chess_player.BoardStateTreeNode import BoardStateTreeNode
from chess_player.Scorer import  SimplifiedEvaluationFunction


class TestBoardStateTreeNode(unittest.TestCase):
    def setUp(self) -> None:
        self._board = chess.Board()
        self._node = BoardStateTreeNode(self._board)
        self._scorer = SimplifiedEvaluationFunction()

    def test_populate_tree_no_depth(self):
        expected = 0
        self._node.populate_tree(depth=0)
        actual = len(self._node.enumerate_moves())
        self.assertEqual(expected, actual)

    def test_populate_tree_new_game(self):
        expected = 20
        self._node.populate_tree(depth=1)
        actual = len(self._node.enumerate_moves())
        self.assertEqual(expected, actual)

    def test_evaluate_moves_leaf_node(self):
        move = chess.Move.from_uci('e2e4')
        # this should be a leaf node since I haven't called populate_tree
        leaf_node = BoardStateTreeNode(self._board, move)
        actual = leaf_node.evaluate_moves(self._scorer)
        self.assertEqual(1, len(actual), 'Unexpected number of results returned.')
        score, move = actual[0]
        self.assertEqual(40, score, 'Unexpected score returned')
        self.assertEqual(chess.Move.from_uci('e2e4'), move, 'Unexpected move returned.')
