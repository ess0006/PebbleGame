"""
Created on Dec 2, 2014

@author: Michael Pritchard
@author: Eric Shaw
"""
from algorithms.algorithm import Algorithm
import board.Board


class AndOrGraphSearch(Algorithm):
    """
    This class handles the operations of the AND-OR graph search algorithm
    given a set of initial conditions for a board and which player
    (top or bottom).

    """
    def __init__(self, heuristic_id, plies, rows=2,
                 row_buckets=2, tile_pebbles=2):
        """
        Constructor

        @param heuristic_id: An int representing the heuristic and player
                     utilizing it. Constants for these are defined in
                     the Menu class in main.py. 2 and 4 are weighted,
                     3 and 5 are weightless.
        @param: plies
        @param: rows
        @param: row_buckets
        @param: tile_pebbles

        """
        super(AndOrGraphSearch, self).__init__(heuristic_id, plies, rows,
                                               row_buckets, tile_pebbles)

        self.board = board(rows, row_buckets, tile_pebbles)
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
