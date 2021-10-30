import chess
from chess_player.Player import Player


class ChessGame:
    def __init__(self, white_player: Player, black_player: Player, board: chess.Board = chess.Board()):
        self._board = board
        self._played_turns = 0
        self._white_player = white_player
        self._black_player = black_player

    def play_turn(self):
        if self._board.turn == chess.WHITE:
            self._white_player.play_move(self._board)
        else:
            self._black_player.play_move(self._board)

    def reset(self):
        self._board.reset()
        self._played_turns = 0

    def print_game_stats(self):
        if not self._board.is_game_over():
            print(f"The game is not over yet. {self._played_turns} turns have been played so far.")
            print(f"The current board state is:\n\n{self._board}\n")
            if self._board.is_check():
                if self._board.turn == chess.WHITE:
                    print(f"White is currently in check.")
                else:
                    print(f"Black is currently in check.")
        else:
            print(f"The game is over after {self._played_turns} moves.")
            print(f"The game's outcome was: {self._board.outcome()}")
            print(f"The final board state was:\n\n{self._board}\n")

    def play_until(self, n_turns):
        while self._played_turns < n_turns and not self._board.is_game_over():
            self.play_turn()
