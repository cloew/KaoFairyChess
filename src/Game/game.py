from Board.board import Board
from Game.Type.game_type import GameType

class Game:
    """ Represents a Game of Chess """
    
    def __init__(self):
        """ Initialize the Game """
        self.over = False
        self.board = Board()
        gameType = GameType()
        self.players = gameType.getPlayersForGame(self.board)