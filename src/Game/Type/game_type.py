
class GameType:
    """ Represents a Chess Game Type """
    
    def __init__(self):
        """ Initialize the Game Type """
        self.playerPreparers = []
        
    @property
    def numberOfPlayers(self):
        """ Return the Number of Players this game type supports """
        return len(self.playerPreparers)