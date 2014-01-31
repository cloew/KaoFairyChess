from tile_picker_screen import TilePickerScreen

from kao_console.ascii import ENDL
from kao_gui.console.console_controller import ConsoleController

from string import ascii_lowercase, digits

class TilePickerController(ConsoleController):
    """ Controller for picking a tile """
    
    def __init__(self, player, game):
        """ Initialize the Tile Picker Controller """
        self.board = game.board
        screen = TilePickerScreen(player, game.board)
        commands = {}
        for character in digits:
            commands[character] = screen.tilePickerWidget.setRow
        
        for character in ascii_lowercase:
            commands[character] = screen.tilePickerWidget.setColumn
        ConsoleController.__init__(self, screen, commands=commands)
        
    def getTile(self):
        """ Return the selected tile """
        row = self.getIndex(self.screen.rowText, digits)
        column = self.getIndex(self.screen.columnText, ascii_lowercase)
        
        if row is None or column is None:
            return None
        
        return self.board.getTileAt(row, column)
            
    def getIndex(self, text, listString):
        """ Return the index of text in the given list """
        if text in listString:
            return listString.index(text)
        else:
            return None