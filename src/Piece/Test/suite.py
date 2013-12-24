import unittest

from Piece.TileFilter.Test.suite import suite as tilefilter_suite
from Piece.TileLocator.Test.suite import suite as tilelocator_suite

suites = [tilelocator_suite,
          tilefilter_suite]
suite = unittest.TestSuite(suites)