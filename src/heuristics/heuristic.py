"""
Created on Nov 25, 2014

@author: Michael Pritchard
@author: Eric Shaw

"""


class Heuristic(object):
    """
    Abstract heuristic class.

    """

    def __init__(self, player_row=None, rows=2, row_buckets=2, tile_pebbles=2):
        """
        Constructor.

        @param: player_row
        @param: rows
        @param: row_buckets
        @param: tile_pebbles

        """
        self._validate_player_row(player_row)
        self._validate_rows(rows)
        self._validate_row_buckets(row_buckets)
        self._validate_tile_pebbles(tile_pebbles)
        self.player_row = player_row
        self.rows = rows
        self.row_buckets = row_buckets
        self.tile_pebbles = tile_pebbles

    def _validate_player_row(self, player_row):
        """
        Performs type, value, and bounds checking on the player_row parameter.

        """
        if not isinstance(player_row, int):
            raise TypeError("heuristic.Heuristic: expected <type \'int\'> " +
                            "for \'player_row\', found "
                            + str(type(player_row)))
        if player_row < 0 or player_row > 1:
            raise ValueError("heuristic.Heuristic: \'player_row\' must have" +
                             " a value of zero of one.")

    def _validate_rows(self, rows):
        """ Performs type and value checking for the rows parameter """
        if not isinstance(rows, int):
            raise TypeError("heuristic.Heuristic: expected <type \'int\'> " +
                            "for \'rows\', found " + str(type(rows)))
        if rows < 2:
            raise ValueError("heuristic.Heuristic: \'rows\' must have a " +
                             "positive value greater than 1.")

    def _validate_row_buckets(self, row_buckets):
        """ Performs type and value checking for the row_buckets parameter. """
        if not isinstance(row_buckets, int):
            raise TypeError("heuristic.Heuristic: expected <type \'int\'> " +
                            "for \'row_buckets\', found "
                            + str(type(row_buckets)))
        if row_buckets < 2:
            raise ValueError("heuristic.Heuristic: \'row_buckets\' must have" +
                             " a positive value greater than 1.")

    def _validate_tile_pebbles(self, tile_pebbles):
        """
        Performs type and value checking for the tile_pebbles parameter

        """
        if not isinstance(tile_pebbles, int):
            raise TypeError("heuristic.Heuristic: expected <type \'int\'> " +
                            "for \'tile_pebbles\', found "
                            + str(type(tile_pebbles)))
        if tile_pebbles < 1:
            raise ValueError("heuristic.Heuristic: \'tile_pebbles\' must have"
                             + " a positive nonzero value.")

    def set_player_row(self, player_row):
        self._validate.player_row(player_row)
        self.player_row = player_row

    def set_rows(self, rows):
        self._validate_rows(rows)
        self.rows = rows

    def set_row_buckets(self, row_buckets):
        self._validate_row_buckets(row_buckets)
        self.row_buckets = row_buckets

    def set_tile_pebbles(self, tile_pebbles):
        self._validate_tile_pebbles(tile_pebbles)
        self.tile_pebbles = tile_pebbles

    def evaluate_board_state(self, board_state):
        raise NotImplementedError("heuristic.Heuristic: " +
                                  "evaluate_board_state() must be " +
                                  "implemented by a child Heuristic.")
