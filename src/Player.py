'''
Created on Nov 22, 2014

@author: Eric Shaw
@author: Michael Pritchard
'''

import abc

class Player(object):
    '''
    This class represents a player of the pebble game.
    '''
    

    def __init__(self):
        '''
        Constructor
        '''
        
    
    def request_move(self, board):
        """ A player will call this method when moving. 
            It will call a particular algorithm to find the optimal move. """
        return 0,0