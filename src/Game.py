'''
Created on Nov 22, 2014

@author: Eric
'''

import Board as Board
import Player as Player
import AIPlayer as AIPlayer
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
        self.n = n
        self.k = k
        self.player1 = player1
        self.player2 = player2
        self.board = Board.Board(n, k)
        self.turn = 1
        
    def get_state(self):
        return self.board.get_state()
    
    def get_k(self):
        return self.k
    
    def get_n(self):
        return self.n
    
    def both_ai(self):
        return isinstance(self.player1, AIPlayer.AIPlayer) and isinstance(self.player2, AIPlayer.AIPlayer)
    
    def has_ai(self):
        return isinstance(self.player1, AIPlayer.AIPlayer) or isinstance(self.player2, AIPlayer.AIPlayer)
    
    def turn(self):
        return self.turn
    
    def update_turn(self):
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1
            
    def move(self, i, j):
        self.board.select_square(i, j)
        self.update_turn()
    
    def next_to_move(self):
        if self.turn == 1:
            return self.player1
        else:
            return self.player2
        
    def is_next_ai(self):
        self.board.select_square(0, 0)
        return isinstance(self.next_to_move(), AIPlayer.AIPlayer)
    
    def ai_move(self):
        #TODO get i and j from algorithm, and replace the next 4 lines
        if(self.turn == 2):
            i,j = 0,0
        else:
            i,j = 1,0
        self.board.select_square(i, j)
        self.update_turn()
    
    def valid_move(self, i, j):
        if self.turn == 1 and i == 1:
            return False
        if self.turn == 2 and i == 0:
            return False
        if self.board.get_state()[i][j] == 0:
            return False
        return True
    
    def winner(self):
        if self._all_zero(self.board.state[0]):
            return 1
        if self._all_zero(self.board.state[1]):
            return 2
        return 0
    
    def _all_zero(self, A):
        for x in A:
            if x != 0:
                return FALSE
        return True
            