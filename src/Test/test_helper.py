from piece_color import WHITE

from Board.tile import Tile

def BuildTile(color=WHITE, row=0, column=0):
    """ Return a test Tile """
    return Tile(color, row, column)