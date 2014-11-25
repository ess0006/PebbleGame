'''
Created on Nov 22, 2014

@author: Eric Shaw
@author: Michael Pritchard
'''

class Board(object):
    '''
    This class represents the 2 x k board.
    '''

    def __init__(self, n, k):
        '''
        Constructor
        @param n: The number of columns in each of the 2 rows.
        @param k: The number of pebbles in each square. 
        '''
        if not isinstance(n, int):
            raise ValueError("Expected int param n, for 2 x n board.")
        if not isinstance(k, int):
            raise ValueError("Expected int param k for number of pebbles per square.")
        self.n = n
        self.k = k
        self.state = self.get_initial_state()
    
    def get_state(self):
        '''
        Returns the 2 x n board as an array of arrays.
        @return: The board as a 2 x n array of integers.
        '''
        return self.state
    
    def reset(self):
        '''
        Sets the board to its initial configuration.
        '''
        self.state = self.get_initial_state() 
        
    def get_initial_state(self):
        '''
        Returns the initial configuration of the board as a 2 x n array of ints.
        @return: The initial configuration.
        '''
        return [[self.k for x in range(self.n)] for x in range(2)] 
    
    def select_square(self, i, j):
        '''
        Selects the square at location i,j for a turn, redistributing pebbles.
        @param i: The i coordinate of the square.
        @param j: The j coordinate of the square.  
        '''
        if not isinstance(i, int) or not isinstance(j, int):
            raise ValueError("Expected int params i and j, indices of the position on the board.")
        num = self.get_item(i, j)
        self.state[i][j] = 0
        i, j = self._rotate_cw(i, j)
        while num > 0:
            self.state[i][j] = self.state[i][j] + 1
            num = num - 1
            i, j = self._rotate_cw(i, j)
    
    def _rotate_ccw(self, i, j):
        '''
        Given coordinates, returns next coordinate in a counter-clockwise direction.
        @return: The next coordinates in a counter-clockwise direction.
        '''
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
        '''
        Given coordinates, returns next coordinate in a clockwise direction.
        @return: The next coordinates in a clockwise direction.
        '''
        if i == 0 and j == self.n-1:
            i = 1
        elif i == 1 and j == 0:
            i = 0
        elif i == 0:
            j = j + 1
        else:
            j = j - 1
        return i, j
    
    def get_item(self, i, j):
        '''
        Gets the number of pebbles in square a coordinate i,j.
        @return: The number of pebbles in square a coordinate i,j.
        '''
        if not isinstance(i, int) or not isinstance(j, int):
            raise ValueError("Expected int params i and j, indices of the position on the board.")
        return self.state[i][j]
    
    def is_game_over(self):
        '''
        Determines if the board is in a win state.
        @return: True if a player has won, False otherwise.
        '''
        return sum(self.state[0]) == 0 or sum(self.state[1]) == 0
    
    def sum(self, array):
        '''
        Gets the sum of all ints in an int array.
        @return: The sum of all ints in the array.
        '''
        total = 0
        for x in array:
            total = total + x
        return total