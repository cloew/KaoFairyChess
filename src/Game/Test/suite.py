import unittest

from Game.Type.Test.suite import suite as type_suite
from Game.Player.Test.suite import suite as player_suite

suites = [player_suite,
          type_suite]
suite = unittest.TestSuite(suites)