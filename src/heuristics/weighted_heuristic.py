"""
Created on Nov 25, 2014

@author: Michael Pritchard
@author: Eric Shaw

"""
from operator import mul

from heuristics.heuristic import Heuristic


class WeightedHeuristic(Heuristic):
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
        """ Constructor """
        super(WeightedHeuristic, self).__init__(player_row, rows,
                                                row_buckets, tile_pebbles)

    def evaluate_board_state(self, board_state):
        weights = [weight for weight in range(1, self.row_buckets + 1)]
        tiles = [tile for tile in board_state[1]]
        # The map operation performs an index-wise
        # multiplication of the weights and tiles.
        bot_value = sum(map(mul, tiles, weights))

        weights = reversed(weights)
        tiles = [tile for tile in board_state[0]]
        top_value = sum(map(mul, tiles, weights))

        return (top_value - bot_value if not self.player_row
                else bot_value - top_value)
