import unittest

from Piece.Test.suite import suite as piece_suite
from Game.Test.suite import suite as game_suite
from Board.Test.suite import suite as board_suite

# Collect all the test suites
suites = [board_suite,
          game_suite,
          piece_suite]

alltests = unittest.TestSuite(suites)

# Run all the tests
if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(alltests)
