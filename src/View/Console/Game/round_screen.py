from kao_gui.console.console_widget import ConsoleWidget

class RoundScreen(ConsoleWidget):
    """ Represents the view for a *** """
    
    def __init__(self):
        """ Initialize the view """
        self.index = 0
        
    def draw(self):
        """ Draw the Widget """
        print "Blah:", self.index
        self.index += 1