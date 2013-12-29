from Piece.Movement.movement_delegate import MovementDelegate
from Piece.TileFilter.empty_tile_filter import EmptyTileFilter
from Piece.TileLocator.vector_tile_locator import VectorTileLocator

class Piece:
    """ Represents a chess piece """
    
    def __init__(self, symbol, color):
        """ Initialize the piece """
        self.symbol = symbol
        self.color = color
        locator = VectorTileLocator((1, 0))
        filter = EmptyTileFilter()
        self.movementDelegate = MovementDelegate(locator, [filter]) # Eventually this will get passed in
        
    def __repr__(self):
        """ Return the String Representation of the piece """
        return str(self.symbol)