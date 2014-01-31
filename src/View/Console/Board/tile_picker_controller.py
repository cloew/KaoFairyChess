from tile_picker_screen import TilePickerScreen

from kao_console.ascii import ENDL
from kao_gui.console.console_controller import ConsoleController

from string import ascii_lowercase, digits

class TilePickerController(ConsoleController):
    """ Controller for picking a tile """
    
    def __init__(self, player, game):
        """ Initialize the Tile Picker Controller """
        screen = TilePickerScreen(player, game.board)
        commands = {}
        for character in digits:
            commands[character] = screen.tilePickerWidget.setRow
        
        for character in ascii_lowercase:
            commands[character] = screen.tilePickerWidget.setColumn
        ConsoleController.__init__(self, screen, commands=commands)