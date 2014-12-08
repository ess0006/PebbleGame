"""
Created on Nov 22, 2014

@author: Eric Shaw
@author: Michael Pritchard

"""
from players.player import Player
from algorithms.and_or_graph_search import AndOrGraphSearch
from algorithms.alpha_beta_minimax import AlphaBetaMinimax


class AI(Player):
    """
    This class represents a computer player.

    """
    def __init__(self, algorithm_id, heuristic_id, plies, rows,
                 row_buckets, tile_pebbles):
        """ Constructor """
        Algorithm = AndOrGraphSearch if algorithm_id % 2 else AlphaBetaMinimax
        self.algorithm = Algorithm(heuristic_id, plies, rows,
                                   row_buckets, tile_pebbles)

    def request_move(self, board):
        """
        The algorithm and heuristic determine the move.

        @return: The i,j coordinates of the move.

        """
        return self.algorithm.decide_move(board)
