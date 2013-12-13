from Board.board import Board
from Game.game_type import GameType

class Game:
    """ Represents a Game of Chess """
    
    def __init__(self):
        """ Initialize the Game """
        self.board = Board()
        gameType = GameType()
        self.players = gameType.getPlayersForGame(self.board)