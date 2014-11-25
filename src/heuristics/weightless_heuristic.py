"""
Created on Nov 25, 2014

@author: Michael Pritchard
@author: Eric Shaw

"""

from heuristics.heuristic import Heuristic


class WeightlessHeuristic(Heuristic):
    """
    This is the weightless heuristic. It determines the board state by
    examining the net change in player pebbles from the start state.

    The initial game state is always zero, and the win state is equal to
    n * k, where n is the number of buckets per row, and k is the number of
    pebbles per bucket.

    """

    def __init__(self):
        """ Constructor """
