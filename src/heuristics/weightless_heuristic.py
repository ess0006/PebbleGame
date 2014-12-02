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
    def __init__(self, player_row=None, rows=2, row_buckets=2, tile_pebbles=2):
        """ Constructor """
        super(WeightlessHeuristic, self).__init__(player_row, rows,
                                                  row_buckets, tile_pebbles)
        self.initial_value = self.calculate_initial_value()

    def calculate_initial_value(self):
        return self.row_buckets * self.tile_pebbles

    def evaluate_board_state(self, board_state):
        tiles = [tile for tile in board_state[self.player_row]]
        current_value = sum(tiles)

        return current_value - self.initial_value
