from View.Console.Board.board_screen import BoardScreen

from kao_gui.console.console_controller import ConsoleController

class BoardController(ConsoleController):
    """ Controller for a *** """
    
    def __init__(self, board):
        """ Initialize the Board Controller """
        screen = BoardScreen(board)
        ConsoleController.__init__(self, screen)