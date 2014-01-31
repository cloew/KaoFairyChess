from Board.board import Board
from Board.tile_picker import TilePicker

import unittest

class getTile(unittest.TestCase):
    """ Test cases of getTile """
    
    def  setUp(self):
        """ Build the Tile Picker for the test """
        board = Board()
        self.tilePicker = TilePicker(board)
        
    def tileFound(self):
        """ Test that a tile can be found """
        self.tilePicker.row = 1
        self.tilePicker.column = 1
        
        expectedTile = self.tilePicker.board.getTileAt(self.tilePicker.row, self.tilePicker.column)
        actualTile = self.tilePicker.getTile()
        
        assert expectedTile is actualTile, 'Should receive the tile at the given coordinate'
        
    def noRow(self):
        """ Test that a bad row causes no tile to be found """
        self.tilePicker.row = None
        self.tilePicker.column = 1
        
        tile = self.tilePicker.getTile()
        
        assert tile is None, 'The tile should be None when there is no row'
        
    def noColumn(self):
        """ Test that a bad column causes no tile to be found """
        self.tilePicker.row = 1
        self.tilePicker.column = None
        
        tile = self.tilePicker.getTile()
        
        assert tile is None, 'The tile should be None when there is no column'

# Collect all test cases in this class
testcasesFunctionToTest = ["tileFound", "noRow", "noColumn"]
suiteFunctionToTest = unittest.TestSuite(map(getTile, testcasesFunctionToTest))

##########################################################

# Collect all test cases in this file
suites = [suiteFunctionToTest]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)