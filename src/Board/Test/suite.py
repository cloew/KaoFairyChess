import unittest

from Board.Test.tile_picker_test import suite as tile_picker_suite
from Board.Test.board_test import suite as board_suite

suites = [board_suite,
          tile_picker_suite]
suite = unittest.TestSuite(suites)