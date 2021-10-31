import argparse
from chess_player.ChessGame import ChessGame
from chess_player.Player import SearchPlayer, RandomPlayer
from chess_player.Scorer import SimplifiedEvaluationFunction
from random import randint
from time import perf_counter


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
        print(f"Playing chess with a search depth of {self._args.search_depth} and {self._args.max_children} "
              f"children for {self._args.max_turns} turns.")
        with open(self._args.outfile, 'a') as outfile:
            for i in range(self._args.iterations):
                start_time = perf_counter()
                termination, winner_won, played_turns = self.play_chess()
                run_time = perf_counter() - start_time
                outfile.write(f"{self._args.search_depth},{self._args.max_children},{self._args.max_turns},"
                              f"{run_time:0.2f},{termination},{winner_won},{played_turns}\n")

    def play_chess(self) -> (str, str, int):
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
        termination, winner_won, played_turns = game.get_results()
        game.reset()
        return termination, winner_won, played_turns

    def add_arguments_and_parse(self):
        self._parser.add_argument("--search-depth", dest="search_depth", required=False, default=3, type=int,
                                  help="How many levels deep to search for a good move. Default: 3")
        self._parser.add_argument("--max-children", dest="max_children", required=False, default=5, type=int,
                                  help="How many random legal moves will be evaluated. Default: 5")
        self._parser.add_argument("--max-turns", dest="max_turns", required=False, default=150, type=int,
                                  help="Play until this many turns have been played. Default: 150")
        self._parser.add_argument("--iterations", dest="iterations", required=False, default=10, type=int,
                                  help="How many iterations to run with this configuration. Default: 10")
        self._parser.add_argument("--outfile", dest="outfile", required=False, default='results.csv', type=str,
                                  help="Where to write the results. Default: results.csv")
        self._args = self._parser.parse_args()


if __name__ == "__main__":
    Program.main()
