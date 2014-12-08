"""
Created on Nov 25, 2014

@author: Michael Pritchard
@author: Eric Shaw

"""
from heuristics.heuristic import Heuristic


class Weightless(Heuristic):
    """
    This is the weightless heuristic. It determines the board state by
    examining the net change in player pebbles from the start state.

    The initial game state is always zero, and the win state is equal to
    n * k, where n is the number of buckets per row, and k is the number of
    pebbles per bucket.

    """
    def __init__(self, player_row=None, rows=2, row_buckets=2, tile_pebbles=2):
        """
        Constructor

        @param player_row: (int) which player (top or bottom) is calling for
                           evaluation. Mandatory, [0, 1]
        @param rows: (int) [2] the number of rows on the game board. Optional,
                     GT 1. For this heuristic the value should always be 2.
        @param row_buckets: (int) [2] the number of "tiles" per row.
                            Optional, GT 1.
        @param tile_pebbles: (int) [2] the number of pebbles per tile.
                             Optional, GT 0

        """
        # Execute the __init__ method of the parent class, Heuristic.
        super(Weightless, self).__init__(player_row, rows,
                                         row_buckets, tile_pebbles)
        self.initial_value = self._calculate_initial_value()

    def _calculate_initial_value(self):
        """
        Calculates the initial value of the board based on
        the total number of pebbles per row.

        """
        return self.row_buckets * self.tile_pebbles

    def evaluate_board_state(self, board_state):
        """
        Returns the heuristic value of a given board state.

        @param board_state: A two-dimensional int array
                            representing a board state.

        """
        # Extract the number of pebbles from the player's tiles.
        tiles = [tile for tile in board_state[self.player_row]]

        current_value = sum(tiles)

        # Return the difference between the current total and initial value.
        return current_value - self.initial_value
