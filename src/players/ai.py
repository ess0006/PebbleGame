"""
Created on Nov 22, 2014

@author: Eric Shaw
@author: Michael Pritchard

"""
from src.algorithms.algorithm import *
from src.main import Menu
from player import Player


class AI(Player):
    """
    This class represents a computer player.

    """
    def __init__(self, alrgorithm_id, heuristic_id, plies, rows,
                 row_buckets, tile_pebbles):
        """ Constructor """
        if heuristic_id == Menu.MINIMAX1 or heuristic_id == Menu.MINIMAX2:
            self.algorithm = alpha_beta_minimax.AlphaBetaMinimax(heuristic_id, plies, rows,
                 row_buckets, tile_pebbles)
        else:
            self.algorithm = and_or_graph_search.AndOrGraphSearch(heuristic_id, plies, rows,
                 row_buckets, tile_pebbles)

    def request_move(self, board):
        """
        The algorithm and heuristic determine the move.

        @return: The i,j coordinates of the move.

        """
        # GUI will get move
        return self.algorithm.decide_move(board)
