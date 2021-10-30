import chess
import io
import unittest.mock
from chess_player.ChessGame import ChessGame
from chess_player.Player import RandomPlayer, SearchPlayer
from chess_player.Scorer import SimplifiedEvaluationFunction


class TestChessGame(unittest.TestCase):
    def setUp(self) -> None:
        self._scorer = SimplifiedEvaluationFunction()
        self._white_player = RandomPlayer()
        self._black_player = SearchPlayer(search_depth=2, scorer=self._scorer)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_game_stats_new_game(self, mock_stdout):
        game = ChessGame(self._white_player, self._black_player)
        game.print_game_stats()
        self.assertIn('The game is not over yet.', mock_stdout.getvalue())
        self.assertIn('0 turns have been played so far.', mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_game_stats_end_game(self, mock_stdout):
        board = chess.Board(fen='8/8/8/8/8/8/6rq/7K')
        game = ChessGame(self._white_player, self._black_player, board)
        game.print_game_stats()
        self.assertIn('The game is over', mock_stdout.getvalue())
        self.assertIn('Termination.CHECKMATE', mock_stdout.getvalue())
