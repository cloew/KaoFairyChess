from piece_color import WHITE, BLACK
from View.Console.Piece.piece_view import PieceView

from kao_gui.console.console_widget import ConsoleWidget

class TileView(ConsoleWidget):
    """ Represents the view for a tile """
    colorDictionary = {BLACK:"{t.on_magenta}",
                       WHITE:"{t.on_cyan}"}
    
    def __init__(self, tile):
        """ Initialize the view """
        self.tile = tile
        
    def draw(self):
        """ Draw the Widget """
        if self.tile.piece is not None:
            pieceView = PieceView(self.tile.piece)
            pieceViewString = pieceView.draw()
        else:
            pieceViewString = " "
            
        return self.formatTerminalString(self.getBackgroundColor() + pieceViewString + "{t.normal}")
        
    def getBackgroundColor(self):
        """ Return the background color for the tile """
        return self.colorDictionary[self.tile.color]