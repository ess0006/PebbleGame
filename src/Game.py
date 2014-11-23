'''
Created on Nov 22, 2014

@author: Eric
'''

import Board as Board
import Player as Player
import Tkinter
from Tkinter import *

class Game(object):
    '''
    classdocs
    '''


    def __init__(self, player1, player2, n, k):
        '''
        Constructor
        '''
        if not isinstance(player1, Player.Player) or not isinstance(player2, Player.Player):
            raise ValueError("Players should be passed as parameters")
        self.player1 = player1
        self.player2 = player2
        self.board = Board.Board(n, k)
        
    def get_state(self):
        return self.board.get_state()
