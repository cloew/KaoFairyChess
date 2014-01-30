from View.Console.Board.board_widget import BoardWidget
from View.Console.Board.tile_picker_widget import TilePickerWidget

from kao_gui.console.console_widget import ConsoleWidget

class PlayerTurnScreen(ConsoleWidget):
    """ Represents the view for a *** """
    
    def __init__(self, player, board):
        """ Initialize the view """
        self.player = player
        self.boardWidget = BoardWidget(board)
        self.tilePickerWidget = TilePickerWidget()
        
    def draw(self):
        """ Draw the Widget """
        self.boardWidget.draw()
        print ""
        self.tilePickerWidget.draw()