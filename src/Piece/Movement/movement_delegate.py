
class MovementDelegate:
    """ Movement delegate for a Piece """
    
    def __init__(self, locator, filters):
        """ Initialize the Movement Delegate with its Tile Locator and Filters """
        self.locator = locator
        self.filters = filters
        
    def possibleLocations(self, startingTile, board):
        """ Return the possible locations """
        tiles = self.locator.locateTiles(startingTile, board)
        
        for filter in self.filters:
            tiles = filter.filter(tiles)
        return tiles