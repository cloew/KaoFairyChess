from View.Console.Game.player_turn_screen import PlayerTurnScreen

from kao_console.ascii import ENDL
from kao_gui.console.console_controller import ConsoleController

from string import ascii_lowercase, digits

class PlayerTurnController(ConsoleController):
    """ Controller for a Player Turn """
    
    def __init__(self, player, game):
        """ Initialize the Player Turn Controller """
        screen = PlayerTurnScreen(player, game.board)
        commands = {}
        for character in digits:
            commands[character] = screen.tilePickerWidget.setRow
        
        for character in ascii_lowercase:
            commands[character] = screen.tilePickerWidget.setColumn
        
        ConsoleController.__init__(self, screen, commands=commands)