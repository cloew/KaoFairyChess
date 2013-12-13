from piece_color import WHITE, BLACK
from Game.Player.Preparation.player_preparer import PlayerPreparer

class BlackPlayerPreparer(PlayerPreparer):
    """ Represents the Preparer for the Black Player in a standard Game of Chess """
    
    def __init__(self):
        """ Initialize the Player Preparer """
        self.color = BLACK
    
    def prepare(self, player, board):
        """ Prepare the given player with the given board """
        for column in range(board.size):
            pawn = self.getPieceOnBoard(board, board.last_row-1, column, 'P')
            player.piecesOnBoard.append(pawn)