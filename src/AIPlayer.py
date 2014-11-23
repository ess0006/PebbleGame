'''
Created on Nov 22, 2014

@author: Eric
'''
import Player as Player
import Algorithm as Algorithm

class AIPlayer(Player.Player):
    '''
    classdocs
    '''
    

    def __init__(self):
        '''
        Constructor
        '''
        self.algorithm = Algorithm.Algorithm()
    
    def request_move(self, board):
        return self.algorithm.decide_move(board) #GUI will get move