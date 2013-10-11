from Board.board import Board
from View.Console.Board.board_controller import BoardController

from kao_gui.console.window import Window

import sys

def main(args):
    """ Run the main file """
    with Window.window():
        controller = BoardController(Board())
        controller.run()

if __name__ == "__main__":
    main(sys.argv[1:])