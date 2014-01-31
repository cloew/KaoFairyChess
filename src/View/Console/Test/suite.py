import unittest

from View.Console.Board.Test.suite import suite as board_suite

suites = [board_suite]
suite = unittest.TestSuite(suites)