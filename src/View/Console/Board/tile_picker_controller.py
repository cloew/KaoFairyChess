from tile_picker_screen import TilePickerScreen
from Board.tile_picker import TilePicker

from kao_console.ascii import ENDL
from kao_gui.console.console_controller import ConsoleController

from string import ascii_lowercase, digits

class TilePickerController(ConsoleController):
    """ Controller for picking a tile """
    
    def __init__(self, player, game):
        """ Initialize the Tile Picker Controller """
        self.board = game.board
        self.tilePicker = TilePicker(game.board)
        screen = TilePickerScreen(player, self.tilePicker)
        commands = {}
        for character in digits:
            commands[character] = screen.tilePickerWidget.setRow
        
        for character in ascii_lowercase:
            commands[character] = screen.tilePickerWidget.setColumn
        ConsoleController.__init__(self, screen, commands=commands)
        
    def setRow(self, event):
        """ Set the current row """
        self.tilePicker.row = self.getIndex(event, digits)-1
        
    def setColumn(self, event):
        """ Set the current column """
        self.tilePicker.column = self.getIndex(event, ascii_lowercase)
            
    def getIndex(self, text, listString):
        """ Return the index of text in the given list """
        if text in listString:
            return listString.index(text)
        else:
            return None