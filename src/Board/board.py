from piece_color import WHITE, BLACK
from Board.tile import Tile

class Board:
    """ Represents the chess board """
    
    def __init__(self):
        """ Initialize the board """
        self.size = 8
        
        self.tiles = []
        
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(Tile(self.getColorForSquare(i,j)))
            self.tiles.append(row)
            
    def getColorForSquare(self, row, column):
        """ Return the color for the given square """
        if (row % 2) == 1:
            if (column % 2) == 1:
                return BLACK
            else:
                return WHITE
        else:
            if (column % 2) == 1:
                return WHITE
            else:
                return BLACK