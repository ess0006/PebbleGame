"""
Created on Nov 22, 2014

@author: Michael Pritchard
@author: Eric Shaw

"""
from heuristics.weightless import Weightless
from heuristics.weighted import Weighted


class Algorithm(object):
    """
    This is the abstract parent class implemented by different game-playing
    algorithms. It provides means of validating input parameters.

    """
    def __init__(self, heuristic_id, plies, rows,
                 row_buckets, tile_pebbles):
        """
        Constructor

        @param heuristic_id: (int) indicator of both heuristic and player row.
                             See main.py for enumerations. Mandatory, [1, 4].
        @param plies: (int) the depth to which the tree should be generated
                      before evaluation. Mandatory, GT 0
        @param rows: (int) the number of rows on the game board. Mandatory,
                     GT 1.
        @param row_buckets: (int) the number of "tiles" per row.
                            Mandatory, GT 1.
        @param tile_pebbles: (int) [2] the number of pebbles per tile.
                             Mandatory, GT 0

        """
        # Validate input parameters
        self._validate_heuristic_id(heuristic_id)
        self._validate_plies(plies)
        self._validate_rows(rows)
        self._validate_row_buckets(row_buckets)
        self._validate_tile_pebbles(tile_pebbles)

        # Derive the player_row and heuristic from the heuristic_id
        self.player_row = (heuristic_id / 2) - 1
        Heuristic = Weightless if heuristic_id % 2 else Weighted

        self.heuristic = Heuristic(self.player_row, rows,
                                   row_buckets, tile_pebbles)
        self.plies = plies

    def _validate_heuristic_id(self, heuristic_id):
        """ Performs type validation for heurisitc_id """
        if not isinstance(heuristic_id, int):
            raise TypeError("algorithm.Algorithm: expected <type \'int\'> " +
                            "for \'heuristic_id\', found "
                            + str(type(heuristic_id)))

    def _validate_plies(self, plies):
        """ Performs type and value checking for the plies parameter """
        if not isinstance(plies, int):
            raise TypeError("algorithm.Algorithm: expected <type \'int\'> " +
                            "for \'plies\', found " + str(type(plies)))
        if plies < 2 or plies % 2:
            raise ValueError("algorithm.Algorithm: \'plies\' must have"
                             + " a positive, even value.")

    def _validate_rows(self, rows):
        """ Performs type and value checking for the rows parameter """
        if not isinstance(rows, int):
            raise TypeError("algorithm.Algorithm: expected <type \'int\'> " +
                            "for \'rows\', found " + str(type(rows)))
        if rows < 2:
            raise ValueError("algorithm.Algorithm: \'rows\' must have a " +
                             "positive value greater than 1.")

    def _validate_row_buckets(self, row_buckets):
        """ Performs type and value checking for row_buckets. """
        if not isinstance(row_buckets, int):
            raise TypeError("algorithm.Algorithm: expected <type \'int\'> " +
                            "for \'row_buckets\', found "
                            + str(type(row_buckets)))
        if row_buckets < 2:
            raise ValueError("algorithm.Algorithm: \'row_buckets\' must have" +
                             " a positive value greater than 1.")

    def _validate_tile_pebbles(self, tile_pebbles):
        """ Performs type and value checking for tile_pebbles """
        if not isinstance(tile_pebbles, int):
            raise TypeError("algorithm.Algorithm: expected <type \'int\'> " +
                            "for \'tile_pebbles\', found "
                            + str(type(tile_pebbles)))
        if tile_pebbles < 1:
            raise ValueError("algorithm.Algorithm: \'tile_pebbles\' must have"
                             + " a positive nonzero value.")

    def decide_move(self, board):
        """
        This is a virtual function that should always
        be overwritten by a child class.

        @raise NotImplementedError: Occurs if this function is called
                                    when not overwritten by a child algorithm.

        """
        raise NotImplementedError("algorithm.Algorithm: " +
                                  "decide_move() must be " +
                                  "implemented by a child algorithm.")
