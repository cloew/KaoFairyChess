from Piece.TileLocator.tile_locator import TileLocator

class VectorTileLocator(TileLocator):
    """ Locates tile sbased on a provided vector """
    
    def __init__(self, vector):
        """ Initialize the Tile Locator with the vector it should collect tiles from """
        self.vector = vector
        
    def locateTiles(self, startingTile, board):
        """ Locate and return all potential tiles based on the location algorithm """
        row = startingTile.row + self.vector[0]
        column = startingTile.column + self.vector[1]
        
        newTile = board.getTileAt(row, column)
        
        if newTile is None:
            return []
        else:
            return [newTile]