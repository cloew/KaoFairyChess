from Board.piece_on_board import PieceOnBoard
from Piece.piece import Piece

class PlayerPreparer:
    """ Prepares a Player for a game of chess """
    
    def __init__(self):
        """ Initialize the Player Preparer """
        self.color = None
        
    def prepare(self, player, board):
        """ Prepare the given player with the given board """
        
    def getPiece(self, symbol):
        """ Get the requested Piece in the appropriate color for the Player Preparer """
        return Piece(symbol, self.color)
        
    def getPieceOnBoard(self, board, row, column, pieceSymbol):
        """ Return a new Piece on the Board """
        piece = self.getPiece(pieceSymbol)
        tile = board[row][column]
        return PieceOnBoard(piece, tile)