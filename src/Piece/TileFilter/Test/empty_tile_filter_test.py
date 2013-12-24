from Piece.TileFilter.empty_tile_filter import EmptyTileFilter

from Test.test_helper import BuildTile
import unittest

class filter(unittest.TestCase):
    """ Test cases of filter """
    
    def  setUp(self):
        """ Build the Filter and tiles for the test """
        self.filter = EmptyTileFilter()
    
    def piece(self):
        """ Test that a tile with no piece is returned """
        tile = BuildTile()
        tile.piece = 'Something'
        
        filteredTiles = self.filter.filter([tile])
        
        assert len(filteredTiles) == 0, "Should have filtered out an occupied tile"
    
    def noPiece(self):
        """ Test that a tile with no piece is returned """
        tile = BuildTile()
        tile.piece = None
        
        filteredTiles = self.filter.filter([tile])
        
        assert len(filteredTiles) == 1, "Should have kept an empty tile"
        assert filteredTiles[0] is tile, "Should have the tile provided to the filter"

# Collect all test cases in this class
testcasesFilter = ["piece", "noPiece"]
suiteFilter = unittest.TestSuite(map(filter, testcasesFilter))

##########################################################

# Collect all test cases in this file
suites = [suiteFilter]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)