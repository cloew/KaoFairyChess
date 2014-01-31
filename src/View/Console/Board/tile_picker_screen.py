from View.Console.Board.board_widget import BoardWidget
from View.Console.Board.tile_picker_widget import TilePickerWidget

from kao_gui.console.console_widget import ConsoleWidget

class TilePickerScreen(ConsoleWidget):
    """ Represents the screen for Tile Picking """
    
    def __init__(self, player, tilePicker):
        """ Initialize the view """
        self.player = player
        self.boardWidget = BoardWidget(tilePicker.board)
        self.tilePickerWidget = TilePickerWidget(tilePicker)
        
    def draw(self):
        """ Draw the Widget """
        self.boardWidget.draw()
        print ""
        self.tilePickerWidget.draw()