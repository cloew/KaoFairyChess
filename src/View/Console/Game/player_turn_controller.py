from View.Console.Game.player_turn_screen import PlayerTurnScreen

from kao_console.ascii import ENDL
from kao_gui.console.console_controller import ConsoleController

class PlayerTurnController(ConsoleController):
    """ Controller for a Player Turn """
    
    def __init__(self, player, game):
        """ Initialize the Player Turn Controller """
        screen = PlayerTurnScreen()
        ConsoleController.__init__(self, screen)