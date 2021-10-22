from abc import ABC, abstractmethod
import chess


class Scorer(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def evaluate(self, board: chess.Board) -> float:
        pass


# https://www.chessprogramming.org/Simplified_Evaluation_Function
class SimplifiedEvaluationFunction(Scorer):
    def evaluate(self, board: chess.Board) -> float:
        pass


# https://www.chessprogramming.org/PeSTO%27s_Evaluation_Function
class PeSTOEvaluationFunction(Scorer):
    def evaluate(self, board: chess.Board) -> float:
        pass
