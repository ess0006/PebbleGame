'''
Created on Nov 22, 2014

@author: Eric
'''
import unittest
import src.board as Board

class Test(unittest.TestCase):


    def test_board_size(self):
        board = Board.Board(3, 5)
        state = board.get_state()
        self.assertEqual(2, len(state), "Board should be 2 x n")
        self.assertEqual(3, len(state[0]), "Board should be 2 x n")
        self.assertEqual(3, len(state[1]), "Board should be 2 x n")

    def test_intial_board_state(self):
        board = Board.Board(3, 5)
        state = board.get_state()
        expected = []
        expected.append(5)
        expected.append(5)
        expected.append(5)
        self.assertSequenceEqual(state[0], expected, "Board should be initialized to 2 x n array with value k")
        self.assertSequenceEqual(state[1], expected, "Board should be initialized to 2 x n array with value k")
        
    def test_get_item(self):
        board = Board.Board(3, 5)
        self.assertEqual(board.get_item(0, 0), 5, "Error in get_item method")
        
    def test_select_square(self):
        board = Board.Board(3, 5)
        newBoard = board.select_square(0, 2)
        expected1 = []
        expected1.append(6)
        expected1.append(6)
        expected1.append(0)
        expected2 = []
        expected2.append(6)
        expected2.append(6)
        expected2.append(6)
        state = newBoard.get_state()
        self.assertEqual(state[0], expected1, "Error in select_square")
        self.assertEqual(state[1], expected2, "Error in select_square")
        
    def test_str(self):
        board = Board.Board(3, 5)
        self.assertEqual('555555', str(board), "Error in __str__")
        
    def test_legal_moves(self):
        board = Board.Board(3, 5)
        moves = board.legal_moves(1)
        self.assertEqual(moves[0], (0,0), "Error in select_square")
        self.assertEqual(moves[1], (0,1), "Error in select_square")
        self.assertEqual(moves[2], (0,2), "Error in select_square")
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()