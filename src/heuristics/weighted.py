"""
Created on Nov 25, 2014

@author: Michael Pritchard
@author: Eric Shaw

"""
from operator import mul

from heuristics.heuristic import Heuristic


class Weighted(Heuristic):
    """
    This is the weighted heuristic. It evaluates a board state by examining
    both the number of pebbles in a given tile and the position of the tile.

    The value of a particular bucket is calculated as p * w, where p is the
    current number of pebbles in the bucket, and w is the weight. The weight
    is based on the coordinates of the bucket.

    For the player on the top row, the weight is equivalent to the index of
    the bucket (starting at an index of 1 and proceeding left-to-right). For
    example, the second bucket from the left has a weight of 2.

    For the player on the bottom row, the weight is equivalent to an index
    starting from one and proceeding right-to-left (e.g., the right-most bucket
    has a value of 1, the second from the right has a value of 2, etc).

    The final evaluation of the board state is taken by summing the tile values
    on the top row and subtracting the sum of the tile values on the bottom
    row.

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
        super(Weighted, self).__init__(player_row, rows,
                                                row_buckets, tile_pebbles)

    def evaluate_board_state(self, board_state):
        """
        Returns the heuristic value of a given board state.

        @param board_state: A two-dimensional int array
                            representing a board state.

        """
        # Extract the number of pebbles from the bottom tiles
        # and create a corresponding list of weights.
        weights = [weight for weight in range(1, self.row_buckets + 1)]
        tiles = [tile for tile in board_state[1]]

        # Perform an index-wise multiplication of the
        # weights and pebble counts using a map.
        bot_value = sum(map(mul, tiles, weights))

        # Repeat the above procedure for the top tiles.
        weights = reversed(weights)
        tiles = [tile for tile in board_state[0]]
        top_value = sum(map(mul, tiles, weights))

        # Return the heuristic value relative to the calling player.
        return (top_value - bot_value if not self.player_row
                else bot_value - top_value)
