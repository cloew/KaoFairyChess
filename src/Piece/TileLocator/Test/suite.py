import unittest

from Piece.TileLocator.Test.vector_tile_locator_test import suite as vector_tile_locator_suite

suites = [vector_tile_locator_suite]
suite = unittest.TestSuite(suites)