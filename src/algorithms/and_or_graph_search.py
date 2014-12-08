"""
Created on Dec 2, 2014

@author: Michael Pritchard
@author: Eric Shaw

"""
import math

from algorithms.algorithm import Algorithm
from board import Board
from src.node import Node


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

        self.board = Board(rows, row_buckets, tile_pebbles)
        self.game_tree = Node()

    def build_tree(self, node, depth, path=[]):
        child_values = []

        # Check for loops
        board = node.get_board()
        looping = str(board) in path

        if not looping and depth < self.plies and not board.is_game_over():
            # Add the current node to the path
            path.append(str(board))

            for child in board.get_possible_states(depth % 2):
                child_node = Node(child)
                node.add_child(child_node)
                child_values.append(self.build_tree(child_node, depth + 1,
                                                    path))
            node.set_value(math.ceil(sum([(1.0 / len(child_values)) * child
                                          for child in child_values])))
        else:
            node.set_value(self.heuristic.evaluate_board_state(node.get_board().get_state()))

        return node.get_value()

    def decide_move(self, board):
        """
        Determines the next move that the player should make.

        @return: a tuple with the coordinates of the next move.

        """
        self.game_tree = Node(board)
        self.build_tree(self.game_tree, 0)
        moves = [move for move in self.game_tree.get_board().legal_moves(self.player_row)]
        values = [node.get_value() for node in self.game_tree.get_children()]

        return moves[values.index((max(values)))]


