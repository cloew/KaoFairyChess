from Game.Player.player_preparer import PlayerPreparer

class BlackPlayerPreparer(PlayerPreparer):
    """ Represents the Preparer for the Black Player in a standard Game of Chess """
    
    def prepare(self, player, board):
        """ Prepare the given player with the given board """