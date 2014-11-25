"""
Created on Nov 25, 2014

@author: Michael Pritchard
@author: Eric Shaw

"""


class Heuristic(object):
    """
    Abstract heuristic class.

    """

    def __init__(self, rows=2, row_buckets=2):
        """
        Constructor.

        @param: rows
        @param row_buckets

        """
        self.validate_rows(rows)
        self.validate_row_buckets(row_buckets)
        self.rows = rows
        self.row_buckets = row_buckets

    def validate_rows(self, rows):
        """ Performs type and value checking for the rows parameter """
        if not isinstance(rows, int):
            raise TypeError("heuristic.Heuristic: expected <type \'int\'> " +
                            "for \'rows\', found " + type(rows))
        if rows < 2:
            raise ValueError("heuristic.Heuristic: \'rows\' must have a " +
                             "positive value greater than 1.")

    def validate_row_buckets(self, row_buckets):
        """ Performs type and value checking for the row_buckets paramter. """
        if not isinstance(row_buckets, int):
            raise TypeError("heuristic.Heuristic: expected <type \'int\'> " +
                            "for \'row_buckets\', found " + type(row_buckets))
        if row_buckets < 2:
            raise ValueError("heuristic.Heuristic: \'row_buckets\' must have" +
                             " a positive value greater than 1.")

    def set_rows(self, rows):
        self.validate_rows(rows)
        self.rows = rows

    def set_row_buckets(self, row_buckets):
        self.validate_row_buckets(row_buckets)
        self.row_buckets = row_buckets

    def evaluate_board_state(self, board_state):
        pass
