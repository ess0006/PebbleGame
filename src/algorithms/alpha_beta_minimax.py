"""
Created on Dec 2, 2014

@author: Michael Pritchard
@author: Eric Shaw

"""
from algorithms.algorithm import Algorithm
from heuristics.weightless_heuristic import WeightlessHeuristic as Weightless
from heuristics.weighted_heuristic import WeightedHeuristic as Weighted


class AlphaBetaMinimax(Algorithm):
    """
    Handles the execution of the Alpha-Beta MINIMAX algorithm.

    """
    def __init__(self, heuristic_id, plies,
                 rows, row_buckets, tile_pebbles):
        """
        Constructor

        @param heuristic_id: An int representing the heuristic and player
                     utilizing it. Constants for these are defined in
                     the Menu class in Main.py. 2 and 4 are weighted,
                     3 and 5 are weightless.

        """
        self._validate_heuristic_id(heuristic_id)
        self._validate_plies(plies)

        self.player_row = (heuristic_id / 2) - 1
        self.Heuristic = Weightless if heuristic_id % 2 else Weighted

        super(AlphaBetaMinimax, self).__init__(self.player_row, rows,
                                               row_buckets, tile_pebbles)
