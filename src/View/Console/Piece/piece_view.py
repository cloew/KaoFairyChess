from piece_color import WHITE, BLACK

from kao_gui.console.console_widget import ConsoleWidget

class PieceView(ConsoleWidget):
    """ Represents the view for a Chess Piece """
    colorDictionary = {BLACK:"{t.black}",
                       WHITE:"{t.white}"}
    
    def __init__(self, piece):
        """ Initialize the view """
        self.piece = piece
        
    def draw(self):
        """ Draw the Widget """
        return self.colorDictionary[self.piece.color]+str(self.piece)+"{t.normal}"