'''
Created on Nov 22, 2014

@author: Eric Shaw
@author: Michael Pritchard
'''

class Board(object):
    '''
    classdocs
    '''

    def __init__(self, n, k):
        '''
        Constructor
        '''
        if not isinstance(n, int):
            raise ValueError("Expected int param n, for 2 x n board.")
        if not isinstance(k, int):
            raise ValueError("Expected int param k for number of pebbles per square.")
        self.n = n
        self.k = k
        self.state = self.get_initial_state()
    
    def get_state(self):
        return self.state
    
    def reset(self):
        self.state = self.get_initial_state() 
        
    def get_initial_state(self):
        return [[self.k for x in range(self.n)] for x in range(2)] 
    
    def select_square(self, i, j):
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
        if not isinstance(i, int) or not isinstance(j, int):
            raise ValueError("Expected int params i and j, indices of the position on the board.")
        return self.state[i][j]
    
    def is_game_over(self):
        return sum(self.state[0]) == 0 or sum(self.state[1]) == 0
    
    def sum(self, array):
        total = 0
        for x in array:
            total = total + x
        return total