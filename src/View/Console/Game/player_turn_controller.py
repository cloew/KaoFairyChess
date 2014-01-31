from View.Console.Board.tile_picker_controller import TilePickerController

from kao_gui.console.console_controller import ConsoleController


class PlayerTurnController(ConsoleController):
    """ Controller for a Player Turn """
    
    def __init__(self, player, game):
        """ Initialize the Player Turn Controller """
        self.player = player
        self.game = game
        ConsoleController.__init__(self, None)
        
    def run(self):
        """ Run the controller """
        self.running = True
        
        self.runController(TilePickerController(self.player, self.game))