"""
Created on Nov 22, 2014

@author: Eric
"""
import board as Board

from players.ai import AI
from players.player import Player


class Game(object):
    """
    This class manages the playing of the pebble game.
    """
    def __init__(self, player1, player2, n, k):
        """
        Constructor
        @param player1: The first player.
        @param player2: The second player.
        @param n: The number of columns in each row.
        @param k: The number of pebbles in each square.
        """
        if not isinstance(player1, Player) or not isinstance(player2, Player):
            raise ValueError("Players should be passed as parameters")
        self.n = n
        self.k = k
        self.player1 = player1
        self.player2 = player2
        self.board = Board.Board(n, k)
        self.turn = 1

    def get_state(self):
        """
        Gets the state of the board.
        @return: A 2 x n array of ints representing the state.
        """
        return self.board.get_state()

    def get_k(self):
        """
        Returns the original number of pebbles per square.
        @return: The original number of pebbles per square. 
        """
        return self.k

    def get_n(self):
        """
        Returns the number of columns per row.
        @return: The number of columns per row.
        """
        return self.n

    def both_ai(self):
        """
        Determines if both players are computers.
        @return: True if both players are AI players, False otherwise.
        """
        return isinstance(self.player1, AI) and isinstance(self.player2, AI)

    def has_ai(self):
        """
        Determines if one player is a computer.
        @return: True if either player is a computer, False if both are human players.
        """
        return isinstance(self.player1, AI) or isinstance(self.player2, AI)

    def get_turn(self):
        """
        Returns an int representing the next player to move.
        @return: An int representing the next player to move.
        """
        return self.turn

    def update_turn(self):
        """
        Advances to the next turn.
        """
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1

    def move(self, i, j):
        """
        Selects square with coordinates i,j for a move.
        @param i: The i coordinate for the move.
        @param j: The j coordinate for the move.  
        """
        self.board = self.board.select_square(i, j)
        self.update_turn()

    def next_to_move(self):
        """
        Returns the next player to move.
        @return: The next player to move.
        """
        if self.turn == 1:
            return self.player1
        else:
            return self.player2

    def is_next_ai(self):
        """
        Determines if the next player to move is an AI player.
        @return: True if the next player to move is an AI player, False otherwise.
        """
        return isinstance(self.next_to_move(), AI)

    def ai_move(self):
        """
        Determines and makes a move based on heuristic.
        """
        if self.turn == 1 and isinstance(self.player1, AI):
            move = self.player1.request_move(self.board)
        elif self.turn == 2 and isinstance(self.player2, AI):
            move = self.player2.request_move(self.board)
        else:
            raise RuntimeError("game.Game: The AI didn't make a move!")

        self.board.select_square(move[0], move[1])
        self.update_turn()

    def valid_move(self, i, j):
        """
        Determines if a given move is valid.
        @param i: The i coordinate for the move.
        @param j: The j coordinate for the move.
        @return: True if move is valid, False otherwise. 
        """
        if self.turn == 1 and i == 1:
            return False
        if self.turn == 2 and i == 0:
            return False
        if self.board.get_state()[i][j] == 0:
            return False
        return True

    def winner(self):
        """
        Returns an int representing the winner of the game, or 0 if game is not over.
        @return: An int representing the winner of the game, or 0 if game is not over. 
        """
        if self._all_zero(self.board.state[0]):
            return 1
        if self._all_zero(self.board.state[1]):
            return 2
        return 0

    def _all_zero(self, A):
        """
        Determines if an array is all zero values.  Required for a win.
        @return: True if the array has only zero values, False otherwise.
        """
        for x in A:
            if x != 0:
                return False
        return True

