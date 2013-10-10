from piece_color import WHITE, BLACK
from Board.board import Board

import unittest

class getColorForSquare(unittest.TestCase):
    """ Test cases of getColorForSquare """
    
    def  setUp(self):
        """ Build the Board for the test """
        self.board = Board()
        
    def oddRowOddColumn(self):
        """ Test that an odd row and column has the proper color """
        assert self.board.getColorForSquare(1,1) == BLACK, "Tile should be black"
        assert self.board.getColorForSquare(3,3) == BLACK, "Tile should be black"
        
    def oddRowEvenColumn(self):
        """ Test that an odd row and even column has the proper color """
        assert self.board.getColorForSquare(1,2) == WHITE, "Tile should be white"
        assert self.board.getColorForSquare(3,4) == WHITE, "Tile should be white"
        
    def evenRowOddColumn(self):
        """ Test that an even row and column has the proper color """
        assert self.board.getColorForSquare(0,1) == WHITE, "Tile should be white"
        assert self.board.getColorForSquare(2,3) == WHITE, "Tile should be white"
        
    def evenRowEvenColumn(self):
        """ Test that an even row and even column has the proper color """
        assert self.board.getColorForSquare(0,2) == BLACK, "Tile should be black"
        assert self.board.getColorForSquare(4,4) == BLACK, "Tile should be black"

# Collect all test cases in this class
testcasesGetColorForSquare = ["oddRowOddColumn", "oddRowEvenColumn", "evenRowOddColumn", "evenRowEvenColumn"]
suiteGetColorForSquare = unittest.TestSuite(map(getColorForSquare, testcasesGetColorForSquare))

##########################################################

# Collect all test cases in this file
suites = [suiteGetColorForSquare]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)