from View.Console.Board.tile_view import TileView

from kao_gui.console.console_widget import ConsoleWidget

from string import ascii_lowercase

class BoardScreen(ConsoleWidget):
    """ Represents the view for a Chess Board """
    
    def __init__(self, board):
        """ Initialize the board view """
        self.board = board
        self.tileViews = []
        tiles = list(board.tiles)
        tiles.reverse()
        for row in tiles:
            tileViewsInRow = []
            for tile in row:
                tileViewsInRow.append(TileView(tile))
            self.tileViews.append(tileViewsInRow)
        
    def draw(self):
        """ Draw the Widget """
        print " {0}\r".format(ascii_lowercase[:self.board.size])
        
        i = 8
        for row in self.tileViews:
            line = ""
            for tileView in row:
                line += tileView.draw()
            print str(i)+line + "\r"
            i -= 1