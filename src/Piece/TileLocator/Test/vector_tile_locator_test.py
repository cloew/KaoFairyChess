from Board.board import Board
from Board.tile import Tile
from Piece.TileLocator.vector_tile_locator import VectorTileLocator

import unittest

class locateTiles(unittest.TestCase):
    """ Test cases of locateTiles """
    
    def  setUp(self):
        """ Build the Board and Tile Locator for the test """
        self.board = Board()
        self.vector = (1, 0)
        self.tileLocator = VectorTileLocator(self.vector)
        
    def validLocation(self):
        """ Test that a valid location is returned properly """
        coord = (0, 0)
        tile = Tile(None, coord[0], coord[1])
        tiles = self.tileLocator.locateTiles(tile, self.board)
        
        assert len(tiles) == 1, "Should have a single tile"
        assert tiles[0].row == coord[0] + self.vector[0], "The returned tile should be off by the vector given"
        assert tiles[0].column == coord[1] + self.vector[1], "The returned tile should be off by the vector given"
        
    def invalidLocation(self):
        """ Test that a invalid location is returned properly """
        coord = (self.board.last_row, self.board.last_col)
        tile = Tile(None, coord[0], coord[1])
        tiles = self.tileLocator.locateTiles(tile, self.board)
        
        assert len(tiles) == 0, "Should have no tiles"

# Collect all test cases in this class
testcasesLocateTiles = ["validLocation", "invalidLocation"]
suiteLocateTiles = unittest.TestSuite(map(locateTiles, testcasesLocateTiles))

##########################################################

# Collect all test cases in this file
suites = [suiteLocateTiles]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)