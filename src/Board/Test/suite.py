import unittest

from Board.Test.board_test import suite as board_suite

suites = [board_suite]
suite = unittest.TestSuite(suites)