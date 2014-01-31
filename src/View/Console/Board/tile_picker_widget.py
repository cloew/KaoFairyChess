from kao_gui.console.console_widget import ConsoleWidget

from string import ascii_lowercase

class TilePickerWidget(ConsoleWidget):
    """ Represents the view for a picking a tile """
    
    def __init__(self, tilePicker):
        """ Initialize the view """
        self.tilePicker = tilePicker
        
    def setRow(self, text):
        """ Set the current Row """
        if text.isdigit():
            self.rowText = text[0]
        
    def setColumn(self, text):
        """ Set the current Column """
        if text.islower():
            self.columnText = text[0]
        
    def draw(self):
        """ Draw the Widget """
        print "Select Tile\r"
        print "Row:", self.rowText, "\r"
        print "Column:", self.columnText, "\r"
        print "Press Enter to submit\r"
        
    @property
    def rowText(self):
        """ Return the proper row character """
        if self.tilePicker.row is None:
            return ''
        else:
            return str(self.tilePicker.row+1)
        
    @property
    def columnText(self):
        """ Return the proper column character """
        if self.tilePicker.column is None:
            return ''
        else:
            return ascii_lowercase[self.tilePicker.column]