
class Piece:
    """ Represents a chess piece """
    
    def __init__(self, symbol, color):
        """ Initialize the piece """
        self.symbol = symbol
        self.color = color
        
    def __repr__(self):
        """ Return the String Representation of the piece """
        return str(self.symbol)