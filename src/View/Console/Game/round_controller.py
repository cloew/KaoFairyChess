from View.Console.Game.player_turn_controller import PlayerTurnController
from View.Console.Game.round_screen import RoundScreen

from kao_console.ascii import ENDL
from kao_gui.console.console_controller import ConsoleController

class RoundController(ConsoleController):
    """ Controller for running a Round of the Game """
    
    def __init__(self, game):
        """ Initialize the Round Controller """
        self.game = game
        screen = RoundScreen()
        ConsoleController.__init__(self, screen, commands={ENDL:self.performATurn})
        
        self.performPlayerTurn = self.performPlayerTurn()
        self.performPlayerTurn.next()
        
    def performATurn(self, event):
        """ Perform a single Player's Turn """
        self.performPlayerTurn.next()
        
    def performPlayerTurn(self):
        """ Perfrom a player's turn """
        i = 0
        while True:
            for player in self.game.players:
                self.screen.currentPlayer = player
                yield
                self.runPlayerTurn(player)
                
                if self.game.over:
                    self.stopRunning()
                i += 1
                
    def runPlayerTurn(self, player):
        """ Run the Player's Turn """
        self.runController(PlayerTurnController(player, self.game))