from Game.Player.player import Player

from Game.Player.Preparation.black_player_preparer import BlackPlayerPreparer
from Game.Player.Preparation.white_player_preparer import WhitePlayerPreparer

class GameType:
    """ Represents a Chess Game Type """
    
    def __init__(self):
        """ Initialize the Game Type """
        self.playerPreparers = [WhitePlayerPreparer(), BlackPlayerPreparer()]
        
    def getPlayersForGame(self, board):
        """ Return all the players for use in the game """
        players = []
        for preparer in self.playerPreparers:
            player = Player()
            preparer.prepare(player, board)
            players.append(player)
        
        return players
        
    @property
    def numberOfPlayers(self):
        """ Return the Number of Players this game type supports """
        return len(self.playerPreparers)