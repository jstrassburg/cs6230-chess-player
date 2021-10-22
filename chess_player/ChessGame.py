import chess
from Player import Player


class ChessGame:
    def __init__(self, white_player: Player, black_player: Player):
        self._board = chess.Board()
        self._played_turns = 0
        self._white_player = white_player
        self._black_player = black_player

    def play_turn(self) -> bool:
        pass

    def reset(self):
        self._board.reset()
        self._played_turns = 0

    def print_game_stats(self):
        pass

    def play_until(self, n_turns) -> bool:
        pass
