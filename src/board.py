"""
Created on Nov 22, 2014

@author: Eric Shaw
@author: Michael Pritchard
"""


class Board(object):
    """
    This class represents the 2 x n board, with k pebbles in each square.

    """
    def __init__(self, n, k, state=None):
        """
        Constructor
        @param n: The number of columns in each of the 2 rows.
        @param k: The number of pebbles in each square.

        """
        if not isinstance(n, int):
            raise ValueError("Expected int param n, for 2 x n board.")
        if not isinstance(k, int):
            raise ValueError("Expected int param k for number of pebbles per square.")
        self.n = n
        self.k = k
        self.state = state if state is not None else self.get_initial_state()

    def __str__(self):
        """
        Returns a string representation of the object.
        @return a string representation of the object.
        """
        ret = ''
        for x in self.state[0]:
            ret = ret + str(x)
        for x in self.state[1]:
            ret = ret + str(x)
        return ret

    def get_state(self):
        """
        Returns the 2 x n board as an array of arrays.

        @return: The board as a 2 x n array of integers.

        """
        return self.state

    def reset(self):
        """ Sets the board to its initial configuration. """
        self.state = self.get_initial_state()

    def get_initial_state(self):
        """
        Returns the initial configuration of the board as a 2 x n array of ints.

        @return: The initial configuration.

        """
        return [[self.k for x in range(self.n)] for x in range(2)]

    def select_square(self, i, j):
        """
        Selects the square at location i,j for a turn, redistributing pebbles.

        @param i: The i coordinate of the square.
        @param j: The j coordinate of the square.

        """
        if not isinstance(i, int) or not isinstance(j, int):
            raise ValueError("Expected int params i and j, indices of the position on the board.")
        num = self.get_item(i, j)
        newState = self.state_copy()
        newBoard = Board(self.n, self.k, newState)
        newBoard.set_item(i, j, 0)
        i, j = newBoard._rotate_cw(i, j)
        while num > 0:
            newBoard.set_item(i, j, newBoard.get_item(i, j) + 1)
            num = num - 1
            i, j = newBoard._rotate_cw(i, j)
        return newBoard

    def set_item(self, i, j, val):
        self.state[i][j] = val

    def _rotate_ccw(self, i, j):
        """
        Given coordinates, returns next coordinate in a counter-clockwise direction.
        @return: The next coordinates in a counter-clockwise direction.
        """
        if i == 0 and j == 0:
            i = 1
        elif i == 1 and j == self.n - 1:
            i = 0
        elif i == 0:
            j = j - 1
        else:
            j = j + 1
        return i, j

    def _rotate_cw(self, i, j):
        """
        Given coordinates, returns next coordinate in a clockwise direction.
        @return: The next coordinates in a clockwise direction.
        """
        if i == 0 and j == self.n - 1:
            i = 1
        elif i == 1 and j == 0:
            i = 0
        elif i == 0:
            j = j + 1
        else:
            j = j - 1
        return i, j

    def get_item(self, i, j):
        """
        Gets the number of pebbles in square a coordinate i,j.
        @return: The number of pebbles in square a coordinate i,j.
        """
        if not isinstance(i, int) or not isinstance(j, int):
            raise ValueError("Expected int params i and j, indices of the position on the board.")
        return self.state[i][j]

    def is_game_over(self):
        """
        Determines if the board is in a win state.
        @return: True if a player has won, False otherwise.
        """
        return sum(self.state[0]) == 0 or sum(self.state[1]) == 0

    def sum(self, array):
        """
        Gets the sum of all ints in an int array.
        @return: The sum of all ints in the array.
        """
        total = 0
        for x in array:
            total = total + x
        return total

    def legal_moves(self, row):
        """
        Returns a list of all legal moves as (i,j) tuples.
        @param row: The row for which the list of legal moves is requested.
        @return: A list of all legal moves as (i, j) tuples. 
        """
        moves = []
        for j in range(self.n):
            if not self.state[row][j] == 0:
                moves.append((row, j))
        return moves

    def state_copy(self):
        """
        Makes a copy of the 2 x n state array.
        @return a copy of the 2 x n state array.
        """
        list1 = []
        list2 = []
        for x in self.state[0]:
            list1.append(x)
        for x in self.state[1]:
            list2.append(x)
        ret = []
        ret.append(list1)
        ret.append(list2)
        return ret

    def get_possible_states(self, row):
        """
        Gets all possible next states given a row.
        @param row: the row number for which the possible states list is requested. 
        @return the list of all possible next states for the row.
        """
        states = []
        moves = self.legal_moves(row)
        for move in moves:
            states.append(self.select_square(move[0], move[1]))
        return states
