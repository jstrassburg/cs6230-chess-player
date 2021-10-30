import argparse
from chess_player.ChessGame import ChessGame
from chess_player.Player import SearchPlayer, RandomPlayer
from chess_player.Scorer import SimplifiedEvaluationFunction
from random import randint


class Program:
    @staticmethod
    def main():
        program = Program()
        program.run()

    def __init__(self):
        self._args = None
        self._parser = argparse.ArgumentParser(description="Play some chess")
        self._scorer = SimplifiedEvaluationFunction()

    def run(self):
        self.add_arguments_and_parse()
        self.play_chess()

    def play_chess(self):
        search_depth = self._args.search_depth
        max_children = self._args.max_children

        # flip a coin to see who gets the better player (search vs. random)
        if randint(0, 1) == 0:
            print(f"The white player should be stronger.")
            white_player = SearchPlayer(
                search_depth=search_depth, max_children=max_children, scorer=self._scorer)
            black_player = RandomPlayer()
        else:
            print(f"The black player should be stronger.")
            white_player = RandomPlayer()
            black_player = SearchPlayer(
                search_depth=search_depth, max_children=max_children, scorer=self._scorer)

        game = ChessGame(white_player=white_player, black_player=black_player)
        game.play_until(self._args.max_turns)
        game.print_game_stats()

    def add_arguments_and_parse(self):
        self._parser.add_argument("--search-depth", dest="search_depth", required=False, default=3, type=int,
                                  help="How many levels deep to search for a good move. Default: 3")
        self._parser.add_argument("--max-children", dest="max_children", required=False, default=5, type=int,
                                  help="How many random legal moves will be evaluated. Default: 5")
        self._parser.add_argument("--max-turns", dest="max_turns", required=False, default=20, type=int,
                                  help="Play until this many turns have been played. Default: 20")
        self._args = self._parser.parse_args()


if __name__ == "__main__":
    Program.main()
