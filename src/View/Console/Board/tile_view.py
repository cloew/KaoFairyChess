from piece_color import WHITE, BLACK
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
        return self.formatTerminalString(self.getBackgroundColor() + " " + "{t.normal}")
        
    def getBackgroundColor(self):
        """ Return the background color for the tile """
        return self.colorDictionary[self.tile.color]