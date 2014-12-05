'''
Created on Nov 24, 2014

@author: Eric
'''
import unittest
import src.game as Game
import src.players.human as HumanPlayer

class GameTest(unittest.TestCase):
    '''
    This class tests the Game class.
    '''

    def test_get_n(self):
        player1 = HumanPlayer.HumanPlayer()
        player2 = HumanPlayer.HumanPlayer()
        game = Game.Game(player1, player2, 3, 7)
        n = game.get_n()
        self.assertEqual(n, 3, "Wrong n value.")
    
    def test_get_k(self):
        player1 = HumanPlayer.HumanPlayer()
        player2 = HumanPlayer.HumanPlayer()
        game = Game.Game(player1, player2, 3, 7)
        k = game.get_k()
        self.assertEqual(k, 7, "Wrong n value.")
        
    def test_get_state(self):
        player1 = HumanPlayer.HumanPlayer()
        player2 = HumanPlayer.HumanPlayer()
        game = Game.Game(player1, player2, 3, 7)
        expected1 = []
        expected1.append(7)
        expected1.append(7)
        expected1.append(7)
        expected2 = []
        expected2.append(7)
        expected2.append(7)
        expected2.append(7)
        state = game.get_state()
        self.assertSequenceEqual(state[0], expected1, "Error in select_square")
        self.assertSequenceEqual(state[1], expected2, "Error in select_square")
        pass
    
    def test_both_ai(self):
        player1 = HumanPlayer.HumanPlayer()
        player2 = HumanPlayer.HumanPlayer()
        game = Game.Game(player1, player2, 3, 7)
        self.assertFalse(game.both_ai(), "Both players are human, should return False.")
        pass
    
    def test_has_ai(self):
        player1 = HumanPlayer.HumanPlayer()
        player2 = HumanPlayer.HumanPlayer()
        game = Game.Game(player1, player2, 3, 7)
        self.assertFalse(game.has_ai(), "Both players are human, should return False.")
        pass
    
    def test_get_turn(self):
        player1 = HumanPlayer.HumanPlayer()
        player2 = HumanPlayer.HumanPlayer()
        game = Game.Game(player1, player2, 3, 7)
        self.assertEquals(game.get_turn(), 1, "Turn should be 1 originally.")
        pass
    
    def test_update_turn(self):
        player1 = HumanPlayer.HumanPlayer()
        player2 = HumanPlayer.HumanPlayer()
        game = Game.Game(player1, player2, 3, 7)
        game.update_turn()
        self.assertEquals(game.get_turn(), 2, "Turn should be 2 after one move.")
        pass
    
    def test_move(self):
        player1 = HumanPlayer.HumanPlayer()
        player2 = HumanPlayer.HumanPlayer()
        game = Game.Game(player1, player2, 3, 7)
        game.move(0, 0)
        expected1 = []
        expected1.append(1)
        expected1.append(9)
        expected1.append(8)
        expected2 = []
        expected2.append(8)
        expected2.append(8)
        expected2.append(8)
        state = game.get_state()
        self.assertSequenceEqual(state[0], expected1, "Error in move")
        self.assertSequenceEqual(state[1], expected2, "Error in move")
        pass
    
    def test_next_to_move(self):
        player1 = HumanPlayer.HumanPlayer()
        player2 = HumanPlayer.HumanPlayer()
        game = Game.Game(player1, player2, 3, 7)
        self.assertEquals(game.next_to_move(), player1, "Turn should be player1.")
        pass
    
    def test_is_next_ai(self):
        player1 = HumanPlayer.HumanPlayer()
        player2 = HumanPlayer.HumanPlayer()
        game = Game.Game(player1, player2, 3, 7)
        self.assertFalse(game.is_next_ai(), "Both players are human, should return False.")
        pass
    
    def test_valid_move(self):
        player1 = HumanPlayer.HumanPlayer()
        player2 = HumanPlayer.HumanPlayer()
        game = Game.Game(player1, player2, 3, 7)
        self.assertTrue(game.valid_move(0, 1), "Error in valid_move.")
        self.assertFalse(game.valid_move(1, 1), "Error in valid_move.")
        pass
    
    def test_winner(self):
        player1 = HumanPlayer.HumanPlayer()
        player2 = HumanPlayer.HumanPlayer()
        game = Game.Game(player1, player2, 3, 7)
        self.assertEquals(game.winner(), 0, "There should be no winner currently.")
        pass
    
    def test_all_zero(self):
        player1 = HumanPlayer.HumanPlayer()
        player2 = HumanPlayer.HumanPlayer()
        game = Game.Game(player1, player2, 3, 7)
        A = []
        A.append(0)
        A.append(0)
        A.append(0)
        self.assertTrue(game._all_zero(A), "_all_zero should return true if all elements are zero.")
        pass
    
    #TODO rework logic based on heuristics
    def test_ai_move(self):
        player1 = HumanPlayer.HumanPlayer()
        player2 = HumanPlayer.HumanPlayer()
        game = Game.Game(player1, player2, 3, 7)
        game.ai_move()
        expected1 = []
        expected1.append(1)
        expected1.append(9)
        expected1.append(8)
        expected2 = []
        expected2.append(8)
        expected2.append(8)
        expected2.append(8)
        state = game.get_state()
        self.assertSequenceEqual(state[0], expected1, "Error in ai_move")
        self.assertSequenceEqual(state[1], expected2, "Error in ai_move")
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()