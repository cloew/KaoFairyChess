from piece_picker_screen import PiecePickerScreen

from kao_gui.console.console_controller import ConsoleController

class PiecePickerController(ConsoleController):
    """ Controller for a *** """
    
    def __init__(self):
        """ Initialize the *** Controller """
        screen = PiecePickerScreen()
        ConsoleController.__init__(self, screen)