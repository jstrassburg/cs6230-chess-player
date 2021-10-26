import unittest
import chess
from chess_player.BoardStateTreeNode import BoardStateTreeNode


class TestBoardStateTreeNode(unittest.TestCase):
    def setUp(self) -> None:
        self._board = chess.Board()
        self._node = BoardStateTreeNode(self._board)

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
