
class PieceOnBoard:
    """ Represents a Piece on the Board """
    
    def __init__(self, piece, tile):
        """ Initialize the Piece on the Board """
        self.piece = piece
        self.tile = tile
        self.tile.piece = self.piece