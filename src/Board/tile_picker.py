
class TilePicker:
    """ Represents a Tile Picker """
    
    def __init__(self, board):
        """ Initialize the Tile Picker """
        self.row = None
        self.column = None
        self.board = board
        
    def getTile(self):
        """ Return the current tile """
        if self.row is None or self.column is None:
            return None
        else:
            return self.board.getTileAt(self.row, self.column)