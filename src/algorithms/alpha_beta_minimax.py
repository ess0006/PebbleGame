"""
Created on Dec 2, 2014

@author: Michael Pritchard
@author: Eric Shaw

"""
from algorithms.algorithm import Algorithm


class AlphaBetaMinimax(Algorithm):
    """
    Handles the execution of the Alpha-Beta MINIMAX algorithm.

    """
    def __init__(self, heuristic_id, plies, rows=2,
                 row_buckets=2, tile_pebbles=2):
        """
        Constructor

        @param heuristic_id: An int representing the heuristic and player
                     utilizing it. Constants for these are defined in
                     the Menu class in main.py. 2 and 4 are weighted,
                     3 and 5 are weightless.
        @param: plies
        @param: rows
        @param: row_buckets
        @param: tile_pebbles

        """
        super(AlphaBetaMinimax, self).__init__(heuristic_id, plies, rows,
                                               row_buckets, tile_pebbles)
