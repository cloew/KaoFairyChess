from Game.game import Game
from View.Console.Game.game_controller import GameController

from kao_gui.console.window import Window

import sys

def main(args):
    """ Run the main file """
    with Window.window():
        game = Game()
        controller = GameController(game)
        controller.run()

if __name__ == "__main__":
    main(sys.argv[1:])