from piece_color import WHITE, BLACK
from Game.Player.Preparation.player_preparer import PlayerPreparer

class WhitePlayerPreparer(PlayerPreparer):
    """ Represents the Preparer for the White Player in a standard Game of Chess """
    
    def __init__(self):
        """ Initialize the Player Preparer """
        self.color = WHITE
    
    def prepare(self, player, board):
        """ Prepare the given player with the given board """
        for column in range(board.size):
            pawn = self.getPieceOnBoard(board, 1, column, 'P')
            player.piecesOnBoard.append(pawn)