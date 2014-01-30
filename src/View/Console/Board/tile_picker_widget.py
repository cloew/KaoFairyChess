from kao_gui.console.console_widget import ConsoleWidget

from string import ascii_lowercase

class TilePickerWidget(ConsoleWidget):
    """ Represents the view for a picking a tile """
    
    def __init__(self):
        """ Initialize the view """
        self.rowTextSelected = True
        self.rowText = ''
        self.columnText = ''
        
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