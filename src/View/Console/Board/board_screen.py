from View.Console.Board.tile_view import TileView

from kao_gui.console.console_widget import ConsoleWidget

class BoardScreen(ConsoleWidget):
    """ Represents the view for a Chess Board """
    
    def __init__(self, board):
        """ Initialize the board view """
        self.board = board
        self.tileViews = []
        for row in board.tiles:
            tileViewsInRow = []
            for tile in row:
                tileViewsInRow.append(TileView(tile))
            self.tileViews.append(tileViewsInRow)
        
    def draw(self):
        """ Draw the Widget """
        print " abcdefgh\r"
        
        i = 1
        for row in self.tileViews:
            line = ""
            for tileView in row:
                line += tileView.draw()
            print str(i)+line + "\r"
            i += 1