
class Tile:
    """ Represents a tile on the game board """
    
    def __init__(self, color, row, column):
        """ Initialize the tile with its color """
        self.color = color
        self.row = row
        self.column = column
        self.piece = None 