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
                row.append(Tile(self.getColorForSquare(i,j), i, j))
            self.tiles.append(row)
            
    def getTileAt(self, row, column):
        """ Returns the tile at the coordinate given or None """
        if row in range(self.size) and column in range(self.size):
            return self.tiles[row][column]
        else:
            return None
            
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
        
    @property
    def last_row(self):
        """ Return the last Row index of the board """
        return self.size-1
        
    @property
    def last_col(self):
        """ Return the last Column index of the board """
        return self.size-1
                
    def __getitem__(self, index):
        """ Return the row requested """
        return self.tiles[index]