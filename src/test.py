import unittest

from Board.Test.suite import suite as board_suite

# Collect all the test suites
suites = [board_suite]

alltests = unittest.TestSuite(suites)

# Run all the tests
if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(alltests)
