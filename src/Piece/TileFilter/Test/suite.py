import unittest

from Piece.TileFilter.Test.empty_tile_filter_test import suite as empty_tile_filter_suite

suites = [empty_tile_filter_suite]
suite = unittest.TestSuite(suites)