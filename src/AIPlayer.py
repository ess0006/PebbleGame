'''
Created on Nov 22, 2014

@author: Eric Shaw
@author: Michael Pritchard
'''
import Player as Player
import algorithm as Algorithm

class AIPlayer(Player.Player):
    '''
    This class represents a computer player.
    '''
    

    def __init__(self, heuristic):
        '''
        Constructor
        '''
        self.algorithm = Algorithm.algorithm(heuristic)
    
    def request_move(self, board):
        '''
        The algorithm and heuristic determine the move.
        @return: The i,j coordinates of the move.
        '''
        return self.algorithm.decide_move(board) #GUI will get move