"""
Created on Nov 22, 2014

@author: Eric Shaw
@author: Michael Pritchard

"""
from algorithms.algorithm import Algorithm

from player import Player


class AI(Player):
    """
    This class represents a computer player.

    """
    def __init__(self, heuristic):
        """ Constructor """
        self.algorithm = Algorithm.Algorithm(heuristic)

    def request_move(self, board):
        """
        The algorithm and heuristic determine the move.

        @return: The i,j coordinates of the move.

        """
        # GUI will get move
        return self.algorithm.decide_move(board)
