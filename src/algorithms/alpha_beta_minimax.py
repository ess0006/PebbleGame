"""
Created on Dec 2, 2014

@author: Michael Pritchard
@author: Eric Shaw

"""
from algorithms.algorithm import Algorithm


class AlphaBetaMinimax(Algorithm):
    """
    Handles the execution of the Alpha-Beta MINIMAX algorithm.

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
        super(AlphaBetaMinimax, self).__init__(heuristic_id, plies, rows,
                                               row_buckets, tile_pebbles)
        self.transposition_table = {}

    def alpha_beta_search(self, board):
        path = [str(board)]
        value = -10000000
        alpha = -1000000
        beta = 1000000
        action = None

        moves = [move for move in board.legal_moves(self.player_row)]
        states = [state for state in board.get_possible_states(self.player_row)]

        if self.player_row:
            moves.reverse()
            states.reverse()

        for state, move in zip(states, moves):
            new_value = self.min(state, alpha, beta, 1, path)
            if new_value > value:
                value = new_value
                action = move
            if value >= beta:
                return action
            elif value > alpha:
                alpha = value

        return action

    def min(self, board, alpha, beta, depth, path):
        # Check for loops
        looping = str(board) in path

        value = 1000000

        # Perform the terminal test  (depth, looping, win/loss conditions)
        if not looping and depth < self.plies and not board.is_game_over():
            # Add the board state to the path
            path.append(str(board))

            states = [state for state in board.get_possible_states(depth % 2)]
            if not (depth + self.player_row) % 2:
                states.reverse()
            for state in states:
                if str(state) in self.transposition_table:
                    new_value = self.transposition_table[str(state)]
                else:
                    new_value = self.max(state, alpha, beta, depth + 1, path)
                    self.transposition_table[str(state)] = new_value
                if new_value < value:
                    value = new_value
                if value <= alpha:
                    return value
                elif value < beta:
                    beta = value
        # If the terminal test fails, return the heuristic evaluation
        else:
            return self.heuristic.evaluate_board_state(board.get_state())

        return value

    def max(self, board, alpha, beta, depth, path):
        # Check for loops
        looping = str(board) in path

        value = -10000000

        # Perform the terminal test (depth, looping, win/loss conditions)
        if not looping and depth < self.plies and not board.is_game_over():
            # Add the board state to the path
            path.append(str(board))

            states = [state for state in board.get_possible_states(depth % 2)]
            if not (depth + self.player_row) % 2:
                states.reverse()
            for state in states:
                if str(state) in self.transposition_table:
                    new_value = self.transposition_table[str(state)]
                else:
                    new_value = self.min(state, alpha, beta, depth + 1, path)
                    self.transposition_table[str(state)] = new_value
                if new_value > value:
                    value = new_value
                if value >= beta:
                    return value
                elif value > alpha:
                    alpha = value
        # If the terminal test fails, return the heuristic evaluation
        else:
            return self.heuristic.evaluate_board_state(board.get_state())

        return value

    def decide_move(self, board):
        self.transposition_table = {}
        return self.alpha_beta_search(board)
