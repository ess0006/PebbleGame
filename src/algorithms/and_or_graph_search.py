"""
Created on Dec 2, 2014

@author: Michael Pritchard
@author: Eric Shaw
"""
from algorithms.algorithm import Algorithm
from Board import Board


class AndOrGraphSearch(Algorithm):
    """
    This class handles the operations of the AND-OR graph search algorithm
    given a set of initial conditions for a board and which player
    (top or bottom).

    """
    def __init__(self, player_row=None, rows=2, row_buckets=2, tile_pebbles=2):
        """
        Constructor

        @param: player_row
        @param: rows
        @param: row_buckets
        @param: tile_pebbles

        """
        super(AndOrGraphSearch, self).__init__(player_row, rows,
                                               row_buckets, tile_pebbles)

        self.board = Board(rows, row_buckets, tile_pebbles)
        self.plan = {}

    def generate_plan(self):
        """ Generates a conditional plan based on the current board state. """
        pass

    def or_search(self, board, path):
        if board.victory(self.player_row):
            return path
        if board.get_state in path:
            return None
        # move should be a set of coordinates
        for move in board.legal_moves(self.player_row):
            
        return None

    def and_search(self, path):
        pass
